---
layout: page
title: World Cup Forecasting
description: Chronological football probability models with calibration-aware evaluation.
importance: 1
category: quant-research
---

## Research question

How well can pre-game international football outcomes be modeled when every
prediction is restricted to information available before the match?

## Implemented

- Elo with a Davidson draw model and a Dixon–Coles goals model.
- Strict yearly walk-forward evaluation with log loss, Brier score, and
  expected calibration error.
- Neutral-venue handling and optional squad-strength features.
- A Python 3.11 package with strict type checking, deterministic tests, a
  frozen dependency lock, and CI.

The published table in the repository records a historical evaluation run.
Upstream match data changes over time, so rerunning the method does not
guarantee the exact same row count or metrics without the original data
snapshot.

Repository access is available on request while the research package is being
prepared for public release.
