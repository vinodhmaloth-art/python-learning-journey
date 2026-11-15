# Day 5 - Counting: how many students passed and failed
marks = [65, 30, 88, 45, 22]
passed = 0
failed = 0
for m in marks:
    if m >= 35:
        passed = passed + 1
    else:
        failed = failed + 1
print("Pass:", passed, "Fail:", failed)
