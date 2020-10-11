list = [["yes", 5.87], ["me", 2.29], ["them", 4.55], ["him", 0.34], ["she", 2.29], ["our", 4.55]]
names = []
scores = []
arranged = []
unique = []
my_dict = {}

for i in list:
    names.append(i[0])
    scores.append(i[1])
    arranged.append(i[1])
    arranged.sort()
    my_dict[i[0]] = i[1]    # names as keys and scores as values
print(list) 
print(names)
print(scores)
print(arranged)
print(my_dict)
print()

for x in list:
    if x not in unique:
        unique.append(x)
    if x[1] in unique:
        print(x[0])
        print(x[1])
        #print(y[0])
#print(unique)