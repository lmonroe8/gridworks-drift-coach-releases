# Gridworks Drift Coach

**Production release · version 7.19.0**

A standalone Windows app for original Assetto Corsa drift practice, tandem analysis, setup work, saved run review and a paired tablet display.

## Update from inside the app

Installed **7.17.0 and 7.18.0** can update directly to 7.19.0 through **App Updates**. The 7.18 update is approximately **21 MB** and reuses the installed runtime.

1. Open **App Updates → Check for updates**. Choose **Download update** if it has not started automatically.
2. Finish driving, close Assetto Corsa, and select **Restart to update** when ready.
3. Confirm **7.19.0**, then close Assetto Corsa, SimHub and Stream Deck.
4. In App Updates, choose **Apply component updates**. These verified files are included in the download; protected folders may show **Allow Windows permission**.
5. Choose **Import Session XL layout**, reopen Stream Deck and select **Gridworks Session XL** for the two-page controls.

Existing customized Stream Deck profiles are preserved. Normal upgrades preserve drivers, saved runs, courses, setups, preferences, trial dates and licenses. Component updates validate files and keep backups with rollback support.

## New installation

[Download the 7.19 all-in-one Windows installer](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.0/Gridworks-Drift-Coach-Setup.zip) · [Full release notes](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.0)

Download **Gridworks-Drift-Coach-Setup.zip**, extract it, open the **Gridworks-Drift-Coach** folder and run **Gridworks-Setup.exe**. The ZIP contains the installer and Start Here guide. Older builds that report **Installer needed** also use this download.

The release also provides a **Small Update ZIP for installed 7.18.0** if its in-app connection is unavailable. Normal updates use App Updates. The `.gwupdate` assets are handled by the app's signed updater.

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

Earlier notes: [7.18](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.18.0), [7.17](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.17.0), [7.16](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.16.0), [7.15](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.15.0), [7.14](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.14.0).

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

Use installed 7.19 guides and page Help for the current features. The older [49-page visual manual](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.14.0/Gridworks_Drift_Coach_7.14_Visual_Instruction_Manual.pdf) and [screenshot pack](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.14.0/Gridworks_Drift_Coach_7.14_Screenshot_Pack.zip) remain available as **7.14 references**, not updated 7.19 manuals. Their screenshots use demonstration data and native-template previews.

## Support and validation

[Report an issue or suggest a feature](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose). Include the app version, car/track, AC/CSP versions, display/browser and reproduction steps.

The 7.19 package matches the verified application sources, guides, integration payloads and two-page Stream Deck profile. Both supported versions' shipped updaters accept the signed manifest and reconstruct all 253 target App files. Success and failed-readiness rollback fixtures preserve the prior installation and saved data. The public release assets have independently checked sizes and SHA-256 digests. See the release notes for validation scope and the remaining driving-PC checks.

**Real two-car AC/CSP calibration, intended-mod setup tests, physical SimHub/Stream Deck import, actual OBS clip paths and Windows component permissions still need driving-rig validation.** The signed-update reconstruction uses explicit process/readiness fixtures and does not claim a live Windows restart. Scores remain practice estimates.

This repository hosts public downloads and signed feeds. App source stays in a separate private repository. Publishing downloads does not grant an open-source license for the app; third-party notices and terms remain applicable.

