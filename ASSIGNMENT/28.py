def isPerfect( n ):
   
    sum = 1
   
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1
    
     
    return (True if sum == n and n!=1 else False)
 


n = int(input())

if isPerfect (n):
        print(n , " is a perfect number")
else:
    print(n , " is not a perfect number")