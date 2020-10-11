#String Formatting in Python - Hacker Rank Solution
def print_formatted(number):
    # your code goes here
    # String Formatting in Python - Hacker Rank Solution START
    l1 = len(bin(number)[2:])
    print(l1)
    for i in range(1,number+1):
        print(str(i).rjust(l1,' '),end=" ")
        print(oct(i)[2:].rjust(l1,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1,' '),end=" ")
        print(bin(i)[2:].rjust(l1,' '),end=" ")
        print("")
    # String Formatting in Python - Hacker Rank Solution END

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
