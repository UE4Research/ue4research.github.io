---
layout: default
pageclass: about
title: Rationale
tagline: Why use the Unreal Engine for scientific research?
permalink: /rationale
---

## Contents
{:.no_toc}

* TOC
{:toc}


## When does a researcher need a game engine?

Modern game engines are sophisticated pieces of middleware that provide convenient abstractions for a variety of complex functionality. Due to economies of scale, the implementations of features included within widely-used game engines are often far more rigorously tested and optimised than the equivalent implementations within software or frameworks designed purely for scientific purposes. Researchers should consider utilising a game engine if they will make use of one or more key features common to most modern implementations:

- **Powerful GPU-accelerated 3D rendering**: if you are performing data visualisation and only need to generate static 2D images or plots then you will be best served by the myriad of available tools and workflows designed specifically for this purpose. However, if you need to visualise data in 3D or produce detailed representations of virtual environments then the rendering system of a game engine will provide the most powerful and flexible solution. The real-time nature of game engine rendering systems allows you to visualise complex 3D information in an extremely performant manner whilst retaining access to powerful lighting and material customisations. Game engines also provide first-class support for interactivity during rendering. If interactivity is a requirement of the visualisation then the game engine's input system will provide convenient abstractions for implementing common interaction patterns. If interactivity is not required, then the real-time rendering capabilities will allow you to make modifications to the visualisation and observe their outcomes immediately so that the output can be thoroughly fine-tuned prior to being exported.

- **Real-time physics simulation**: if you need to perform extremely accurate physics-based simulations and do not have a requirement for real-time processing then you will invariably achieve the best results by precomputing simulation outcomes in dedicated software and storing them for subsequent visualisation or analysis. However, if simulations need to be performed and/or recorded in real-time then the physics system of a modern game engine will provide a well-optimised and performant implementation with a convenient interface. The rendering system of the game engine will also allow the simulation results to be visualised in real-time without requiring any additional configuration. Precomputed simulation results can be visualised in a similar manner, albeit typically with a small amount of configuration required to import the data.

- **VR and AR support:** game engines are typically the best supported tools for creating virtual/augmented/mixed reality software, making them the *de facto* choice of middleware when implementing such systems. VR-specific performance optimisations present in most modern game engines also help to ensure smooth framerates and thus reduced likelihood of users experiencing motion sickness effects. Game engines also provide convenient hooks for recording telemetry information, which is useful when performing experiments in which human users interact with virtual environments and data on these interactions needs to be collected and stored.

- **Network replication:** if you are performing experiments in which multiple human participants interact with a shared virtual environment on separate network-connected devices then the environment state on each participant's device must be kept in close synchronisation with the state of all other participants to ensure the validity of any collected data. Modern game engines provide powerful and well-optimised network replication functionality for exactly this purpose, typically accompanied by convenient abstractions to minimise the amount of required configuration. The networked nature of this synchronisation also allows experiment facilitators to observe the state of the virtual environment in real-time through a separate device without directly observing the participants themselves, which is extremely useful in experiments seeking to minimise observer effects.

- **Spatial audio**: modern game engines provide either native support for spatial audio or compatibility with plugins such as [Steam Audio](https://valvesoftware.github.io/steam-audio/). Physics-based audio propagation and transformation more accurately models how sound behaves in the real world, and the combination of spatial audio output with accompanying telemetry from the physics system provides a potential source of ground truth training data for machine learning algorithms that focus on acoustics. Framebuffer and depth information from the rendering system can also be included to provide training data for algorithms that incorporate a machine vision component.


## Why choose the Unreal Engine for research use?

Researchers who have made the decision to utilise a game engine are subsequently faced with the need to select a specific engine with which to familiarise themselves. Since all modern game engines provide the key functionality described in the previous section (to varying degrees of sophistication), researchers should consider a number of additional contributing factors when evaluating the suitability of any given game engine.

The sections that follow focus solely on the factors that have made the Unreal Engine a popular choice for existing research, as other game engines are outside the scope of the UE4Research project. We invite researchers to take these factors into account when critically evaluating and comparing other game engines to the Unreal Engine, so that they can make an informed decision and select the engine which will be of most benefit to their research.

### Unreal Engine selection rationale from the existing literature

The [Publications]({{ "/publications" | relative_uri }}) page provides a non-exhaustive list of academic publications that present research projects utilising Unreal Engine 4 as a component of their software implementations. Analysis of these publications reveals that they cite a number of common factors when justifying their decision to use the Unreal Engine. These factors are listed in Table 1, sorted based on the number of publications that cited a given factor.

{::nomarkdown}
<figure>
	<table>
	<thead>
		<tr>
			<th>Factor</th>
			<th>Publications</th>
		</tr>
	</thead>
	<tbody>
		{% for reason in site.data.rationale %}
		<tr>
			<td>{{ reason[0] | escape }}</td>
			<td>
				{% for publication in reason[1] %}
				<a href="{{ "/publications" | relative_uri }}#{{ publication.key | uri_escape }}">[{{ publication.index | escape }}]</a>
				{% endfor %}
			</td>
		</tr>
		{% endfor %}
	</tbody>
	</table>
	
	<figcaption>Table 1: Factors that commonly contribute to the selection of the Unreal Engine for research purposes.</figcaption>
</figure>
{:/}

Each of these factors relates to a specific characteristic of Unreal Engine 4 that the publication authors deemed well-suited to their research use cases:

- **Produces photo-realistic images:** generation of ground truth training data for machine vision applications is an extremely common use of the Unreal Engine. Publications concerned with this use case cited the visual fidelity of the rendering system's output as a key factor in their decision to use the engine. Photo-realistic rendered imagery more closely resembles images captured from the real world, making the trained machine learning systems better suited to working with images from reality.

- **High-quality physics/collision simulation:** publications that utilised the Unreal Engine's physics simulation system commonly cited the accuracy of the simulation as a key factor in their decision to use the engine. The physics system in Unreal Engine 4 is extremely customisable and allows researchers to specify the level of accuracy that they wish to simulate.

- **Engine is open source:** although the Unreal Engine is not free and open-source software (FOSS) according to the [strictest definitions of the term](https://opensource.org/osd), anyone can access the engine source code by signing up for a free Epic Games account. Developers are free to modify and share the source code with other Engine Licensees, as well as contribute new code to the engine, so long as they comply with the terms of the [Unreal Engine EULA](https://www.unrealengine.com/eula). This provides a middle ground between truly FOSS game engines with OSI-approved licenses and entirely proprietary game engines whose developers charge fees for source code access.

- **Availability of pre-made assets:** the [Unreal Engine Marketplace](https://www.unrealengine.com/marketplace/) provides access to a wide variety of existing assets that are ready for use with Unreal Engine 4. Unlike similar marketplaces for other game engines, the Unreal Engine Marketplace enforces [strict guidelines](https://www.unrealengine.com/en-US/marketplace-guidelines) to ensure the quality of available content. Publications that utilised marketplace assets commonly cited the quality of these assets when justifying their selection, particularly when attempting to achieve photo-realistic rendering output for training computer vision systems.

- **Blueprints visual scripting language:** Unreal Engine 4 includes a visual scripting language called [Blueprints](https://docs.unrealengine.com/en-us/Engine/Blueprints) that can be used as an alternative to, or in conjunction with, the engine's native C++ programming language. This visual, node-based system is designed to facilitate rapid prototyping without requiring advanced programming skills, and provides an experience consistent with the visual systems used to create art assets such as materials. Publications that cited Blueprints as a reason for selecting the Unreal Engine often explicitly referred to their rapid prototyping capabilities.

- **Interoperability with external software:** the Unreal Engine is designed to interoperate with a wide variety of external software, either through support for common file formats or through [direct communication](https://docs.unrealengine.com/en-us/Studio/Datasmith/SoftwareInteropGuides) with the external software. This allows researchers to use data or assets created in applications with which they are already familiar and makes it simpler to incorporate the Unreal Engine into their existing workflows.

- **Engine is cross-platform:** Unreal Engine 4 runs on Windows, macOS, and Linux. Projects created with the Unreal Engine can be exported for not only these desktop platforms but also mobile platforms such as Android and iOS, game consoles, and also as HTML5 pages that run entirely within a web browser. Linux support is particularly valuable to researchers because Linux is widely used for research purposes. Publications that cited cross-platform support as a reason for selecting the Unreal Engine also commonly utilised Linux for running experiments.

- **Engine is well-maintained:** the Unreal Engine is actively maintained and receives regular updates that provide improvements to the functionality and performance of the engine. For more details on the maintenance of Unreal Engine 4, see the section below that discusses the engine's contribution statistics.

### Contribution statistics from GitHub

In addition to being actively developed by Epic Games and their industry customers, Unreal Engine 4 has an extremely active community of open-source contributors on GitHub. Table 2 lists the number of commits and contributors who made those commits for each year since the Unreal Engine GitHub repository became accessible for free. The statistics were computed by analysing the output of the `git rev-list` command for the `release` branch of the repository using [this Python script](https://github.com/UE4Research/ue4research.github.io/blob/master/_stats/stats.py).

{::nomarkdown}
<figure>
	<table>
	<thead>
		<tr>
			<th>Year</th>
			<th>Commits</th>
			<th>Contributors</th>
		</tr>
	</thead>
	<tbody>
		{% for row in site.data.stats %}
		<tr>
			<td>{{ row.year | escape }}</td>
			<td>{{ row.commits | escape }}</td>
			<td>{{ row.contributors | escape }}</td>
		</tr>
		{% endfor %}
	</tbody>
	</table>
	
	<figcaption>Table 2: The number of yearly commits and contributors for the <code>release</code> branch of the Unreal Engine GitHub repository.</figcaption>
</figure>
{:/}

After an initial frenzy of development activity immediately following [the announcement](https://www.unrealengine.com/en-US/blog/ue4-is-free) that Unreal Engine source code access had been made free, the repository has maintained a steady stream of commits from a wide variety of contributors year-on-year. It should be noted that these counts include both community contributions and automated commits to synchronise changes from the Epic Games internal Perforce repository, where all changes made by Epic Games engineers are stored.

The combination of industry-funded development and community-driven development allows the Unreal Engine to maintain a development pace that is difficult to achieve when utilising a single model alone. This hybrid model is similar to the one used by many large open source projects such as the [Linux kernel](https://www.kernel.org/) and the [LLVM project](https://llvm.org/) (albeit supported by a decidedly different governance structure), which has a proven track record of producing high-quality software even when managing significant levels of technical complexity.
