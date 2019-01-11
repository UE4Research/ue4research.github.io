#!/usr/bin/env python3
import argparse, csv, datetime, os, subprocess

# Captures the output of a subprocess
def capture(command, cwd):
	result = subprocess.run(command, cwd=cwd, check=True, stdout=subprocess.PIPE)
	return result.stdout.decode('utf-8')

# Retrieves the list of commits for a repository branch within a given year
def getCommits(repository, branch, year):
	output = capture(['git', 'rev-list', '--after={}-01-01'.format(year), '--before={}-01-01'.format(year+1), '--format=format:%H,%aI,%an', branch], repository)
	commits = [line.strip().split(',', 3) for index, line in enumerate(output.split('\n')) if index % 2 == 1]
	return [
		{
			'sha': commit[0],
			'timestamp': commit[1],
			'author': commit[2]
		}
		for commit in commits
	]

import json

# Computes commit count and author count statistics for a repository branch within a given year
def computeStatistics(repository, branch, year):
	commits = getCommits(repository, branch, year)
	authors = set([commit['author'].lower() for commit in commits])
	authors.discard('unrealbot')
	return {
		'year': year,
		'commits': len(commits),
		'contributors': len(authors)
	}

# Parse the supplied command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('repository', help='The path to the UnrealEngine git repository')
parser.add_argument('branch', nargs='?', default='release', help='The branch to compute statistics for (defaults to "release")')
args = parser.parse_args()

# Compute statistics for each year since UE4 went up on GitHub, excluding the current year
years = range(2015, datetime.date.today().year)
statistics = [computeStatistics(args.repository, args.branch, year) for year in years]

# Compute the file path for our output CSV file based on the location of this script
scriptDir = os.path.dirname(os.path.abspath(__file__))
csvFile = os.path.join(os.path.dirname(scriptDir), '_data', 'stats.csv')

# Write the statistics to our output CSV file
with open(csvFile, 'w', newline='') as outfile:
	fieldnames = list(statistics[0].keys())
	writer = csv.DictWriter(outfile, dialect='unix', fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows(statistics)
