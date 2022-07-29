def Palindrome(c):
    if len(str(c))<=3:
        if c[0]==c[-1]:
            return True
        else:
            return False
    else:
        return Palindrome(c[1:len(c)-1])

print(Palindrome('123221'))