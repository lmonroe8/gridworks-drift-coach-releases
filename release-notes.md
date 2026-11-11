# Gridworks Drift Coach 7.19.1 — update repair

**7.19.1 fixes the missing dashboard-preview file error during in-app updates.** It includes all 7.19 features and the two-page Session XL profile.

## Update through the app

If your update stopped with `No such file or directory` for `App\\Dashboard-Preview\\Detailed-Dash.json`:

1. Open **App Updates → Check for updates** and confirm the offered version is **7.19.1**.
2. Choose **Download update** if it has not started automatically.
3. Finish driving, close Assetto Corsa, and choose **Restart to update**.
4. Confirm the app reports **7.19.1**.

The failed 7.19 preparation leaves the old installation active. No manual preview-file creation, uninstall or saved-data deletion is required.

| Installed build | Direct update to 7.19.1 |
|---|---:|
| 7.17.0 | 26.4 MB |
| 7.18.0 | 21.1 MB |
| 7.19.0 | 145 KB |

These are signed app patches that reuse the installed private Python runtime. Existing driver profiles, saved runs, setups, settings, trial dates and licenses remain in place.

## What was corrected

The 7.18 and 7.19 installer packages contained six dashboard-preview files, but their installer did not copy that folder into the installed App. The patch builder compared package contents and omitted those unchanged files. The old updater then failed while preparing the new version.

The corrected patch supplies all six authenticated preview files, even if their bytes match the old package. New full installations validate and copy the folder. Existing signature verification, archive checks and file-inventory validation remain enforced.

The earlier release test missed the defect because it constructed a complete baseline directly from package contents. Validation now executes each older installer's actual `Install-AppPayload` function and uses its unchanged shipped updater. A separate complete-inventory fixture covers installations created by earlier app patches.

## Components and two-page Stream Deck

When upgrading from 7.17 or 7.18, after the app restarts:

1. Close Assetto Corsa, SimHub and Stream Deck.
2. In **App Updates**, choose **Apply component updates**.
3. Choose **Import Session XL layout**, reopen Stream Deck and select **Gridworks Session XL**.

The two pages are **Drive & Review** and **Setup & OBS**, with native gold page-switch controls. Existing customized profiles are preserved. Components already updated to 7.19 need no reimport for this packaging repair.

## Downloads

- **Gridworks-Drift-Coach-Setup.zip**: the complete 7.19.1 installer for new installations or older unsupported builds. Extract it and run `Gridworks-Setup.exe`.
- **Gridworks-Small-Update-7.19.1.zip**: offline fallback specifically for installed **7.18.0**. Extract and run `Update-Gridworks.cmd`.
- **.gwupdate files**: handled by the app's signed updater.
- **SHA256SUMS.txt**: checksums of all five downloads.

The usual path for supported installed builds is **App Updates**.

## Verification

- Reproduced the exact original missing-`Detailed-Dash.json` failure with the published 7.18 installer's real output, its unmodified updater and the authentic signed 7.19 patch.
- **17 focused Python checks** and **72 PowerShell bundle checks** passed.
- **12 signed upgrade/rollback scenarios** passed across 7.17, 7.18 and 7.19, covering both real full-installer output and complete prior-patch inventory fixtures.
- The corrected full installer and every prepared update match all **253 target App files**. Each signed scenario preserves **34 runtime files**, **11 saved-data fixtures** and the old installation.
- All six preview HTTP routes work from the installed App. Missing or malformed previews fail installer preflight before App files are staged.
- The full installer verifier passed PE/bootstrap, exact embedded payload, bundled downloads, runtime checksum and both native Session XL pages.
- Exact-commit CI passed **550 core tests with three skips**, functional browser checks, native Windows app launch, full installer upgrade and clean standalone installation.
- An independent package comparison found exactly six intended payload-file changes. All **692 native/runtime/integration assets**, including all 91 desktop-host files and the two-page profile, are byte-identical to 7.19.0.

GitHub Actions artifact uploads still failed because the account storage quota is full, so its dependent package job was skipped. The release installer was rebuilt and fully verified separately using the unchanged validated 7.19 native host; public release transfers are checksum-verified.

Portable signed activation tests use explicit process/readiness fixtures; they do not claim a live Windows restart. Real AC/CSP driving, intended-mod setup behavior, physical SimHub/Stream Deck, OBS clip paths and driving-PC component permissions retain the 7.19 validation limits. Results remain practice estimates. Community leaderboard hosting remains unconfigured.

[Full 7.19 feature notes](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/tag/v7.19.0)
