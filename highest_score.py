student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

highest = student_scores[0]

for i in student_scores[1:]:
    if i > highest:
        highest = i

print(highest)
