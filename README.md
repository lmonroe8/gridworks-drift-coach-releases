# Gridworks Drift Coach

**Production release · version 7.12.0**

A standalone Windows app for Assetto Corsa drift practice, setup work, individual run review and a paired tablet display.

## Download and install

[Download the latest release](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/latest)

Choose **Gridworks-Drift-Coach-Setup.zip**, extract it and double-click **Gridworks-Setup.exe**. Setup starts automatically and creates the **Gridworks Drift Coach** shortcut. The ZIP contains setup and the Start Here guide.

Existing users on **7.9.9, 7.10.0, 7.10.1, 7.10.2, 7.11.0 or 7.11.1** can use **App updates → Check for updates → Restart to update**. Finish driving first. The signed migration preserves saved data and private Python, updates the desktop window, and moves the official release channel to stable.

The separate **Gridworks-Update-7.12.0.zip** supports **7.10.2** as a manual alternative: extract it and run **Update-Gridworks.cmd**. Other supported versions use the app update or full installer.

GitHub's automatic **Source code** ZIPs contain this release-channel repository. Use the named installer/update assets for the app.

## Requirements

- **Windows 10/11 x64** and original **Assetto Corsa**.
- **Content Manager and CSP** for the supported full car/setup workflow.
- **Microsoft WebView2 Runtime** for the desktop window. Setup reuses it or installs Microsoft's signed runtime once when missing.
- **SimHub** is optional for its native dashboards and angle overlay.
- A tablet, Stream Deck XL, OBS and a second display are optional.

Private runtimes are included. Keep the PC app open while recording and using the tablet.

## Community and Pro licensing

**Community includes all current coaching, scoring, course, setup, run-review and tablet tools.** Existing users keep those tools after upgrading.

The new **License** page accepts signed **Pro** codes or `.gwlicense` files from Gridworks. It supports perpetual or expiring licenses, optional installation binding, status display and removal from the PC while preserving saved data.

Pro pricing, payment processing, automatic delivery and the paid feature split will be announced separately. The current app does not collect payments.

License management stays on the PC. Codes and installation identity are excluded from telemetry, diagnostic exports and user-data backups.

## Tablet display

Open **Tablet display → Enable tablet display**. The page shows the tablet address, QR code, six-digit pairing code and copy buttons.

Use the same home network for both devices. Scan the QR code, or open the displayed address in the tablet browser and enter the code. Codes expire after ten minutes; paired browsers reconnect for thirty days, including after app restarts.

The tablet switches between driving, the latest run and setup checklists. It also includes manual screen lock, fullscreen, a reconnect indicator, address selection and Private-network firewall help. Keep Gridworks open on the PC.

## Coaching and review

- **Qualifying practice:** independent **Line 40 / Angle 40 / Estimated style 20** scoring from telemetry. Damgam ingestion has been removed.
- **Course editor:** turn a recorded route into directed start/finish gates and inner/outer targets; save revisions and import/export profiles.
- **Run review:** inspect deductions at their replay timestamps, individual transitions, driver inputs and selected ranges. Compare eligible runs with a matching best.
- **Setup Lab:** six starting guides, baselines/revisions and setup import/export, with evidence and uncertainty shown.
- **Session view:** latest result, next-run focus and detail panels that open when needed.
- **Data tools:** reviewed backups/restores, diagnostics, notes, favorites, search, reference comparisons and prepared support messages.

Full practice totals require an authored course and enough continuous telemetry. Free practice saves slides of at least ten seconds when the car straightens. Missing data stays explained and unscored. Vehicle-centre line and automated style are estimates. This is independent practice feedback, not official competition judging or licensed UDSM.

Optional SimHub exports, Angle Coach, Stream Deck XL profiles, OBS controls and icons remain bundled. When upgrading from 7.10.2 or earlier, reimport the optional **Gridworks Sim Center** companion from Bundled downloads once for its qualifying-practice page.

## Support and validation

[Report an issue or suggest a feature](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose). Include your app version, car/track, AC/CSP versions, tablet/browser and steps to reproduce the problem.

Automated checks cover signed licensing, stable-channel migration, preservation of records and licenses, real Chromium workflows, native WebView2 launch and a real Windows automatic installation without SimHub. The migration test uses the actual 7.10.2 update worker to open the new desktop. Live game/mod and physical device combinations still benefit from user reports.

This repository hosts public releases and signed update feeds. App source is maintained separately in a private repository. Publishing downloads does not grant an open-source license for the app; third-party components retain their own notices and terms.
