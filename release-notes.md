## Gridworks Drift Coach 7.12.2

**Immediate run results and separate PC/tablet Pit views.**

### An ended attempt always has a result

Straightening after a slide, returning or teleporting to pits, a position reset or another detected interruption finalizes the captured attempt immediately. The result shows the finish reason, a numeric score and its save status. A pit/reset sample is excluded from the preceding run, and a brief reset cooldown prevents a ghost run.

Free practice now receives a clearly labelled **Drift practice estimate**: Angle target 60, Angle control 25 and Drift continuity 15. It uses only captured telemetry. An interrupted result explains that it covers the part of the run recorded before interruption. Insufficient usable data produces 0 with an explanation, rather than an empty score.

When an authored course and required coverage are available, the full **Line 40 / Angle 40 / Estimated style 20** course result replaces the immediate estimate after analysis. Practice estimates remain distinct from course scores and qualifying bests. These are independent practice estimates, not official judging.

Attempts lasting at least **ten seconds** are saved individually by car/track, including interrupted attempts. Shorter attempts still display a score and finish reason but are not archived. Save/analysis failures show an explicit retryable error while keeping the immediate result visible.

### PC Pit review and tablet summary

The PC **Pit screen** now includes score components, deductions, eight measured run summaries, transition details with individual review links, coaching, recent saved runs and the complete selected setup checklist. Replay, transition and setup controls open the corresponding PC detail pages.

The paired tablet stays concise: score, mean angle, duration and one next-run focus, plus a short setup checklist. It directs full review back to the PC. Full traces, analysis and administration are no longer exposed through the tablet gateway.

### Install or update

Download **Gridworks-Drift-Coach-Setup.zip**, extract it and double-click **Gridworks-Setup.exe**. Requirements: Windows 10/11 x64, original Assetto Corsa, Content Manager and CSP for the supported workflow. SimHub is optional.

Builds **7.9.9, 7.10.0, 7.10.1, 7.10.2, 7.11.0, 7.11.1, 7.12.0 and 7.12.1** can use **App updates → Check for updates → Restart to update**. Finish driving first. The 7.12.1 patch is about **143 KB**; the 7.12.0 patch is about **163 KB**. Saved data, trial dates, lifetime licenses and the private runtime are preserved. The separate manual **Gridworks-Update-7.12.2.zip** supports **7.10.2** only; other supported versions use the app updater or full installer.

The **seven-day full-app trial, then $5 USD once for a lifetime license** is unchanged. Updating from 7.12.1 does not restart the trial. Open **License → Request a $5 lifetime license** for manual purchase instructions; import the signed `.gwlicense` file after payment is confirmed. Automatic checkout and license delivery are not connected yet.

### Validation

275 core tests and the update interface checks passed. Real Chromium covered a live captured attempt interrupted by a pit return, visible scores on both displays, saved interrupted status, working run/transition links, separate PC/tablet layouts, active and expired trials, activation and update notifications. Windows checks passed for native launch, automatic installation without SimHub, migration through the old update worker and the installer package. All eight signed update baselines reconstruct the exact target app and preserve data and licenses.

[Report a problem or suggestion](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose).
