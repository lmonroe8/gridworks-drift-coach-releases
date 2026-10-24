## Gridworks Drift Coach 7.12.0

This is the first production release under the proper product name **Gridworks Drift Coach**. The app window, installer, shortcuts, help and downloads use that name.

### Install or upgrade

Download **Gridworks-Drift-Coach-Setup.zip**, extract it and double-click **Gridworks-Setup.exe**. Close Assetto Corsa first. Setup preserves existing data and opens the app.

Builds **7.9.9, 7.10.0, 7.10.1, 7.10.2, 7.11.0 and 7.11.1** can use **App updates → Check for updates → Restart to update**. The signed migration updates the desktop and moves the official beta feed to stable. Old shortcuts are replaced only when they point to this installation.

**Gridworks-Update-7.12.0.zip** is a manual alternative for **7.10.2** only. Other supported versions use the app update or full installer. The `.gwupdate` assets are consumed by the updater.

### Licensing

**Community keeps all current tools.** The new PC-only **License** page supports signed Pro code/file activation, expiry checks, optional installation binding and removal while preserving saved data. Invalid replacement codes leave a valid license intact.

Pricing, payment processing, automatic license delivery and the paid feature split are future configuration. The app does not collect payments.

### Included coaching and tablet features

The release includes the standalone desktop, visible tablet address and QR/code pairing, reconnect status, automatic tablet screens, the independent **40 line / 40 angle / 20 estimated style** practice model, course editor, clickable deductions and transition comparisons.

Full totals require an authored course and sufficient telemetry. Scores are independent practice estimates. Existing setups, courses, runs, pairing and licenses are preserved by supported upgrades.

If coming from **7.10.2 or earlier**, reimport the optional **Gridworks Sim Center** companion from Bundled downloads for its new scoring page. Full setup installs it when SimHub is detected. Main dash, Angle Coach and original Stream Deck/OBS controls are retained.

### Validation

Python/core and real Chromium suites passed, including license import, activation, persistence, invalid/expired/wrong-installation cases, removal and responsive layouts. Windows checks passed for native launch, single-instance behaviour, graceful shutdown, automatic installation without SimHub and migration through the actual old 7.10.2 update worker.

All six signed patch baselines reconstruct the exact target app inventory and preserve saved data, licenses and private Python. Legacy verifiers accept the migration metadata. Public downloads contain no private signing material.

[Report a problem or suggestion](https://github.com/lmonroe8/gridworks-drift-coach-releases/issues/new/choose).
