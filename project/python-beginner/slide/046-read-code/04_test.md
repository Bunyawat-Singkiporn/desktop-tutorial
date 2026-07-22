# 💬 Read Code — Question 3: Explain in Thai

**Difficulty:** 🟡 Medium

---

## โจทย์

อ่านโค้ดด้านล่างแล้วอธิบายเป็นภาษาไทยในกล่อง comment ว่า:
1. โปรแกรมรับข้อมูลอะไร
2. ประมวลผลอย่างไร
3. แสดงผลอะไร

```python
def process(data):
    result = {}
    for item in data:
        first_letter = item[0].upper()
        if first_letter in result:
            result[first_letter].append(item)
        else:
            result[first_letter] = [item]
    return result

words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
grouped = process(words)
for letter, group in grouped.items():
    print(f"{letter}: {group}")
```

---

## Starter Code

```python
# อธิบายโปรแกรมด้านล่างเป็นภาษาไทย:
# รับ: 
# ประมวลผล: 
# แสดงผล: 

def process(data):
    result = {}
    for item in data:
        first_letter = item[0].upper()
        if first_letter in result:
            result[first_letter].append(item)
        else:
            result[first_letter] = [item]
    return result

words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
grouped = process(words)
for letter, group in grouped.items():
    print(f"{letter}: {group}")
```
