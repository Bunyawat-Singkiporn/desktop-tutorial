# Python Beginner — English slides

Full-English teaching track for Python Beginner.

| Locale | Folder |
|--------|--------|
| English (this) | `slide-en/` |
| Thai | [`../slide/`](../slide/) |

## Parity with Thai

- Same 48 week folders (`001`–`048`)
- Same filenames for lesson slides, exercises, and `answer/*.py`
- Standard set per chapter: `00_index.md`, teaching `01_*.md`, 15 exercises (`02`–`16`), matching answers
- Scope and problem rules: [`_SCOPE.md`](_SCOPE.md), [`_PROBLEM_STANDARD.md`](_PROBLEM_STANDARD.md)

Only the markdown teaching/exercise prose is translated. Sample I/O and answer logic follow the Thai track.

## Check filename parity

```bash
python tools/sync_slide_en_parity.py diff
python tools/sync_slide_en_parity.py thai-md
python tools/sync_slide_en_parity.py compile
```
