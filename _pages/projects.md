---
layout: page
title: Projects
permalink: /projects/
description: Things I have built to explore probability, language, simulation, and reliable software.
nav: true
nav_order: 2
---

<p class="projects-intro">
  Some began as research questions; others started because I wanted to understand
  how a system behaved. Each page keeps the implementation details, tests, and
  limits close to the result.
</p>

{% assign sorted_projects = site.projects | sort: "importance" %}

<div class="projects-grid">
  {% for project in sorted_projects %}
    {% include project_card.liquid project=project heading_tag='h2' %}
  {% endfor %}
</div>
