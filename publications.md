---
layout: default
pageclass: about
title: Publications
tagline: A list of academic publications that utilise the Unreal Engine.
permalink: /publications
---

## Scope
{:.no_toc}

This page provides a list of academic publications that present research projects utilising Unreal Engine 4 or newer as a component of their software implementations. This list does **not include**:

- Non-academic publications (e.g. blog posts, whitepapers, technical reports, etc.)
- Publications that discuss the Unreal Engine but do not utilise it as a component of a software implementation
- Publications that present a software/multimedia implementation without any research component
- Publications that present research which utilises versions of the Unreal Engine prior to Unreal Engine 4
- Publications that present research concerning the underlying technologies that power game engines (e.g. rendering techniques, networking algorithms, etc.) that provide an implementation for the Unreal Engine

Although the UE4Research contributors do our best to keep this publication list up-to-date, we cannot guarantee that the list is exhaustive. If you find a relevant publication that we've missed, please [let us know about it]({{ "/community" | relative_uri }}). If you would like to cite any of the publications in your own research, you can access [the underlying BibTeX database for the list here](https://github.com/UE4Research/ue4research.github.io/blob/master/_publications/publications.bib).


## Publications by year
{:.no_toc}

* TOC
{:toc}


{% for year in site.data.publications %}
## {{ year[0] | escape }}

{::nomarkdown}
<ul class="publication-list">
{% for item in year[1] %}
	<li id="{{ item.key | escape }}">
		<p>{{ item.html }}</p>
	</li>
{% endfor %}
</ul>
{:/}

{% endfor %}
