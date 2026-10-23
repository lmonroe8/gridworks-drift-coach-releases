## Drift Coach — Beta Version 2.0

**Build 7.10.2 · Windows / original Assetto Corsa**

### New: an update reminder each time you open the app

When a newer version is available, Gridworks opens a notification showing your installed build and the available build. It tells you to open **APP UPDATES → CHECK FOR UPDATES**, then finish driving and choose **RESTART TO UPDATE** when the patch is ready.

- **LATER** or Escape closes the popup for this opening only. It returns the next time you open Gridworks until the latest build is installed.
- Downloading a patch does not clear the reminder; installing and running the current version does.
- A previously found update is remembered using signed release metadata and shown again on an offline launch. Reconnect to check/download it. A new release cannot be discovered while offline.
- The banner and sidebar indicator remain after dismissal, including after a failed check/download.
- Reopening the PC app starts a background check even when the local controller is already running. Hidden pages and paired tablets do not manage updates.
- The notification waits for another dialog to close and fits narrow screens. It does not restart the app automatically.

### Install or update

- **On 7.10.1:** open **App Updates**, choose **Check for updates**, then **Restart to update** after driving. The patch is about **63 KB**.
- **On 7.10.0:** use the same updater; its patch is about **139 KB**.
- **On 7.9.9:** use App Updates or the small ZIP. For optional features introduced in 7.10.0, follow the existing Angle Coach 1.2 / Coach Tools import instructions.
- **Manual update from 7.9.9/7.10.0/7.10.1:** extract **Gridworks-Small-Update-7.10.2.zip**, close Assetto Corsa and run **Update-Gridworks.cmd**. Keep the extracted files together.
- **New user or older build:** extract **Gridworks-Drift-Coach-Beta-2.0.zip**, read **START-HERE.html** and run **Gridworks-Setup.exe**. The download contains exactly those two files.

Saved profiles, setups, runs and reference recordings stay in place. The existing private runtime is reused by app updates. **SimHub dashboards and Stream Deck exports are unchanged from 7.10.0/7.10.1; no reimport is needed from those builds.**

You need **original Assetto Corsa, Content Manager, CSP and SimHub**. Stream Deck, OBS and a tablet are optional. A separate Python installation is not required.

### Existing coaching tools

This update retains the transition and section/range breakdowns, looped replay, setup import/export, paired tablet review, Gridworks practice index and separate original Damgam points from 7.10.1. See the included Complete Coach Guide for measurements, scoring limits and setup workflows.

### Validation and feedback

212 core Python checks and 24 update-interface scenarios passed. Actual Chromium checks cover repeated openings, dismissal, current/newer installed versions, offline/error states, ready-to-restart notices, the installer route, dialog handling and narrow screens, along with the existing coaching/scoring regressions. Each of the three signed upgrade paths reconstructs all 69 target App files and preserves saved-data fixtures and the installed runtime. Installer staging and Win32 bootstrap checks passed.

These are automated tests and protocol fixtures. A live Windows / AC / CSP / SimHub rig still needs beta confirmation.

[Report a problem or share your experience](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose). Use the named release assets; GitHub's automatic Source code archives are not the app installer.
