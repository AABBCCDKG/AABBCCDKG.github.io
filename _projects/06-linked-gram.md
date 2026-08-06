---
layout: page
title: LinkedGram
description: A race-tested Go social-domain and persistence example.
importance: 6
category: research-engineering
github: https://github.com/AABBCCDKG/LinkedGram
---

## Purpose

LinkedGram reconstructs a set of conflicting standalone translations as one
buildable Go module with clear domain and persistence boundaries.

## Engineering

- Synchronized post, comment, follow, and news-feed state with safe profile replacement.
- Bounded JSON Lines persistence and atomic credential-file replacement.
- Bcrypt-only credential storage with legacy plaintext rejection.
- Race-enabled tests, `go vet`, coverage, and pinned CI.
- Original conflicting sources preserved outside the Go build graph.

[View the repository](https://github.com/AABBCCDKG/LinkedGram)
