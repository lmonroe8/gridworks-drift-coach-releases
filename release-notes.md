# Gridworks Drift Coach 7.19.6

Setup Test now accepts more ordinary variation between runs, so small changes in temperature, route position or a brief shift are less likely to keep the counter from progressing.

## More forgiving matching

| Check | Matching window |
| --- | --- |
| Usable trace coverage | At least **85%** |
| Route start and finish | Within **30 m** |
| Driven distance | Within **±30%** |
| Starting rear tire core temperature | Within **±25°C** |
| Road and reported air temperature | Within **±10°C** |
| Reported surface grip | Within **±0.05** |

**Brief shifts are allowed.** Use the same primary drift gear across the test, with at least **70% of measured forward-gear slide time** in that gear.

The entry-speed window remains **±15 mph (±24.1 km/h)**. Each run still needs **ten qualifying slide seconds** and an original saved solo recording. Keep the same complete, confirmed setup within each collection stage. Three accepted runs are required before the evidence review, and the recommendation and A/B comparison checks remain in place.

Active baseline and retest collections recheck original recordings rejected by the matching rules relaxed in this update. The remaining evidence requirements still apply. Completed tests, historical recordings and original scores are preserved. Open Setup Test or choose **Refresh Evidence** to recheck a collecting test; resetting it is not required. The page shows the current windows and explains why a run did not count.

Reset Test, save/counter recovery, VDC 6.0 identity checks, the ten-second result display and existing solo/tandem review remain available. Separate Practice mode is unchanged. The online leaderboard remains deferred.

## Update or install

**In-app update:** Open **App Updates → Check for updates** and download the compatible signed patch. Finish your session, close Assetto Corsa and choose **Restart to update**. Direct patches support **7.17.0, 7.18.0, 7.19.0, 7.19.1, 7.19.2 and 7.19.5**.

**Offline update from 7.19.5:** Download **Gridworks-Small-Update-7.19.6.zip**, extract it, close Assetto Corsa and run **Update-Gridworks.cmd**. This ZIP is specifically for installed **7.19.5**.

**New installation or another version:** Download **Gridworks-Drift-Coach-Setup.zip**, extract it, open the **Gridworks-Drift-Coach** folder and run **Gridworks-Setup.exe**. The installer includes the app's private runtimes and retains saved driver data and activation. Windows 10/11 x64 is required; missing WebView2 may need an internet connection for its installation. Assetto Corsa, Content Manager, CSP and optional SimHub are installed separately.

After updating, choose **Apply component updates** if offered, with Assetto Corsa, SimHub and Stream Deck closed. Existing customized Stream Deck profiles do not need to be imported again.

Licensing remains a **seven-day full trial, then $5 USD once for a lifetime license**. Existing profiles, saved setups, trial dates and activation are retained.

## Validation scope

Release source: `ffd1084a784c75833f34848f1e2cf60817a12766`.

Automated verification covers matching boundaries, time-weighted primary-gear measurement, active-test rechecks, historical evidence preservation, the displayed requirements, Windows installation and signed upgrades. Upgrade verification checks complete target-file reconstruction, rollback and preserved saved-data fixtures for all six advertised baselines.

Live Assetto Corsa/CSP driving and physical Windows/SimHub operation have not been verified on a driving rig for this release. Download checksums are provided in **SHA256SUMS.txt**.
