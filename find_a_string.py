'''
def count_substring(string, sub_string):
    c=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            c +=1
    return c

if __name__=='__main__':
    string = input("Enter string: ").strip()
    sub_string = input("Enter substring: ").strip()
    count = count_substring(string, sub_string)
    print(count)
'''
string = input("Enter a word: ")
sub_string = input("Enter substring: ")
    
def count_substring(string, sub_string):
    count = 0
    
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    print(count)
        
count_substring(string, sub_string)