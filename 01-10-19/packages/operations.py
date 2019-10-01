def addition(a,b):
    c=a+b
    print(c)
def isprime(n):
    factors=0
    for i in range(1,n+1):
         if n%i==0:
            factors+=1
    if factors==2:
        return True
    else:
        return False
        