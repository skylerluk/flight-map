# Skyler · Flight Journal 2026

An offline-capable personal flight atlas, built with vanilla HTML, CSS and JavaScript. No package install or API keys required.

## Develop

```sh
python3 build.py
python3 -m http.server 8766 --bind 127.0.0.1
```

Open http://127.0.0.1:8766. Edit `template.html` for layout/styles, `app.js` for behavior, and the flight records in `build.py`. Build regenerates `data.js`, `index.html` and the portable `2026-flight-journal.html`. Both HTML files embed all required assets and can be opened offline.

## Features

- Pacific-centered atlas, keyboard-accessible route selection, pan and zoom
- Flight-ticket detail panel with previous/next navigation
- Departure-month filters and an animated journey replay with pause, scrub and step controls
- Stats, monthly departures, airport ranking and searchable flight log
- December 2025 scope toggle; reduced-motion support and responsive layouts

## Data

30 recorded flight legs in 2026; 32 including December 2025. Source/uncertainty notes remain attached to the records. Airport distances use great-circle calculations; airtime is a rough distance-based estimate, not a measured duration. The last records review was October 4, 2026. This repository contains the personal flight data rendered by the journal.

## Design references

Inspired by the user's Tobi article: start with a product-specific concept, render, critique and refine. Concept: a personal airline field journal.

Three references browsed on recent.design:
- [Paper Receipt — Kirill Migel](https://recent.design/i/xeax4oj-crumplable-paper-receipt): tactile paper treatment adapted to the ticket details and travel record.
- [Sam Cheng Personal Site](https://recent.design/i/uugl3yv-sam-cheng-personal-site): oversized editorial typography and a personal badge adapted to the journal identity.
- [Invite Code Microinteraction — Nitish Khagwal](https://recent.design/i/ex3s3bx-invite-code-microinteraction): compact expanding interaction adapted to journey replay controls and ticket transitions.

## Third-party assets

D3 7.9.0 (ISC), topojson-client 3.1.0 (ISC), World Atlas / Natural Earth geography and OurAirports coordinates via DataHub. Libraries and geography are vendored in `assets/`; see `THIRD_PARTY.md` for sources. No reference-site media is copied into the app.
