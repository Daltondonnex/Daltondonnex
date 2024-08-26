subjects = ['Math', 'Science', 'History', 'English']
scores = [85, 90, 75, 88]

grades = []

for score in scores:
    if score >= 90:
        grades.append('A')
    elif score >= 80:
        grades.append('B')
    elif score >= 70:
        grades.append('C')
    elif score >= 60:
        grades.append('D')
    else:
        grades.append('F')

for i in range(len(subjects)):
    print(f"Subject: {subjects[i]}\t Score: {scores[i]}\t Grade: {grades[i]}")
