import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
'''
string = "This very very very very long string"
print(textwrap.wrap(string, 4))
print()
print(textwrap.fill(string, 8))
'''