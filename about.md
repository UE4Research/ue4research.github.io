---
layout: default
pageclass: about
title: About
tagline: What is the UE4Research project and who maintains it?
permalink: /about
---

## Project overview

Founded in 2018, the Unreal Engine For Research ("UE4Research") project aims to act as a central hub for anyone who uses, or wishes to use, Epic Games' [Unreal Engine 4](https://www.unrealengine.com/) within the context of scientific research.

The project has three key goals:

- To increase awareness of the capabilities of the Unreal Engine within the research community, so that researchers are able to make an informed decision when selecting a software framework for the implementation of their projects. (Addressed by the [Rationale]({{ "/rationale" | relative_uri }}) and [Publications]({{ "/publications" | relative_uri }}) pages.)

- To provide resources that assist researchers in getting up and running with the Unreal Engine and integrating it with the existing tools, libraries, and programming languages they use in their research workflows. (Addressed by the [Resources]({{ "/resources" | relative_uri }}) page.)

- To foster a collaborative community where researchers working with the Unreal Engine are able to assist one another and share their experiences. (Addressed by the [Community]({{ "/community" | relative_uri }}) page.)


## Contributors

The UE4Research project was founded by [Dr Adam Rehn](https://adamrehn.com), a researcher from James Cook University. Adam and his fellow contributors maintain the project on a volunteer basis in the hopes that it proves useful for fellow researchers.

The following contributors currently assist in maintaining the project:

{::nomarkdown}
<ul>
	{% for contributor in site.data.contributors %}
	<li>{{ contributor.name | escape }} (&nbsp;<a href="https://github.com/{{ contributor.username | uri_escape }}"><span class="icon icon-left fab fa-github"></span>{{ contributor.username | escape }}</a>&nbsp;)</li>
	{% endfor %}
</ul>
{:/}

If you are interested in contributing to the project, see the [Community]({{ "/community" | relative_uri }}) page for details on how to contact us.
