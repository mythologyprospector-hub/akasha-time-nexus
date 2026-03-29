# akasha-time-nexus

Akasha-native context engine that expands a plain event timestamp into a multi-axis record of world time, environmental state, and cyclical context.

## What it is

`akasha-time-nexus` is the temporal/context core for Akasha.

Given:

- a UTC timestamp
- a latitude
- a longitude
- optional event metadata

it returns a normalized context bundle such as:

- local civil time
- sunrise / sunset
- day / night status
- moon phase / illumination
- season / day-of-year
- weather snapshot
- optional tide / geomagnetic context
- derived offsets and query-friendly fields

This is **not** an interpretation engine. It does not decide what an event means.
It produces **structured world-state context** so that higher Akasha layers can analyze patterns honestly.

## Why it exists

Most observations are logged with only:

- date
- time
- note

That is too thin for pattern analysis.

Akasha Time Nexus treats time as a **bundle of concurrent clocks and conditions**.

## MVP scope

V1 includes:

- event ingestion model
- normalized context model
- local/UTC clock expansion
- season/day-of-year derivation
- sunrise/sunset enrichment stub
- lunar enrichment stub
- weather enrichment stub
- SQLite storage layer
- CLI example path

V1 intentionally ships with conservative stub enrichers so the architecture is locked down before API sprawl begins.
