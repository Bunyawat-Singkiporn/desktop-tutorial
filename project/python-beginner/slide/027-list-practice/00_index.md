# 📋 สารบัญโจทย์ — บท 027 List Practice

**ขอบเขตของบทนี้:** ความรู้ list ทั้งหมด + filter เข้า list ใหม่ + นับด้วย counter + `for i in range(len(...))`

> ❌ ไม่มี `in` (บท 030) · ไม่มี `enumerate` · ไม่มี `min()`/`max()`/`sorted()`

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | พิมพ์งานบ้านพร้อมเลข | range(len) พื้นฐาน |
| 2 | `03_test.md` | 🟢 | นับคะแนนผ่านเกณฑ์ | counter ใน loop |
| 3 | `04_test.md` | 🟢 | กรองสินค้าราคาถูก | filter เข้า list ใหม่ |
| 4 | `08_easy.md` | 🟢 | ป้ายชั้นเรียนแบบ index | range(len) + ชื่อ |
| 5 | `09_easy.md` | 🟢 | นับอุณหภูมิร้อน | counter + เงื่อนไข |
| 6 | `06_medium.md` | 🟡 | กรองชื่อสั้น | filter ด้วย len(ชื่อ) |
| 7 | `07_medium.md` | 🟡 | รวมเฉพาะคะแนนผ่าน | accumulator มีเงื่อนไข |
| 8 | `10_medium.md` | 🟡 | รายการงานพร้อมสถานะ | range(len) + if |
| 9 | `11_medium.md` | 🟡 | กรองแล้วเรียงราคา | filter + sort |
| 10 | `12_medium.md` | 🟡 | ค่าเฉลี่ยเฉพาะที่ผ่าน | filter แล้วเฉลี่ย |
| 11 | `13_medium.md` | 🟡 | นับและรวมราคาแพง | counter + total คู่กัน |
| 12 | `05_challenge.md` | 🔴 | รายงานงานบ้าน | range(len) + สรุป |
| 13 | `14_challenge.md` | 🔴 | ตะกร้าหลังกรอง | filter+append+sort+สรุป |
| 14 | `15_challenge.md` | 🔴 | ผลสอบแบบมีเลขที่ | range(len)+Pass/Fail |
| 15 | `16_challenge.md` | 🔴 | สรุปอุณหภูมิรายสัปดาห์ | หลายสถิติจาก list เดียว |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

- ข้อ 02 ไม่ซ้ำตัวอย่าง todos ในบทเรียนทุกตัวอักษร — เปลี่ยนสถานการณ์
- เน้น range(len) / filter / count
- ห้ามใช้ in / enumerate / max
