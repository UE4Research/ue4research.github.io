---
layout: default
pageclass: about
title: Resources
tagline: Get started with the Unreal Engine and integrate it with existing tools and libraries.
permalink: /resources
---

## Contents
{:.no_toc}

* TOC
{:toc}


## Getting started

There are a wide variety of freely-available resources dedicated to helping new users familiarise themselves with the Unreal Engine. Key resources include:

- The [official Unreal Engine documentation](https://docs.unrealengine.com/) provides tutorials and getting started guides alongside detailed technical information about various engine subsystems and full API documentation.

- [Unreal Academy](https://academy.unrealengine.com/) provides videos and online training for a wide variety of topics, ranging from engine basics and key concepts to advanced topics organised by industry-based use cases. Scientific research is not currently one of the industries that is explicitly catered to, but this may change in the future.

- The [official Unreal Engine YouTube channel](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) provides access to live training livestreams and archives, as well as various videos exploring specific features of the engine.

- The [Unreal Slackers](http://unrealslackers.org/) Discord community is a great place to connect with other Unreal Engine users and ask questions. There are a variety of channels dedicated to common topics and use cases.


## Infrastructure Projects

The projects listed below provide additional infrastructure that complements the native capabilities of the Unreal Engine in order to simplify development workflows or provide integration with third-party libraries or tools. A number of these projects are maintained by the UE4Research contributors themselves and were developed with a specific focus on research use cases.

Projects maintained by the UE4Research contributors are listed first, followed by all other projects in alphabetical order.

{% for tool in site.data.infrastructure %}
### {{ tool.name }}
{::nomarkdown}
<p><strong>Created by:</strong> {{ tool.author | escape }}</p>
<ul class="infrastructure-links">
	<li><strong>Links:</strong></li>
	{% if tool.homepage != "" %}<li><a href="{{ tool.homepage | uri_escape }}"><span class="fas fa-home fa-fw icon-left"></span> Homepage</a></li>{% endif %}
	{% if tool.repository != "" %}<li><a href="{{ tool.repository | uri_escape }}"><span class="fab fa-github fa-fw icon-left"></span> Repository</a></li>{% endif %}
	{% if tool.docs != "" %}<li><a href="{{ tool.docs | uri_escape }}"><span class="fas fa-book fa-fw icon-left"></span> Documentation</a></li>{% endif %}
</ul>
{:/}

**Description (from the project's documentation):**

{::nomarkdown}<blockquote>{:/}

{{ tool.description }}

{::nomarkdown}</blockquote>{:/}

**Research uses:**

{{ tool.uses }}
{% endfor %}


## Integrations

This section provides guidance and examples to assist in integrating existing third-party libraries, tools, and programming languages with the Unreal Engine. Many of these components are widely used in research and will therefore be a familiar (or in some cases essential) part of researchers' existing workflows.

Libraries, tools, and programming languages are listed in alphabetical order.

### C#

- The [MonoUE](https://mono-ue.github.io/) plugin provides C# and F# bindings for the Unreal Engine. Note that the project is still under development and there are a number of features that are yet to be implemented.

### Javascript

- The [Unreal.js](https://github.com/ncsoft/Unreal.js) plugin provides support for embedding the V8 Javascript interpreter in the Unreal Engine and provides Javascript bindings for most of the Engine API.

### OpenCV

- The [ue4-opencv-demo](https://github.com/adamrehn/ue4-opencv-demo) GitHub repository demonstrates the use of [conan-ue4cli](#conan-ue4cli) to build a UE4-compatible version of [OpenCV](https://opencv.org/) and then statically link against it.

### Protobuf and gRPC

- The [ue4-grpc-demo](https://github.com/adamrehn/ue4-grpc-demo) GitHub repository demonstrates the use of [conan-ue4cli](#conan-ue4cli) to build a UE4-compatible version of [gRPC](https://grpc.io/) and then statically link against it and implement a gRPC service inside the Unreal Engine.

### Python

- There is currently experimental support provided by Epic Games themselves for Python scripting in the Editor, although this does not work in packaged projects. See the [Scripting the Editor using Python](https://docs.unrealengine.com/en-US/Editor/Scripting-and-Automating-the-Editor/Scripting-the-Editor-using-Python) page of the official UE4 documentation for details.

- The [UnrealEnginePython](https://github.com/20tab/UnrealEnginePython) plugin provides support for embedding the Python interpreter in the Unreal Engine, and works in both the Editor and in packaged projects. Python bindings are provided for most of the Engine API.
