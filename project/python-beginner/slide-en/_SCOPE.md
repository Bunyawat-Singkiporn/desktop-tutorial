# CUMULATIVE SCOPE LEDGER — python-beginner (chapters 001–048)

Source: `/mnt/user-data/uploads/python-beginner/slide/*/01_*.md` + `017-for-loop/02_range.md`

Rule for readers: a concept is IN SCOPE only from the chapter where it appears under **NEW**.
Anything listed under NOTES as "used but not explained" is NOT safe to require in a practice problem
at that chapter — it only becomes safe at the chapter where it appears under NEW (if ever).

---

### 001-what-is-python
NEW: `print()` with a single string literal, double-quoted string literal `"..."`, multiple `print()` calls on separate lines (each ends with a newline automatically)
EXAMPLES: `print("Hello, World!")`, three-line Thai greeting (`สวัสดี!` / `ฉันชื่อ Python` / `ยินดีที่ได้รู้จัก`), recipe-vs-program analogy table, Python-use-cases table (games/web/AI/science/robots)
NOTES: No variables, no input, no numbers at all. Only string literals inside `print()`. Analogy-heavy conceptual opening; the only executable syntax is `print("text")`.

### 002-python-environment
NEW: (concept only) — editors (VS Code / PyCharm / IDLE), how to run a `.py` file (Run button, `python hello.py` in terminal), how to read an error message (error type / detail / line number)
EXAMPLES: `print("Hello"` (unclosed paren) vs `print("Hello")`, SyntaxError traceback anatomy table, common-error table (`SyntaxError`, `NameError`, `IndentationError`), 4 debugging tips
NOTES: No new Python syntax. Error names `SyntaxError` / `NameError` / `IndentationError` are introduced as vocabulary only. `python hello.py` is a shell command, not Python.

### 003-python-syntax
NEW: (concept only) — three syntax rules: Python is case-sensitive (commands are always lowercase), brackets/quotes must be balanced, no leading spaces on a normal line (indentation rules)
EXAMPLES: `Print("Hello")` → NameError, `print("Hello"` → SyntaxError, `  print("Hello")` → IndentationError, correct/incorrect tables, 3-rule summary table
NOTES: No new executable syntax — still only `print("...")`. Mentions that indentation "will have special meaning when you learn `if` and `for`" but does not teach either.

### 004-comments
NEW: `#` comment (own line and trailing after code), multi-line commenting by repeating `#`
EXAMPLES: `x = 86400` / `print(x * 7)` (bad, no comment) vs `seconds_per_day = 86400` / `print(seconds_per_day * 7)` (good), shop sign banner (`print("====...")`, `print("   BEST SHOP EVER  ")`, `print("Open: 8am - 10pm")`), header block comment (program name / author / date)
NOTES: **Uses but does not explain: variable assignment (`x = 86400`, `seconds_per_day = 86400`) and the `*` operator (`x * 7`)** — variables are only formally taught in 005 and `*` in 011. Good-vs-bad comment table (explain WHY, not WHAT).

### 005-variables
NEW: variable assignment with `=`, reassignment (rebinding a variable), `print(variable)`, **`print` with comma separators** (`print("Hello,", name)` — multiple args), string variables, int variables, float variables, `+` used to add two numeric variables
EXAMPLES: `age = 12` / `name = "Alex"` / `price = 99.5`, `print("Hello,", name)`, `score = 0` then `score = 100`, price+tax total (`price = 100`, `tax = 7`, `total = price + tax`), personal info program (name/age/city with `print("Name:", name)` style)
NOTES: This is the FIRST chapter with `print` comma-separated output — it stays the only interpolation style until 010. `+` on numbers is used here (price + tax) but the operator table is only taught in 011. Box-with-a-label diagram. Notes that `=` means "store", not mathematical equality; `"Alex" = name` is invalid.

### 006-naming-rules
NEW: (concept only) — naming rules (letters/digits/`_`, no leading digit, no spaces, all lowercase, meaningful names), `snake_case` convention, reserved keywords cannot be variable names
EXAMPLES: `x = 100` / `y = 50` / `print(x - y)` vs `price = 100` / `discount = 50` / `print(price - discount)`, snake_case list (`first_name`, `total_price`, `player_score`, `is_game_over = False`), camelCase counter-examples, keyword misuse (`if = 5`, `for = 10`, `print = "hi"`), T-shirt price program (`product_name`, `original_price = 500`, `discount_amount = 100`, `final_price`)
NOTES: **Uses but does not explain: `-` subtraction, and the boolean literal `False` (`is_game_over = False`)** — booleans are formally taught in 007, `-` in 011. Keyword table mentions `if`, `else`, `for`, `while`, `input`, `True`, `False` by name only — none are taught here.

### 007-data-types
NEW: the four types `int`, `float`, `str`, `bool`; `True` / `False` literals; `type()` function; the fact that `"5"` is a str and `"5" + "5"` concatenates while `5 + 5` adds
EXAMPLES: int set (`age = 15`, `score = 100`, `temperature = -5`, `floor = 3`), float set (`price = 29.99`, `pi = 3.14159`, `weight = 55.5`, `height = 1.75`), str set (`name = "Alice"`, `city = "Bangkok"`, `greeting = "Hello, World!"`, `emoji_text = "I love 🐍"`), bool set (`is_open = True`, `has_discount = False`, `is_student`, `game_over`), `print(type(age))` for all four, `a = 5` / `b = "5"` with `print(a + a)` → 10 and `print(b + b)` → 55
NOTES: String concatenation with `+` first appears here, but only as a gotcha demo (`"5" + "5"` → `"55"`), not taught as a formatting technique. `type()` output shown as `<class 'int'>`. No `input()` yet.

### 008-type-conversion
NEW: `int()`, `float()`, `str()`; **`int(input())` and `float(input())` (first appearance)**; **string concatenation with `+` as a deliberate output technique** (`"Your score is: " + str(score)`); the rule that `input()` always returns str
EXAMPLES: `age = input()` then `print(type(age))` → str, `print(age + 1)` → TypeError, conversion table (`int("15")`, `float("3.5")`, `str(100)`), next-year age (`age = int(input())`, `age + 1`), VAT price (`price = float(input())`, `price * 1.07`), `message = "Your score is: " + str(score)`, when-to-use summary table
NOTES: **This chapter comes BEFORE 009-input but is where `input()`, `int(input())` and `float(input())` actually first appear in code.** `input()` is used here with NO prompt argument. `*` (multiplication, `price * 1.07`) used before 011 teaches it. `TypeError` named. Output is still `print("text:", var)` comma style plus `+`-concatenation — no f-string yet.

### 009-input
NEW: `input()` taught formally (program pauses and waits for one line), one `input()` per line of user input, combining several `input()` calls
EXAMPLES: `name = input()` / `print("Hello,", name)`, `age = input()` / `print(type(age))`, two-name program (`first_name`, `last_name`, `print("Full name:", first_name, last_name)`), `age = int(input())` / `next_year = age + 1`, complete program (name + age → prints Name / Age / Next year)
NOTES: `input()` is ALWAYS called with no prompt argument in this chapter (`input()`, never `input("...")`). Summary table repeats `x = input()`, `x = int(input())`, `x = float(input())`. All output uses comma-separated `print` — still no f-string.

### 010-output-formatting
NEW: **f-string** (`f"...{var}..."`), float format spec `:.2f` inside an f-string, `print(..., sep="...")`, `print(..., end="...")`, `end=" "` to keep output on one line
EXAMPLES: old-style `print("My name is " + name + " and I am " + str(age) + " years old.")` vs `print(f"My name is {name} and I am {age} years old.")`, discount receipt (`price = 250`, `discount = 50`, `final`, three aligned f-string lines), `print(f"Pi = {pi:.2f}")` and `print(f"Price: {price:.2f}")`, `print("A", "B", "C", sep="-")` and `sep=" | "`, `print("Hello", end=" ")` + `print("World")`, Name/Score/Grade comparison (`"Sam"`, `95`, `"A"`)
NOTES: Explicitly frames `+`-concatenation as the old/bad way and f-string as recommended. `:.2f` is the only format spec taught (`:.1f` appears later in 018 without further explanation). `sep=` and `end=` are taught here; `end=""` is reused heavily in 021.

### 011-operators
NEW: `+`, `-`, `*`, `/`, `//`, `%`, `**`; comparison operators `==`, `!=`, `>`, `<`, `>=`, `<=`; operator precedence (`**` then `*`/`/`/`//`/`%` then `+`/`-`) and parentheses to override
EXAMPLES: arithmetic table (`10 + 3`, `10 - 3`, `10 * 3`, `10 / 3`, `10 // 3`, `10 % 3`, `2 ** 3`), `print(10 / 3)` vs `print(10 // 3)`, modulo demos (`10 % 3`, `15 % 4`, `8 % 2`), comparison table (`5 == 5`, `5 != 3`, `5 > 3`, `5 < 3`, `5 >= 5`, `3 <= 5`), change-calculation program (`price = int(input())`, `paid = int(input())`, `change = paid - price`, three f-string prints), `print(2 + 3 * 4)` vs `print((2 + 3) * 4)`
NOTES: Comparison operators are presented as producing `True`/`False`, but there is NO `if` yet — they cannot be used in a branch until 013. Modulo is explicitly flagged as "used a lot for even/odd in the next chapter". This is the first chapter where f-string and `int(input())` appear together in a full program.

### 012-review
NEW: (concept only, no new syntax) — review of chapters 1–11, the 3-step program formula (input → process → output), a submission checklist
EXAMPLES: week-by-week recap table, combined program (`name = input()`, `age = int(input())`, `price = float(input())`, `price_with_vat = price * 1.07`, three f-strings incl. `{price_with_vat:.2f}`), common-error table (`NameError`, `TypeError` from `"5" + 5`, `SyntaxError`)
NOTES: Teaser list at the end names `%`, `if/else`, `elif`, `and`/`or`/`not`, and For Loop as UPCOMING — none of them are taught here. Checklist pushes snake_case, converting input, and f-strings.

### 013-if-else
NEW: `if condition:`, `else:`, the colon `:`, 4-space indentation of the body, `if`/`else` two-way branching
EXAMPLES: abstract skeletons (`if เงื่อนไข:` / `if`+`else`), Pass/Fail program (`score = int(input())`, `if score >= 50: print("Pass") else: print("Fail")`), input/output table (80→Pass, 45→Fail, 50→Pass)
NOTES: Only `>=` is used in a real condition here. No `elif`, no `and`/`or`/`not`, no nested `if`. Warns: colon required, body must be indented 4 spaces, `else` takes no condition.

### 014-even-odd
NEW: (no brand-new syntax — first APPLICATION of `%` inside an `if` condition) — the even/odd idiom `number % 2 == 0` / `number % 2 != 0`
EXAMPLES: modulo table (`7 % 2`, `10 % 2`, `9 % 2`), even/odd condition table, Even/Odd program (`number = int(input())`, `if number % 2 == 0: print("Even") else: print("Odd")`), I/O table (8→Even, 7→Odd)
NOTES: This is where `==` and `!=` are first used inside an actual `if` (they were only shown in a table in 011). Very short lesson — one program, one idea. Do not duplicate the plain Even/Odd program in practice problems.

### 015-elif
NEW: `elif`, chaining multiple `elif` branches, top-to-bottom evaluation that stops at the first True branch
EXAMPLES: motivation (2 outcomes vs 4 grades A/B/C/F), abstract skeleton (`if` / `elif` / `elif` / `else`), grade program (`score = int(input())`, `>= 80` → A, `>= 70` → B, `>= 60` → C, else F), I/O table (85→A, 72→B, 61→C, 45→F)
NOTES: The 80/70/60 → A/B/C/F grader is THE canonical example here and is repeated almost verbatim in 039, 040 and 044 — avoid reusing it as a practice problem. Still no logical operators, still no nested `if`.

### 016-logical-operator
NEW: `and`, `or`, `not`; combining two comparisons in one `if`; using a bool variable directly as a condition
EXAMPLES: operator meaning table, `if age >= 12 and score >= 50: print("Pass")` with a truth table (15/80 pass, 10/80 no, 15/30 no), `if score > 90 or score < 20: print("Special")` (95 yes, 10 yes, 50 no), `is_raining = False` / `if not is_raining: print("Go Outside")` with a truth table
NOTES: Every example is `if` with NO `else`. Variables `age`, `score`, `is_raining` are hard-coded, not read from `input()`. `not` is only demonstrated on a bool variable, never on a comparison. No nested `if` anywhere; no `and`/`or` mixed in one expression.

### 017-for-loop (01_for_loop.md)
NEW: `for i in range(n):` (single-argument `range`), loop body indentation, the loop variable `i`, the fact that `range(5)` yields 0–4
EXAMPLES: five identical `print("Hello")` lines replaced by `for i in range(5): print("Hello")`, `for i in range(5): print(i)` → 0 1 2 3 4, summary table
NOTES: Only the 1-argument form of `range` here. Loop variable is unused in the first example, used in the second. No list iteration yet, no nesting, no accumulation.

### 017-for-loop (02_range.md)
NEW: `range(start, stop)` (2-arg) and `range(start, stop, step)` (3-arg); stop is exclusive; default step = 1
EXAMPLES: parameter table (start / stop / step), `for i in range(1, 6): print(i)` → 1–5, `for i in range(2, 11, 2): print(i)` → 2 4 6 8 10, comparison table (`range(5)`, `range(1, 6)`, `range(2, 11, 2)`)
NOTES: Negative step / counting down is NEVER shown (`range(10, 0, -1)` is out of scope for the whole course). Only `print(i)` bodies — no accumulation, no `if` inside a loop yet.

### 018-loop-with-lists
NEW: list literal (`["Apple", "Banana", "Mango"]`, numeric lists), **iterating a list directly (`for item in mylist:`)**, `len()`, accumulator pattern (`total = 0` … `total = total + score`), division of a total by `len()`, `:.1f` format spec
EXAMPLES: `fruits = ["Apple", "Banana", "Mango"]` with an index table, `for fruit in fruits: print(fruit)`, score sum (`scores = [85, 92, 78, 95, 88]`, total 438, count 5, `f"Average: {total / len(scores):.1f}"` → 87.6), for-range vs for-list side by side (`colors = ["Red", "Green", "Blue"]`), `len(names)` → 3 and `len(numbers)` → 5, summary table
NOTES: Indexing (`fruits[0]`) is shown ONLY in a table and in the summary row `items[0]` → `"a"` — no runnable indexing code in the body; treat real indexing as taught at 025. `:.1f` is used without re-explaining (only `:.2f` was taught, in 010). This is the first list content in the course; full List chapter is 025.

### 019-while-loop
NEW: `while condition:`, the requirement to change the loop variable inside the body, `while True`-style infinite-loop hazard (as a warning, not yet as a technique), `count = count + 1` / `count = count - 1` counters, `while` driven by `input()`
EXAMPLES: count-up (`count = 1`, `while count <= 5`, print, `count = count + 1`) → 1–5, for-vs-while comparison table, countdown (`count = 5`, `while count > 0`, `count = count - 1`, then `print("Blast off! 🚀")`), guess-the-secret (`secret = 42`, `guess = int(input())`, `while guess != secret:` re-prompt, `print("Correct!")`), infinite-loop bad/good pair
NOTES: `while True:` as a deliberate pattern is NOT taught here — only the accidental infinite loop is shown. `break` does not exist yet (the guessing loop exits via its condition). Ctrl+C mentioned as the escape hatch.

### 020-loop-safety
NEW: `break`, `continue`, **`while True:` + `break` as a deliberate idiom**, `if` nested inside a loop, comparing a string to a string literal (`word == "quit"`)
EXAMPLES: `for i in range(10): if i == 5: break` → 0–4, `for i in range(6): if i == 3: continue` → 0 1 2 4 5, break-vs-continue table, `while True:` reading `word = input()` until `"quit"` then `print("Goodbye!")` (prints `print("You typed:", word)`), odd-number filter (`for i in range(1, 11): if i % 2 == 0: continue` → 1 3 5 7 9), loop-safety checklist
NOTES: First string equality comparison against a literal. `input()` still used without a prompt. `break`/`continue` are shown in both `for` and `while` contexts. No `else` clause on loops (never taught in this course).

### 021-nested-loops
NEW: nested `for` loops, using the outer loop variable to control the inner `range` (`range(row)`), `print("*", end="")` to stay on one line, bare `print()` to emit a newline, `end="\t"` and the `\t` escape
EXAMPLES: `for i in range(3): for j in range(3): print(i, j)` (9 lines), 3×4 rectangle of `*`, triangle pattern (`for row in range(1, 6): for col in range(row):`) → 1–5 stars, 3×3 multiplication table (`print(i * j, end="\t")`), summary table
NOTES: `end=` was taught in 010; `\t` as an escape sequence appears here for the first time and is not explained. Star-pattern triangle and the small multiplication table are heavily used here — avoid re-using them verbatim.

### 022-loop-review
NEW: **`+=` augmented assignment (`total += number`, `count += 1`) — first appearance, used but not explained**; `range(1, n + 1)` with a variable bound from `input()`
EXAMPLES: loop-selection table, score sum/average (`scores = [85, 92, 78, 95, 88]` → Total 438, Average 87.6 with `:.1f`), `while True:` reading numbers until `0` then printing `f"Count: {count}, Total: {total}"`, variable-size star triangle (`n = int(input())`, `for row in range(1, n + 1)`), decision flowchart for choosing a loop
NOTES: **Used but not explained: `+=`** (introduced silently; it is never formally taught anywhere in the course but is used from here onward). No new loop construct — this is a consolidation chapter.

### 023-debugging-loops
NEW: (concept only, no new constructs) — four loop bug classes: off-by-one in `range`, infinite `while`, wrong indentation putting a statement outside the loop, using the list name instead of the loop variable; the technique of adding a temporary `print(f"[debug] i = {i}")`
EXAMPLES: `range(1, 5)` vs `range(1, 6)`, missing `count = count + 1`, `for i in range(3): pass` + `print(i)` outside vs inside, `for name in names: print(names)` vs `print(name)` with `names = ["Alice", "Bob", "Charlie"]`, debug-print inside a loop, bug summary table
NOTES: **Used but not explained: the `pass` statement** (appears once in the indentation bug example). The debug snippet references an undefined `total` — it is illustrative pseudo-code, not a runnable program.

### 024-midyear-review
NEW: (concept only, no new syntax) — consolidation of chapters 1–23
EXAMPLES: three recap tables (basics / conditions / loops), one combined program: `name = input()`, `scores = []`, `for i in range(3): score = int(input()); scores.append(score)`, accumulate `total`, `average = total / len(scores)`, `f"Average: {average:.1f}"`, then `if average >= 80` → A / `elif >= 60` → B / `else` → C; end-of-half-year checklist
NOTES: **Uses but does not explain: the empty list literal `scores = []` and `.append()`** — both are only formally taught in 025/026. If a problem at this point needs to build a list, that is technically ahead of scope until 026. Everything else in the program is in scope.

### 025-lists
NEW: list literal formally taught (`[1, 2, 3]`, `["Alice", "Bob"]`, mixed `[10, "hello", True]`, empty `[]`), **indexing `list[0]`**, **negative indexing `list[-1]`, `list[-2]`**, `len()` on a list (re-taught), `for x in list:`, accumulator with `+=`
EXAMPLES: three separate `name1/name2/name3` variables vs one `names` list, creation set (`numbers`, `names`, `mixed`, `empty = []`), `fruits = ["apple", "banana", "mango"]` with `fruits[0]`/`[1]`/`[2]`/`[-1]`/`[-2]`, `len(fruits)` → 3, `for fruit in fruits: print(fruit)`, score total (`scores = [85, 90, 78, 92, 88]`, `total += score`, `print("Total:", total)`), positive/negative index table
NOTES: Negative indexing first appears HERE. `+=` used again without explanation. Still NO slicing (never taught in the whole course), no `.index()`, no `.count()`, no list unpacking.

### 026-list-methods
NEW: item assignment by index (`fruits[1] = "orange"`), `.append()`, `.remove()`, `.sort()`, `.sort(reverse=True)`, the concept "list is mutable", `ValueError` from removing a missing value
EXAMPLES: `fruits[1] = "orange"` → `['apple', 'orange', 'mango']`, `fruits.append("mango")`, `fruits.remove("banana")`, `numbers = [5, 2, 9, 1, 7]` → `.sort()` → `[1, 2, 5, 7, 9]` → `.sort(reverse=True)` → `[9, 7, 5, 2, 1]`, method summary table, score list program (`append(80)`, `remove(68)`, `sort(reverse=True)`)
NOTES: **Only four list methods exist in this course: `append`, `remove`, `sort` (with `reverse=True`), plus index assignment. `.insert()`, `.pop()`, `.reverse()`, `.clear()`, `.extend()`, `.index()`, `.count()` and `sorted()` are NEVER taught anywhere.** Printing a whole list (`print(fruits)`) is shown here for the first time.

### 027-list-practice
NEW: (no new syntax) — two idioms: filter-into-a-new-list and count-with-a-counter; `for i in range(len(mylist)):` index-based loop combined with `mylist[i]`
EXAMPLES: skill recap table, filter (`numbers = [3, 15, 7, 22, 8, 30]` → `big` = `[15, 22, 30]` for `n > 10`), count (`scores = [85, 45, 92, 38, 77, 61]`, `passed += 1` for `score >= 50`), to-do list (`todos = ["Buy food", "Do homework", "Clean room"]`, `for i in range(len(todos)): print(i + 1, ".", todos[i])`), 4-step workflow
NOTES: `range(len(...))` first appears here. Note the to-do output uses comma-`print`, so it renders with spaces (`1 . Buy food`) — a deliberate simple style, not an f-string. No `enumerate()` (never taught).

### 028-review-lists
NEW: (concept only, no new syntax) — consolidation of lists
EXAMPLES: create/access recap (`fruits[0]`, `fruits[-1]`, `len(fruits)`), both loop forms (`for fruit in fruits` and `for i in range(len(fruits)): print(i, ":", fruits[i])`), method recap (`append`, `remove`, index assignment, `sort()`, `sort(reverse=True)`), average pattern (`scores = [80, 75, 90, 65, 88]`, `total += score`, `average = total / len(scores)`), common-mistake table, pre-exam checklist
NOTES: **Mentions `in` only inside a table cell ("check with `in` before removing") — the `in` operator is NOT taught here.** `in` as a membership test is first actually taught in 030 (sets) / 033 (dicts). `IndexError` implied by the "index out of range" row.

### 029-tuples
NEW: tuple literal with `()`, tuple indexing `t[0]` / `t[-1]`, `len()` on a tuple, `for x in tuple:`, immutability (assignment raises `TypeError`)
EXAMPLES: `days = ("Mon", "Tue", "Wed", "Thu", "Fri")`, `point = (10, 20)`, `student = ("Alice", 15, "Grade 9")`, `days[0]`/`days[-1]`/`len(days)`, `for day in days: print(day)`, `days[0] = "Sunday"` → TypeError, list-vs-tuple when-to-use table, student record program (`student = ("Bob", 14, "Grade 8")` printing Name/Age/Grade with comma-`print`)
NOTES: No tuple unpacking (`a, b = point`) is ever taught. No single-element tuple syntax. Tuples are only read, iterated and indexed.

### 030-sets
NEW: set literal `{...}`, automatic de-duplication, `set(list)` conversion, `.add()`, `.remove()` on a set, **the `in` membership operator (first real teaching)**, union `|`, intersection `&`
EXAMPLES: `fruits = {"apple", "banana", "mango"}`, `numbers = {1, 2, 3, 4, 5}`, `nums = {1, 2, 2, 3, 3, 3}` → `{1, 2, 3}`, `data = [1, 2, 2, 3, 4, 4, 5]` → `set(data)`, `.add("mango")` / `.remove("banana")`, `"apple" in fruits` → True and `"grape" in fruits` → False, `a = {"A","B","C"}` / `b = {"B","C","D"}` with `a | b` and `a & b`, method summary table
NOTES: **`in` is introduced here, in the context of sets only** — `print("apple" in fruits)` is the first executable membership test in the course. Set difference `-`, `.discard()`, and `len()` on a set are not shown. Empty set (`set()` vs `{}`) is not discussed.

### 031-choosing-data-types
NEW: (concept only, no new syntax) — decision framework for List vs Tuple vs Set (mutable? ordered? duplicates? indexable?)
EXAMPLES: 4-property comparison table, 2-question decision tree, situation→type table (student roster→list, weekdays→tuple, unique names→set, coordinates→tuple), code trio (`shopping = ["milk","eggs","bread"]` + `.append("butter")`, `weekdays = (...)`, `visitors = {"Alice","Bob","Alice"}`)
NOTES: Pure comparison chapter; every construct shown was already taught in 025/029/030.

### 032-collection-review
NEW: (concept only, no new syntax) — side-by-side review of list/tuple/set; `AttributeError` from `tuple.append()` named
EXAMPLES: all three declared at once (`students` list with duplicate "Alice", `days` tuple, `unique_students` set), index access on list/tuple vs loop-only for set, tuple immutability do/don't block (`days[0] = "Sunday"` → TypeError, `days.append("Sat")` → AttributeError), combined program (`all_students` list → `set(all_students)` → `len()` of both + `grade_info = ("Grade 9", "Room 3")`), final comparison table
NOTES: Uses comma-`print` throughout, not f-strings. Nothing new is executable here.

### 033-dictionaries
NEW: dict literal `{"key": value, ...}` (including multi-line layout), **`dict[key]` access**, adding a new key by assignment (`d["score"] = 92`), `in` on a dict to test key existence, `for key in dict:` (iterating keys implicitly) with `dict[key]` lookup
EXAMPLES: `student = {"name": "Alice", "age": 15, "score": 92}`, `contact = {"name": "Bob", "phone": "081-234-5678", "city": "Bangkok"}`, `print(student["name"])` / `print(student["age"])`, `student["score"] = 92`, `if "name" in student: print("Found:", student["name"])`, `for key in student: print(key, ":", student[key])` → name/age/score lines, contact program (`contact["name"]`, `contact["phone"]`)
NOTES: `.keys()` is NOT used — key iteration is done with the bare `for key in student:` form. `.get()` is NEVER taught in this course; the safe-access idiom taught is `if key in d:`. No dict deletion yet (that is 034).

### 034-dictionary-methods
NEW: value update by key (`d["age"] = 16`), `.update({...})`, `del d["key"]`, `.values()`, `.items()` with two loop variables (`for key, value in d.items():`)
EXAMPLES: `student["age"] = 16`, `student.update({"age": 16, "score": 90})`, `del student["score"]`, `for value in student.values(): print(value)` → Alice/15/90, `for key, value in student.items(): print(f"{key}: {value}")` → `name: Alice` / `age: 15`, method summary table
NOTES: **`.keys()` and `.get()` are never taught in this chapter or anywhere in the course.** The only dict methods in scope are `.update()`, `.values()`, `.items()`, plus `del` and `in`. `for key, value in ...` is the first (and only) multiple-target assignment form in the course.

### 035-dictionary-practice
NEW: **`input()` with a prompt argument (`input("q1: ")`) — first appearance**; the frequency-counting idiom (`if word in count: count[word] += 1 else: count[word] = 1`) starting from an empty dict `{}`; `+=` on a dict value
EXAMPLES: skill recap table, a practice-ordering table (exercise numbers 02–24 by difficulty), word frequency (`words = ["cat","dog","cat","bird","dog","cat"]` → `{'cat': 3, 'dog': 2, 'bird': 1}`), quiz checking (`answers = {"q1":"A","q2":"C","q3":"B"}`, `user_answer = input("q1: ")`, compare to `answers["q1"]`), price table (`prices = {"apple": 15, "banana": 8, "mango": 25}`, `for item, price in prices.items():` with `f"{item}: {price} บาท"` and running `total`)
NOTES: The empty dict literal `{}` first appears here. `input("prompt")` appears here for the first time — before this, every `input()` in the course is bare. Thai text inside f-strings appears here (`f"รวม: {total} บาท"`).

### 036-review-dictionaries
NEW: (no new syntax) — consolidation; the max-finding idiom over `.items()`
EXAMPLES: all-commands recap block (create, access, add, modify, `.update()`, `del`, `.items()` loop), safe access (`if "score" in student: ... else: print("No score yet")`), find-the-top-scorer (`scores = {"Alice": 88, "Bob": 72, "Charlie": 95}`, `highest = ""`, `max_score = 0`, loop `.items()`, `print(f"Top: {highest} ({max_score})")`), pre-exam checklist
NOTES: The "find the maximum by looping and comparing" pattern is introduced here as a manual idiom — the builtin `max()` is never taught. Avoid duplicating the top-scorer program.

### 037-functions
NEW: `def name():` with no parameters, 4-space indented body, calling a function `name()`, the rule that a function must be defined before it is called
EXAMPLES: three hard-coded greeting prints vs `def greet(): print("Hello!")` called three times, anatomy of `def` (keyword / name / colon / indent), `greet()` printing two lines called twice, wrong order (call before def) vs right order
NOTES: No parameters, no `return`, no arguments in this chapter — every function is zero-arg and side-effecting via `print`. Docstrings are not mentioned.

### 038-parameters
NEW: parameters in `def f(x):`, arguments at the call site, multiple parameters, parameter-vs-argument vocabulary, argument-count errors, using parameters in a computation
EXAMPLES: `def greet(name): print("Hello", name)` called with `"Alice"`/`"Bob"`, `def describe(name, age): print(f"{name} is {age} years old.")` with `("Alice", 15)` / `("Bob", 14)`, `def add(a, b): print(a + b)` with `add(3, 5)` / `add(10, 20)`, parameter/argument table, wrong arity (`add(3)`, `add(3, 5, 7)`), BMI (`def show_bmi(weight, height): bmi = weight / (height ** 2)`, `f"BMI: {bmi:.1f}"`, called with `(60, 1.70)` and `(75, 1.75)`)
NOTES: **Default argument values and keyword arguments are NEVER taught in this course.** All functions here still `print` rather than `return`. `**` is used again (height squared).

### 039-return-values
NEW: `return`, capturing a returned value (`result = f(...)`), `return` inside `if`/`elif`/`else`, returning `True`/`False`, the fact that a function without `return` yields `None`, the fact that `return` exits the function immediately
EXAMPLES: `def add_print(a, b): print(a + b)` → `result` is `None`, vs `def add_return(a, b): return a + b` → 8, `def square(n): return n * n` (`square(5)` → 25, `square(4)` → 16), `def is_even(n):` returning True/False, `def get_grade(score):` with 80/70/60 → A/B/C/F and `print(f"Grade: {grade}")`
NOTES: **Returning multiple values (`return a, b`) is NEVER taught.** Multiple `return` STATEMENTS in different branches are taught here (that is the "multiple returns" this course covers). `None` is named but never used as a literal.

### 040-function-practice
NEW: (no new function syntax) — passing a list into a function, passing a dict into a function, composing two functions, calling `int(input("prompt"))` and feeding the result to a function
EXAMPLES: skill recap table, `def get_total(scores):` accumulating with `+=` over a list then `return total` (with `my_scores = [80, 75, 90, 65, 88]`), `def show_student(student):` looping `.items()` with `alice = {"name": "Alice", "score": 92}`, `def get_average(scores): return sum(scores) / len(scores)` + `def get_grade(average):` (80/70 → A/B/C) composed over `[85, 90, 78]`, `score = int(input("Enter score: "))` → `get_grade(score)`, good-function guidelines
NOTES: **Used but not explained: the builtin `sum()`** (`sum(scores) / len(scores)`) — it appears here for the first time with no explanation and is never formally taught. `min()`, `max()`, `sorted()`, `round()`, `abs()` never appear at all. `int(input("..."))` with a prompt appears here for the second time (after 035).

### 041-scope
NEW: local variables (created inside a function, invisible outside → `NameError`), global variables (readable inside a function), shadowing (same name local vs global), variable lifetime, the `global` keyword
EXAMPLES: `def my_func(): x = 10` then `print(x)` outside → NameError, `name = "Alice"` global read inside `def show()`, shadowing demo (`x = 100` global, `x = 50` local → "Inside: 50" / "Outside: 100"), `def calc(): result = 42; return result` then `value = calc()`, `count = 0` with `def add_one(): global count; count += 1` called twice → 2
NOTES: `global` is explicitly labelled "advanced" (ขั้นสูง) but IS shown in runnable code. `nonlocal` never appears. The `global count` example is the only mutation of a global in the course.

### 042-debugging
NEW: (concept only, no new constructs) — the three error categories: Syntax / Runtime / Logic; named exceptions `SyntaxError`, `ZeroDivisionError`, `IndexError`, `TypeError`; debugging by inserting `print` calls inside a function
EXAMPLES: missing colon (`if x > 5` without `:`), `10 / 0` → ZeroDivisionError, `nums = [1, 2, 3]` / `nums[5]` → IndexError, `"5" + 3` → TypeError, logic error (`total = i` overwriting vs `total += i` over `range(1, 5)` → 4 vs 10), `def calc(x, y):` with two debug prints around `result = x * y`, summary table
NOTES: **`try` / `except` is NOT taught** — error handling is explicitly deferred to Phase 2 (mentioned only in 047/048 as future content). Errors are diagnosed and prevented, never caught.

### 043-code-readability
NEW: (concept only, no new syntax) — meaningful names, correct indentation, comment only where needed, prefer f-string over `+` concatenation, split long code into functions; ALL_CAPS constant naming convention
EXAMPLES: `x = 75` / `y = x >= 50` vs `score = 75` / `is_passed = score >= 50`, bad vs good `def greet()` indentation, over-commented `x`/`y`/`z` vs `DISCOUNT_RATE = 0.1` + `final_price = price * (1 - DISCOUNT_RATE)`, `print("Name: " + name + ", Age: " + str(age))` vs `print(f"Name: {name}, Age: {age}")`, inline `n`/`t` loop vs `def get_sum(n):` + `return total`, 5-point clean-code list
NOTES: Storing a comparison result in a variable (`is_passed = score >= 50`) is shown here for the first time as a named technique. `DISCOUNT_RATE` introduces the UPPERCASE-constant convention (006 had said uppercase is "for constants only" but showed none).

### 044-practice-review
NEW: (no new syntax) — integration of lessons 025–043; nesting a list inside a dict value (dict of lists)
EXAMPLES: topic recap table (Lists / Tuples / Sets / Dicts / Functions / Scope / Debugging / Readability), one combined program: `def get_average(scores):` with a `len(scores) == 0` guard returning 0 and `sum(scores) / len(scores)`, `def get_grade(average):` (80/70/60 → A/B/C/F), `student_scores = {"Alice": [85, 90, 78], "Bob": [72, 68, 75]}` looped with `.items()` printing `f"{name}: {avg:.1f} → {grade}"`, 4 review tips
NOTES: **Used but not explained: triple-quoted docstrings (`"""คำนวณค่าเฉลี่ย..."""`) inside both functions — first and only appearance, never taught.** Also reuses `sum()` (still unexplained, from 040). A dict whose values are lists is a new structure shape, shown but not discussed.

### 045-logic-integration
NEW: (no new core syntax) — the algorithmic-thinking checklist (identify input → output → steps → tools) and a tool-selection table; building a list from a loop of `input()` calls with a prompt built by an f-string
EXAMPLES: 4-question thinking checklist, tool-selection table (list / dict / tuple / set / for / while / function), worked problem "read 5 names, print those starting with A": `names = []`, `for i in range(5): name = input(f"Enter name {i+1}: ")`, `names.append(name)`, then `for name in names: if name.startswith("A"): print(name)`
NOTES: **Used but not explained: the string method `.startswith()`** — this is the only string method used anywhere in the course and it is never taught. (`.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`, `.replace()` never appear at all.) Also the first use of an f-string as an `input()` prompt.

### 046-read-code
NEW: (concept only, no new syntax) — a 7-step method for reading unfamiliar code and hand-tracing variable values
EXAMPLES: 7-step reading procedure, max-finding trace (`numbers = [3, 7, 2, 9, 4]`, `result = 0`, `if num > result: result = num`, round-by-round trace → 9), two-function program (`def double(x): return x * 2` and `def apply_all(lst):` building a `result` list with `.append(double(item))` and returning it, `nums = [1, 2, 3]` → `[2, 4, 6]`), tracing tips
NOTES: A function that returns a list, and calling one function from inside another, are both shown here for the first time (as reading exercises, not as new constructs). `print()` of a whole list appears again.

### 047-final-review
NEW: (concept only, no new syntax) — final Phase-1 checklist and a preview of Phase 2
EXAMPLES: topic recap lists (basics / collections / functions / quality), three-part readiness checklist (Collections / Functions / Problem Solving), Phase-2 preview list
NOTES: Names OOP, File I/O, Modules & Libraries and Error Handling as FUTURE topics — none are taught. Explicitly lists the in-scope list methods as "append, remove, sort" only, confirming the narrow list-method scope from 026.

### 048-transition-prep
NEW: (concept only, no new syntax for Phase 1) — how Phase 1 topics map onto Phase 2 topics
EXAMPLES: Phase 1 → Phase 2 flow diagram, mapping table (Functions→Methods/OOP, Dictionaries→JSON/API, Lists→file lines, Loops→large datasets, Debugging→try/except), preview snippets: `class Student:` with `def __init__(self, name, score)` and `self.`, `with open("data.txt", "r") as f: content = f.read()`, `import math` / `import random`, final self-check list
NOTES: **`class`, `__init__`, `self`, `with open(...)`, `.read()`, `import math`, `import random` and `try/except` appear ONLY as a Phase-2 teaser — they are explicitly out of scope and must never be used in Phase-1 practice problems.**

---

## FIRST-APPEARANCE INDEX (quick lookup)

| Construct | First taught | Note |
|---|---|---|
| `print("literal")` | 001 | only string literals |
| `#` comment | 004 | |
| variable assignment `=` | 005 | (silently used in 004) |
| `print` with comma separators | 005 | the only output style until 010 |
| snake_case / naming rules | 006 | |
| `int` `float` `str` `bool`, `True`/`False`, `type()` | 007 | |
| string concat with `+` | 007 (as a gotcha) / 008 (as a technique) | needs `str()` |
| `int()` `float()` `str()` | 008 | |
| `input()` | 008 (used) / 009 (taught) | bare, no prompt |
| `int(input())` / `float(input())` | 008 | |
| f-string, `:.2f`, `sep=`, `end=` | 010 | |
| `+ - * / // % **` | 011 | (`*`,`-` used earlier in 004/006/008) |
| `== != > < >= <=` | 011 (table) / 013–014 (in `if`) | |
| operator precedence | 011 | |
| `if` / `else` | 013 | |
| `%` even/odd idiom | 014 | |
| `elif` | 015 | |
| `and` / `or` / `not` | 016 | |
| `for i in range(n)` | 017/01 | |
| `range(a,b)` / `range(a,b,c)` | 017/02 | no negative step, ever |
| list literal, `for x in list`, `len()`, accumulator | 018 | |
| `:.1f` | 018 | used, only `:.2f` was taught |
| `while` | 019 | |
| `break`, `continue`, `while True:` | 020 | |
| nested loops, `end=""`, bare `print()`, `\t` | 021 | |
| `+=` | 022 | **used, never explained** |
| `pass` | 023 | **used, never explained** |
| `scores = []` + `.append()` | 024 | **used before being taught (026)** |
| list indexing `[0]`, negative indexing `[-1]` | 025 | |
| index assignment, `.append()`, `.remove()`, `.sort()`, `.sort(reverse=True)` | 026 | **the only list methods in the course** |
| `for i in range(len(x))` + `x[i]` | 027 | |
| tuple `()`, tuple indexing, immutability | 029 | |
| set `{}`, `set(list)`, `.add()`, `.remove()`, `|`, `&` | 030 | |
| `in` membership operator | 030 | (mentioned in a table at 028) |
| dict literal, `d[key]`, add key, `for key in d`, `key in d` | 033 | |
| `d[k] = v` update, `.update()`, `del d[k]`, `.values()`, `.items()` | 034 | |
| `input("prompt")` | 035 | |
| empty dict `{}`, frequency-count idiom | 035 | |
| `def f():` + call | 037 | |
| parameters / arguments | 038 | |
| `return`, returning from branches, `None` | 039 | |
| `sum()` | 040 | **used, never explained** |
| local vs global scope, `global` keyword | 041 | |
| error taxonomy (`ZeroDivisionError`, `IndexError`, `TypeError`) | 042 | no `try`/`except` |
| ALL_CAPS constants, `is_x = <comparison>` | 043 | |
| docstring `"""..."""` | 044 | **used, never explained** |
| dict of lists | 044 | |
| `.startswith()` | 045 | **used, never explained; only string method in the course** |
| function returning a list; function calling a function | 046 | |

## NEVER TAUGHT ANYWHERE IN CHAPTERS 001–048

Slicing (`a[1:3]`), `.insert()`, `.pop()`, `.reverse()`, `.clear()`, `.extend()`, `.index()`, `.count()`,
`sorted()`, `enumerate()`, `zip()`, `min()`, `max()`, `round()`, `abs()`, `dict.keys()`, `dict.get()`,
`list.copy()`, list comprehensions, tuple unpacking (`a, b = t`), default/keyword arguments,
returning multiple values (`return a, b`), `*args` / `**kwargs`, lambda, `try` / `except` / `finally`,
`with open(...)`, `import` anything, `class` / OOP, `nonlocal`, `else` on a loop, `match`,
string methods other than `.startswith()` (no `.upper()`, `.lower()`, `.split()`, `.strip()`, `.join()`,
`.replace()`, `.find()`), `str.format()`, `%`-formatting, f-string specs other than `:.2f` / `:.1f`,
`range()` with a negative step, explicitly-taught nested `if` (an `if` inside an `if` block is never
demonstrated — only `if` inside a loop, from 020, and `if`/`elif`/`else` chains from 015).
