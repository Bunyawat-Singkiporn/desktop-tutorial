# บัค 1: return total / 10 → ควรหารด้วย len(scores) ไม่ใช่ 10 (Logic Error)
# บัค 2: if avg > 80 → ควรเป็น >= 80 เพื่อให้ 80.0 เป็น Excellent (Logic Error)

def find_average(scores):
    total = 0
    for score in scores:
        total = total + score
    return total / len(scores)  # แก้: หารด้วย len(scores)

def classify(avg):
    if avg >= 80:               # แก้: >= แทน >
        return "Excellent"
    if avg > 60:
        return "Good"
    else:
        return "Needs Work"

data = [70, 80, 90, 85, 75]
avg = find_average(data)
print(f"Average: {avg}")
print(f"Level: {classify(avg)}")
