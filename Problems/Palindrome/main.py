'''
def palindrome(word):

    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")


palindrome(input())
'''

t = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


ch = ''.join([''.join(x) for x in t])
print(ch)
for pl in (ch[::4], ch[2:8:2], ch[::3], ch[1::3], ch[2::3], ch[:3], ch[3:6], ch[6:]):
    print(pl, end=' ')


print()
ch = [c for c in ch]
print(ch)
for pl in (ch[::4], ch[2:8:2], ch[::3], ch[1::3], ch[2::3], ch[:3], ch[3:6], ch[6:]):
    print(pl, end=' ')
