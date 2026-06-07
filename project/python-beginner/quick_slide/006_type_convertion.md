Type Conversion

## ปัญหาของ input()

input() จะได้ข้อมูลเป็นข้อความเสมอ

เช่น

```python
age = input()
```

ถ้าพิมพ์

```text
10
```

Python จะมองเป็น

```python
"10"
```

ไม่ใช่

```python
10
```

ดังนั้นต้องแปลงก่อน

```python
age = int(input())
```


---


## ลองทำเอง

รับอายุ

แล้วแสดงอายุในอีก 5 ปี

### Input

```text
11
```

### Output

```text
16
```