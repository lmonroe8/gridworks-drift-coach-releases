# Gridworks Drift Coach 7.18.0

## Install this update

Use **Gridworks-Drift-Coach-Setup.zip** below for the complete update, including the refreshed SimHub templates and Assetto Corsa Tandem Link. This is the ready-to-install Windows package, not a source-code ZIP.

1. Finish your session and close Assetto Corsa, Drift Coach and SimHub.
2. Back up your saved Gridworks data as a precaution. Do not uninstall the existing app or delete its data folder.
3. Extract the ZIP, open the `Gridworks-Drift-Coach` folder and run `Gridworks-Setup.exe`.
4. Follow the installer, retaining your existing game and SimHub locations. Open Drift Coach and check that it reports **7.18.0**.

The installer preserves existing profiles, setups, run history and preferences. A source archive or `.patch` file is not needed.

## Included

- Independent **numeric-only lead and chase practice scores**, with component breakdowns and telemetry coverage. No letter grades or automatic competition winner.
- Versioned saved scoring snapshots so new saved results do not silently change when reopened after a later scoring update.
- Shared completed results in the app, Run Review and SimHub, with the existing ten-second finish display.
- Locked-partner tandem endings for pit teleports/resets and sustained crash/spin evidence. Missing telemetry does not automatically become bad driving, and motion estimates do not assign collision blame.
- Clickable review observations and one evidence-based improvement tip per driver.
- Session progress separated into solo, lead and chase, comparing compatible runs rather than mixing incompatible scoring/settings.
- Read-only dashboard preview across six layouts and eight synthetic states; preview runs do not affect real statistics.
- Refreshed SimHub angle guides, clearer partner status, bounded long driver names, and retained original branding/classic controls.
- Local-driver final-score-only voice behavior. The online leaderboard remains deferred; Event Director remains separate.

## Existing-user app patch

`Gridworks-7.17.0-to-7.18.0.gwupdate` is for the app's signed updater, not a file to double-click. It supports **7.17.0** and replaces the App tree while keeping the private runtime and saved data. It updates app/bundled exports, not already-installed SimHub templates or Assetto Corsa game-link files. **Use the full installer for the complete 7.18 update.** Older installations should also use the full installer.

## Validation and limitations

The exact source passed application/browser checks, tandem scoring/end-condition checks, native dashboard binding/export checks, and the Windows desktop/installer workflow. The downloaded installer ZIP, executable and embedded payload hashes were verified. The signed patch was accepted by the 7.17 updater and reconstructed all 222 target App files; success and failed-readiness rollback scenarios preserved saved-data fixtures.

These automated checks do **not** establish real two-car Assetto Corsa/SimHub calibration. Tandem scores remain observed-data practice estimates, and crash detection remains motion-based. Real hardware/multiplayer feedback is still needed.

## Integrity

- Installer ZIP SHA-256: `17ce6d600d61ef5dc351f7389aaa9b7a1a8b726f19615dd1a92e4f16cbb55aef`
- Embedded setup executable SHA-256: `1cea575e4cd573749574989291d0fcffed1893b3a729a950f2c704458695b100`
- App patch SHA-256: `3f7c9f8a6bc5a5c31f45dd8c7e7ff298c63c2cb7c5bd7d5e3c4069468709386e`

The existing update trust key and checkout configuration are unchanged. No private signing key is included in downloads or Actions artifacts.
