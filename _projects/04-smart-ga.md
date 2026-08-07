---
layout: page
title: SmartGA
description: I wanted to see whether a genetic algorithm could rediscover compact formulas from a few examples.
importance: 4
category: research-engineering
featured: true
emoji: 🧬
kicker: Search · Scientific computing
accent: green
github: https://github.com/AABBCCDKG/SmartGA
repository_visibility: public
tags: [C++20, Genetic algorithms, CMake]
---

## Purpose

SmartGA searches for compact mathematical expressions that fit supplied
input-output samples. Candidate formulas are encoded as small instructions so
mutation can replace individual operations.

## Engineering

- Reproducible genetic search through explicit random seeds.
- Strict parsing, complete numeric-token validation, and finite scoring.
- Strong exception safety when mutating candidate expressions.
- Portable CMake packaging with an installed `SmartGA::core` target.
- Linux and Windows CI, warning-as-error builds, and standalone consumer tests.

[View the repository](https://github.com/AABBCCDKG/SmartGA)
