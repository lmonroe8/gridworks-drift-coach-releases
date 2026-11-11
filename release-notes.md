# Gridworks Drift Coach 7.19.0

## Update from inside Gridworks

Installed **7.18.0 and 7.17.0** can update directly to 7.19.0 through **App Updates**. The signed update downloads changed files and reuses the existing runtime. The 7.18 update is approximately **21 MB**; the complete installer is approximately **136 MB**.

1. Open **App Updates → Check for updates**. If downloading has not started automatically, select **Download update**.
2. Finish your driving session, close Assetto Corsa, and select **Restart to update** when the app says it is ready.
3. Confirm that Gridworks reports **7.19.0**.
4. Close Assetto Corsa, SimHub and Stream Deck. In **App Updates**, select **Apply component updates** to refresh supported installed Gridworks dashboards, Car Link, Tandem Link and the Stream Deck plugin. Select **Allow Windows permission** if shown. The component payload is already included in the app update.
5. Select **Import Session XL layout** to add the new two-page profile, then reopen Stream Deck and select **Gridworks Session XL**. Existing customized profiles are preserved.

Normal upgrades preserve saved drivers, runs, courses, setups, preferences, trial dates and licenses. Updated component files are validated and backed up, with rollback support. New component installations remain available through Setup.

For a new installation, or an older build that reports **Installer needed**, download **Gridworks-Drift-Coach-Setup.zip**, extract it, open the `Gridworks-Drift-Coach` folder and run `Gridworks-Setup.exe`.

## Included in 7.19

### Driving and results

- Slides need **at least three qualifying drift seconds** to register. Shorter attempts create no completed score, saved run or spoken recap, and leave the previous result intact.
- Each ready completed result stays visible for **ten full seconds**. Starting another drift keeps that result visible while recording the next attempt. The app, tablet and native displays use the same held-result identity; additional completed runs remain available in Run Review.
- A clearer Drive dashboard separates live readings from completed results, including distinct lead/chase results and missing-data labels.
- Tandem Run Review compares the latest eligible matching earlier run using original saved scores and component measurements. Stale, malformed and out-of-order evidence is rejected; missing data remains unavailable.
- Saved-run timestamp precision now preserves genuine final telemetry frames. Tablet live readings clear on disconnect and recover when fresh telemetry returns.
- Private standings separate eligible solo, course, lead and chase results by matching recorded conditions. The community service is not configured in this release, and no scores are uploaded automatically.

### Three-run Setup Test

**Garage → Setup Test** has its own page. Complete three matching live baseline runs with confirmed direct CSP setup evidence before the app proposes a supported adjustment. Each proposal explains the measured evidence, mechanical effect, expected tradeoff and uncertainty.

Apply the proposed control change manually in Assetto Corsa, confirm that exactly that control changed, and complete three matching retest runs. The comparison keeps the original measurements and can report an inconclusive result. Initial mechanical recommendations cover supported anti-roll-balance and gearing cases; unsupported mod settings do not receive invented recommendations.

### Automatic Track Library

**Practice → Track Library** stores track/layout identities and bounded observed driving routes per driver. Pit returns, resets and missing telemetry split route segments. A stored route can be partial; it is not automatically an authored judging course.

### Local run clips

In **Run Review → Notes & video**, attach an existing local video or save an already-running **OBS Replay Buffer** and link its confirmed file to the correct qualifying run. Open and detach links explicitly. Moved or missing files are marked, and videos remain in their original folders. Saving the current replay buffer cannot recreate an older run that is no longer in the buffer. Private file paths are excluded from normal backups, diagnostics and public results.

### Two-page Stream Deck XL

| Page | Main controls |
| --- | --- |
| **Drive & Review** | Driving, saved runs, clips, results, leaderboard and quick OBS controls |
| **Setup & OBS** | Setup Test, Setup Lab, coaching adjustments, OBS and review shortcuts |

Each page has **23 controls, eight empty keys and a gold page-switch key in the bottom-right corner**. All 32 distinct functions remain available. Navigation uses Stream Deck's native Next/Previous controls and works with Gridworks and OBS closed. Switching pages cancels an unfinished Stream-button hold. Configure your own OBS scene/source names after importing.

### Performance and maintenance

Completed-run metadata saves run in the background rather than holding the telemetry lock. Less active pages poll more slowly, hidden windows stop normal polling, unchanged graphs avoid redraws, and track sampling is bounded. These changes reduce measured app overhead; they do not establish a specific game-FPS increase.

## Download choices

- **Gridworks-Drift-Coach-Setup.zip:** complete Windows installer for new installs and unsupported older upgrade paths.
- **Gridworks-7.18.0-to-7.19.0.gwupdate:** signed-updater package selected automatically for 7.18.0.
- **Gridworks-7.17.0-to-7.19.0.gwupdate:** signed-updater package selected automatically for 7.17.0.
- **Gridworks-Small-Update-7.19.0.zip:** optional recovery updater for an installed 7.18.0 if its in-app connection is unavailable. Extract it, finish driving, close Assetto Corsa, and run `Update-Gridworks.cmd`. Normal updates use App Updates.
- **SHA256SUMS.txt:** checksums for these four downloads.

The `.gwupdate` files are consumed by Gridworks' updater and are not standalone installers.

## Validation and remaining hardware checks

The release package matches the application, installed guides, integration payloads and two-page profile source. Its installer inventory, embedded payload and runtime checksums are verified. Both supported versions' unmodified shipped updaters accept the signed manifest and reconstruct all 253 target App files. Success and failed-readiness rollback fixtures preserve the prior installation and saved-data fixtures. The 7.18 update reuses its complete existing desktop host and runtime.

Automated application, browser and Windows installation results are recorded in the source PR. GitHub's Actions artifact-storage quota can block test attachment uploads; the published release files are independently built, byte-verified and checksummed through the existing release publisher.

Actual two-car AC/CSP calibration, three-run setup confirmation with the intended car mods, physical SimHub/Stream Deck import, real OBS clip paths and Windows component permissions have not been tested on the driving rig. The signed-update reconstruction uses explicit process/readiness fixtures on Linux and does not claim a live Windows restart. Tandem results remain observed-data practice estimates. Event Director remains separate.

## Integrity

| File | SHA-256 |
| --- | --- |
| Gridworks-Drift-Coach-Setup.zip | `2ff9417e72d7da7c800ac93e5919fda16967a9d81d199f00207cb24cb81975a4` |
| Gridworks-7.18.0-to-7.19.0.gwupdate | `c909520250ed38a13294c823e8b9e646a0ee90ef87fbea73094e2576300d51d3` |
| Gridworks-7.17.0-to-7.19.0.gwupdate | `b34b059e07c10629a21799f0f0f0495b0042870887337514671a069e9e0c58bc` |
| Gridworks-Small-Update-7.19.0.zip | `c1b36c5ec5b046c8c802b2a81b6c1e15156dc1c1dbf58ff3f2449ebd8f80ccad` |

The existing trusted update-signing key and verified checkout settings are retained. No private signing key is included in downloads or repository content.
