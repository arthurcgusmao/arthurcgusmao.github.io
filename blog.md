---
layout: page
title: Blog
permalink: /blog/
comments: false
order_nav: 4
order_home: 3
---



<div class="posts-list">
{% for category in site.categories reversed %}
  <div class="category-group">
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <div id="#{{ category_name | slugize }}"></div>

    <h2 class="category-head">{{ category_name }}</h2>
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.categories[category_name] %}
      <div class="post-item">
          <p><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></p>
      </div>
    {% endfor %}
  </div>
{% endfor %}
</div>
