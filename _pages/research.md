---
permalink: /research/
title: "Research"
excerpt: "My Research"
author_profile: true
---
<img src="../files/agu_sign.webp" alt="Image of Dr. Waterman with fellow students and his undergraduate mentee while a PhD student. Image taken at the AGU Conference, 2023" style="float:left;max-width:100%;height:auto;padding:1px;"/>

I am an atmospheric modeler, boundary layer meteorologist, computational hydrologist, engineer, teacher and mentor working to improve global understanding of the connection between the land surface we live on and the atmosphere above us. My research aims to build models for water, carbon and energy that apply in data rich uniform cropland, or poorly instrumented, vast mountain forests, allowing environmental scientists, modelers and decision makers in all parts of our earth to make informed decisions. To this end, I work collaboratively to harness a wealth of satellite and in-situ data, high resolution models, fundamental physics, and modern machine learning methods to improve predictions of how water, energy, and carbon moves across the land-atmosphere continuum, especially in complex terrain and heterogeneous landscapes.

My core research is outlined in the four categories below:


Modeling the Impact of Mesoscale Circulations
=====

<img src="../files/circulations.webp" alt="Image 1" style="float:right;max-width:50%;height:auto;padding:15px;"/>

When there is a hot dry patch of land, next to a cool wet patch, circulations can begin to form. The literature has shown that these circulations can impact cloud development and patterning. Modern Earth System Models (ESMs) operate at a much larger scale than than the kilometer scale surface heterogeneity needed to form these circulations. This work uses large-eddy simulation (LES) output to parameterize these circulations and their impacts on clouds.

> ### Key Results
> * CLUBB, a boundary layer scheme, is run as a single column model with two columns, one over the hot dry patch and another over the cold wet patch, for 92 one day simulations, with a modeled circulation connecting them
> * The two column model shows qualitative agreement with high resolution models, with increased cloud development when circulations are modeled, at a fraction of the compuational cost

> ### Publications
> * [A Two-Column Model Parameterization for Subgrid Surface Heterogeneity Driven Circulations](https://tswater.github.io/publication/2022_a)
> * Related Work:  [Assessing the Atmospheric Response to Subgrid Surface Heterogeneity in the Single-column Community Earth System Model, version 2 (CESM2).](https://doi.org/10.1029/2022MS003517 )


<br>

Continental Scale Impact of Surface Heterogeneity
=====

<img src="../files/wrf_hethmg.webp" alt="Image 1" style="float:right;max-width:50%;height:auto;padding:15px;"/>

When ESMs and numerical weather prediction (NWP) schemes are run, they often operate with a higher resolution land surface model (LSM) which is then homogenized for exchange with the atmosphere. This "lost" heterogeneity can have atmospheric impacts locally and downstream. The impact this homogenization has, and how land surface heterogeneity is connected to atmospheric impact, is explored as part of this project.

> ### Key Results
> * Three summers of daily, 3km resolution WRF simulations across the continental United States (CONUS) with heterogeneous and homogenized surface fluxes show significant changes in precipitation statistics
> * Homogenization leads to increases in latent heat fluxes and rainfall, and a decrease in mesoscale turbulence in the boundary layer.
> * Most significant imapacts are observed where bodies of water, (small lakes, large rivers, coastal regions) are homogenized with drier land

> ### Publications 
> * First manuscript from the project in preparation for publication


<br>

Turbulence Anisotropy to Improve Surface Exchange
=====

<img src="../files/ani.webp" alt="Image 1" style="float:right;max-width:50%;height:auto;padding:15px;"/>

In modern atmospheric models (NWP, ESMs, LES) Monin-Obukhov Similarity Theory (MOST) is applied to determine exchange of heat, energy, and moisture from the land surface to the atmosphere, despite significant errors. Recent work from [Stiperski et. al](https://doi.org/10.1103/PhysRevLett.130.124001) has shown the anisotropy of turbulence may account for observed deviations from MOST. This project seeks to bridge the gap between the work of Stiperski, and the needs for application in modeling systems.

> ### Key Results
> * Relations developed by Stiperski have shown strong applicability over the vast and diverse [NEON eddy-covariance tower network](https://www.neonscience.org/field-sites) with little modification.

> ### Publications 
> * First Manuscript from the project in preparation for publication


<br>

Potential Temperature Variance in Surface Models
=====

<img src="../files/ptv.webp" alt="Image 1" style="float:right;max-width:50%;height:auto;padding:15px;"/>

To model the lower atmosphere, we need accurate boundary conditions at the earth's surface. This work examines one of the surface boundary conditions of turbulence, potential temperature variance. The typical parameterizations used in modern atmospheric and Earth System Models are evaluated accross many varried terrain types, and constraints on model performance as well as proposed alterations to the existing parameterizations are evaluated.

> ### Key Results
> * Models of potential temperature variance in the surface layer based on similarity theory were evaluated using data from 39 varied sites over 2.5 years
> * Existing schemes perform well across most surfaces, although the data shows a significant bias in the values of the similarity constants
> * Canopy structure and surface heterogeneity drive a large portion of inter-site variability in model performance

> ### Publications
> * [Examining Parameterizations of Potential Temperature Variance Across Varied Landscapes for Use in Earth System Models](https://tswater.github.io/publication/2022_a)

