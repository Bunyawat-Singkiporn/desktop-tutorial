# 🔥 Practice Dictionaries — Question 4: Phonebook Lookup

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างสมุดโทรศัพท์ 3 คน และรับชื่อจากผู้ใช้เพื่อค้นหาเบอร์ (ทำ 3 ครั้ง)

```python
phonebook = {
    "Alice": "081-111-1111",
    "Bob": "082-222-2222",
    "Charlie": "083-333-3333"
}
```

**ตัวอย่าง Session:**
```
Search: Alice
Phone: 081-111-1111
Search: David
Not found: David
Search: Bob
Phone: 082-222-2222
```

---

## 💡 Hint

ใช้ `if name in phonebook:` ก่อนเข้าถึงค่า

---

## Starter Code

```python
phonebook = {
    "Alice": "081-111-1111",
    "Bob": "082-222-2222",
    "Charlie": "083-333-3333"
}

for i in range(3):
    name = input("Search: ")
    # Write your code here
```
