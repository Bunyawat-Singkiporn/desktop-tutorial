# What is a Flowchart?

Plan before you code — **like a map before a trip.**

---

## Symbols

| Shape | Meaning | Example |
|-------|---------|---------|
| ⬭ Oval | Start / End | Start, End |
| ▭ Rectangle | Do something | `score = 0` |
| ◇ Diamond | Ask a question → Yes / No | `guess == secret?` |

---

## Step 1 — Game Overview

Every game has 3 main parts:

```mermaid
flowchart TD
    A([Start]) --> B["Set variables\nsecret_number = 3\nscore = 0"]
    B --> C["🔄 Game Loop\nRuns until the game closes"]
    C --> D([End])
```

---

## Step 2 — Inside the Game Loop

Every time the player presses a key, the game decides:

```mermaid
flowchart TD
    A["Player presses 1-5"] --> B{"guess == secret_number?"}
    B -- Yes --> C["'Correct!'\nscore += 1"]
    B -- No --> D{"guess < secret_number?"}
    D -- Yes --> E["'Too Low!'"]
    D -- No --> F["'Too High!'"]
```

---

## Flowchart → Code

| Flowchart | Python |
|-----------|--------|
| ▭ `secret_number = 3` | `secret_number = 3` |
| ▭ Player presses a key | `if event.type == pygame.KEYDOWN` |
| ◇ `guess == secret?` | `if guess == secret_number:` |
| ◇ `guess < secret?` | `elif guess < secret_number:` |
| ▭ `"Too High!"` | `else:` |

---

## ✏️ Activity — Draw Your Own Flowchart

Draw on paper. Take 5 minutes.

**Check that you have:**
- [ ] Start / End
- [ ] ▭ Set secret_number and score
- [ ] ▭ Player presses a key
- [ ] ◇ guess == secret? → Yes / No
- [ ] ◇ guess < secret? → Yes / No
- [ ] ▭ Output for all 3 cases: Correct / Too Low / Too High

---

> **Rule**: Every new game → draw a Flowchart first.
