# Unreal Engine For Research project website

This repository contains the code for the Unreal Engine For Research ("UE4Research") project website, which can be viewed live at <https://ue4research.org>.


## Building from source

The site is implemented using the [Jekyll](https://jekyllrb.com/) static site generator and targets GitHub pages. You can use the [GitHub Pages Ruby Gem](https://github.com/github/pages-gem) to install all of the necessary dependencies to build and run the site locally. Once the dependencies are installed, generate and start the local server by running the command:

```
jekyll serve
```

If you have modified the list of publications then you will need to run the Python preprocessing script to parse the BibTeX file and update the site's JSON data files accordingly. The script requires Python 3.5 or newer with the [natsort](https://pypi.org/project/natsort/) and [pybtex](https://pypi.org/project/pybtex/) packages, and can be run like so:

```
python3 ./_publications/publications.py
```


## Contributing

The UE4Research contributors maintain the project on a volunteer basis and we are always happy to accept additional assistance from the community. We particularly welcome issues that notify us of new publications to add to the [Publications](https://ue4research.org/publications) page and new infrastructure projects or integrations to add to the [Resources](https://ue4research.org/resources) page.


## Legal

The code for the site is licensed under the MIT License, see the file [LICENSE](./LICENSE) for details.

All site content is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
