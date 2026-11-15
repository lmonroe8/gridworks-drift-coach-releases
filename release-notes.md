# Gridworks Drift Coach 7.19.5

This release brings the pending Setup Test fixes into the public Windows download and restores the ten-second slide-time requirement for new recordings.

## What changed

- **Entry-speed matching: ±15 mph.** Setup Test allows entries within 15 mph of the first reference run, equivalent to ±24.14016 km/h. A 50 mph reference allows 35–65 mph when the other evidence matches. Collection and repeatability use the same window. Collecting tests recheck saved recordings excluded only by the old speed rule.
- **Reset Test.** A visible button clears the current experiment, counter, exclusions, recommendation and comparison, including after Stop. Saved runs and setup revisions remain available. Start a new three-run baseline when ready.
- **Reliable counter recovery.** Eligible runs can count after delayed saves, successful save retries, temporary recording-read failures or a late final setup confirmation. Each run counts once. The page shows counted, saving, checking or an exclusion reason.
- **VDC 6.0 recognition.** The garage distinguishes the installed car's declared pack version from the current VDC 6.0 reference and uses that car's exposed controls. A changed declared version requests a fresh baseline. Existing VDC 5.0 numbers are not presented as tested 6.0 presets.
- **At least ten seconds of actual sliding.** New automatic recordings, recovery captures and Setup Test evidence require ten measured qualifying slide seconds before rounding. Elapsed time and straightening/transition gaps do not add slide time. Shorter attempts finish cleanly without creating a new saved result. Existing shorter recordings and their original scores remain readable.

Completed scores retain their full ten-second display. Car/track/layout history, separate solo and tandem review with lead/chase information, the quick tablet summary, starter/already-running dashboard activation and final-score voice feedback are preserved. The offline male voice remains available, and saved voice preferences are retained. The online leaderboard remains deferred.

## Download and install

Download **Gridworks-Drift-Coach-Setup.zip**, extract it, close Assetto Corsa and run **Gridworks-Setup.exe**. The ZIP contains the installer and START-HERE guide. The installer includes the app's private runtimes and preserves saved driver data and activation.

Requires Windows 10/11 x64. If Microsoft WebView2 is missing, setup installs it once using an internet connection. Original Assetto Corsa is installed separately. Use Content Manager and CSP for the enhanced car/setup workflow. SimHub supplies the optional native dashboards and overlays.

Licensing is unchanged: a seven-day full trial, then a $5 USD one-time lifetime license. Existing activation is retained.

## Update an existing installation

Open **App Updates → Check for updates**, download the signed patch, finish driving and choose **Restart to update**. Direct in-app updates are provided for **7.17.0, 7.18.0, 7.19.0, 7.19.1 and 7.19.2**. Use the full installer if your installed version is not supported by a patch.

The optional **Gridworks-Small-Update-7.19.5.zip** is specifically for **7.19.2** installations. It contains the updater and that version's signed patch.

After the app update, close Assetto Corsa, SimHub and Stream Deck and choose **Apply component updates** if changed native dashboards are offered. This updates the main dashboard's standalone fallback to the ten-second minimum. Existing customized Stream Deck profiles do not need to be imported again.

## Validation

The release is built from source commit `6a09983f96fc8bcb44825846aa4ba965ffc28a81`. Automated checks cover duration boundaries and old-recording compatibility, Reset/Stop/restart, counter recovery, speed boundaries, VDC identity, run endings, score holds, browser interactions and Windows installation. Signed upgrade verification checks complete target-file reconstruction, rollback and preservation of saved-data fixtures for every advertised baseline.

Live Assetto Corsa driving, VDC 6.0 physics and physical SimHub/Stream Deck operation are separate from these automated checks and have not been verified on a driving rig for this release. Download checksums are provided in **SHA256SUMS.txt**.
