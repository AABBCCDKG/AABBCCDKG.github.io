---
layout: about
title: About
seo_title: Dong Wang
description: Dong Wang's personal website, projects, research, and software engineering work.
permalink: /

profile:
  align: right
  image: personal.jpg
  image_circular: true
  more_info: >
    <p>Updated <time datetime="2026-08-06">Aug 6, 2026</time></p>
news: false
social: true
---

Hi 👋 I’m Dong. I graduated from Purdue University with a B.S. in Computer
Science after completing 93% of the degree requirements in 1.5 years. Before
Purdue, I studied Electrical and Computer Engineering at Northeastern
University (China), where I ranked 2nd in a cohort of 290.

I’m a Software Engineer at TikTok / ByteDance working on search recommendation
and ranking systems. Previously, I interned at Amazon Web Services and Bank of
China. I also conducted [physics-informed deep learning
research](https://royal-celestite-49a.notion.site/Motion-Prediction-through-Physical-Laws-b75fba68cf2f414e9ebd9f84c0db00d7)
under [Prof. Yexiang Xue](https://www.cs.purdue.edu/homes/yexiang/) at Purdue AI
Lab, joined the Purdue Aerial Robotics Team, and participated in Y Combinator's
AI Startup School.

<section class="home-projects" aria-labelledby="selected-projects-title">
  <div class="home-projects__heading">
    <div>
      <p class="section-eyebrow">A few things I have been building</p>
      <h2 id="selected-projects-title">Selected projects</h2>
    </div>
    <a class="home-projects__all" href="{% link _pages/projects.md %}">
      View all projects
      <span aria-hidden="true">→</span>
    </a>
  </div>

{% assign featured_projects = site.projects | where: "featured", true | sort: "importance" %}

  <div class="projects-grid projects-grid--featured">
    {% for project in featured_projects %}
      {% include project_card.liquid project=project heading_tag='h3' %}
    {% endfor %}
  </div>
</section>
