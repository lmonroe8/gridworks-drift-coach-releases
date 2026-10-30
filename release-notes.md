# Gridworks Drift Coach 7.15.0

## Update

**On 7.13.0 or 7.14.0:** finish your run, open **App Updates → Check for updates**, then choose **Restart to update** when the download is ready. Existing driver profiles, recordings, setups, trial dates and licenses stay in place.

**New installation or 7.12.2 and earlier:** download **Gridworks-Drift-Coach-Setup.zip**, close Assetto Corsa and Gridworks, extract the ZIP and run **Gridworks-Setup.exe**. Use the existing installation location when upgrading.

The `.gwupdate` files are used by App Updates; do not run them as installers. GitHub's Source code downloads are not the app.

## What's new

- **Scoring reliability:** qualifying results require strictly more than ten seconds of qualifying drift. Short crashes and spins do not become scored recordings. Brief transitions and speed dips remain part of the run without adding non-drifting time. Demo, interrupted, truncated and incomplete-course results cannot become clean personal bests. Matching comparisons retain the car, track/layout, compound and scoring rules.
- **Shareable run cards:** choose **Review → Run review → Export run card** to preview and download a branded 1080 × 1350 PNG. Set the public name before sharing. Private notes and license details are excluded; demo and incomplete recordings are labeled.
- **Setup wizard:** open **Settings → Setup wizard** for game-folder and live-telemetry checks, optional Car Link, SimHub and tablet steps, and your first clean saved run. Progress resumes after reopening the app. Manual display confirmation is distinguished from a live connection check.
- **Tandem reconnect fixes:** the reader checks the selected game folder and the installer's saved folder against the live car, track and layout. A brief partial file write no longer discards a still-fresh complete frame. Stale data still expires, and a partner is never silently replaced mid-run. Connection status now appears separately from partner detection.

The existing ten-second dashboard result display, driver profiles, simpler menu and license controls remain. **The online leaderboard is deferred and is not included.**

## Tandem Link 0.2

To get the updated in-game status messages, open **Drive → Tandem → Download Tandem Link**. Extract the entire ZIP, close Assetto Corsa and run **Install-Tandem-Link.cmd**. Restart the game, open Gridworks Tandem Link and enable capture. Enable Tandem Mode in Gridworks and save its settings. Drive with the intended partner and wait for **READY** before initiating.

The app update does not automatically replace the installed CSP add-on. Link 0.2 reports waiting, sending and write-error states. If Gridworks reports **Link connected** but no partner is ready, check the nearby-car count, direction of travel and partner selection.

## Verification and limits

Automated core, actual Lua exporter, Chromium, native Windows desktop and installer checks cover this update. Signed patches are verified against the target app inventory and tested for preservation of existing data and rollback on failed startup. Synthetic checks do not establish live two-car AC/CSP behavior or physical SimHub rendering; those still need confirmation on the driving rig. Tandem remains observed lead/chase capture and paired review, not calibrated competition judging.

The optional Crew Chief voice link remains off by default; audible Drift Coach playback is not part of this update's confirmed live validation.

Seven-day full-app trial, then **$5 once for a lifetime license**. Existing trial dates and licenses are retained.
