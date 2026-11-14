# Gridworks Drift Coach

**Production release · version 7.19.2**

A standalone Windows app for original Assetto Corsa drift practice, tandem analysis, setup work, saved run review and a paired tablet display.

## Update from inside the app

Installed **7.17.0, 7.18.0, 7.19.0 and 7.19.1** can update directly to **7.19.2** through **App Updates**. This update fixes Setup Test progress after temporary save or file-read errors and adds version-aware VDC 6.0 identification in the garage. Signed patches reuse the installed runtime and include the earlier dashboard-preview repair.

1. Open **App Updates → Check for updates**. Choose **Download update** if it has not started automatically.
2. Finish driving, close Assetto Corsa, and select **Restart to update** when ready.
3. Confirm **7.19.2**. If upgrading from 7.17 or 7.18, close Assetto Corsa, SimHub and Stream Deck before completing steps 4–5. Components already updated to 7.19 need no additional dashboard or Stream Deck profile import for this patch.
4. In App Updates, choose **Apply component updates**. These verified files are included in the download; protected folders may show **Allow Windows permission**.
5. Choose **Import Session XL layout**, reopen Stream Deck and select **Gridworks Session XL** for the two-page controls.

Existing customized Stream Deck profiles are preserved. Normal upgrades preserve drivers, saved runs, courses, setups, preferences, trial dates and licenses. Component updates validate files and keep backups with rollback support.

## New installation

[Download the 7.19.2 all-in-one Windows installer](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.2/Gridworks-Drift-Coach-Setup.zip) · [Full release notes](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.2)

Download **Gridworks-Drift-Coach-Setup.zip**, extract it, open the **Gridworks-Drift-Coach** folder and run **Gridworks-Setup.exe**. The ZIP contains the installer and Start Here guide. Older builds that report **Installer needed** also use this download.

The release also provides a [Small Update ZIP](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.2/Gridworks-Small-Update-7.19.2.zip) for installed **7.17.0, 7.18.0, 7.19.0 and 7.19.1** if the in-app connection is unavailable. Extract it, close Assetto Corsa and run **Update-Gridworks.cmd**. Normal updates use App Updates. The `.gwupdate` assets are handled by the app's signed updater.

## Fixed in 7.19.2

- **Setup Test save recovery:** a failed save stays pending and is checked after **Retry Save** succeeds. A temporary file-read error no longer permanently excludes the recording. Older active tests containing the specific temporary-save exclusion can recover that run while keeping the same evidence requirements.
- **Visible run progress:** the counter shows collecting, recording, saving or checking. The latest completed-run outcome appears below it, with an exclusion reason and a link to the saved run when available. Completion refreshes wait for an in-flight request instead of being lost, and active collection no longer tells you to park the car.
- **VDC 6.0 garage identity:** the garage separates the installed car's declared version from the latest known public pack. VDC 5.0 remains identifiable as legacy; unknown or conflicting version data stays explicit. Current values and available controls come from the installed car, and old 5.0 targets are not presented as validated 6.0 tunes.
- **Pack changes during testing:** new Setup Tests retain the declared pack/version identity. A detected change pauses collection, blocks a cross-version retest and locks the previous proposal until the matching context returns or you start a fresh baseline. Existing histories remain intact; legacy tests are not assigned a version retrospectively. Recheck a saved garage checklist after changing the installed pack.

The three-run gate, three-second qualifying recording minimum and matching requirements remain in place. Declared identity cannot prove that a mod's underlying physics are unchanged. If a run still does not count, review its visible outcome and reason in Setup Test.

## Included repair from 7.19.1

Earlier full installers omitted six packaged dashboard-preview files. The 7.19 app patch incorrectly assumed those files were installed and could fail before switching versions. 7.19.1 carries all six verified files in the patch and includes them in new installations. No manual file repair or saved-data deletion is needed. Release validation now uses each older installer's actual App staging output as well as complete prior-patch inventory fixtures.

## New in 7.19

- **Three-second minimum:** attempts under three qualifying drift seconds produce no completed score, saved run or spoken recap.
- **Full ten-second result hold:** the previous result stays visible while the next drift records.
- **Drive dashboard and private standings:** clearer live/result areas and eligible solo, course, lead and chase rankings under matching recorded conditions.
- **Three-run Setup Test:** three matched baseline runs, a supported mechanical adjustment with evidence and tradeoffs, then three matched retest runs. Initial support covers appropriate anti-roll-balance and gearing cases.
- **Automatic Track Library:** per-driver track/layout identities and observed routes, with gaps for resets, pits and missing telemetry.
- **Run clips:** link an existing local video or save an already-running OBS Replay Buffer to a qualifying run.
- **Two-page Session XL:** Drive & Review and Setup & OBS, each with 23 controls, eight empty keys and a gold bottom-right page switch. All 32 distinct functions remain available.
- **In-app component updates:** update existing supported Gridworks SimHub templates, game links and Stream Deck plugin files with validation, backups and rollback.
- **Performance and reliability:** background metadata saves, slower non-live polling, bounded track sampling, saved-run timestamp precision and tablet disconnect recovery.

Local voice still announces the local driver's final score only. The **community leaderboard service remains unconfigured** and scores/videos are not automatically uploaded. **Event Director remains separate.** Tandem results are observed-data practice estimates.

## Existing capabilities

Separate Solo/Tandem Run Review tabs, lead/chase and partner filters, saved views, run cards, driver profiles, setup guides/import/export, course authoring and Course Test, zoomable review maps, a resumable setup wizard, first-time tour with Don't show this again, and page-specific Help remain included.

The offline male voice pack, local voice volume and optional Crew Chief integration remain included. Optional SimHub dashboards/overlays, Stream Deck XL profiles, OBS controls and icons are bundled. Open **Settings → Setup wizard** for guided setup.

Earlier notes: [7.19.1](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.1), [7.19](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.0), [7.18](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.18.0), [7.17](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.17.0), [7.16](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.16.0), [7.15](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.15.0), [7.14](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.14.0).

## Requirements

- Windows 10/11 x64 and original Assetto Corsa.
- Content Manager and CSP for the supported full car/setup workflow.
- Microsoft WebView2 Runtime for the desktop window; setup reuses it or installs Microsoft's signed runtime when missing.
- SimHub is optional for native dashboards and overlays. A tablet, Stream Deck XL, OBS and a second display are optional.

Private runtimes are included. Keep the PC app open while recording and using the tablet.

## Seven-day full-app trial, then $5 lifetime

The full-app trial lasts seven calendar days from the first trial-enabled launch. Closing the app does not pause it. Updating preserves the original trial dates and existing lifetime licenses; it does not start another trial.

After the trial, a **$5 USD one-time lifetime license** restores full access with no subscription or expiry. Live coaching/recording, new setup/course work and the paired tablet require trial or licensed access. Saved runs/setups remain readable and exportable; backups, support, updates and activation remain available. License includes saved setup downloads without a connected car.

Open **Settings → License → Buy $5 lifetime license** for Stripe checkout. The verified signed release configuration supplies checkout and includes this PC's random installation reference. Use an email address you can receive mail at. After verified settled payment, the hosted service emails a ZIP containing the signed `.gwlicense` file. Extract it and import the license in the app. Sandbox licenses do not activate the public app. Keep license files and installation IDs private.

Normal updates/reinstalls that retain user data preserve activation and trial dates. Trial tracking is local; license management stays on the PC. Codes, customer names and installation identity are excluded from telemetry and diagnostics. User-data backups exclude activation and trial records.

## Tablet

Open **Settings → Tablet → Enable tablet display** for the address, QR code, six-digit pairing code and copy buttons. Use the same home network, scan the QR code or open the address, then enter the pairing code. Codes expire after ten minutes; paired browsers reconnect for thirty days, including after app restarts.

The tablet shows driving information, a quick latest-run summary and short setup checklists. Full traces, replay, detailed analysis and setup review remain in the PC app. Fullscreen, screen lock, reconnect status and Private-network firewall help are included.

## Scoring and saved data

Practice estimates and authored-course scores remain distinct. Course scoring requires defined targets/gates; vehicle-centre line and automated style are estimates. Interrupted runs use the telemetry captured before the interruption. No automatic collision blame or invented deductions for missing evidence.

New saved runs require **at least three qualifying drift seconds**. Short/nonqualifying attempts are excluded from saved history, completed results and spoken recaps. Each ready result stays visible for ten full seconds while a new drift may record. Course and tandem scoring still require their own usable evidence. Save/analysis failures show an explicit retryable state. Driver profiles keep personal runs, setups and preferences separate.

## Guides

Use installed 7.19.2 guides and page Help for the current features. The older [49-page visual manual](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.14.0/Gridworks_Drift_Coach_7.14_Visual_Instruction_Manual.pdf) and [screenshot pack](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.14.0/Gridworks_Drift_Coach_7.14_Screenshot_Pack.zip) remain available as **7.14 references**, not updated 7.19.2 manuals. Their screenshots use demonstration data and native-template previews.

## Support and validation

[Report an issue or suggest a feature](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose). Include the app version, car/track, installed car-pack version, AC/CSP versions, display/browser and reproduction steps. For a Setup Test issue, include the outcome or exclusion reason shown below the counter.

Release checks passed for the 7.19.2 source tree shared by the release commit and merged main. [Windows desktop CI](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/43632572261) passed native WebView2 startup/shutdown, full-installer upgrade, standalone installation and installer packaging; [App checks](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/43632572231) also passed. The final local installer ZIP contains exactly the installer and Start Here guide, and its embedded payload and all seven staged release-file checksums match the verified artifacts. Signed-update validation passed all **16 success/rollback scenarios** across **7.17.0, 7.18.0, 7.19.0 and 7.19.1**, using both actual installer staging and explicitly modeled prior-patch origins. Every reconstructed target matched all **253 App files** byte for byte; runtime bytes and saved-data fixtures were preserved. All seven public release downloads were retrieved without authentication and verified against their expected byte counts and SHA-256 checksums after the [publishing workflow](https://github.com/lmonroe8/gridworks-drift-coach-releases/actions/runs/43642683908) passed. The production update feed now offers 7.19.2. [Validation record](validation/7.19.2.json).

**Automated checks do not establish live VDC 6.0 handling or physical-rig behavior.** Real AC/CSP driving and device testing remain necessary. Signed-update reconstruction uses explicit process/readiness fixtures; scores remain practice estimates.

This repository hosts public downloads and signed feeds. App source stays in a separate private repository. Publishing downloads does not grant an open-source license for the app; third-party notices and terms remain applicable.
