list = [["yes", 5.87], ["me", 2.29], ["them", 4.55], ["him", 0.34], ["she", 2.29], ["our", 4.55]]

score = []
for i in list:
    score.append(i[1])
    score.sort()
print(score)

names = []
for name, mark in list:
    if mark == score[-2]:
        names.append(name)
        names.sort()

for i in names:
    print(i)