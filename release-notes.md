# Gridworks Drift Coach 7.19.9

**17 offline coaching lessons** bring explanations from [Will Hurst (Gone)'s Assetto Corsa setup guide](https://docs.google.com/document/d/1rITmKOnmwWcvm4aGIs6t-27tlaGlD3dTdfVH8WdUnmY/edit) and [Derrion Bass's coaching session with Gone](https://www.youtube.com/watch?v=CwtXSohnthU) into the app. Topics include repeatable baselines, track references, entry and throttle timing, tires, alignment, suspension, gearing, brakes, differential behavior and chase technique.

## Where to find the lessons

- **Setup Library:** open **Garage → Setup Lab → Gridworks Setup Library → Coaching lessons**. Each collapsible lesson includes what to check, a focused practice step, a tradeoff, scope and source links. Video links open at the relevant timestamp. Lesson text is available offline; opening a source requires internet access.
- **Setup Test:** newly completed baselines add **Learn why** alongside their existing result. Supported adjustment proposals receive a relevant explanation; a hold can receive inspection or repeatability guidance while retaining the current setup. The installed car's controls and the existing three-run decision remain authoritative.
- **Run Review:** the **Practice** card can show a relevant lesson when the saved trace supports it. Solo lessons focus on track references or reviewing entry/throttle timing. Tandem lessons focus on replay review; chase-transition guidance requires validated paired transition observations. Limited traces do not receive a new contextual lesson.

The lessons use compact, attributed explanations. Demonstrated settings are not universal presets, and a practice suggestion does not establish the cause of a measured result. Setup changes remain manual and the scoring rules are unchanged. General suspension explanations include qualifications and engineering sources in the library.

## Existing features retained

The Setup Library still includes **12 pack/physics families and 24 parameter-reference cards**, including **DCGP Season 13** and VDC 6.0. Pack season, individual car revision and physics identity remain distinct, with saved checklist history preserved.

The wider Setup Test rules remain: **at least ten qualifying slide seconds**, **85% usable coverage**, **±15 mph entry speed**, route endpoints within **30 m**, distance within **±30%**, and the same primary drift gear for at least **70%** of measured forward-gear slide time. Brief shifts are allowed. Starting rear tire core temperature can vary by **±25°C**, road and reported air temperatures by **±10°C**, and reported surface grip by **±0.05**.

The **three-run baseline and retest**, **Reset Test**, run-count recovery, original saved scores, setup revisions, completed test history, separate Solo/Tandem reviews and the ten-second completed-result display remain in place. Voice remains score-only and the tablet retains its compact summary. The online leaderboard stays deferred and unconfigured. Licensing remains a **seven-day full trial**, then **$5 USD once for a lifetime license**.

## Install or update

- **Existing users:** open **App Updates → Check for updates**, download the compatible signed patch, finish driving and choose **Restart to update** after closing Assetto Corsa.
- **New users or builds requesting a full installer:** download [Gridworks-Drift-Coach-Setup.zip](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.9/Gridworks-Drift-Coach-Setup.zip), extract it, open the **Gridworks-Drift-Coach** folder and run **Gridworks-Setup.exe**. The ZIP contains the installer and **START-HERE.html**.
- **Offline update:** [Gridworks-Small-Update-7.19.9.zip](https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.9/Gridworks-Small-Update-7.19.9.zip) supports **7.19.8 only**. Extract it, close Assetto Corsa and run **Update-Gridworks.cmd**. Other supported versions should use App Updates or the full installer.

The signed online update supports exact installed builds **7.17.0, 7.18.0, 7.19.0, 7.19.1, 7.19.2, 7.19.5, 7.19.6, 7.19.7 and 7.19.8**. Saved driver data, setups, runs, trial dates and license settings are retained.

## Validation scope

All seven source workflows passed for the release commit, including [App checks](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/45067607317) and the [Windows desktop and installer build](https://github.com/lmonroe8/gridworks-drift-coach/actions/runs/45067607301). Checks cover lesson/source integrity, timestamped links, conditional selection, evidence gates, compatibility with older records, safe text/link rendering, source-to-package parity and installer inventory. Real Chromium checks exercise the Setup Library, completed-test explanations and saved-run Practice cards against the app backend, alongside existing setup/workspace regressions.

Signed-update validation passed all **36 success/rollback scenarios** across nine exact published baselines, plus the **7.19.8-only offline update**. Public assets are downloaded without authentication and verified against their expected size and SHA-256 before the update feed advances. The [public validation record](https://github.com/lmonroe8/gridworks-drift-coach-releases/blob/main/validation/7.19.9.json) records release evidence; source workflow logs require access to the private source repository.

Browser and telemetry fixtures are synthetic. Live Assetto Corsa/CSP driving with third-party cars or physics revisions and physical SimHub/rig behavior remain separate checks. Practice estimates do not establish a setup's handling effect.

Source commit: `467657ee9cd9036e4970f9d67250b214df474895`  
Source tree: `44e7447399bfaa3103c956283a5b6de2c9140d99`
