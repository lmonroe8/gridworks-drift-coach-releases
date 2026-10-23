## Drift Coach — Beta Version 2.0

**Build 7.10.1 · Windows / original Assetto Corsa**

### Install or update

- **On 7.10.0:** open **App Updates**, check for the update, then **Restart to update** after driving. The changed-file patch is about 130 KB. Native dashboards and Stream Deck exports are byte-identical to 7.10.0; no reimport is needed.
- **On 7.9.9:** use App Updates or the small upgrade below. This patch also includes the 7.10.0 coaching tools. For their optional native features, import Angle Coach 1.2 and run Coach Tools from Bundled downloads once.
- **Offline upgrade from 7.9.9/7.10.0:** extract **Gridworks-Small-Update-7.10.1.zip**, close Assetto Corsa and run **Update-Gridworks.cmd**. Keep the files together. Your installed runtime and saved data are reused.
- **New user or older build:** extract **Gridworks-Drift-Coach-Beta-2.0.zip**, read **START-HERE.html** and run **Gridworks-Setup.exe**. The download has exactly those two files.
- You need **original Assetto Corsa, Content Manager, CSP and SimHub**. Stream Deck, OBS and a tablet are optional. Python is included privately with the app.

### Fixed controls and clearer pages

Saved-result links, Profile Best and the Pit screen now open the selected archived run. Paired tablets can open read-only run breakdowns and return to Pit; administrative commands remain on the gaming PC. Action errors appear visibly. The duplicate live recap and second setup-comparison card have been removed; each selected run and setup experiment has one review.

### Individual transition and range breakdown

Run review has **Overview**, **Transitions**, **Sections & range**, **Driver inputs** and **Notes & video** tabs. Select a confirmed direction change to inspect threshold-to-threshold time, signed entry/exit angles, speed change, throttle/brake/clutch use and time to regain the target. Short sign chatter and crossings over missing-data gaps are excluded.

Sections follow measured direction changes. Select a phase or mark an arbitrary start/end time to measure it, zoom the trace and loop the replay. Metrics are weighted by observed time; gaps over 300 ms are excluded. Recorded traces normally sample every 100 ms, so timing is an estimate at that resolution. Handbrake input is not inferred. Existing traces can be analyzed without re-recording; summary-only legacy records remain limited.

### Scoring sources

**Gridworks training** now works directly from qualifying saved telemetry. Its personal practice index is **60% angle control + 40% continuity**, with component percentages and weighted contributions visible in each run. Missing, interrupted, truncated or insufficient-coverage traces are not rated. Compare the same car, route, compound and training profile. This is not competition judging; line, clipping zones and proximity are not scored.

**Damgam points** stays separate and retains its original calculations. Gridworks identifies missing, invalid, stopped, frozen and other-layout exports, reloads changed configuration and recovers a live export in the connected game folder even if an old folder still exists. Keep **Drift Score Display** running inside Assetto Corsa; use **Recheck Damgam link** after fixing it. A custom unsupported scorer is not silently overwritten.

### Validation and feedback

223 Python checks, eight update-interface scenarios and 52 actual Chromium scenarios cover app behavior, measurements, scoring, source separation, selected-range replay, setup tools and paired-tablet access. Installer staging/worker/launcher and native export checks also passed. Both signed upgrades reconstruct all 69 target App files while preserving saved-data fixtures, the existing runtime and the previous app version.

These are automated and protocol fixtures. Live AC/CSP, SimHub/OBS, physical devices and a real Windows install still need beta rig confirmation.

[Report a problem or share your tester experience](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose). Include your build, AC/CSP/SimHub versions, which control you clicked and what happened. Use the named release assets; GitHub's automatic Source code downloads contain the release-channel repository, not the app installer.
