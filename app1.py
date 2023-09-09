def reverse(a):
    res=""
    for i in range(1,len(a)+1):
        res = res+a[-i]
    return res
s = input()
print(reverse(s))