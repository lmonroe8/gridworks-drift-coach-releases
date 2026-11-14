# Gridworks Drift Coach 7.19.2

## Setup Test progress and VDC 6.0

This update repairs Setup Test progress after temporary save or file-read errors, makes each completed run's outcome visible, and updates the garage to identify VDC 6.0 separately from older or unknown installed versions.

### Runs recover after a successful save retry

A failed save stays pending while you use **Retry Save**. After the retry succeeds, Setup Test checks the recording again. Temporary file-read errors also remain retryable. Older active tests containing the specific temporary-save exclusion can recover that run without relaxing the evidence requirements.

The counter now shows whether the app is **collecting, recording, saving or checking**. The latest completed-run outcome appears directly below it, including an exclusion reason and a link to the saved run when available. A completion refresh arriving during another request is queued, and active collection no longer displays the start-only instruction to park the car.

The three-run gate, three-second qualifying recording minimum and matching requirements remain in place. A saved run can still be excluded when its evidence or recorded conditions do not meet the test requirements; the visible reason explains that decision.

### The garage recognizes declared VDC 6.0 identity

The garage separates the **installed car's declared version** from the **latest known public pack, VDC 6.0**. It identifies VDC 5.0 as legacy and leaves unknown or conflicting metadata explicit. A generic VDC car name does not automatically become version 6.0.

Current setup values and available controls come from the installed car. Historical 5.0 targets are not relabeled as validated 6.0 tunes. When the detected pack or car revision changes, the garage refreshes its selection and asks you to recheck the current controls. The previous saved checklist is retained until you save a replacement.

### Setup Tests retain the pack identity

New tests retain the declared pack/version identity alongside their baseline. A detected change blocks further collection or a cross-version retest and locks the previous proposal until you restore the matching context or start a fresh baseline.

Legacy tests keep their history without being assigned a pack version retrospectively. Start a fresh baseline after changing packs. Identity metadata does not verify that a mod's underlying physics are unchanged.

## Update to 7.19.2

Direct signed app updates support installed **7.17.0, 7.18.0, 7.19.0 and 7.19.1**. The patches retain the existing production trust configuration and reuse the installed runtime. Driver profiles, runs, courses, setups, preferences, trial dates and licenses remain outside the app's version folder.

1. Open **App Updates → Check for updates** and confirm that the offered version is **7.19.2**.
2. Choose **Download update** if it has not started automatically.
3. Finish driving, close Assetto Corsa and choose **Restart to update**.
4. Confirm **7.19.2** after the app restarts.

If the in-app connection is unavailable, the [Small Update ZIP](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.2/Gridworks-Small-Update-7.19.2.zip) supports the same four starting versions. Extract it, close Assetto Corsa and run **Update-Gridworks.cmd**. The `.gwupdate` files are handled by the signed updater.

For a new installation or an **Installer required** notice, use the [all-in-one Windows installer](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.2/Gridworks-Drift-Coach-Setup.zip). Extract the ZIP, open **Gridworks-Drift-Coach** and run **Gridworks-Setup.exe**. The download contains the installer and Start Here guide.

### Components when upgrading from 7.17 or 7.18

After the app restart, close Assetto Corsa, SimHub and Stream Deck. In **App Updates**, choose **Apply component updates**, then explicitly choose **Import Session XL layout**. Reopen Stream Deck and select **Gridworks Session XL** for its two pages. Protected folders may show **Allow Windows permission**. Customized Stream Deck profiles are preserved.

Components already updated for 7.19 need no additional dashboard or Stream Deck profile import for 7.19.2. This patch changes the app and its help.

## The 7.19.1 dashboard-preview repair remains included

Earlier full installers omitted six packaged dashboard-preview files. An app update could then fail with a missing `Dashboard-Preview/Detailed-Dash.json` error before switching versions. The repair carries all six authenticated preview files in supported patches and includes them in new installations. No manual preview-file repair or saved-data deletion is required.

The other 7.19 features remain included: the ten-second result hold, private standings, automatic Track Library, local run clips, two-page Session XL and controlled component updates. Event Director remains separate.

## Validation

Release checks passed for the 7.19.2 source tree shared by the release commit and merged main. [Windows desktop CI](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/43632572261) passed native WebView2 startup/shutdown, full-installer upgrade, standalone installation and installer packaging; [App checks](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/43632572231) also passed. The final local installer ZIP contains exactly the installer and Start Here guide, and its embedded payload and all seven staged release-file checksums match the verified artifacts. Signed-update validation passed all **16 success/rollback scenarios** across **7.17.0, 7.18.0, 7.19.0 and 7.19.1**, using both actual installer staging and explicitly modeled prior-patch origins. Every reconstructed target matched all **253 App files** byte for byte; runtime bytes and saved-data fixtures were preserved. All seven public release downloads were retrieved without authentication and verified against their expected byte counts and SHA-256 checksums after the [publishing workflow](https://github.com/lmonroe8/gridworks-drift-coach-releases/actions/runs/43642683908) passed. The production update feed now offers 7.19.2. [Validation record](validation/7.19.2.json).

Regression checks cover save failure and retry, recovery of eligible older exclusions, temporarily unreadable recordings, final setup-sample waiting, recorder-to-archive acceptance, duplicate prevention, pack changes with identical raw setup values, legacy journals, blocked cross-version retests, installed-metadata refresh and queued browser refreshes.

Automated checks do not establish live VDC 6.0 handling or physical-rig behavior. Signed-update reconstruction uses explicit process/readiness fixtures; real AC/CSP driving and device testing remain necessary. Scores remain practice estimates.

If a run still does not count, [report the issue](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose) with the app version, installed car-pack version, car/track, AC/CSP versions and the outcome or exclusion reason shown below the Setup Test counter.
