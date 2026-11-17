# Gridworks Drift Coach 7.19.7

**The Setup Library now supports 11 pack and physics families with 22 parameter-reference cards.** Open **Garage → Setup Lab → Gridworks Setup Library** to review the car you are driving.

## Added references

| Reference | Coverage |
| --- | --- |
| WDT Street | Separate Street family with the creator’s v1.1 reference. |
| WDT Competition / Pro Spec | Separate competition family, referenced to the creator’s World Drift Tour Car Pack 2021. Generic WDT or Enjoy labels are not assumed to identify it. |
| Death Wish Garage | DWG recognition and a public 3.0 Part 1 reference. |
| Gravy Garage | Gravy Garage recognition and a V2 / public 2.0 reference. |
| Swarm Pro | Its own family, kept distinct from the existing Swarm V3 / V3.2 reference. |
| Arch Physics | Explicit physics attribution and donor-specific declared revisions, including dated revision text. |
| Lenny’s 180SX | Specific Type-X / Drift donor identities and declared Arch revisions. A generic 180SX name does not identify this model. |
| Instyle / manual reference | Available for manual selection. Its exact creator identity is still unverified; it is not automatically mapped to N-Style or another pack. |

Existing **VDC 6.0, BDC and Swarm V3** references remain available, with their original guide and checklist-step identifiers.

## How the library works

The app distinguishes the installed car’s declared identity from the reviewed reference, shows sources for the selected family and preserves saved checklists. An unrecognized car asks you to choose a reference. A changed declared version or family requests a recheck while keeping the previous saved record.

The cards explain parameters and show the actual car’s reported controls. Personalized adjustment guidance still requires a completed three-run **Setup Test**. Recognition does not verify the loaded physics files or establish compatibility between releases. Obtain car mods separately from their creators.

The wider **7.19.6** matching rules remain: **10 qualifying slide seconds**, **85% coverage**, **±15 mph entry speed**, route endpoints within **30 m**, route distance within **±30%**, and the same primary drift gear for at least **70%** of measured forward-gear slide time. Brief shifts are allowed. Rear starting tire core temperature may vary by **±25°C**, road and reported air temperature by **±10°C**, and surface grip by **±0.05**. Reset, run-count recovery, completed-score handling and saved run history remain in place.

## Install or update

- **Existing users:** open **App Updates → Check for updates**, download the offered patch, finish driving and choose **Restart to update** after closing Assetto Corsa.
- **New users or builds requesting a full installer:** download **Gridworks-Drift-Coach-Setup.zip**, extract it and run **Gridworks-Setup.exe**. The ZIP contains the installer and **START-HERE.html**.
- **Offline update ZIP:** **Gridworks-Small-Update-7.19.7.zip** supports **7.19.6 only**. Other supported versions should use App Updates or the full installer.

The signed online update supports exact installed builds **7.17.0, 7.18.0, 7.19.0, 7.19.1, 7.19.2, 7.19.5 and 7.19.6**. Saved driver data, setups, runs and license settings are retained. Licensing remains a **7-day full trial**, then **$5 USD once for a lifetime license**.

## Validation

Release validation covers all seven source workflows, the native Windows desktop and installer checks, metadata recognition and identity preservation, actual browser rendering and real checklist save/reload requests, narrow layouts, source-to-package parity, and **28 signed upgrade/rollback scenarios** across the seven exact published baselines. Public release assets are downloaded without authentication and verified against their expected checksums before the update feed advances.

Browser and telemetry fixtures are synthetic. Live Assetto Corsa/CSP driving with every third-party car pack or physics revision, physical SimHub dashboards and the driving rig are separate checks.

Source commit: `5d30ced87db409eda3563a3c8e1f3c762a1af9a2`  
Source tree: `e968307fa76f6754fa6c97c27b8359fa922f3980`
