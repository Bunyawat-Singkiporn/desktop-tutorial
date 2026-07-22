def check_pass(scores):
    for score in scores:
        if score >= 50:
            print(f"{score} → Pass")
        else:
            print(f"{score} → Fail")

check_pass([85, 45, 92, 38, 77])
