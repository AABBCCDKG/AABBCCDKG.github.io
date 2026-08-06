# Bruce Wang — Quantitative Research Portfolio

Source for [AABBCCDKG.github.io](https://aabbccdkg.github.io/), a personal site
focused on quantitative research, statistical modeling, numerical systems, and
research engineering.

## Content

- `_pages/about.md` — homepage and research positioning
- `_projects/` — implemented portfolio projects with explicit evidence boundaries
- `assets/img/personal.jpg` — homepage portrait
- `assets/img/wechat-qr.jpg` — WeChat QR image

The website intentionally does not publish a resume draft. Resume facts remain
subject to the separate human-verification workflow in the private job-search
workspace.

## Local build

The deployment environment uses Ruby 3.4.10 from `.ruby-version`, Bundler 2.5.7,
and the checked-in lockfile. Select Ruby 3.4.10 with your preferred version
manager before running:

```bash
gem install bundler -v 2.5.7
bundle _2.5.7_ install
npm ci
JEKYLL_ENV=production bundle _2.5.7_ exec jekyll build
bundle _2.5.7_ exec bundle-audit check --update
bundle _2.5.7_ exec ruby bin/check_site.rb
npm run format:check
```

The generated site is written to `_site/`.

## Deployment

A push to `master` runs `.github/workflows/deploy.yml`, builds and validates the
Jekyll site, and publishes `_site/` to the `gh-pages` branch. Pull requests run
the same build and generated-site validation without deployment. GitHub Pages
serves the deployment branch at the repository root.

## Theme attribution

This site is adapted from
[al-folio](https://github.com/alshedivat/al-folio), which is available under the
MIT License. The upstream copyright and license notice remain in `LICENSE`.
