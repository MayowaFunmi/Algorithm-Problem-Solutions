def print_formatted(number): # n
    dist = len(bin(n)[2:])
    for i in range(1, number+1):
        #dist = len(bin(n))
        print(str(i).rjust(dist), end=" ")
        print(oct(i).rjust(dist).replace("0o", " "),end=" ")
        print(hex(i).rjust(dist).replace("0x", " ").upper(), end=" ")
        print(bin(i).rjust(dist).replace("0b", " "), sep=" ")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)