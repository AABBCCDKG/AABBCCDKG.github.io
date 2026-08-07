---
layout: page
title: LinkedGram
description: I rebuilt conflicting Go snippets into one working module for posts, profiles, follows, and feeds.
importance: 6
category: research-engineering
emoji: 🔗
kicker: Go · Systems
accent: cyan
github: https://github.com/AABBCCDKG/LinkedGram
repository_visibility: public
tags: [Go, Concurrency, Persistence]
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
