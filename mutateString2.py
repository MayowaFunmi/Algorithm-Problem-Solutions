'''
string = input("Enter a string: ")
position, character = input().split()

def mutate_string(string, position, character):
    l = list(string)
    l[int(position)] = character
    li = ''.join(l)
    print(li)

mutate_string(string, position, character)

'''

def mutate_string(string, position, character):
    l = list(s) # or use string
    l[int(i)] = c #or use character
    li = "".join(l)
    return li
    
if __name__ == '__main__':
    s = input("word: ")
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)