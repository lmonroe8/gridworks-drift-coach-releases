## Gridworks Drift Coach — Beta Version 2.0, build 7.11.0

### Install or upgrade

Download **Gridworks-Drift-Coach-Beta-2.0.zip**, extract it and double-click **Gridworks-Setup.exe**. Close Assetto Corsa first. The ZIP contains only setup and the Start Here guide. Existing profiles, setups and saved runs are preserved.

Use the **full installer for this desktop migration**, including if you already have 7.10.2. The signed in-app migration is not published yet; the signed feed remains at 7.10.2. Normal signed app updates remain supported when published.

Windows 10/11 x64 and original Assetto Corsa are required. Content Manager and CSP support the enhanced car/setup workflow. SimHub is now optional for its dashboards/overlay. Private runtimes are bundled; WebView2 is reused or installed from Microsoft when missing.

### Changes

- Own desktop window, single-instance launch, safe close and local controller recovery.
- Rebuilt **Tablet display** connection page with a visible address, QR pairing, six-digit code, copy buttons, active-device status, address selection and Private-network firewall help. Paired browsers reconnect after app restarts.
- **Line 40 / Angle 40 / Estimated style 20** independent qualifying-practice model replaces Damgam ingestion.
- Visual course profiles with directed gates, inner/outer targets, revisions and import/export.
- Clickable deductions, matching-course best-run comparisons and transition-level inspection.
- Clearer latest-result/next-focus layout and smaller live telemetry packets.

To connect a tablet: put both devices on the same home network, choose **Tablet display → Enable tablet display**, then scan the QR code or open the displayed address and enter the code. Keep the PC app open.

For full practice scores, create and select a course with gates and targets. Free practice still saves slides of at least ten seconds. Missing data does not become a fabricated total. Vehicle-centre line and automated style are estimates, not official judging or licensed UDSM. Transition/deceleration markers are descriptive in model 1.

The updated optional SimHub companion is installed when SimHub is detected; its export remains in Bundled downloads. Main dash, Angle Coach and original Stream Deck/OBS controls are retained.

### Validation and beta feedback

Python/core and real Chromium suites passed, alongside native Windows WebView2, duplicate-launch, shutdown and automatic installation checks without SimHub. Installer staging and embedded payload checks also run during packaging. Synthetic and automated checks do not replace live game, mod and device testing.

[Report a problem or suggestion](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose). Include your build, car/track, AC/CSP versions, tablet/browser and the steps that produced the problem.
