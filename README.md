# Gridworks Drift Coach

**Production release · version 7.13.0**

A standalone Windows app for Assetto Corsa drift practice, setup work, individual run review and a paired tablet display.

## Download and install

[Download the latest release](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/latest)

Choose **Gridworks-Drift-Coach-Setup.zip**, extract it and double-click **Gridworks-Setup.exe**. Setup starts automatically and creates the **Gridworks Drift Coach** shortcut. The ZIP contains setup and the Start Here guide.

**Existing users on 7.12.2 or earlier must use the full installer once for 7.13.0.** Close Assetto Corsa and Gridworks, extract **Gridworks-Drift-Coach-Setup.zip**, and run **Gridworks-Setup.exe** using the existing installation. Saved runs, setups, trial dates and existing lifetime licenses are preserved. This release refreshes update verification and cannot arrive through the old App Updates verifier. Normal signed app updates resume on the new stable recovery channel after this one-time upgrade. Deliberately configured custom channels are preserved.

GitHub's automatic **Source code** ZIPs contain this release-channel repository. Use the named installer/update assets for the app.

## Requirements

- **Windows 10/11 x64** and original **Assetto Corsa**.
- **Content Manager and CSP** for the supported full car/setup workflow.
- **Microsoft WebView2 Runtime** for the desktop window. Setup reuses it or installs Microsoft's signed runtime once when missing.
- **SimHub** is optional for its native dashboards and angle overlay.
- A tablet, Stream Deck XL, OBS and a second display are optional.

Private runtimes are included. Keep the PC app open while recording and using the tablet.

## Seven-day full-app trial, then $5 lifetime

Try every feature for **seven calendar days from the first trial-enabled launch**. Updating from 7.12.1 preserves the original trial dates and existing lifetime licenses; it does not start another trial. Closing the app does not pause the trial.

After the trial, a **$5 USD one-time lifetime license** restores full access, with **no subscription or expiry**. Live coaching and recording, new setup/course work and the paired tablet require trial or licensed access. Saved runs and setups stay readable/exportable; backups, support, app updates and activation remain available. License includes saved setup downloads even without a connected car.

Open **License → Buy $5 lifetime license** to purchase through Stripe. Checkout uses the verified signed release configuration and includes this PC's random installation reference. Use an email address you can receive mail at. After verified settled payment, the hosted service emails a ZIP containing your signed `.gwlicense` file. Extract the ZIP and import that file in the License page. The seven-day trial stays inside Gridworks; checkout is a one-time payment. Sandbox licenses do not activate the public app. Keep your license file and installation ID private.

Trial dates and activated licenses survive app updates and normal reinstallations that retain the user-data folder. Trial tracking is local. License management stays on the PC; codes, customer names and installation identity are excluded from telemetry and diagnostics. User-data backups exclude activation and trial records.

## Tablet display

Open **Tablet display → Enable tablet display**. The page shows the tablet address, QR code, six-digit pairing code and copy buttons.

Use the same home network for both devices. Scan the QR code, or open the displayed address in the tablet browser and enter the code. Codes expire after ten minutes; paired browsers reconnect for thirty days, including after app restarts.

The tablet switches between driving, a quick latest-run summary and short setup checklists. After a run it shows the score, mean angle, duration and one next-run focus. Full replay, transitions, score details, recent runs and complete setup review stay in the PC app’s **Pit screen** and **Run review**. The tablet does not load full run traces or analysis.

The tablet also includes manual screen lock, fullscreen, a reconnect indicator, address selection and Private-network firewall help. Keep Gridworks open on the PC.

## Coaching and review

- **Immediate run results:** straightening, returning to pits or another detected interruption ends the attempt with a numeric score. The finish reason and whether the attempt was saved are shown.
- **Drift practice estimate:** **Angle target 60 / Angle control 25 / Drift continuity 15** gives free practice an immediate result without requiring an authored course. It uses captured telemetry and is clearly labelled as an estimate.
- **Course qualifying practice:** independent **Line 40 / Angle 40 / Estimated style 20** scoring when an authored course and required gate coverage are available. Damgam ingestion has been removed.
- **Course editor:** turn a recorded route into directed start/finish gates and inner/outer targets; save revisions and import/export profiles.
- **Run review:** inspect deductions at their replay timestamps, individual transitions, driver inputs and selected ranges. Compare eligible runs with a matching best.
- **Setup Lab:** six starting guides, baselines/revisions and setup import/export, with evidence and uncertainty shown.
- **Session view:** latest result, next-run focus and detail panels that open when needed.
- **Data tools:** reviewed backups/restores, diagnostics, notes, favorites, search, reference comparisons and prepared support messages.

A completed authored-course score replaces the immediate estimate once full analysis is ready. Practice estimates and course scores are labelled separately and are not mixed in course bests. Interrupted runs use only telemetry captured before the interruption.

Attempts of at least **ten seconds** are archived for individual review under their car/track combination, including interrupted attempts. Shorter attempts still show a score and finish reason, but are not archived. Insufficient usable telemetry shows **0 with an explanation**. A background save or analysis error shows an explicit retryable state while the immediate score remains visible. Vehicle-centre line and automated style are estimates. This is independent practice feedback, not official competition judging or licensed UDSM.

Optional SimHub exports, Angle Coach, Stream Deck XL profiles, OBS controls and icons remain bundled. When upgrading from 7.10.2 or earlier, reimport the optional **Gridworks Sim Center** companion from Bundled downloads once for its qualifying-practice page.

## Support and validation

[Report an issue or suggest a feature](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose). Include your app version, car/track, AC/CSP versions, tablet/browser and steps to reproduce the problem.

331 core tests, update interface checks, real Chromium workflows, and Windows desktop/full-installer checks passed for 7.13.0. The published installer payload, replacement public update key, recovery channel, unchanged production license trust and absence of private keys were verified. The signed recovery feed and $5 checkout configuration were verified, and the changed-file patch reconstructs the target app exactly. Stripe sandbox checkout/email delivery and live restricted-key read access were verified; no live self-purchase was used for testing. Live game/mod and physical-device combinations still benefit from user reports.

This repository hosts public releases and signed update feeds. App source is maintained separately in a private repository. Publishing downloads does not grant an open-source license for the app; third-party components retain their own notices and terms.
