# Gridworks Drift Coach 7.19.8

**DCGP / Drift Corner Grand Prix is now in the Setup Library.** Open **Garage → Setup Lab → Gridworks Setup Library** to find its two parameter-reference cards. The library now contains **12 families and 24 cards**.

## DCGP Season 13

The [official Downloads page](https://driftcornergp.com/page/20-downloads), checked 17 November 2026, identifies the reference as **Season 13 (S13), updated 11 November 2026**.

- Explicit DCGP season labels and current `dcgp_13_<car>` folder forms are recognized.
- The installed pack season stays separate from the individual car's declared revision. A revision such as `1.0` does not mean Season 1.
- A Nissan S13 model name or ambiguous old `dcgp_s13` folder does not establish Season 13. Older, unknown and conflicting season labels remain distinct.
- Saved checks survive reload. Changing the declared season or car revision requests a fresh review while retaining the previous saved record, and an active Setup Test waits for a new baseline.

The cards explain parameters and show the current car's reported controls. Supported adjustment guidance still requires a completed three-run **Setup Test**. Obtain car mods separately from their creators; metadata recognition does not verify loaded physics or establish compatibility between seasons.

All previous families remain available: **VDC 6.0, BDC, Swarm V3, WDT Street, WDT Competition / Pro Spec, Death Wish Garage, Gravy Garage, Swarm Pro, Arch Physics, Lenny's 180SX, and the manual Instyle reference**.

## Existing fixes retained

The wider Setup Test rules remain: **at least ten qualifying slide seconds**, **85% usable coverage**, **±15 mph entry speed**, route endpoints within **30 m**, distance within **±30%**, and the same primary drift gear for at least **70%** of measured forward-gear slide time. Brief shifts are allowed. Starting rear tire core temperature can vary by **±25°C**, road and reported air temperatures by **±10°C**, and reported surface grip by **±0.05**.

Reset, run-count recovery, clean run finalization, the ten-second completed-result display, saved history, separate Solo/Tandem reviews, starter-driven dashboards and final-score voice remain in place. The online leaderboard stays deferred and unconfigured. Licensing remains a **seven-day full trial**, then **$5 USD once for a lifetime license**.

## Install or update

- **Existing users:** open **App Updates → Check for updates**, download the offered patch, finish driving and choose **Restart to update** after closing Assetto Corsa.
- **New users or builds requesting a full installer:** download **Gridworks-Drift-Coach-Setup.zip**, extract it and run **Gridworks-Setup.exe**. The ZIP contains the installer and **START-HERE.html**.
- **Offline update ZIP:** **Gridworks-Small-Update-7.19.8.zip** supports **7.19.7 only**. Other supported versions should use App Updates or the full installer.

The signed online update supports exact installed builds **7.17.0, 7.18.0, 7.19.0, 7.19.1, 7.19.2, 7.19.5, 7.19.6 and 7.19.7**. Saved driver data, setups, runs and license settings are retained.

## Validation

Release validation covers all seven source workflows, native Windows desktop and installer checks, DCGP recognition and identity preservation, real-browser metadata refresh and checklist saves, desktop and narrow layouts, source-to-package parity, and **32 signed upgrade/rollback scenarios** across eight exact published baselines. Public assets are downloaded without authentication and verified before the update feed advances.

Browser and telemetry fixtures are synthetic. Live Assetto Corsa/CSP driving with each third-party car or physics revision and physical SimHub/rig behavior remain separate checks.

Source commit: `5fd6f93d1cf96fc82291919af4e950a5d099c625`  
Source tree: `0426f1db41cb65009486ec8cf7dce7e87a0ca7ab`
