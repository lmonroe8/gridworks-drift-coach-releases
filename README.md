# Gridworks Drift Coach

**Beta Version 2.0 · build 7.11.0**

A local Windows app for Assetto Corsa drift practice, car/setup tools, individual run review and a paired tablet display. SimHub dashboards, the Angle Coach overlay and Stream Deck controls are included as optional extras.

## Download and install

[Download build 7.11.0](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/beta-2.0.7.11.0)

1. Download **Gridworks-Drift-Coach-Beta-2.0.zip** from the named release assets.
2. Extract the ZIP and double-click **Gridworks-Setup.exe**. Setup begins automatically.
3. Use the **Gridworks Drift Coach Beta 2.0** desktop shortcut for later sessions.

The download contains the installer and **START-HERE.html**. It does not contain promotional material. The installer contains the app, private Python runtime, desktop host, dashboards, overlay, supported game links, Stream Deck XL profile and icon pack. Python is not a separate prerequisite.

**Existing users: use this full installer for the 7.11.0 desktop migration.** It preserves your existing data. The signed in-app migration for this build is not yet published, so the signed update feed remains at 7.10.2. Do not use an older small-update ZIP to install this build. Normal signed changed-file updates remain supported when published.

GitHub's automatic **Source code** archives contain this release-channel repository, not the Gridworks app.

## What you need

- **Windows 10/11 x64**, original **Assetto Corsa**, **Content Manager** and **Custom Shaders Patch (CSP)** for the supported car/setup workflow.
- **Microsoft WebView2 Runtime** supplies the desktop window. Setup reuses it, or downloads Microsoft's signed runtime once if missing.
- **SimHub is optional**, for the native dashboards and angle overlay.
- A tablet, Stream Deck XL, OBS and a second display are optional.

Keep Gridworks open while recording and using the tablet. Its main controller stays local to your PC.

## Connect a tablet

Open **Tablet display → Enable tablet display**. The page displays the tablet address, a QR code, a six-digit pairing code and copy buttons.

Connect the tablet and PC to the same home network. Scan the QR code, or open the displayed address in the tablet browser and enter the code. Codes expire after ten minutes; paired browsers reconnect for thirty days, including after an app restart.

The tablet switches automatically between driving, the last run and setup checklists. Manual screen lock, fullscreen and a visible reconnect indicator are included. Troubleshooting offers adapter selection, a manual private IPv4 address and an optional Windows Firewall rule limited to Private networks and the local subnet. Updates, course editing, backups and administration stay on the PC.

## What's new

- **Native desktop window:** private runtimes, single-instance launch, safe shutdown and controller recovery. SimHub no longer gates the connection check.
- **Qualifying practice:** independent **Line 40 / Angle 40 / Estimated style 20** scoring from saved telemetry. Damgam ingestion and its installation steps have been removed.
- **Course editor:** build a route from a recorded run, place directed start/finish gates and inner/outer targets, and import/export course profiles. Profiles and revisions are saved with scored runs.
- **Useful deductions:** inspect a deduction at its replay timestamp, compare eligible transitions with a matching best run, and see the largest measured deduction as the next-run practice focus.
- **Clearer session screen:** the latest result and next practice focus stay visible; detailed input/tire graphs open when needed.
- **Lower UI load:** compact live packets, no full course geometry in the fast telemetry stream, and rendering limited to visible views.

A full practice total requires an authored course and enough continuous telemetry. Free practice still records slides of at least ten seconds when the car straightens. Missing measurements remain explained and unscored. Line uses vehicle-centre distance; automated style is an estimate. Transition/deceleration markers describe a course visually but do not directly change scoring in model 1. This is practice feedback, not official competition judging or licensed UDSM.

## Also included

Setup Lab with six starting guides, baselines/revisions and setup import/export; per-car/track/layout run archives; transition and range replay; setup experiments; reference comparisons with declared provenance; reviewed backups and diagnostics; and a **Support message** tool that prepares feedback without sending it automatically.

The optional SimHub companion now shows qualifying practice results. Main dash and Angle Coach exports are retained. Original Stream Deck XL controls and eight OBS actions are preserved, with a separate optional Coach Tools profile.

## Feedback and testing

[Report a bug or suggest a change](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose), or share the prepared Support message with Leo through your beta conversation. Public downloads do not require a GitHub account; posting an issue does.

Automated checks cover scoring, pairing/revocation, data preservation, updates, real Chromium interactions, native WebView2 launch and a real Windows automatic installation without SimHub. Live AC driving, particular mod telemetry, tablet/browser combinations and physical SimHub/Stream Deck devices still need tester feedback.

This repository hosts public beta releases and the signed update channel. App source is maintained separately in a private repository. Publishing downloads does not grant an open-source license for the app; third-party components retain their own notices and terms.
