---
layout: page
title: EchoGen
description: Safe image-to-physics prototyping with a validated simulation DSL.
importance: 5
category: research-engineering
github: https://github.com/AABBCCDKG/EchoGen
---

## Purpose

EchoGen explores how multiple vision-language-model samples can be aggregated
into a simplified 2D physics scene without executing model-generated code.

## Safety and validation

- AST parsing with a small allowlist of simulation operations.
- Finite numeric and geometry checks.
- Deterministic one-to-one matching for repeated objects across model samples.
- Fail-closed handling for ambiguous or distant matches.
- Offline fixtures, packaged sample assets, and Python 3.9/3.11 CI.

This is a research prototype, not a physically accurate predictor.

[View the repository](https://github.com/AABBCCDKG/EchoGen)
