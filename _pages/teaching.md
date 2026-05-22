---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

<img src="../files/img_2.webp" alt="Image 2" style="float:right;max-width:47%;height:auto;padding:15px;"/>
<img src="../files/present.webp" alt="Image 1" style="float:right;max-width:53%;height:auto;padding:15px;"/>
{% include base_path %}

{% for post in site.teaching reversed %}
  {% include archive-single.html %}
{% endfor %}
