# Experiment web publication — review-branch notes

Status: **draft implementation for PR review**

## Authority

- Product and implementation authority: current `main` at the branch point.
- Report content authority for this pass: `EpochLex_Experiment_Report_Styled_Pass_Final.docx`.
- Observation period: August 28–September 17, 2026.
- Reporting snapshot: September 18, 2026.

The public overview summarizes the report. It must not strengthen a claim beyond what the report supports.

## Implemented in this branch

- `/experiment/`: visual public overview based on the approved mockup direction.
- `/experiment/report/`: web-report reading surface, executive material, metrics, complete current report map, case-study index, limitations, appendices, and sync notes.
- About and Methodology cross-links.
- PWA More-sheet access to the Experiment.
- service-worker cache entries for the new pages and stylesheet.
- sitemap entries.
- DESIGN.md site-structure documentation.

## Intentionally provisional

The following are expected to be revisited after the long-form report review:

1. **Figures and quantitative graphics.** Current visuals are web-native placeholders, not final report figures.
2. **PDF download.** The control remains disabled until the approved PDF exists in the repository.
3. **Case-study prominence.** The overview currently gives all ten case studies equal weight. Selective highlighting should happen only after the report review.
4. **Page count / reading time.** Omitted because pagination is not stable.
5. **Full section-by-section body transcription.** The web report locks the reading system and complete report hierarchy now; final approved prose should be synchronized after report review.
6. **Any changed findings, metrics, limitations, captions, or headings.** Report changes remain authoritative and should be mirrored here.

## Claims that should remain qualified

- Do not turn PR, corpus, token, or issue counts into a productivity multiplier.
- Do not claim labor savings; historical human effort was not tracked systematically.
- Do not present EpochLex as autonomous or wholly AI-created.
- Do not generalize this case study automatically to other architectures, teams, or risk profiles.
- Distinguish direct measurement, reconstruction, and prospective measurement.
- Preserve uncertainty around historical token use and exact model identity where the report does.

## Final-sync checklist

- [ ] Replace web figure placeholders with approved figures or faithful web adaptations.
- [ ] Synchronize final report prose section by section.
- [ ] Confirm metrics against the approved report.
- [ ] Revisit which case studies receive featured treatment.
- [ ] Commit the approved PDF and enable the download link.
- [ ] Add final PDF file size/page count only after the artifact is stable.
- [ ] Re-run responsive, dark-mode, keyboard, PWA, and offline QA.
- [ ] Confirm canonical URLs, sitemap entries, and social metadata.
