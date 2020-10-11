x = list(map(int, input('Enter numbers separated by whitespace : ').split()))
x.sort()
# To reverse the sord order use sort(reverse = True)
print("The list of numbers you entered: ", x)

a = []
for i in x:
    if i not in a:
        a.append(i)
print("List without duplicate: ", a)
runner_up = a[-2]
print("Runner up is ", runner_up)