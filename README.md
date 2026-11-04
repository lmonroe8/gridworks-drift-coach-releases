# Gridworks Drift Coach

**Production release · version 7.18.0**

A standalone Windows app for original Assetto Corsa drift practice, tandem analysis, setup work, saved run review and a paired tablet display.

## Download and install

[Download the 7.18 all-in-one Windows installer](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.18.0/Gridworks-Drift-Coach-Setup.zip) · [Release notes](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.18.0)

**Use the full installer for this update**, including existing 7.17 users. It refreshes the installed SimHub templates and Assetto Corsa Tandem Link as well as the app.

1. Finish your session and close Assetto Corsa, Gridworks and SimHub.
2. Back up saved data as a precaution. Do not uninstall the app or delete its user-data folder.
3. Extract **Gridworks-Drift-Coach-Setup.zip**, open its **Gridworks-Drift-Coach** folder and run **Gridworks-Setup.exe**.
4. Retain the existing game/SimHub locations when following setup. Open the desktop shortcut and confirm **7.18.0**.

The ZIP contains the Windows setup executable and Start Here guide—not development source. Setup preserves existing runs, profiles, courses, setups, trial dates, licenses and preferences.

**App Updates:** a signed **7.17.0 → 7.18.0** patch is available on the existing stable-recovery channel. It updates the app and bundled exports, not already-installed SimHub templates or game-link files. Use the full installer for the complete integration refresh. Older versions also need the full installer. A `.gwupdate` file is handled by the app; do not double-click it or copy it into SimHub.

GitHub's automatic **Source code** ZIPs contain this release-channel repository. Choose the named installer asset above instead.

## New in 7.18

- **Two numeric tandem results:** independent lead/chase practice scores, component breakdowns and data-coverage labels. No letter grades or automatic winner.
- **Stable saved results:** versioned scoring snapshots retain the completed assessment instead of silently changing new saved runs after a scoring update.
- **Immediate finish results:** shared app/Run Review/SimHub results, retaining the ten-second finish window.
- **Partner ending conditions:** locked-partner pit teleports/resets and sustained crash/spin evidence end the shared run. Missing telemetry does not automatically fail a driver; motion estimates do not assign collision blame.
- **Review and progress:** clickable observed events, one evidence-based improvement tip per driver, and compatible solo/lead/chase session comparisons.
- **Dashboard refresh:** six layouts, eight read-only preview states, angle guides, clearer partner status, bounded long names, and original branding/classic controls preserved.

Local voice still announces the local driver's final score only. **The online leaderboard remains deferred. Event Director remains separate.** Tandem scoring is observed-data practice feedback, not official competition judging.

## Existing capabilities

Separate Solo/Tandem Run Review tabs, lead/chase and partner filters, saved views, run cards, driver profiles, setup guides/import/export, course authoring and Course Test, zoomable review maps, a resumable setup wizard, first-time tour with Don't show this again, and page-specific Help remain included.

The offline male voice pack, local voice volume and optional Crew Chief integration remain included. Optional SimHub dashboards/overlays, Stream Deck XL profiles, OBS controls and icons are bundled. Open **Settings → Setup wizard** for guided setup.

Earlier notes: [7.17](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.17.0), [7.16](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.16.0), [7.15](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.15.0), [7.14](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.14.0).

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

New saved runs require **more than ten seconds of qualifying drift**, not merely ten seconds of elapsed recording. Short/nonqualifying attempts are excluded from saved history and the completed-score display. Save/analysis failures show an explicit retryable state. Driver profiles keep personal runs, setups and preferences separate.

## Guides

Use installed 7.18 guides and page Help for the current features. The older [49-page visual manual](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.14.0/Gridworks_Drift_Coach_7.14_Visual_Instruction_Manual.pdf) and [screenshot pack](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.14.0/Gridworks_Drift_Coach_7.14_Screenshot_Pack.zip) remain available as **7.14 references**, not updated 7.18 manuals. Their screenshots use demonstration data and native-template previews.

## Support and validation

[Report an issue or suggest a feature](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose). Include the app version, car/track, AC/CSP versions, display/browser and reproduction steps.

The exact 7.18 source passed automated application/browser, tandem scoring/end-condition, native dashboard binding/export, Windows desktop, upgrade/install and final packaging checks. The published installer/patch sizes and SHA-256 digests match the verified artifacts. The signed patch was accepted by the 7.17 client and reconstructed all 222 target App files; success and failed-readiness rollback scenarios preserved saved-data fixtures.

**Real two-car Assetto Corsa/SimHub calibration and every physical audio/display configuration are not established by automated tests.** Crash detection is motion-based, and scores remain practice estimates. Real hardware/multiplayer feedback is still needed.

This repository hosts public downloads and signed feeds. App source stays in a separate private repository. Publishing downloads does not grant an open-source license for the app; third-party notices and terms remain applicable.
