#!/usr/bin/env python3
import json, os, pybtex, re, sys
import pybtex.database, pybtex.plugin
from natsort import natsorted

# Retrieves the year for a BibTeX entry
getYear = lambda entry: int(entry[1].fields['year'])

# Retrieves the Jabref groups for a BibTeX entry
getGroups = lambda entry: entry[1].fields['groups'].split(', ') if 'groups' in entry[1].fields else []

# Parses a Jabref metadata line for a group definition
def parseGroup(line):
	matches = re.search('([0-9]+) ([a-z|A-Z]+)\\:([^;]+?)\\\\;', line)
	return {
		'level': int(matches.group(1)),
		'type': matches.group(2),
		'name': matches.group(3)
	}

# Reconstructs a tree of Jabref groups from a list of parsed metadata lines
def reconstructTree(groups):
	tree = {'AllEntriesGroup': {}}
	lastForLevel = { 0: tree['AllEntriesGroup'] }
	for group in groups:
		parent = lastForLevel[ group['level'] - 1 ]
		parent[ group['name'] ] = {}
		lastForLevel[ group['level'] ] = parent[ group['name'] ]
	
	return tree

# Generates the formatted HTML for a BibTeX entry
def processEntry(entry):
	formatted = style.format_entries([entry[1]])
	html = list(formatted)[0].text.render(backend)
	html = re.sub(', (<a href=".+?">doi:.+?</a>)', ', DOI: \\1', html)
	html = html.replace('<span class="bibtex-protected">', '')
	html = html.replace('</span>', '')
	html = html.replace('\n', ' ')
	return {
		'key': entry[0],
		'html': html
	}

# Compute absolute file paths based on the location of this script
scriptDir = os.path.dirname(os.path.abspath(__file__))
siteRoot = os.path.dirname(scriptDir)
bibtexFile = os.path.join(scriptDir, 'publications.bib')
publicationsOutfile = os.path.join(siteRoot, '_data', 'publications.json')
rationaleOutfile = os.path.join(siteRoot, '_data', 'rationale.json')

# Parse the BibTeX database file
with open(bibtexFile, 'rb') as infile:
	bibtex = infile.read().decode('utf-8')
	db = pybtex.database.parse_string(bibtex, 'bibtex')

# Retrieve the style class for the "plain" style
PlainStyle = pybtex.plugin.find_plugin('pybtex.style.formatting', 'plain')
style = PlainStyle()

# Retrieve the HTML backend
HtmlBackend = pybtex.plugin.find_plugin('pybtex.backends', 'html')
backend = HtmlBackend('utf-8')

# Retrieve the list of years that have publications and sort them in reverse-chronological order
years = reversed(sorted(set([getYear(entry) for entry in db.entries.items()])))

# Process the publications for each year, sorting them in order of BibTeX key
publicationsForYears = {
	year: natsorted([processEntry(entry) for entry in db.entries.items() if getYear(entry) == year], key = lambda e: e['key'])
	for year in years
}

# Write the HTML entries to our publications JSON file
with open(publicationsOutfile, 'wb') as outfile:
	outfile.write(json.dumps(publicationsForYears, indent=4).encode('utf-8'))

# Extract the groups hierarchy from the Jabref metadata
matches = re.search('\\@Comment\\{jabref\\-meta\\: grouping\\:(.+?)\\}', bibtex, re.DOTALL)
meta = matches.group(1).strip().split('\n')
groups = [parseGroup(line) for line in meta if line != '0 AllEntriesGroup:;']
groupsTree = reconstructTree(groups)

# Retrieve the list of rationale groups
rationaleGroups = list(groupsTree['AllEntriesGroup']['rationale'].keys())

# Retrieve the BibTeX keys of the publications for each rationale group
rationale = {
	group: [entry[0] for entry in db.entries.items() if group in getGroups(entry)]
	for group in rationaleGroups
}

# Extract the list of unique cited BibTeX keys in the rationale groups and use the sorted order for our citation indices
citedKeys = set()
for group, keys in rationale.items():
	for key in keys:
		citedKeys.add(key)
indices = sorted(list(citedKeys))

# Sort the rationale groups in descending number of publications, and in alphabetical order when publication count is equal
sortedRationale = sorted(rationale.keys())
sortedRationale = sorted(sortedRationale, key = lambda reason: 1 - len(rationale[reason]))

# Expand the rationale entries to include numeric indices, sorting each group's list in ascending order of index
expanded = {
	group: sorted([{'index': str(indices.index(key) + 1), 'key': key} for key in rationale[group]], key = lambda c: int(c['index']))
	for group in sortedRationale
}

# Write the sorted entries to the rationale JSON file
with open(rationaleOutfile, 'wb') as outfile:
	outfile.write(json.dumps(expanded, indent=4).encode('utf-8'))
