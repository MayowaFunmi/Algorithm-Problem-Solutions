N, M = map(int, input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
def topmat():
    for i in range(1,N,2): 
        print (('.|.'*i).center(M,'-'))

def welcome():
    print ("WELCOME".center(M,'-'))

def belowmat():
    for i in range(N-2,-1,-2): 
        print (('.|.'*i).center(M,'-'))

print(topmat())
print(welcome())
print(belowmat())