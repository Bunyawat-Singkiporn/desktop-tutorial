# โจทย์: รับคะแนน 3 วิชา คำนวณผลรวม เฉลี่ย สูงสุด ต่ำสุด

# รับคะแนน 3 วิชา แปลงเป็น int ทันที
score1 = int(input())
score2 = int(input())
score3 = int(input())

# คำนวณ
total = score1 + score2 + score3
average = total / 3
highest = max(score1, score2, score3)   # หาค่าสูงสุด
lowest = min(score1, score2, score3)    # หาค่าต่ำสุด

# แสดงผล
print(f"Scores: {score1}, {score2}, {score3}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
