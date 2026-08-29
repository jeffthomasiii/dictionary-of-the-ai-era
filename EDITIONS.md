# EpochLex Editions

EpochLex is a living dictionary. The public site and the `main` branch are expected to change as terminology, evidence, definitions, and editorial judgments evolve.

Annual editions provide stable historical snapshots without turning the live dictionary into a frozen publication.

## Two publication states

### Living Dictionary

The Living Dictionary is the current public version of EpochLex.

- Source: `main`
- Public site: the current canonical EpochLex site
- Mutable: yes
- Purpose: reflect the best current editorial state
- Terms may be added, revised, reclassified, connected to new related terms, or updated when better evidence becomes available

The Living Dictionary is the version readers should normally use when they want the most current EpochLex entry.

### Annual Edition

An Annual Edition is an immutable snapshot of the Living Dictionary at a declared editorial cutoff.

The naming convention is:

`EpochLex YYYY`

For example, **EpochLex 2026** represents the dictionary's editorial state through its declared 2026 cutoff. The release itself may be created shortly after the cutoff while retaining the 2026 edition name.

Annual editions are intended for historical reference, citation, comparison, and preservation. They are not separate forks of the live website.

## What an edition contains

An edition points to one exact repository commit containing the complete published state at the cutoff, including:

- `data/terms.json`
- `data/provenance.json`
- dedicated term pages
- category and relationship data represented by those files
- editorial and methodology documentation present at the snapshot commit

The repository commit is the archival unit. EpochLex does not copy the entire website into a new `/2026/`, `/2027/`, or similar directory for each edition.

## Release mechanics

Each released annual edition should have:

1. A declared editorial cutoff date.
2. A final validation confirming term/provenance parity and published-page integrity.
3. A record added to `data/editions.json`.
4. An immutable Git tag using the convention `epochlex-YYYY`.
5. A GitHub Release titled `EpochLex YYYY` pointing to that tag.
6. Release notes containing at minimum the edition year, cutoff date, release date, term count, and any material editorial notes.

Tags for published editions must not be moved.

The earlier planned `ailex-YYYY` convention was changed before any annual edition was released, so no historical edition tag is being rewritten by this migration.

## Cutoff policy

The normal annual cutoff is the end of the named calendar year. The exact date used for an edition must be recorded in `data/editions.json` and the GitHub Release notes.

An edition can be released after the cutoff. For example, a snapshot finalized in early January 2027 may still be **EpochLex 2026** when it represents the reviewed dictionary state through the 2026 cutoff.

## Corrections after release

The Living Dictionary should be corrected whenever better evidence or editorial review warrants a change.

A published annual edition remains immutable so it continues to represent what EpochLex contained at that historical point. If an important correction affects a released edition:

- correct the Living Dictionary;
- document the correction or erratum in the relevant GitHub Release notes when appropriate;
- do not move or rewrite the original edition tag.

If a replacement archival release ever becomes necessary, use an explicitly differentiated tag rather than silently changing the original snapshot.

## Citation guidance

For current information, cite the Living Dictionary and include the access date when useful.

For a stable historical reference, cite the named edition and its release/tag. A suggested form is:

> EpochLex. *EpochLex 2026: Dictionary of the AI Era*. Annual edition, 2026. GitHub release/tag `epochlex-2026`.

The exact release URL can be added once the edition exists.

## Machine-readable edition registry

`data/editions.json` is the source of truth for edition metadata. It describes the mutable Living Dictionary and records released annual editions.

An annual edition is not considered released merely because a calendar year appears in the registry or documentation. It becomes a released edition only when its record has `status: "released"`, an immutable tag, a snapshot commit, and a release date.

## Inaugural edition

The first planned annual snapshot is **EpochLex 2026**. Until that snapshot is formally released, EpochLex remains the Living Dictionary and no historical annual edition should be presented as already published.
