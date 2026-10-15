# Problem Standard — python-beginner

Rules for every exercise in `slide-en/`, so each chapter has the same quality and scope.

---

## 1) Count and mix per chapter

| Level | Count | When to use |
|-------|-------|-------------|
| Easy | 5 | In class after the lesson |
| Medium | 6 | In class / graded |
| Challenge | 4 | Fast finishers / extra homework |
| **Total** | **15** | |

> Each chapter's `00_index.md` is the table of contents with the recommended order.

---

## 2) Scope rule (most important)

> **Never use something that has not been taught yet.** See `_SCOPE.md`.

- Chapter N exercises may only use knowledge from chapters 1 through N
- Prior chapters are fair game (and should be reused for review)
- **Challenge problems must also stay in scope** — they are hard because they *combine* conditions/steps, not because they introduce new syntax
- If you want a problem that needs something new → save it for the chapter that teaches it

**Making problems harder without going out of scope**

| Allowed | Not allowed |
|---------|-------------|
| Stack two condition checks | Use `elif` before chapter 015 |
| Compute first, then compare | Use `and` / `or` before chapter 016 |
| Read several inputs | Use `for` before chapter 017 |
| Format output as a table/box | Use `list` before chapter 018 |

---

## 3) The first exercise must **not** be the lesson example

Exercise `02` in every chapter must not be the same problem as the demo in the lesson file.

- Lesson teaches "score >= 50 → Pass/Fail" → first exercise must change the situation (e.g. temperature, battery, height)
- Changing only the numbers does not count — change the **situation** too
- Check the `EXAMPLES:` field in `_SCOPE.md` for what that chapter already used

---

## 4) Problems must be real situations, not abstract drills

| Good | Bad |
|------|-----|
| "Shop charges 40 baht delivery; free if spend reaches 300" | "Read n; if n >= 300 print 0 else 40" |
| "App warns when battery is under 20%" | "Read x and compare to 20" |
| "Parking: first hour free" | "Read h; compute (h-1)*20" |

**Naturalness checklist**

- [ ] You can picture where this happens in real life
- [ ] Starter variable names mean something (`price`, not `x`)
- [ ] Numbers are realistic (price 499, not 7)
- [ ] No odd wording / bad translations

---

## 5) Exercise file skeleton (same for every problem)

````markdown
# Battery if/else — Q3: Low battery warning

**Difficulty:** Easy

---

## Task

<1–3 sentence situation>

**Rules:**

- If ... → `Low Battery`
- Else → `Battery OK`

---

## Input

<what to read, how many lines>

## Output

<what to print>

---

## Example

**Input:**

```text
15
```

**Output:**

```text
Battery : 15%
Status  : Low Battery
```

---

## Hint

<idea, not solution code>

---

## Starter Code

```python
battery = int(input())

# Write your code here
```
````

**Rules per section**

| Section | Rule |
|---------|------|
| Title | `# <emoji> <chapter> — QN: <English title>` |
| Difficulty | Easy / Medium / Challenge only |
| Task | Tell a situation; do not dictate the exact code structure |
| Input / Output | Be clear how many values and how many lines |
| Example | At least **one** pair inside ` ```text ` blocks |
| Hint | Optional for Easy; required for Medium/Challenge |
| Starter Code | Input lines + comment only; do not give a finished if/else skeleton |

> Do **not** write compact examples like `**Input:** 10 → Open`
> Always use separate blocks (automated checkers read those blocks)

---

## 6) Good hints

A hint is an **idea**, not the answer.

| Good hint | Bad hint |
|-----------|----------|
| "Compute the net price into a variable first, then print" | `final = price - 20` |
| "First check if the money is enough, then compute change" | `if money >= price:` |
| "Parking fee uses hours beyond the first hour" | `(hours - 1) * 20` |

> If pasting the hint runs as working code, the hint breaks the rule.

---

## 7) Output styles

Pick what fits the problem.

**Style 1 — single line** (simple, one result)

```text
Even Number
```

**Style 2 — labels** (2–3 values)

```text
Total: 18
```

```text
Battery : 15%
Status  : Low Battery
```

**Style 3 — summary box** (many values / Medium–Challenge)

```text
========================
      SHOPPING
========================
Price       : 499
Discount    : 10
Final Price : 489
========================
```

> Output text should be English (easy to type).
> Boxes use `=` of equal length and align the `:` columns.

---

## 8) No duplicates inside a chapter

The 15 exercises in one chapter must **not share the same thinking core**.

- Bad: Q2 "score >= 50 → Pass/Fail" + Q7 "score >= 60 → Pass/Fail" = duplicate
- Good: Q2 "compare to a fixed threshold" + Q7 "compare two input values" = different

**Ways to vary the thinking core**

1. Compare to a constant
2. Compare two inputs
3. Compute first, then compare
4. Compare, then compute further
5. Two condition blocks in sequence
6. Condition whose result is a number, not a message

---

## 9) Answer files

- Every exercise needs an answer in `answer/` whose name starts with the same number
- Answers must **run**, and with the sample Input they must match Output character-for-character
- Answers stay in scope too (no shortcuts from later chapters)

---

## 10) Chapter close-out checklist

- [ ] All 15 exercises exist
- [ ] Q02 is not the lesson demo
- [ ] Nothing out of scope (checker passes)
- [ ] Every exercise has Input/Output example blocks
- [ ] Hints are not solutions
- [ ] Answers match the samples
- [ ] No two exercises share the same thinking core
- [ ] `00_index.md` is up to date
