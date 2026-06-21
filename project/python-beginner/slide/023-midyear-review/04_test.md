# 🏆 Practice: Mid-Year Review — Question 3: Shopping Cart

**Difficulty:** 🟡 Medium

---

## โจทย์

รับชื่อสินค้าและราคาซ้ำๆ จนพิมพ์ `"done"` แล้วแสดงใบเสร็จ

**Input:**
```
Apple
15
Bread
40
Milk
35
done
```

**Output:**
```
=== Receipt ===
Apple: 15 baht
Bread: 40 baht
Milk: 35 baht
---
Total: 90 baht
```

---

## 💡 Hint

- รับชื่อสินค้าก่อน ถ้า `== "done"` → `break`
- ถ้าไม่ใช่ → รับราคา → เก็บทั้งสองใน list

---

## Starter Code

```python
items = []
prices = []

while True:
    name = input()
    if name == "done":
        break
    price = int(input())
    items.append(name)
    prices.append(price)

print("=== Receipt ===")
for i in range(len(items)):
    print(f"{items[i]}: {prices[i]} baht")
print("---")
print(f"Total: {sum(prices)} baht")
```
