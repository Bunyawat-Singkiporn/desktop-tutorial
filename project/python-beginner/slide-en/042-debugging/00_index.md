# 📋 Exercise index — บท 042 Debugging

**Chapter scope:** แยก Syntax / Runtime / Logic · ป้องกัน error ด้วยเงื่อนไข · ใส่ print ตรวจค่า · ความรู้ถึง 041

> ❌ ห้าม `try` / `except` เด็ดขาด

---

## Recommended order

| # | File | Level | Problem | Core idea |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | เติม colon ที่หาย | SyntaxError |
| 2 | `03_test.md` | 🟢 | กันหารศูนย์ | ป้องกัน Runtime |
| 3 | `04_test.md` | 🟢 | แก้ index เกิน | IndexError |
| 4 | `08_easy.md` | 🟢 | แปลงก่อนบวก | TypeError |
| 5 | `09_easy.md` | 🟢 | แก้ยอดรวมในลูป | LogicError |
| 6 | `06_medium.md` | 🟡 | ใส่ print ดีบัก | debug print |
| 7 | `07_medium.md` | 🟡 | ตรวจความยาว list | กัน IndexError |
| 8 | `10_medium.md` | 🟡 | ตรวจตัวหารก่อน | กัน ZeroDivision |
| 9 | `11_medium.md` | 🟡 | แก้เงื่อนไขกลับด้าน | Logic |
| 10 | `12_medium.md` | 🟡 | แก้ชื่อตัวแปรผิด | NameError แนวคิด |
| 11 | `13_medium.md` | 🟡 | หาผลรวมช่วงถูก | Logic สะสม |
| 12 | `05_challenge.md` | 🔴 | รายงานบั๊กสามชนิด | แยกประเภท |
| 13 | `14_challenge.md` | 🔴 | ซ่อมฟังก์ชันคูณ | ใส่ขั้นตอน |
| 14 | `15_challenge.md` | 🔴 | กัน list ว่าง | ป้องกันก่อนใช้ |
| 15 | `16_challenge.md` | 🔴 | ดีบักreceiptผิดยอด | หาจุดผิด |

**Summary:** 🟢 Easy 5 problems · 🟡 Medium 6 problems · 🔴 Challenge 4 problems = **15 ข้อ**

---

## Notesสำหรับครู

Problemคือแก้หรือป้องกันบั๊ก ไม่ใช่จับ error