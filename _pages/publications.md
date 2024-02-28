---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

First Author Publications
=====

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

Other Publications
=====
* Fowler, M., Neale, R., **Waterman, T.**, et. al (2024) Assessing the Atmospheric Response to Subgrid Surface Heterogeneity in the Single-column Community Earth System Model, version 2 (CESM2). *Journal of Advances in Modelling Earth Systems, 16(3)*. https://doi.org/10.1029/2022MS003517
* Lau, R., Seguí, C. **Waterman, T.**, Chaney, N., Veveakis, M. (2024) InSAR-Informed In-Situ Monitoring for Deep-Seated Landslides: Insights from El Forn (Andorra). Submitted to *Journal for Remote Sensing and the Environment*. Preprint: https://doi.org/10.48550/arXiv.2311.01564
* Bacelar, L., Torres Rojas, L., Vergopolan, N., **Waterman, T.**, Chaney, N. Leveraging clustering to enable locally relevant and computationally efficient runoff predictions. Submitted to *Journal of Hydrology.* Preprint: http://dx.doi.org/10.2139/ssrn.4737923 
* Torres Rojas, L., Waterman, T., Cai, J., Zorzetto, E. Wainwright, H., Chaney, N. (2024)  The observed spatio-temporal patterns of Land surface temperature over the Contiguous United States.  Submitted to *Journal of Geophysical Research: Atmospheres*.
