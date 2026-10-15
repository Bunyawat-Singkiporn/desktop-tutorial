# 📋 Exercise index — Lesson 002 Run programs and read errors

**Scope of this lesson:** `print("...")` only (no new syntax) + reading three kinds of errors

> ❌ No variables yet (Lesson 005) · no `input()` (Lesson 008) · no calculations (Lesson 011)

---

## Recommended order

| # | File | Level | Exercise | Core idea |
|---|------|-------|----------|-----------|
| 1 | `02_test.md` | 🟢 | Forgot to close a quote | One SyntaxError |
| 2 | `03_test.md` | 🟢 | Wrong command spelling | NameError from capital letter |
| 3 | `04_test.md` | 🟢 | Leading spaces on a line | IndentationError |
| 4 | `08_easy.md` | 🟢 | Forgot to close parentheses | SyntaxError, different from Q1 |
| 5 | `09_easy.md` | 🟢 | Error shows the line number | Read a traceback |
| 6 | `06_medium.md` | 🟡 | Two bugs in one program | Multiple error types in one file |
| 7 | `07_medium.md` | 🟡 | Three bugs | All three error types in one file |
| 8 | `10_medium.md` | 🟡 | Wrong quote character type | Hard-to-spot bug |
| 9 | `11_medium.md` | 🟡 | Runs but output incomplete | Syntax fix plus missing line |
| 10 | `12_medium.md` | 🟡 | Runs but wrong order | No error, wrong output |
| 11 | `13_medium.md` | 🟡 | Fix the whole report card | Longer file, scattered bugs |
| 12 | `05_challenge.md` | 🔴 | Hunt all four bug types | Four bugs, four types, one program |
| 13 | `14_challenge.md` | 🔴 | Match error to cause | Predict error names from code |
| 14 | `15_challenge.md` | 🔴 | Rescue the whole menu sign | Long file, errors and wrong order |
| 15 | `16_challenge.md` | 🔴 | Personal debug checklist | Summarize fixes as your own work |

**Summary:** 🟢 Easy 5 · 🟡 Medium 6 · 🔴 Challenge 4 = **15 exercises**

---

## Notes for teachers

- The core of this lesson is **reading errors and fixing them**, not writing new code from scratch.
- Three error types to distinguish: `SyntaxError` (unclosed parens/quotes) ·
  `NameError` (unknown name, e.g. `Print`) · `IndentationError` (leading spaces)
- Q10 is important: the program **runs but output is wrong** — show that “no error” ≠ “correct”.
- Q8 is a very common real trap (copy from Word/web → curly quotes).
- Q13 does not require fixing code — **predict** the error name; good check for understanding.
- Workflow: fix one issue, then run again every time.
