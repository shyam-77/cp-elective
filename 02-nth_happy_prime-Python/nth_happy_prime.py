# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def isprime(x):
    count=0
    if x>1:
        for i in range(1,x+1):
            if(x%i)==0:
                count = count+1
        if count == 2:
            return True
        else:
            return False
  
def numSquareSum(n):
    squareSum = 0;
    while(n>0):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum
def ishappynumber(n):
    slow = n;
    fast = n;
    while(True):
        slow = numSquareSum(slow);
        fast = numSquareSum(numSquareSum(fast));
        if(slow != fast):
            continue;
        else:
            break;
    if (slow == 1):
        return True
    else:
        return False
def fun_nth_happy_prime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if ((ishappynumber(guess)) and (isprime(guess))):
            found += 1
    return guess