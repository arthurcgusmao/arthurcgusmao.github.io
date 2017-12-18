---
layout: page
title: About Me
permalink: /about-me/
comments: false
---

<ul class="contact-list">
  <h3><b>{{ site.author }}</b></h3>

  {% if site.email %}
  <li><a href="mailto:{{ site.email }}">{{ site.email }}</a></li>
  {% endif %}


  {% if site.github_username %}
  <li>
    {% include icon-github.html username=site.github_username %}
  </li>
  {% endif %}


  <li>{{ site.author_about | escape }}</li>
</ul>
