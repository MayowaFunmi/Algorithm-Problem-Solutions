if __name__ == '__main__':
    result_list = [] # nested list, each list contains names and score
    score_list = []
    for x in range(int(input("Enter number: "))):
        name = input("Enter name: ")
        score = float(input("Enter score: "))
        
        result_list.append([name, score])
        score_list.append(score)
        score_list.sort()
    print("Number of students registered: ", x+1)
    print("List of students and their scores: ", result_list)
    print()

    names = []
    for name, mark in result_list:
        print("Names of student: ", name)
        print("Scores of student: ", mark)
        if mark == score_list[1]:
            names.append(name)
            names.sort()
    print()
    for i in names:
        print(i)