def ispalindrome(s):
    n=len(s)
    for i in range(n//2):
        if(s[i]!=s[n-1-i]):
            return False
    return True

s=input("enter any string:")

print(ispalindrome(s))