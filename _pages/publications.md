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

## Featured Publications

{% for post in site.publications reversed %}
  {% if post.feature == 'yes' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Additional Publications

{% for post in site.publications reversed %}
  {% if post.feature == 'no' %}
    {% include archive-single-nft.html %}
  {% endif %}
{% endfor %}
