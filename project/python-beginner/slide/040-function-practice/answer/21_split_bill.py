def calc_tip(bill):
    return bill * 10 // 100

def per_person(bill, tip, people):
    return (bill + tip) // people

bill = int(input())
people = int(input())
tip = calc_tip(bill)
print(tip)
print(per_person(bill, tip, people))
