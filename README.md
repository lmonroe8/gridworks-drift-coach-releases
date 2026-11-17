# Gridworks Drift Coach

**Production release · version 7.19.8**

A standalone Windows app for original Assetto Corsa drift practice, tandem analysis, setup work, saved run review and a paired tablet display. Use Content Manager and CSP for the full car/setup workflow; SimHub is optional for native dashboards and overlays.

[Download the 7.19.8 all-in-one Windows installer](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.8/Gridworks-Drift-Coach-Setup.zip) · [Full release notes](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.8)

## Update from inside the app

The signed online update supports these exact installed builds: **7.17.0, 7.18.0, 7.19.0, 7.19.1, 7.19.2, 7.19.5, 7.19.6 and 7.19.7**. They can update directly to **7.19.8** through **App Updates**. Signed patches reuse the installed runtime and retain the earlier dashboard-preview repair.

1. Open **App Updates → Check for updates**. Choose **Download update** if it has not started automatically.
2. Finish driving, close Assetto Corsa and choose **Restart to update** when ready.
3. Confirm **7.19.8**, then check **Installed dashboards and controls** in App Updates.
4. If component updates are offered, close Assetto Corsa, SimHub and Stream Deck, then choose **Apply component updates**. These verified files are included in the download; protected folders may show **Allow Windows permission**.
5. To add the two-page controls, choose **Import Session XL layout**, reopen Stream Deck and select **Gridworks Session XL**. Profile import is explicit; existing customized profiles are preserved.

Components already current do not need another import. Normal upgrades preserve drivers, saved runs, courses, setups, preferences, trial dates and licenses. Component updates validate files and keep backups with rollback support. If App Updates requests a full installer for another installed build, use the download above.

## New installation

Download **Gridworks-Drift-Coach-Setup.zip**, extract it, open the **Gridworks-Drift-Coach** folder and run **Gridworks-Setup.exe**. Setup starts automatically. The ZIP contains exactly the installer and **START-HERE.html**.

### Offline update from 7.19.7 only

The [Small Update ZIP for 7.19.8](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.8/Gridworks-Small-Update-7.19.8.zip) supports an installed **7.19.7 only**. Extract it, close Assetto Corsa and run **Update-Gridworks.cmd**. Other supported versions should use App Updates or the full installer. The separate `.gwupdate` assets are handled by the app's signed updater.

## New in 7.19.8: DCGP Season 13

The Setup Library contains **12 families and 24 parameter-reference cards**. Open **Garage → Setup Lab → Gridworks Setup Library** to inspect the car you are driving.

| Reference | Coverage |
| --- | --- |
| VDC | Existing public 6.0 reference. Older, unknown and conflicting installed declarations remain distinct. |
| BDC | Existing Street-family reference; confirm the installed variant and version. |
| Swarm V3 | Existing Team SWARM V3.2 public reference, kept separate from Pro cars. |
| WDT Street | Separate Street family with the creator's v1.1 reference. |
| WDT Competition / Pro Spec | Separate competition family, referenced to World Drift Tour Car Pack 2021. Generic WDT or Enjoy labels do not establish this variant. |
| Death Wish Garage | DWG recognition and a public 3.0 Part 1 reference. |
| Gravy Garage | Gravy Garage recognition and a V2 / public 2.0 reference. |
| Swarm Pro | Its own family, separate from the public Swarm V3 pack. |
| Arch Physics | Explicit physics attribution and donor-specific declared revisions, including dated revision text. |
| Lenny's 180SX | Specific Type-X / Drift donor identities and declared Arch revisions. A generic 180SX name does not identify this model. |
| Instyle / manual reference | Available for manual selection. Its exact creator identity remains unverified; it is not automatically mapped to N-Style or another pack. |
| DCGP / Drift Corner Grand Prix | Season 13 (S13), updated 11 November 2026. Explicit pack season and individual car revision remain distinct. |

The [official DCGP Downloads page](https://driftcornergp.com/page/20-downloads), checked 17 November 2026, identifies the reference as **Season 13 (S13), updated 11 November 2026**. Explicit season labels and `dcgp_13_<car>` folders can identify the pack season. A Nissan S13 model name or old `dcgp_s13` folder cannot establish Season 13; a car revision such as `1.0` does not mean Season 1. A changed season or revision requests a checklist recheck and a fresh Setup Test baseline while preserving the previous saved record.

The app distinguishes the installed car's declared identity from the reviewed reference and shows sources for the selected family. An unrecognized car asks you to choose a reference; a saved valid reference restores. Original guide and checklist-step identifiers remain available. A changed declared version, family or physics credit can request a recheck while preserving the previous saved record.

The cards explain parameters and show the actual car's reported controls. They do not provide universal preset targets. Personalized adjustment guidance still requires the three-run **Setup Test**. Recognition does not verify loaded physics files or establish compatibility between releases. Obtain car mods separately from their creators and follow their donor-car, installation and CSP requirements.

## Setup Test: three accepted runs, with room for normal variation

Save and select a complete direct CSP setup capture, then start the baseline while parked before driving. Collect three original, fully saved live solo runs with the same confirmed setup, car, track, layout, compound and training settings. Recommendations stay locked at 0/3, 1/3 and 2/3. At 3/3 the app reviews the evidence; inconsistent inputs or missing mechanical evidence can still leave an adjustment unproposed.

The wider **7.19.6 matching rules remain in 7.19.8**:

| Requirement | Matching window |
| --- | --- |
| Measured qualifying slide time | At least **10 seconds** per run |
| Usable trace coverage | At least **85%**; position and forward-gear evidence also have coverage checks |
| Entry speed | **±15 mph (±24.1 km/h)** from the reference run |
| Route start and finish | Each within **30 m** of the reference |
| Driven distance | Within **±30%** of the reference |
| Primary drift gear | Same across runs; at least **70%** of measured forward-gear slide time in that gear. Brief shifts are allowed. |
| Starting rear tire core temperature | Within **±25°C** of the reference |
| Road and reported air temperatures | Within **±10°C** each |
| Reported surface grip | Within **±0.05** |

Fresh full setup confirmation and continuous telemetry checks still apply. The first accepted run anchors the matching windows for the baseline and retest. Apply one supported adjustment manually in Assetto Corsa, capture a new complete revision, confirm its physical direction in the game, then collect three matched retest runs. Original run scores are preserved.

**Visible progress and run-count recovery:** the counter shows collecting, recording, saving or checking. The latest completed-run outcome explains whether the recording counted or was excluded, with a link to the saved run when available. Temporary save/read failures can recover; use **Retry Save** in Run Review when prompted and keep the app open until saving succeeds. A completed save queues a fresh check even if a page request is already in progress. The same run cannot count twice.

**Reset Test:** the visible Reset button clears the current test's counter, exclusions, proposal and comparison and returns it to ready, including after Stop. Original saved runs and setups remain available. Stop keeps the current progress; Reset lets you start a clean baseline when parked with the intended setup confirmed.

New tests retain their declared pack/version identity. A detected identity change pauses collection and prevents a retest across known different identities. Existing histories remain intact; legacy tests are not assigned a version retrospectively. The separate Practice mode retains its behavior.

## Recording, completed results and saved data

New automatic recordings require **at least 10 seconds of qualifying slide time, measured before rounding**. Elapsed wall time, linked transitions, straightening confirmation and waiting do not add qualifying slide time. Short attempts produce no new saved recording, completed score or spoken recap. Existing shorter recordings remain readable with their original scores.

Straightening and returning or teleporting to the pits finish the active attempt cleanly. Interrupted recordings with sufficient slide evidence remain distinguished from complete runs. Runs are stored by **car, track and layout**. Save or analysis failures show an explicit retryable state.

Each ready completed result stays on the main dashboard for **10 full seconds**, even while the next drift records. Full review remains in the PC app, with separate **Solo and Tandem** tabs and lead/chase and partner filters. Driver profiles keep personal runs, setups and preferences separate.

Practice estimates and authored-course scores remain distinct. Course scoring requires defined targets and gates; vehicle-centre line and automated style are estimates. Course and tandem scoring still require their own usable evidence. Interrupted runs use the telemetry actually captured. Missing evidence does not create automatic collision blame or invented deductions.

## Included capabilities

- **Drive dashboard and local standings:** clear live/result areas and eligible solo, course, lead and chase rankings under matching recorded conditions.
- **Run Review:** individual telemetry timelines, transitions, sections, driver inputs, zoomable maps, replay, saved views and run cards.
- **Automatic Track Library:** per-driver track/layout identities and observed routes, with gaps for resets, pits and missing telemetry.
- **Run clips:** link an existing local video or save an already-running OBS Replay Buffer to a qualifying run.
- **Setup tools:** actual exposed controls, saved revisions, setup import/export, parameter checklists and measured A/B retests.
- **Course tools:** authored practice targets and gates, Course Test and map editing.
- **Two-page Session XL:** Drive & Review and Setup & OBS, each with 23 controls, eight empty keys and a gold bottom-right page switch. All 32 distinct functions remain available.
- **Optional SimHub displays:** native dashboards and the Angle Coach overlay, with starter-driven activation and support for joining an already-running car.
- **Final-score voice:** the offline male voice option, independent local volume and optional Crew Chief integration remain included. Driving recaps announce the local driver's final run score.
- **Setup and help:** a resumable setup wizard, first-time tour with Don't show this again, and page-specific Help. Open **Settings → Setup wizard** for guided setup.
- **Performance and reliability:** background metadata saves, slower non-live polling, bounded track sampling, saved-run timestamp precision and tablet disconnect recovery.

Optional Stream Deck XL profiles, OBS controls and icons are bundled. **The online/community leaderboard remains deferred and unconfigured**; scores and videos are not automatically uploaded. **Event Director remains separate.** Tandem results are observed-data practice estimates.

The earlier dashboard-preview repair remains included: patches carry the six authenticated preview files that older full installers omitted, and new installations include them. No manual file repair or saved-data deletion is needed. Upgrade validation uses each older installer's actual App staging output as well as complete prior-patch inventory fixtures.

## Requirements

- Windows 10/11 x64 and original Assetto Corsa.
- Content Manager and CSP for the supported full car/setup workflow. Individual car and physics releases may have their own CSP requirements.
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

## Guides and earlier releases

Use installed **7.19.8** guides and page Help for current features. **Setups-and-Run-Review.md** covers the expanded references and recording policy; **Practice-and-Updates-719.md** explains Setup Test and component updates.

The older [49-page visual manual](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.14.0/Gridworks_Drift_Coach_7.14_Visual_Instruction_Manual.pdf) and [screenshot pack](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.14.0/Gridworks_Drift_Coach_7.14_Screenshot_Pack.zip) remain available as **7.14 references**, not current manuals. Their screenshots use demonstration data and native-template previews.

Earlier release notes: [7.19.7](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.7), [7.19.6](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.6), [7.19.5](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.5), [7.19.2](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.2), [7.19.1](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.1), [7.19](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.0), [7.18](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.18.0), [7.17](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.17.0), [7.16](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.16.0), [7.15](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.15.0), [7.14](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.14.0).

## Support and validation

[Report an issue or suggest a feature](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose). Include the app version, car/track, installed car-pack version, AC/CSP versions, display/browser and reproduction steps. For a Setup Test issue, include the outcome or exclusion reason shown beside the counter.

All seven source workflows passed for **7.19.8**:

| Source workflow | Verified run |
| --- | --- |
| App checks | [44185102194](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/44185102194) |
| Three-run practice and in-app component updates | [44185102155](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/44185102155) |
| Windows desktop build | [44185102180](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/44185102180) |
| Leaderboard and dashboard development checks | [44185103976](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/44185103976) |
| Native dashboard name fit | [44185102657](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/44185102657) |
| Tandem end-condition checks | [44185102114](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/44185102114) |
| Next-update result integrity and comparison checks | [44185102127](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/44185102127) |

The source repository and its workflow logs are private; the [public validation record](validation/7.19.8.json) records the release evidence. Windows checks cover native WebView2 startup/shutdown, full-installer upgrade, standalone installation and installer packaging. Actual Chromium checks exercise pack-reference rendering, real checklist save/reload requests and narrow layouts with synthetic car fixtures.

Signed-update verification passed all **32 success/rollback scenarios** across the eight exact online baselines listed above, using both actual installer staging and explicitly modeled prior-patch origins. Each reconstructed target is checked against the complete App inventory, with runtime bytes and saved-data fixtures preserved. The installer ZIP contains exactly **Gridworks-Setup.exe** and **START-HERE.html** inside its folder, with the embedded payload matched to the verified build.

The release has **11 assets**: the full installer ZIP, eight direct `.gwupdate` patches, the 7.19.7-only offline update ZIP and [SHA256SUMS.txt](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.8/SHA256SUMS.txt). The [publishing workflow](https://github.com/lmonroe8/gridworks-drift-coach-releases/actions/runs/44190700453) publishes the staged files. The production feed now offers **7.19.8** after all eleven public release assets were downloaded without authentication and verified against their expected byte counts and SHA-256 checksums.

Source commit: `5fd6f93d1cf96fc82291919af4e950a5d099c625`  
Source tree: `0426f1db41cb65009486ec8cf7dce7e87a0ca7ab`

**Automated checks do not establish live handling or physical-rig behavior for every third-party pack or physics revision.** Real Assetto Corsa/CSP driving and device testing remain separate checks. Signed-update reconstruction uses explicit process/readiness fixtures; scores remain practice estimates.

This repository hosts public downloads and signed feeds. App source stays in a separate private repository. Publishing downloads does not grant an open-source license for the app; third-party notices and terms remain applicable.
