# Day 7 - Counting (Friday practice)
# Given a list of marks in 5 subjects, count how many are Pass
# (40 or more) and how many are Fail (below 40), then print both counts.

marks = [65, 30, 88, 45, 22]

pass_count = 0
fail_count = 0

for m in marks:
    if m >= 40:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

print("Pass:", pass_count, "Fail:", fail_count)
