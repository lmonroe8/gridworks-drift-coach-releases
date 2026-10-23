## Drift Coach — Beta Version 2.0

**Build 7.10.0 · Windows / original Assetto Corsa**

### Install or update

- **New user:** download **Gridworks-Drift-Coach-Beta-2.0.zip** (about 25.5 MB), extract it, open **START-HERE.html**, then run **Gridworks-Setup.exe**.
- **On 7.9.9 with the beta channel:** use **App Updates → Check → Download**, finish driving and choose **Restart to update**. The patch is about 1.1 MB.
- **On 7.9.7, 7.9.8, or needing an offline upgrade:** download **Gridworks-Small-Update-7.10.0.zip** (about 3.2 MB). Finish driving, close Assetto Corsa, extract it and run **Update-Gridworks.cmd**. Keep its files together.
- You need **Assetto Corsa, Content Manager, CSP and SimHub**. The app includes its private Python runtime. Stream Deck, OBS and a tablet are optional.

### New in this build

1. **Ready:** first-launch connection checks and fixes, distinguishing live acknowledgements from found files.
2. **Recorded-path replay:** play, scrub and inspect your driven path together with angle, speed, steering and pedals. Path data is used when recorded; no circuit boundaries are invented.
3. **Keep / Review / Practice:** evidence-led debriefs, event jumps, trace-quality labels and practice goals with progress.
4. **Matched setup experiments:** inspect one-change comparisons, entry/tire/road conditions and confirmed-versus-selected setup provenance. Observations do not prove a setup cause.
5. **Pit screen:** paired tablet access, automatic driving/last-run/setup pages, manual lock, quiet coaching and setup checklists.
6. **Separate Coach Tools XL profile:** highlight, bookmark, last run, setup test, quiet mode, practice, readiness and pit controls, plus eight OBS controls. The original profile and artwork are retained. Highlights save an already running OBS Replay Buffer and link its confirmed filename; no streaming or recording starts automatically.
7. **Clearer pages:** stronger black/red/white/gold hierarchy, focused review cards and a large tablet driving display.
8. **Data and performance tools:** run names/notes/favorites/search, validated backup preview/restore, conflict choices, safety backups and reviewed diagnostics. Balanced/low display modes pause hidden-tab work.

### Optional component step after an app update

From **Dash settings → Bundled downloads**, import **Angle Coach 1.2** once for Quiet Coach support. For the new Stream Deck actions, download **Coach Tools**, extract it and run **Install-Coach-Tools.cmd** once. It backs up the old plugin, restarts Stream Deck and imports the separate Coach Tools XL profile; OBS stays running and existing profiles are kept.

App patches update the app, help and bundled exports. Installed SimHub components, game links, Stream Deck plugins and runtime changes have their own installation/import paths. Profiles, setups, run records and the original runtime are preserved by this upgrade.

### Validation and feedback

187 local Python checks, eight update-interface scenarios, 36 angle-overlay scenarios, native Stream Deck asset checks and the installer harness passed. Real Chromium covers the new screens plus 27 existing regressions. All three signed upgrades reconstructed the 67-file target App inventory and preserved saved-data fixtures. The 10,000-run performance fixture measures controller work, not game FPS.

Live Windows installation, SimHub/AC rendering, OBS, tablet LAN access and physical Stream Deck behavior still need beta rig confirmation. Setup guides are starting points; no VDC driver reference runs are bundled.

Please [report a bug or your tester experience](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose) with your build, AC/CSP/SimHub versions and reproduction steps. Public downloads and update checks do not require a GitHub account.

Use the named assets below. GitHub's automatic **Source code** archives contain this release-channel repository, not the app installer. **SHA256SUMS.txt** records the download checksums.
