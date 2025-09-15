import sys
sys.stdin = open("input.txt", 'r')

score_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}


li = list()
for i in range(20):
    temp = list(input().split())
    li.append(temp)
score = 0
grade = 0
for sub in li:
    if sub[2] != 'P':
        score += score_dict.get(sub[2]) * float(sub[1])
        grade += float(sub[1])
print(round(score/grade, 6))


