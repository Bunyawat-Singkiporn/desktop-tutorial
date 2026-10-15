# ↩️ Return Values — Q14: สถานะกระเป๋าเงิน

**Difficulty:** 🔴 Challenge

---

## Task

สถานะเงินในกระเป๋า

**Requirements:**

- สร้าง `wallet_status(money)` คืน `Broke` ถ้า money < 50, `OK` ถ้า < 200, ไม่งั้น `Rich`
- พิมพ์ผลของ `30` `120` `500`

---

## Input

None (values are set in the program / call functions in code)

## Output

3 บรรทัด

---

## Example

**Output:**

```text
Broke
OK
Rich
```


---

## 💡 Hint

ใช้ elif หลายขั้น คืนสตริง

---

## Starter Code

```python
def wallet_status(money):
    # return
    # Write your code here

print(wallet_status(30))
print(wallet_status(120))
print(wallet_status(500))
```
