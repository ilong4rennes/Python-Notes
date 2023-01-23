# 2: Loops and Strings

## 2.2 Loops

### isPrime

Write the function `isPrime(n)` which takes a possibly-negative integer `n`, and returns True if `n` is prime, and False otherwise.


```python
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    max_factor = rounded(n**0.5) 
    for factor in range(3,max_factor+1,2):
        if n % factor == 0:
            return False
    return True

# @testFunction
# def testIsPrime():
#     assert(isPrime(1) == False)
#     assert(isPrime(2) == True)
#     assert(isPrime(7) == True)
#     assert(isPrime(8) == False)
#     assert(isPrime(9) == False)
#     assert(isPrime(0) == False)
#     assert(isPrime(-1) == False)
#     assert(isPrime(-7) == False)

# def main():
#     testIsPrime()

# main()

```

### nthPrime

Write the function `nthPrime(n)` which takes a non-negative integer `n`, and returns the nth prime number. 2 is the 0th prime number, 3 is the 1st prime number, etc.


```python
# from cmu_cs3_utils import testFunction, rounded

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    max_factor = rounded(n**0.5) 
    for factor in range(3,max_factor+1,2):
        if n % factor == 0:
            return False
    return True

def nthPrime(n):
    number = 0
    guess = 0
    while number <= n:
        guess += 1
        if isPrime(guess):
            number += 1
    return guess

# @testFunction
# def testNthPrime():
#     assert(nthPrime(0) == 2)
#     assert(nthPrime(1) == 3)
#     assert(nthPrime(2) == 5)
#     assert(nthPrime(3) == 7)
#     assert(nthPrime(4) == 11)
#     assert(nthPrime(5) == 13)

# def main():
#     testNthPrime()

# main()

```

### reverseNumber

Write the function reverseNumber(n) which takes an integer n, and returns an integer with its digits in the reverse order of the digits in n.


```python
# from cmu_cs3_utils import testFunction

def reverseNumber(n):
    result = 0
    sign = 1 if n > 0 else -1
    n = abs(n)
    while n>0:
        last_digit = n % 10
        n = n//10
        result = result * 10 + last_digit
    return sign * result

# @testFunction
# def testReverseNumber():
#     assert(reverseNumber(12345) == 54321)
#     assert(reverseNumber(34) == 43)
#     assert(reverseNumber(0) == 0)
#     assert(reverseNumber(1) == 1)
#     assert(reverseNumber(10) == 1)
#     assert(reverseNumber(2500) == 52)
#     assert(reverseNumber(-12345) == -54321)
#     assert(reverseNumber(-1) == -1)

# def main():
#     testReverseNumber()

# main()

```

### mostFrequentDigit

Write the function mostFrequentDigit(n) which takes a possibly-negative integer n, and returns the digit from 0 to 9 that occurs most frequently in n. Ties go to the larger digit.


```python
# from cmu_cs3_utils import testFunction

def countOccurences(digit, n):
    if (digit == 0 and n == 0):
        return 1
    count = 0 
    while n > 0:
        currDigit = n % 10
        if currDigit == digit:
            count += 1
        n //= 10
    return count

def mostFrequentDigit(n):
    n = abs(n)
    bestDigit = -1
    bestCount = -1
    for digit in range(10):
        occurrences = countOccurences(digit, n)
        if occurrences >= bestCount:
            bestCount = occurrences
            bestDigit = digit
    return bestDigit

# @testFunction
# def testMostFrequentDigit():
#     assert(mostFrequentDigit(55) == 5)
#     assert(mostFrequentDigit(1223) == 2)
#     assert(mostFrequentDigit(33221) == 3)
#     assert(mostFrequentDigit(23232) == 2)
#     assert(mostFrequentDigit(12345) == 5)
#     assert(mostFrequentDigit(0) == 0)
#     assert(mostFrequentDigit(-12233) == 3)
#     assert(mostFrequentDigit(-12345) == 5)

# def main():
#     testMostFrequentDigit()

# main()

```

### hasConsecutiveDigits

Write the function `hasConsecutiveDigits(n)` which takes a possibly-negative integer `n`, and returns `True` if that number contains two consecutive digits that are the same, and `False` otherwise.

For example, `1223` has two consecutive 2's, but `1232` does not.


```python
# from cmu_cs3_utils import testFunction

def hasConsecutiveDigits(n):
    n = abs(n)
    prevDigit = None
    while n > 0:
        currDigit = n % 10
        if currDigit == prevDigit:
            return True
        prevDigit = currDigit
        n //= 10
    return False

# @testFunction
# def testHasConsecutiveDigits():
#     assert(hasConsecutiveDigits(55) == True)
#     assert(hasConsecutiveDigits(1223) == True)
#     assert(hasConsecutiveDigits(1232) == False)
#     assert(hasConsecutiveDigits(12225) == True)
#     assert(hasConsecutiveDigits(1223344) == True)
#     assert(hasConsecutiveDigits(0) == False)
#     assert(hasConsecutiveDigits(-1223) == True)
#     assert(hasConsecutiveDigits(-1232) == False)

# def main():
#     testHasConsecutiveDigits()

# main()

```

### nthEmirpPrime

Background: An Emirp prime is a prime number which becomes a different prime number when its digits are reversed. For example, 13 is an Emirp prime because when we reverse the digits, we get 31, which is also prime. 2, 3, 5, 7, and 11 are not Emirp primes because they are the same prime when the digits are reversed. The 0th Emirp prime is 13.

With this in mind, write the function nthEmirpPrime(n) which takes a non-negative int n, and returns the nth Emirp prime as described above.


```python
# from cmu_cs3_utils import testFunction, rounded

def isPrime(n):
    if n < 2: 
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, rounded(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
    
def reverseNumber(n):
    result = 0
    while n > 0:
        lastDigit = n % 10
        result = result * 10 + lastDigit
        n //= 10
    return result

def isEmirpPrime(n):
    if isPrime(n) and isPrime(reverseNumber(n)) and n != reverseNumber(n): 
        return True
    else: return False

def nthEmirpPrime(n):
    guess = 0
    count = 0
    while count <= n:
        guess += 1
        if isEmirpPrime(guess):
            count += 1
    return guess

# @testFunction
# def testIsEmirpPrime():
#     assert(isEmirpPrime(13) == True)
#     assert(isEmirpPrime(17) == True)
#     assert(isEmirpPrime(31) == True)
#     assert(isEmirpPrime(37) == True)
#     assert(isEmirpPrime(71) == True)
#     assert(isEmirpPrime(73) == True)
#     assert(isEmirpPrime(0) == False)
#     assert(isEmirpPrime(1) == False)
#     assert(isEmirpPrime(7) == False)
#     assert(isEmirpPrime(11) == False)
#     assert(isEmirpPrime(23) == False)
#     assert(isEmirpPrime(14) == False)
    
# @testFunction
# def testNthEmirpPrime():
#     assert(nthEmirpPrime(0) == 13)
#     assert(nthEmirpPrime(1) == 17)
#     assert(nthEmirpPrime(2) == 31)
#     assert(nthEmirpPrime(3) == 37)
#     assert(nthEmirpPrime(4) == 71)
#     assert(nthEmirpPrime(5) == 73)
#     assert(nthEmirpPrime(53) == 1223)

# def main():
#     testIsEmirpPrime()
#     testNthEmirpPrime()

# main()

```

### nthEinNumber

Background: A number is an ein number (short for even increasing number) if the even digits in the number are strictly increasing from left to right. The odd digits in the number can be in any order.

For example, 2478 is an ein number because the even digits 248 are in increasing order. However, 14236 is not an ein number, since the even digits 426 are not in increasing order. Note that 137 is also an ein number because there are no even digits, so we will say that the even digits are implicitly in order. Also note that 22 is not an ein number because repeating even digits are not increasing.

With this in mind, write the function nthEinNumber(n) which takes a non-negative int n and returns the nth ein number.


```python
# from cmu_cs3_utils import testFunction

def isEinNumber(n):
    if n < 0:
        return False
    result = True
    lastDigit = 10 ** 7
    while n > 0:
        currDigit = n % 10
        if currDigit % 2 == 0:
            if currDigit >= lastDigit: 
                result = False
            else: 
                lastDigit = currDigit
        n //= 10
    return result

def nthEinNumber(n):
    guess = 0
    count = 0
    while count < n:
        guess += 1
        if isEinNumber(guess):
            count += 1
    return guess

# @testFunction

# def testisEven():
#     assert(isEven(0) == True)
#     assert(isEven(1) == False)
#     assert(isEven(2) == True)
#     assert(isEven(-3) == False)

# @testFunction
# def testIsEinNumber():
#     assert(isEinNumber(0) == True)
#     assert(isEinNumber(1) == True)
#     assert(isEinNumber(2) == True)
#     assert(isEinNumber(10) == True)
#     assert(isEinNumber(114) == True)
#     assert(isEinNumber(238) == True)
#     assert(isEinNumber(317) == True)
#     assert(isEinNumber(1469) == True)
#     assert(isEinNumber(60) == False)
#     assert(isEinNumber(22) == False)

# @testFunction
# def testNthEinNumber():
#     assert(nthEinNumber(0) == 0)
#     assert(nthEinNumber(2) == 2)
#     assert(nthEinNumber(10) == 10)
#     assert(nthEinNumber(99) == 114)
#     assert(nthEinNumber(185) == 238)
#     assert(nthEinNumber(245) == 317)
#     assert(nthEinNumber(1000) == 1469)

# def main():
#     testisEven()
#     testIsEinNumber()
#     testNthEinNumber()

# main()

```

### babylonianSquareRootIterations

Background: The Babylonians used an iterative method to calculate square roots by hand as early as 1500 BC. Here are the steps to find the square root of a positive number n:

1. Start with an initial guess for the square root. This guess can be anything other than 0.
Get a new guess using the following formula: 
2. newGuess = (guess + n / guess) / 2.

3. Repeat step 2, now with the newGuess as the guess.

4. Continue repeating until the difference between newGuess and guess is smaller than a value we'll call epsilon.

5. The newGuess at the end of this process is an approximation of the square root.

With this in mind, write the function `babylonianSqureRootIterations(n, initialGuess, epsilon)` which takes a positive `int` `n`, a positive `float` representing the initial guess, and a positive `float` `epsilon`. Return the number of times the above formula needs to be repeated to converge on a square root.


```python
# from cmu_cs3_utils import testFunction

def babylonianSquareRootIterations(n, initialGuess, epsilon):
    guess = initialGuess
    newGuess = (guess + n / guess) / 2
    count = 1
    while abs(guess - newGuess) > epsilon:
        guess = newGuess
        newGuess = (guess + n / guess) / 2
        count += 1
    return count

# @testFunction
# def testBabylonianSquareRootIterations():
#     assert(babylonianSquareRootIterations(1, 1, 0.25) == 1)
#     assert(babylonianSquareRootIterations(9, 3, 0.1) == 1)
#     assert(babylonianSquareRootIterations(9, 3.5, 0.05) == 2)
#     assert(babylonianSquareRootIterations(9, 5, 0.1) == 3)
#     assert(babylonianSquareRootIterations(4, 7, 0.25) == 4)
#     assert(babylonianSquareRootIterations(0.49, 2, 0.05) == 4)
#     assert(babylonianSquareRootIterations(25, 10, .05) == 4)

# def main():
#     testBabylonianSquareRootIterations()

# main()

```

### stepsToReach495

Backgound: Kaprekar's routine is an algorithm which can be performed on any three digit number, except for numbers with three of the same digit (such as 111). The algorithm always produces the number 495 at the end.

Here are the instructions which describe Kaprekar's routine.

Construct two new numbers by arranging the digits of n in ascending and descending order.
Subtract the smaller number from the larger one.
Repeat the process on the resulting number until you reach 495.
Here is Kaprekar's routine run on the number 251.

Construct the numbers 125 and 521.
Subtract 125 from 521, which results in 396.
Repeat the process on the resulting number (396) until you reach 495:

- 396 --> 963 - 369 --> 594
- 594 --> 954 - 459 --> 495

Note that if the algorithm ever produces a 2 digit number, a zero should be preserved so we consider the number as having three digits. For example, here is Kaprekar's routine run on 898.

- 898 --> 988 - 889 --> 099
- 099 --> 990 - 099 --> 891
- 891 --> 981 - 189 --> 792
- 792 --> 972 - 279 --> 693
- 693 --> 963 - 369 --> 594
- 594 --> 954 - 459 --> 495

With this in mind, write the function stepsToReach495(n), which takes a three digit integer n, runs Kaprekar's routine on it, and returns the number of times it completed step 2 of the routine before reaching 495.

stepsToReach495(251)will return 3, because we complete step 2 of Kaprekar's routine 3 times before reaching 495. Similarly, stepsToReach495(898)will return 6.

Return None if the routine cannot be completed because the number has three of the same digit.


```python
# from cmu_cs3_utils import testFunction

def ascend(n):
    thirdDigit = n % 10
    secondDigit = (n // 10) % 10
    firstDigit = n // 100
    
    smallest = min(thirdDigit, secondDigit, firstDigit)
    largest = max(thirdDigit, secondDigit, firstDigit)
    sumOfDigits = firstDigit + secondDigit + thirdDigit
    middle = sumOfDigits - smallest - largest
    
    result = smallest * 100 + middle * 10 + largest
    return result
    
def reverseDigit(n):
    result = 0
    while n > 0:
        lastDigit = n % 10
        result = result * 10 + lastDigit
        n //= 10
    return result

def stepsToReach495(n):
    step = 0
    isZero = False
    
    thirdDigit = n % 10
    secondDigit = (n // 10) % 10
    firstDigit = n // 100
    if firstDigit == secondDigit == thirdDigit:
        return None
    
    while n != 495:
        ascendingN = ascend(n)
        if ascendingN < 100:
            isZero = True
        
        if isZero:
            descendingN = reverseDigit(ascendingN) * 10
        else: 
            descendingN = reverseDigit(ascendingN)
        isZero = False
        
        maxN, minN = max(ascendingN, descendingN), min(ascendingN, descendingN)
        n = maxN - minN
        
        step += 1
    return step

# @testFunction
def testStepsToReach495():
    assert(stepsToReach495(495) == 0)

    assert(stepsToReach495(594) == 1) # 954 - 459 = 495

    assert(stepsToReach495(396) == 2) # 963 - 369 = 594
                                      # 954 - 459 = 495

    assert(stepsToReach495(936) == 2) # Same as 396

    assert(stepsToReach495(251) == 3) # 521 - 125 = 396
                                      # 963 - 369 = 594
                                      # 954 - 459 = 495
    
    assert(stepsToReach495(516) == 1) # 651 - 156 = 495

    assert(stepsToReach495(891) == 4)

    assert(stepsToReach495(898) == 6) # 988 - 889 = 099
                                      # 990 - 099 = 891
                                      # 981 - 189 = 792
                                      # 972 - 279 = 693
                                      # 963 - 369 = 594
                                      # 954 - 459 = 495

    assert(stepsToReach495(111) == None)
    assert(stepsToReach495(555) == None)
    assert(stepsToReach495(777) == None)
    assert(stepsToReach495(630) == 2)

def main():
    testStepsToReach495()

# main()

```

### occursIn

Write the function `occursIn(haystack, needle)` which takes two non-negative integers, the `haystack` and the `needle`, and returns `True` if the needle is present in the haystack, and `False` otherwise.

For example, `occursIn(183742, 374)` would return True, because the number 374 appears in 183742. However, `occursIn(48372, 374)` would return `False` because 374 does not appear in 48372.


```python
# from cmu_cs3_utils import testFunction
import math

def occursIn(haystack, needle):
    if haystack == 0 and needle == 0:
        return True
    while haystack > 0:
        currHaystackDigit = haystack % 10
        currNeedleDigit = needle % 10
        if currHaystackDigit == currNeedleDigit:
            needle //= 10
        haystack //= 10
        if needle == 0:
            return True
    return False

# @testFunction
# def testOccursIn():
#     assert(occursIn(183742, 374) == True)
#     assert(occursIn(48372, 374) == False)
#     assert(occursIn(1, 1) == True)
#     assert(occursIn(423, 4) == True)
#     assert(occursIn(423, 6) == False)
#     assert(occursIn(12323, 123) == True)
#     assert(occursIn(100, 0) == True)
#     assert(occursIn(0, 0) == True)

# def main():
#     testOccursIn()

# main()

```

### isRotation

A rotation of a number `n` is constructed by shifting digits from one end of the number to the other. For example, 1234 rotated once to the right is 4123. If you continue rotating this number to the right, you get 3412, 2341, and finally 1234 again.

Note that zeros are preserved when rotating. So 250 rotated once is 25, and rotated twice is 502.

With this in mind, write the function `isRotation(x, y)` which takes two non-negative integers `x` and `y`, and returns `True` if `x` is a rotation of `y` or `y` is a rotation of `x`, and `False` otherwise.



```python
# from cmu_cs3_utils import testFunction
import math

def digitCount(n):
    if n == 0:
        return 1
    return 1 + math.floor(math.log10(abs(n)))
    
def isRotation(x, y):
    if x == 0 and y == 0:
        return True
    digitNumber = digitCount(x)
    oriX = x
    while x > 0:
        currDigit = x % 10
        x //= 10
        if (y == currDigit * 10 ** (digitNumber-1) + x or
            (y / (currDigit * 10 ** (digitNumber-1) + x)) % 10 == 0): 
            return True
        x = currDigit * 10 ** (digitNumber-1) + x
        if oriX == x:
            return False

# @testFunction
# def testIsRotation():
#     assert(isRotation(1234, 4123) == True)
#     assert(isRotation(1234, 3412) == True)
#     assert(isRotation(1234, 2341) == True)
#     assert(isRotation(1234, 1234) == True)
#     assert(isRotation(0, 0) == True)
#     assert(isRotation(250, 25) == True)
#     assert(isRotation(25, 250) == True)
#     assert(isRotation(250, 502) == True)
#     assert(isRotation(502, 250) == True)
#     assert(isRotation(1007, 7001) == False)
#     assert(isRotation(1234, 4321) == False)

# def main():
#     testIsRotation()

# main()
```

### integral*

trapezoid method


```python
# from cmu_cs3_utils import testFunction, almostEqual
import math

def integral(f, start, end, N):
    sumOfArea = 0
    height = (end - start) / N
    for numTrapezoid in range(N):
        shortSide = f(start + height * numTrapezoid)
        longSide = f(start + height * (numTrapezoid+1))
        area = (shortSide + longSide) * height / 2
        sumOfArea += area
    return sumOfArea

# #These functions are used in the test cases
# def f1(x): return 42
# def i1(x): return 42*x 
# def f2(x): return 2*x  + 1
# def i2(x): return x**2 + x
# def f3(x): return 9*x**2
# def i3(x): return 3*x**3
# def f4(x): return math.cos(x)
# def i4(x): return math.sin(x)

# @testFunction
# def testIntegral():
#     epsilon = 10**-4
#     assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
#                       epsilon=epsilon))
#     assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
#                       epsilon=epsilon))
#     assert(almostEqual(integral(f2, 1, 2, 1), 4,
#                       epsilon=epsilon))
#     assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
#                       epsilon=epsilon))
#     assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
#                       epsilon=epsilon))
#     assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
#                       epsilon=epsilon))

# def main():
#     testIntegral()

# main()

```

### gcd

Background: According to Euclid, the greatest common divisor, or gcd, can be found like so:

gcd(x, y) == gcd(y, x % y)


```python
# from cmu_cs3_utils import testFunction

def gcd(x, y):
    x, y = max(x,y), min(x,y)
    if x % y == 0: return y
    while y != 0:
        x, y = y, x % y
    return x

# @testFunction
# def testGcd():
#     assert(gcd(3, 3) == 3)
#     assert(gcd(3**6, 3**6) == 3**6)
#     assert(gcd(3**6, 2**6) == 1)
#     assert(gcd(2*3*4*5, 3*5) == 15)
#     x = 1568160 # 2**5 * 3**4 * 5**1 * 11**2
#     y = 3143448 # 2**3 * 3**6 * 7**2 * 11**1
#     g = 7128    # 2**3 * 3**4 *        11**1
#     assert(gcd(x, y) == g)

# def main():
#     testGcd()

# main()
```

### nthAdditivePrime

Background: An additive prime is a prime number such that the sum of its digits is also prime.

For example, 113 is prime and 1 + 1 + 3 = 5, which is also prime, so 113 is an additive prime.

With this in mind, write the function nthAdditivePrime(n) which takes a non-negative int n and returns the nth Additive Prime.


```python
# from cmu_cs3_utils import testFunction, rounded

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maxFactor = rounded(n**0.5)
    for i in range(3, maxFactor + 1, 2):
        if n % i == 0:
            return False
    return True

def isAdditivePrime(n):
    if not isPrime(n):
        return False
    else:
        result = 0
        while n > 0:
            result += n % 10
            n //= 10
        if isPrime(result):
            return True
        else: return False

def nthAdditivePrime(n):
    guess = 0
    count = -1
    while count < n:
        guess += 1
        if isAdditivePrime(guess):
            count += 1
    return guess

# @testFunction
# def testIsAdditivePrime():
#     assert(isAdditivePrime(2) == True)
#     assert(isAdditivePrime(3) == True)
#     assert(isAdditivePrime(23) == True)
#     assert(isAdditivePrime(61) == True)
#     assert(isAdditivePrime(113) == True)
#     assert(isAdditivePrime(13) == False)
#     assert(isAdditivePrime(103) == False)
#     assert(isAdditivePrime(16) == False)
    

# @testFunction
# def testNthAdditivePrime():
#     assert(nthAdditivePrime(0) == 2)
#     assert(nthAdditivePrime(1) == 3)
#     assert(nthAdditivePrime(5) == 23)
#     assert(nthAdditivePrime(10) == 61)
#     assert(nthAdditivePrime(15) == 113)

# def main():
#     testIsAdditivePrime()
#     testNthAdditivePrime()

# main()

```

### nthPowerfulNumber

Background: A powerful number (also called a squareful number) is defined as a positive integer n such that for every prime factor p, p2 is also a factor of n.

With this in mind, write the function nthPowerfulNumber(n) which takes a non-negative int n, and returns the nth powerful number as described above.

Note: Prime numbers are not powerful numbers.


```python
# from cmu_cs3_utils import testFunction, rounded

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maxFactor = rounded(n**0.5)
    for i in range(3, maxFactor+1,2):
        if n % i == 0:
            return False
    return True

def isPowerfulNumber(n):
    result = False
    if n == 1: return True
    if isPrime(n): return False
    for i in range(1, n, 1):
        if n % i == 0:
            if isPrime(i):
                if n % (i**2) == 0:
                    result = True
                else: return False
    return result

def nthPowerfulNumber(n):
    guess = 0
    count = -1
    while count < n:
        guess += 1
        if isPowerfulNumber(guess):
            count += 1
    return guess

# @testFunction
# def testIsPowerfulNumber():
#     assert(isPowerfulNumber(1) == True)
#     assert(isPowerfulNumber(4) == True)
#     assert(isPowerfulNumber(25) == True)
#     assert(isPowerfulNumber(64) == True)
#     assert(isPowerfulNumber(121) == True)
#     assert(isPowerfulNumber(1000) == True)
#     assert(isPowerfulNumber(2) == False)
#     assert(isPowerfulNumber(15) == False)

# @testFunction
# def testNthPowerfulNumber():
#     print(nthPowerfulNumber(2))
#     print(nthPowerfulNumber(3))
#     print(nthPowerfulNumber(4))
#     assert(nthPowerfulNumber(0) == 1)
#     assert(nthPowerfulNumber(1) == 4)
#     assert(nthPowerfulNumber(5) == 25)
#     assert(nthPowerfulNumber(10) == 64)
#     assert(nthPowerfulNumber(15) == 121)


# def main():
#     testIsPowerfulNumber()
#     testNthPowerfulNumber()

# main()

```

### nthPerfectNumber

Background: A number is perfect if it is equal to the sum of its positive factors less than itself.

For example, 6 is perfect because 6 = 1 + 2 + 3.

With this in mind, write the function nthPerfectNumber(n) which takes a non-negative int n and returns the nth perfect number.

Note: For full credit, you need to write a reasonably fast solution, which uses the same observation that sped up isPrime(). You should only search for factors up to the square root of n.


```python
# from cmu_cs3_utils import testFunction, rounded

def isPerfectNumber(n):
    result = 0
    for i in range(1,n,1):
        if n % i == 0:
            result += i
    if result == n:
        return True
    else: return False

def nthPerfectNumber(n):
    guess = 0
    count = -1
    while count < n:
        guess += 1
        if isPerfectNumber(guess):
            count += 1
    return guess

# @testFunction
# def testIsPerfectNumber():
#     assert(isPerfectNumber(6) == True)
#     assert(isPerfectNumber(28) == True)
#     assert(isPerfectNumber(496) == True)
#     assert(isPerfectNumber(8128) == True)
#     assert(isPerfectNumber(1) == False)
#     assert(isPerfectNumber(30) == False)

# @testFunction
# def testNthPerfectNumber():
#     assert(nthPerfectNumber(0) == 6)
#     assert(nthPerfectNumber(1) == 28)
#     assert(nthPerfectNumber(2) == 496)  
#     # assert(nthPerfectNumber(3) == 8128) # this can be slow 

# def main():
#     testIsPerfectNumber()
#     testNthPerfectNumber()

# main()

```

### isSemiPrime

Background: A semi-prime is a positive integer that is the product of exactly two prime numbers.

The first few semi-primes are 4, 6, 9, 10, 14, 15...

With this in mind, write the function isSemiPrime(n) which takes in an arbitrary value (possibly not an int) and returns True if it is a semi-prime and False otherwise.

Note: Semi-primes include the squares of prime numbers because the two primes in the product may equal each other.

Another note: If n is not an integer, it is not considered a semi-prime and the function returns False.


```python
# from cmu_cs3_utils import testFunction, rounded

def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    maxFactor = rounded(n**0.5)
    for i in range(3, maxFactor + 1, 2):
        if n % i == 0:
            return False
    return True

def isSemiPrime(n):
    if isinstance(n,int) or isinstance(n,float):
        for i in range(1,int(n),1):
            if n % i == 0:
                if isPrime(i) and isPrime(n//i):
                    return True
    return False

# @testFunction
# def testIsSemiPrime():
#     assert(isSemiPrime(4) == True)
#     assert(isSemiPrime(21) == True)
#     assert(isSemiPrime(33) == True)
#     assert(isSemiPrime(1) == False)
#     assert(isSemiPrime(7) == False)
#     assert(isSemiPrime(100) == False)
#     assert(isSemiPrime('five') == False)
#     assert(isSemiPrime(2.0) == False)




# def main():
#     testIsSemiPrime()

# main()

```

### nthLeftTruncatablePrime

Background: A left-truncatable prime is a prime number containing no zero digits in which if the leading (left) digit is continuously removed, then all resulting numbers are prime.

For example, 137 is a left-truncatable prime because 137 is prime, 37 is prime, and 7 is prime. However, 103 is not a left-truncatable prime because even though 103, 03, and 3 are prime, 103 contains a zero digit.

With this in mind, write the function nthLeftTruncatablePrime(n) which takes a non-negative int n, and returns the nth left-truncatable prime as described above.


```python
# from cmu_cs3_utils import testFunction, rounded
import math

def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    maxFactor = rounded(n**0.5)
    for i in range(3, maxFactor + 1, 2):
        if n % i == 0: 
            return False
    return True

def digitCount(n):
    if n == 0:
        return 1
    return 1 + math.floor(math.log10(abs(n)))
    
def hasZeroDigit(n):
    while n > 0:
        currDigit = n % 10
        if currDigit == 0: return True
        n //= 10
    return False

def isLeftTruncatablePrime(n):
    if n == 0: return False
    if hasZeroDigit(n): return False
    while n > 0:
        if isPrime(n):
            n = n % (10 ** (digitCount(n) - 1))
        else:
            return False
    return True

def nthLeftTruncatablePrime(n):
    guess = 0
    count = 0
    while count <= n:
        guess += 1
        if isLeftTruncatablePrime(guess):
            count += 1
    return guess

# @testFunction
# def testIsLeftTruncatablePrime():
#     assert(isLeftTruncatablePrime(2) == True)
#     assert(isLeftTruncatablePrime(113) == True)
#     assert(isLeftTruncatablePrime(137) == True)
#     assert(isLeftTruncatablePrime(1223) == True)
#     assert(isLeftTruncatablePrime(0) == False)
#     assert(isLeftTruncatablePrime(11) == False)
#     assert(isLeftTruncatablePrime(103) == False)
#     assert(isLeftTruncatablePrime(1234) == False)

# @testFunction
# def testNthLeftTruncatablePrime():
#     assert(nthLeftTruncatablePrime(0) == 2)
#     assert(nthLeftTruncatablePrime(1) == 3)
#     assert(nthLeftTruncatablePrime(5) == 17)
#     assert(nthLeftTruncatablePrime(10) == 53)
#     assert(nthLeftTruncatablePrime(15) == 113)


# def main():
#     testIsLeftTruncatablePrime()
#     testNthLeftTruncatablePrime()

# main()

```

## 2.3 Style

## 2.4 Strings

### encodeCaesarCipher + decodeCaesarCipher

Background: To shift a letter by n, you use the letter that is n characters after it in the alphabet. For example:

- 'a' shifted by 3 is 'd'.
- 'd' shifted by 2 is 'f'.

Once we reach the end of the alphabet, we wrap back around to the beginning. For example:
- 'z' shifted by 1 is 'a'.
- 'x' shifted by 4 is 'b'.

A Caesar Cipher is a simple cipher that takes a message (a string) and a shift (an integer), and shifts each letter in the message by shift characters.

For example, a Caesar Cipher on the message 'I like zoos!' with a shift of 2 returns 'K nkmg bqqu!'. Notice that we did not shift non-letters, we just used them unmodified. Also notice that we preserved case, so uppercase letters are shifted to uppercase, and lowercase letters are shifted to lowercase.

With this in mind, write the function encodeCaesarCipher(msg, shift) which performs a Caesar Cipher on msg, shifting each letter by shift characters. You are guaranteed that msg is a string, and that shift is a possibly-negative integer.

Also write the function decodeCaesarCipher(encodedMsg, shift), which takes a message that has been encoded using a Caesar Cipher with the given shift, and returns the decoded message. For example:

decodeCaesarCipher('Bgdtc', 2) == 'Zebra'
decodeCaesarCipher('Xczpy', -2) == 'Zebra'

Hint: Once you have written encodeCaesarCipher(), you can write decodeCaesarCipher() in just a couple lines of code.

Important note: The guided solution to this exercise contains the line letterIndex %= 26. Due to a Brython bug, this line of code does not work and should be replaced with letterIndex = letterIndex % 26.




```python
# from cmu_cs3_utils import testFunction

def doShift(char, shift):
    baseChar = 'a' if char.islower() else 'A'
    letterIndex = ord(char) - ord(baseChar)
    newLetterIndex = letterIndex + shift
    newLetterIndex = newLetterIndex % 26
    return chr(ord(baseChar) + newLetterIndex)
    
def encodeCaesarCipher(msg, shift):
    result = ''
    for character in msg:
        if character.isalpha():
            result += doShift(character, shift)
        else:
            result += character
    return result

def decodeCaesarCipher(encodedMsg, shift):
    return encodeCaesarCipher(encodedMsg, -shift)
        
# @testFunction
# def testEncodeCaesarCipher():
#     assert(encodeCaesarCipher('I like zoos!', 2) == 'K nkmg bqqu!')
#     assert(encodeCaesarCipher('Zebra', 1) == 'Afcsb')
#     assert(encodeCaesarCipher('Zebra', -1) == 'Ydaqz')
#     assert(encodeCaesarCipher('I love CS3!', -7) == 'B ehox VL3!')
#     assert(encodeCaesarCipher('Carpe Diem', 63) == 'Nlcap Otpx')
#     assert(encodeCaesarCipher('', 13) == '')

# @testFunction
# def testDecodeCaesarCipher():
#     assert(decodeCaesarCipher('J mjlf appt!', 1) == 'I like zoos!')
#     assert(decodeCaesarCipher('Bgdtc', 2) == 'Zebra')
#     assert(decodeCaesarCipher('Xczpy', -2) == 'Zebra')
#     assert(decodeCaesarCipher('B ehox VL3!', -7) == 'I love CS3!')
#     assert(decodeCaesarCipher('Nlcap Otpx', 63) == 'Carpe Diem')
#     assert(decodeCaesarCipher('', 13) == '')

# def main():
#     testEncodeCaesarCipher()
#     testDecodeCaesarCipher()

# main()

```

### topScorer

Write the function topScorer(data) which takes a multiline string representing the scores for a competition. The first value on each line is the name of the player (which you can assume has no integers in it). Each value after that is an individual score (which you can assume is a non-negative integer). All values on a line are separated by commas.

The function should return the player with the highest total score (where a player's total score is the sum of all their scores). If there is a tie, return the names of the tied players in a comma-separated string. They should appear in the same order they appeared in the original data. If nobody wins (because there is no data), return None (not the string 'None').


```python
# from cmu_cs3_utils import testFunction

def topScorer(data):
    champPlayer = None
    champScore = -1
    for line in data.splitlines():
        firstCommaIndex = line.find(',')
        currPlayer = line[:firstCommaIndex]
        scores = line[firstCommaIndex + 1:]
        
        currScore = 0
        for score in scores.split(','):
            currScore += int(score)
        
        if currScore == champScore:
            champPlayer += ',' + currPlayer
        
        if currScore > champScore:
            champScore = currScore
            champPlayer = currPlayer
            
    return champPlayer

# @testFunction
# def testTopScorer():
#     data = '''\
# Joe,10,20,30,40
# Lauren,10,20,30
# Ben,10,20,30,5
# '''
#     assert(topScorer(data) == 'Joe')

#     data = '''\
# David,11,20,30
# Austin,10,20,30,1
# Lauren,50
# '''
#     assert(topScorer(data) == 'David,Austin')

#     data = '''\
# Ping-Ya,100,80,90
# '''
#     assert(topScorer(data) == 'Ping-Ya')

#     data = '''\
# Reyna,20,40,40
# Ema,5,5,5,5,10
# Ketandu,50,20,10,20
# Tanya,80,20
# Kate,70
# '''
#     assert(topScorer(data) == 'Reyna,Ketandu,Tanya')

#     assert(topScorer('') == None)


# def main():
#     testTopScorer()

# main()

```

### interleave

Write the function `interleave(s1, s2)` which takes two strings, `s1` and `s2`, and returns a string composed of alternating characters from `s1` and `s2` (that is, it interleaves `s1` and `s2`).

For example, `interleave('pto', 'yhn')` returns the string `'python'`. If one string is longer than the other, concatenate the rest of the remaining string onto the end of the new string. For example `interleave('ab', 'xyz?')` returns the string `'axbyz?'`.


```python
# from cmu_cs3_utils import testFunction

def interleave(s1, s2):
    result = ''
    length = min(len(s1), len(s2))
    for i in range(length):
        result += s1[i] + s2[i]
    if len(s1) > len(s2): result += s1[length:]
    if len(s2) > len(s1): result += s2[length:]
        
# @testFunction
# def testInterleave():
#     assert(interleave('pto', 'yhn') == 'python')
#     assert(interleave('ab', 'xyz?') == 'axbyz?')
#     assert(interleave('a', 'b') == 'ab')
#     #assert(interleave('', 'cs3') == 'cs3')
#     #assert(interleave('cs3', '') == 'cs3')
#     assert(interleave('', '') == '')

# def main():
#     testInterleave()

# main()

```

### areAnagrams

Background: Two strings are anagrams if each string can be reordered into the other. Treat uppercase and lowercase as the same letter (so `"Abca"` and `"BAAc"` are anagrams).

With this in mind, write the function `areAnagrams(s1, s2)` which takes two strings, s1 and s2, that you may assume contain only letters, and returns True if the strings are anagrams, and False otherwise.

You may not use `sort()`, `sorted()`, or any other list-based functions or approaches.

Hints:

Do not try to reorder either string! This can be solved more easily by not doing that.
Instead, `s.count()` could be quite handy here.
Also note that every string is an anagram of itself.


```python
# from cmu_cs3_utils import testFunction
import string

def areAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False
        
    s1 = s1.lower()
    s2 = s2.lower()
    for char in s1:
        count_s1 = s1.count(char)
        count_s2 = s2.count(char)
        if count_s1 != count_s2:
            return False
    return True

# @testFunction
# def testAreAnagrams():
#     assert(areAnagrams('Abca', 'BAAc') == True)
#     assert(areAnagrams('Word', 'word') == True)
#     assert(areAnagrams('CAT', 'act') == True)
#     assert(areAnagrams('', '') == True)
#     assert(areAnagrams('abcd', 'abc') == False)
#     assert(areAnagrams('abc', 'abcd') == False)
#     assert(areAnagrams('abc', 'abd') == False)
#     assert(areAnagrams('abc', 'abc') == True)

# def main():
#     testAreAnagrams()

# main()

```

### encodeSubstitutionCipher + decodeSubstitutionCipher

Background: A substitution cipher is a cipher that replaces each letter in the alphabet with another letter. We keep track of which letter maps to which using a key. A key is a jumbled version of the alphabet, where the first character replaces A, the second character replaces B, etc. For example, using the key 'SQGYFEZXLANKJIMPURDCWTHVOB' would turn 'CAB' into 'GSQ'.

With this in mind, write the function encodeSubstitutionCipher(msg, key) which takes a message and a key as described above, and returns the encoded message. You can assume that the key uses uppercase letters, but case should be preserved when encoding the message. Non-letter characters should remain unchanged. For example, using the key 'SQGYFEZXLANKJIMPURDCWTHVOB' would turn 'Cab Z?' into 'Gsq B?'.

Only after you have written encodeSubstitutionCipher(msg, key), write the function decodeSubstitutionCipher(encodedMsg, key) which takes a message that has been encoded with the given key, and returns the original decoded message.


```python
# from cmu_cs3_utils import testFunction

def index(char):
    baseChar = 'a' if char.islower() else 'A'
    i = ord(char) - ord(baseChar)
    return i

def encodeSubstitutionCipher(msg, key):
    result = ''
    for char in msg:
        if char.isalpha():
            if char.islower():
                result += key[index(char)].lower()
            else:
                result += key[index(char)]
        else:
            result += char
    return result

def decodeSubstitutionCipher(encodedMsg, key):
    result = ''
    for char in encodedMsg:
        if char.isalpha():
            if char.islower():
                char = char.upper()
                result += chr(key.find(char) + ord('a')).lower()
            else:
                result += chr(key.find(char) + ord('A'))
        else:
            result += char
    return result

# @testFunction
# def testEncodeSubstitutionCipher():
#     assert(encodeSubstitutionCipher('CAB',
#     'SQGYFEZXLANKJIMPURDCWTHVOB') == 'GSQ')
#     assert(encodeSubstitutionCipher('Cab Z?',
#     'SQGYFEZXLANKJIMPURDCWTHVOB') == 'Gsq B?')
#     assert(encodeSubstitutionCipher('Hello, World!',
#     'ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'Hello, World!')
#     assert(encodeSubstitutionCipher('42 - 0 = 42',
#     'XHNSBMTOPQWGZDCEAVLKJYIURF') == '42 - 0 = 42')
#     assert(encodeSubstitutionCipher('', 'XHNSBMTOPQWGZDCEAVLKJYIURF') == '')

# @testFunction
# def testDecodeSubstitutionCipher():
#     assert(decodeSubstitutionCipher('GSQ',
#     'SQGYFEZXLANKJIMPURDCWTHVOB') == 'CAB')
#     assert(decodeSubstitutionCipher('Gsq B?',
#     'SQGYFEZXLANKJIMPURDCWTHVOB') == 'Cab Z?')
#     assert(decodeSubstitutionCipher('Hello, World!',
#     'ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'Hello, World!')
#     assert(decodeSubstitutionCipher('42 - 0 = 42',
#     'XHNSBMTOPQWGZDCEAVLKJYIURF') == '42 - 0 = 42')
#     assert(decodeSubstitutionCipher('', 'XHNSBMTOPQWGZDCEAVLKJYIURF') == '')

# def main():
#     testEncodeSubstitutionCipher()
#     testDecodeSubstitutionCipher()

# main()

```

### encodeVigenereCipher + decodeVigenereCipher

Background: As we have learned, a Caesar Cipher takes a message and a shift, and encodes each letter by shifting it by the given amount. We can strengthen this by changing the amount we shift each letter by.

For example, say we have the message 'ABC' and we use the shifts 3,4,5. Then we shift 'A' by 3 to get 'D', we shift 'B' by 4 to get 'F', and we shift 'C' by 5 to get 'H'. So the encoded message is 'DFH'.


```python
# from cmu_cs3_utils import testFunction
import math

def doShift(char, shift):
    shift = ord(shift) - ord('A')
    baseChar = 'a' if char.islower() else 'A'
    letterIndex = ord(char) - ord(baseChar)
    newLetterIndex = (letterIndex + shift) % 26
    return chr(ord(baseChar) + newLetterIndex)

def encodeVigenereCipher(msg, key):
    result = ''
    i = 0
    for char in msg:
        if char.isalpha():
            result += doShift(char, key[i])
        else:
            result += char
        i += 1
        if i >= len(key):
            i = 0
    return result

def doBackShift(char, shift):
    shift = ord(shift) - ord('A')
    baseChar = 'a' if char.islower() else 'A'
    letterIndex = ord(char) - ord(baseChar)
    newLetterIndex = (letterIndex - shift) % 26
    return chr(ord(baseChar) + newLetterIndex)

def decodeVigenereCipher(encodedMsg, key):
    result = ''
    i = 0
    for char in encodedMsg:
        if char.isalpha():
            result += doBackShift(char, key[i])
        else:
            result += char
        i += 1
        if i >= len(key):
            i = 0
    return result

# @testFunction
# def testEncodeVigenereCipher():
#     assert(encodeVigenereCipher('ABC', 'DEF') == 'DFH')
#     assert(encodeVigenereCipher('I like zoos!', 'CODE') == 'K omms dqcv!')
#     assert(encodeVigenereCipher('CS3 is fun', 'SCOTTY') == 'UU3 bq hig')
#     assert(encodeVigenereCipher('', 'A') == '')

# @testFunction
# def testDecodeVigenereCipher():
#     assert(decodeVigenereCipher('DFH', 'DEF') == 'ABC')
#     assert(decodeVigenereCipher('K omms dqcv!', 'CODE') == 'I like zoos!')
#     assert(decodeVigenereCipher('UU3 bq hig', 'SCOTTY') == 'CS3 is fun')
#     assert(decodeVigenereCipher('', 'A') == '')

# def main():
#     testEncodeVigenereCipher()
#     testDecodeVigenereCipher()

# main()

```

### wordWrap

Write the function wordWrap(text, width) which takes a string text containing only lowercase letters or spaces and a positive integer width, and returns a possibly-multiline string that matches the original string, only with line wrapping at the given width. For example, wordWrap('abc', 3) just returns 'abc', but wordWrap('abc', 2) returns a 2-line string, with 'ab' on the first line and 'c' on the second line.

All spaces should be converted to dashes ('-'), so they can be easily seen in the resulting string.


```python
# from cmu_cs3_utils import testFunction
import math

def wordWrap(text, width):
    result = ''
    while len(text) > 0:
        result += text[:width] + '\n'
        text = text[width:]
    result = result.strip()
    result = result.replace(' ', '-')
    return result

# @testFunction
# def testWordWrap():
#     assert(wordWrap('abc', 2) == 'ab\nc')
#     assert(wordWrap('abcd', 2) == 'ab\ncd')
#     assert(wordWrap('abc', 3) == 'abc')
#     assert(wordWrap('abcdefghij', 4) == '''\
# abcd
# efgh
# ij''')
#     assert(wordWrap('a b c de fg', 4) == '''\
# a-b-
# c-de
# -fg''')
#     assert(wordWrap('abc', 5) == 'abc')

# def main():
#     testWordWrap()

# main()

```

### collapseWhitespace

Write the function `collapseWhitespace(s)` which takes a string s and returns an equivalent string except that each occurrence of whitespace in the string is replaced by a single space.

For example, `collapseWhitespace('a\t \tb\n\nc')` replaces the two tabs and a space with a single space, and two newlines with another single space, returning `'a b c'`.

Note: You may not use `s.replace()` in your solution.

Hint: You may want to review the String Constants section of the String Literals notes.


```python
# from cmu_cs3_utils import testFunction
import string

def collapseWhitespace(s):
    result = []
    endWithWhiteSpace = False
    if s.startswith('\t') or s.startswith('\n'):
        startWithWhiteSpace = True
        result += ' '
    if s.endswith('\t') or s.endswith('\n') or s.endswith(' ') or \
        s.endswith('\x0b'):
        endWithWhiteSpace = True
    s = s.strip()
    for char in s:
        if char.isalpha():
            result += str(char)
        else:
            if result[-1].isspace():
                result = result
            else:
                result += ' '
    resultStr = ''
    for char in result:
        resultStr += char
    if endWithWhiteSpace == True:
        resultStr += ' '
    return resultStr

# @testFunction
# def testCollapseWhitespace():
#     assert(collapseWhitespace('a\t \tb\n\nc') == 'a b c')
#     assert(collapseWhitespace('a\nb') == 'a b')
#     assert(collapseWhitespace('a\n   \t    b') == 'a b')
#     assert(collapseWhitespace('a\n   \t    b  \n\n  \t\t\t c   ') == 'a b c ')
#     assert(collapseWhitespace('\tw     \t\n x z') == ' w x z')
#     assert((collapseWhitespace('c\r\rd\x0b\x0b')) == 'c d ')

# def main():
#     testCollapseWhitespace()

# main()

```

### solvesCryptarithm

Background: A cryptarithm is a puzzle where we start with a simple arithmetic statement but then we replace all the digits with letters (where the same digit is replaced by the same letter each time). We will limit such puzzles to strings the form 'A + B = C' (always exactly one space on either side of '+' and '=').

For example, 'SEND + MORE = MONEY' is such a puzzle. The solution to a cryptarithm is an assignment of digits to the letters to make the math work out properly. For example, if we assign 0 to 'O', 1 to 'M', 2 to 'Y', 5 to 'E', 6 to 'N', 7 to 'D', 8 to 'R', and 9 to 'S' we get:

  S E N D       9 5 6 7

+ M O R E     + 1 0 8 5

--------------------------

M O N E Y     1 0 6 5 2
And so we see that this assignment does in fact solve the problem! Note: for this problem, you do not have to find a solution. You only have to confirm whether or not a proposed solution actually works.

Next, we need a way to represent a possible solution. For that, we will use a single string solution of length 10, where solution[0] is the letter corresponding to the digit 0, solution[1] is the letter corresponding to the digit 1, and so on. We use '-' to represent unassigned digits. For example, the string 'OMY--ENDRS' represents the assignments listed in the 'SEND + MORE = MONEY' example.

With this in mind, write the function solvesCryptarithm(puzzle, solution) which takes a puzzle (such as 'SEND + MORE = MONEY') and a proposed solution (such as 'OMY--ENDRS'). Your function should return True if substituting the digits from the solution back into the puzzle results in a mathematically correct addition problem, and False otherwise. You do not have to check whether a letter occurs more than once in the proposed solution, but you do have to verify that all the letters in the puzzle occur somewhere in the solution. You may not use the eval() function.


```python
# from cmu_cs3_utils import testFunction

def solvesCryptarithm(puzzle, solution):
    result = ''
    for i in puzzle:
        if i.isalpha():
            index = solution.find(i)
            if index == -1:
                return False
            result += str(index)
        else: result += ' '
    result = result.split('   ')
    if int(result[0]) + int(result[1]) == int(result[-1]):
        return True
    else:
        return False


# @testFunction
# def testSolvesCryptarithm():
#     #                         9567 + 1085 = 10652
#     assert(solvesCryptarithm('SEND + MORE = MONEY', 'OMY--ENDRS') == True)

#     #                         201689 + 201689 = 403378
#     assert(solvesCryptarithm('NUMBER + NUMBER = PUZZLE', 'UMNZP-BLER') == True)

#     #                         91542 + 3077542 = 3169084
#     assert(solvesCryptarithm('TILES + PUZZLES = PICTURE', 'UISPELCZRT') == True)

#     #                         8456 + 1074 = 10542 (False)
#     assert(solvesCryptarithm('SEND + MORE = MONEY', 'OMY-ENDRS') == False)

#     #                         9567 + 1085 = 1062 (False)
#     assert(solvesCryptarithm('SEND + MORE = MONY', 'OMY--ENDRS') == False)

#     #                         No S in solution
#     assert(solvesCryptarithm('SEND + MORE = MONEY', 'OMY--ENDR-') == False)
    
#     assert(solvesCryptarithm('YLQF + SAMR = TMAN', 'TLFRMAYN') == False)
    
#     assert(solvesCryptarithm('ANT + BAT = BEE', 'ANEB--T') == True)

# def main():
#     testSolvesCryptarithm()

# main()

```

## 2.5 Top-down Design

### nthHappyPrime

Background: Given a positive number n, we can compute a new number by summing the squares of every digit of n. If we continually repeat this process on the resulting number, we will eventually reach either 1 or 4. For example:

- 2212 --> 22 + 22 + 12 + 22 = 13
- 13 --> 12 + 32 = 10
- 10 --> 12 + 02 = 1

Numbers that eventually arrive at 1 are called happy, and numbers that arrive at 4 are unhappy. So, from the example above, 2212 is a happy number.

A happy prime is a number which is both happy and prime. For example, 7 is the first happy prime number.

With this in mind, write the function nthHappyPrime(n) which takes an integer n, and returns the nth happy prime.



```python
# from cmu_cs3_utils import testFunction, rounded

def sumOfSquaresOfN(n):
    result = 0
    while n > 0:
        result += (n % 10)**2
        n //= 10
    return result

def isHappy(n):
    while n != 1 and n != 4:
        n = sumOfSquaresOfN(n)
    if n == 1:
        return True
    elif n == 4:
        return False

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    max_factor = rounded(n**0.5) 
    for factor in range(3,max_factor+1,2):
        if n % factor == 0:
            return False
    return True

def isHappyPrime(n):
    return isHappy(n) and isPrime(n)

def nthHappyPrime(n):
    count = 0
    guess = 0
    while count <= n:
        guess += 1
        if isHappyPrime(guess):
            count += 1
    return guess

# @testFunction
# def testNthHappyPrime():
#     assert(nthHappyPrime(0) == 7)
#     assert(nthHappyPrime(1) == 13)
#     assert(nthHappyPrime(2) == 19)
#     assert(nthHappyPrime(3) == 23)
#     assert(nthHappyPrime(4) == 31)
#     assert(nthHappyPrime(5) == 79)

# def main():
#     testNthHappyPrime()

# main()

```

### longestSubpalindrome

Background: A palindrome is a string that is the same when read forwards and backwards. For example, 'abcba' is a palindrome.

With this in mind, write the function longestSubpalindrome(s) which takes a string s and returns the longest palindrome that occurs in s. The palindrome can consist of any consecutive characters, not just letters. For example, longestSubpalindrome('ab-4-be!!!') returns 'b-4-b'.

If there is a tie, return the lexicographically larger value. In Python, a string s1 is lexicographically larger than a string s2 if s1 > s2. Therefore, longestSubpalindrome('abcbce') will return 'cbc' since 'cbc' > 'bcb'.

Note: This function is case-sensitive, so 'A' is not treated the same as 'a' here.


```python
# from cmu_cs3_utils import testFunction

def isSubpalindrome(string):
    result = True
    if len(string) % 2 == 0: 
        for i in range(len(string)//2):
            if string[i] != string[-i-1]:
                result = False
    else:
        if len(string) == 1: return True
        for i in range(len(string)//2 + 1):
            if string[i] != string[-i-1]:
                result = False
    return result

def longestSubpalindrome(s):
    champSubpalindrome = ''
    champLength = len(champSubpalindrome)
    for i in range(len(s)):
        for j in range(len(s)):
            if isSubpalindrome(s[i:j+1]):
                if len(s[i:j+1]) > champLength:
                    champSubpalindrome = s[i:j+1]
                    champLength = len(champSubpalindrome)
                if len(s[i:j+1]) == champLength:
                    if ord(s[i]) > ord(champSubpalindrome[0]):
                        champSubpalindrome = s[i:j+1]
    return champSubpalindrome

# @testFunction
# def testLongestSubpalindrome():
#     assert(longestSubpalindrome('ab-4-be!!!') == 'b-4-b')
#     assert(longestSubpalindrome('abcbce') == 'cbc')
#     assert(longestSubpalindrome('aba') == 'aba')
#     assert(longestSubpalindrome('a') == 'a')
#     assert(longestSubpalindrome('abd') == 'd')
#     assert(longestSubpalindrome('kP:p') == 'p')
#     assert(longestSubpalindrome('TQwGsyysqH') == 'syys')
#     assert(longestSubpalindrome('xAtrj') == 'x')

# def main():
#     testLongestSubpalindrome()

# main()

```

### longestCommonSubstring

If there is a tie, return the lexicographically smaller value. In Python, a string s1 is lexicographically smaller than a string s2 if s1 < s2. Thus, longestCommonSubstring('abcABC', 'zzabZZAB') returns 'AB' and not 'ab' as 'AB' < 'ab'.


```python
# from cmu_cs3_utils import testFunction

def longestCommonSubstring(s1, s2):
    champString = ''
    champLength = len(champString)
    for i in range(len(s1)):
        for j in range(i, len(s1)):
            if s2.find(s1[i:j+1]) != -1:
                if len(s1[i:j+1]) > champLength:
                    champString = s1[i:j+1]
                    champLength = len(champString)
                if len(s1[i:j+1]) == champLength:
                    if champString == '': continue
                    if ord(s1[i]) <= ord(champString[0]):
                        champString = s1[i:j+1]
    return champString

# @testFunction
# def testLongestCommonSubstring():
#     assert(longestCommonSubstring('abcdef', 'abqrcdest') == 'cde')
#     assert(longestCommonSubstring('abcdef', 'ghi') == '')
#     assert(longestCommonSubstring('abcABC', 'zzabZZAB') == 'AB')
#     assert(longestCommonSubstring('abcHIJK', 'aLbNcM') == 'a')
#     assert(longestCommonSubstring('CRANKYcrabby', 'crabbyIsCRANKY') == 'CRANKY')
#     assert(longestCommonSubstring('o', 'pokcq') == 'o')
#     assert(longestCommonSubstring('', 'ZZAB') == '')
#     assert(longestCommonSubstring('abc', '') == '')
    

# def main():
#     testLongestCommonSubstring()

# main()

```

### leastFrequentLetters

Ignore case so 'A' and 'a' are treated the same.


```python
# from cmu_cs3_utils import testFunction
import string

def leastFrequentLetters(s):
    leastLetter = ''
    leastFrequency = 10 ** 7
    for char in string.ascii_lowercase:
        currCount = s.lower().count(char)
        if currCount != 0:
            if currCount < leastFrequency:
                leastLetter = char
                leastFrequency = currCount
            elif currCount == leastFrequency:
                leastLetter += char
    return leastLetter

# @testFunction
# def testLeastFrequentLetters():
#     assert(leastFrequentLetters('aDbq dQ') == 'ab')
#     assert(leastFrequentLetters('Crazy sentences are wild!!!') == 'diltwyz')
#     assert(leastFrequentLetters('a!*@HH#!') == 'a')
#     assert(leastFrequentLetters('') == '')
#     assert(leastFrequentLetters('345623$%@#!#$%') == '')
#     assert(leastFrequentLetters('apkpaaj') == 'jk')


# def main():
#     testLeastFrequentLetters()

# main()

```

### replaceString


```python
# from cmu_cs3_utils import testFunction

def replaceString(s1, s2, s3):
    if s2 == s3: return s1
    while s1.count(str(s2)) != 0:
        index = s1.find(str(s2))
        s1 = s1[:index] + str(s3) + s1[index + len(s2):]
    return s1

# @testFunction
# def testReplaceString():
#     assert(replaceString('abadaf', 'a', 'L') == 'LbLdLf')
#     assert(replaceString('csacademy', 'a', 'A') == 'csAcAdemy')
#     assert(replaceString('csacademy', 'cs', 'CS') == 'CSacademy')
#     s = 'markers make marks'
#     assert(replaceString(s, 'ma', 'ram') == 'ramrkers ramke ramrks')
#     assert(replaceString(s, 'mar', 'ra') == 'rakers make raks')
#     assert(replaceString('case', 'a', 'a') == 'case')
    
# def main():
#     testReplaceString()

# main()

```

### hasBalancedParentheses


```python
# from cmu_cs3_utils import testFunction

def hasBalancedParentheses(s):
    if s.count('(') != s.count(')'): return False
    leftCount = 0
    rightCount = 0
    for char in s:
        if char == '(': leftCount += 1
        if char == ')': rightCount += 1
        if rightCount > leftCount: return False
    return True

# @testFunction
# def testHasBalancedParentheses():
#     assert(hasBalancedParentheses('( ( ( ) ( ) ) ( ) )') == True)
#     assert(hasBalancedParentheses('( ) )') == False)
#     assert(hasBalancedParentheses('( ) ) (') == False)
#     assert(hasBalancedParentheses('( ( ) ) (') == False)
#     assert(hasBalancedParentheses('(hI!)(Whats up?)(not much)') == True)
#     assert(hasBalancedParentheses('((((hEy!)hi!)))') == True)
#     assert(hasBalancedParentheses('!!!!') == True)

# def main():
#     testHasBalancedParentheses()

# main()

```

## Exercises

### sumOfPowersOf2

Background: The powers of 2 are 1, 2, 4, 8, 16, 32, 64, 128, and so on, where each value is 2 times the previous value. Interestingly, every positive integer can be expressed uniquely as the sum of powers of 2. For example, 21 = 16 + 4 + 1. There is no other sum of powers of 2 that equals 21.

Let's see how we can find this sum given some positive integer n.

1. First find the largest power of 2 that is no larger than n. For 21, this would be 16, since 32 > 21.

2. Next, loop over each power of 2 starting from that largest one, down to 1. So for 21, we would loop over 16, 8, 4, 2, and 1.

3. For each power of 2, include it in the sum so long as the sum does not exceed n. Here is the loop for 21:

- Power of 2	/ Action
- 16	/ Include, so sum = 16
- 8	/ Exclude, because 16+8 = 24, and 24 > 21.
- 4	/ Include, so sum = 16+4 = 20, and 20 <= 21.
- 2	/ Exclude, because 16+4+2 = 22, and 22 > 21.
- 1	/ Include, so sum = 16+4+1 = 21.
In this way, we found that 21 = 16 + 4 + 1.

With this in mind, write the function sumOfPowersOf2(n) which takes a possibly-negative integer n and returns a string that shows how to represent n as a sum of powers of 2. If n is exactly a power of 2, or if n is non-positive, indicate that instead as shown in these test cases:
`def testSumOfPowersOf2():
    assert(sumOfPowersOf2(38) == '38 = 32 + 4 + 2.')
    assert(sumOfPowersOf2(21) == '21 = 16 + 4 + 1.')
    assert(sumOfPowersOf2(16) == '16 is a power of 2.')
    assert(sumOfPowersOf2( 1) == '1 is a power of 2.')
    assert(sumOfPowersOf2( 0) == '0 is not positive.')
    assert(sumOfPowersOf2(-1) == '-1 is not positive.')`

Important notes:
1. We highly recommend that you write the helper function maxPowerOf2UpToN(n). This function takes a positive integer n and returns the largest power of 2 that is no larger than n. For example, maxPowerOf2UpToN(21) returns 16 (not 32 because 32 > 21).



```python
# from cmu_cs3_utils import testFunction

def maxPowerOf2UpToN(n):
    result = 1
    while 2*result <= n:
        result *= 2
    return result

def sumOfPowersOf2(n):
    if n <= 0:
        return f'{n} is not positive.'
    
    powerOf2 = maxPowerOf2UpToN(n)
    if powerOf2 == n:
        return f'{n} is a power of 2.'
    
    sumSoFar = 0
    result = f'{n} = '
    while sumSoFar < n:
        if sumSoFar + powerOf2 <= n:
            sumSoFar += powerOf2
            result += f'{powerOf2} + '
        powerOf2 //= 2
    result = result[:-3]
    result += '.'
    return result

# @testFunction
# def testSumOfPowersOf2():
#     assert(sumOfPowersOf2(38) == '38 = 32 + 4 + 2.')
#     assert(sumOfPowersOf2(21) == '21 = 16 + 4 + 1.')
#     assert(sumOfPowersOf2(16) == '16 is a power of 2.')
#     assert(sumOfPowersOf2( 1) == '1 is a power of 2.')
#     assert(sumOfPowersOf2( 0) == '0 is not positive.')
#     assert(sumOfPowersOf2(-1) == '-1 is not positive.')

# def main():
#     testSumOfPowersOf2()

# main()

```

### isWordLadder

Background: A word ladder is a sequence of words where adjacent words differ by only one letter. For example: 'dog-cog-cot-cat' is a word ladder, because 'dog' and 'cog' differ only at index 0, 'cog' and 'cot' differ only at index 2, and 'cot' and 'cat' differ only at index 1.

To be more precise, we will say that a string s is a word ladder if:
1. s is nonempty and contains at least two words, separated by dashes. Here, a "word" is any collection of characters that are not dashes (so words can include letters, digits, etc).
2. All the words in s are the same length.
3. Each word in s differs from the preceding word by exactly one letter (that is, at only one index).
4. No word appears in s more than once.

With this in mind, write the function isWordLadder(s) which takes a string s and returns True if s is a word ladder as just defined, and False otherwise.

Important hints:
1. You may want to use s.split('-') here to loop over each word in a dash-separated list of words.
2. While there are several ways to solve this, we found it helpful to use a variable allPrevWords that keeps track of every word in the word ladder up to the current word. When we are done checking the current word, we add it to this string, also adding dashes to the string so the words remain dash-separated. For example, during a call to isWordLadder('dog-cog-cot-cat'), after we checked the first 2 words, allPrevWords would then be the string 'dog-cog'.


```python
# from cmu_cs3_utils import testFunction

def isDifferByOneLetter(word, newWord):
    if len(word) != len(newWord):
        return False
    result = False
    count = 0
    for i in range(len(word)):
        if word[i] != newWord[i]:
            count += 1
    if count == 1:
        result = True
    return result

def isWordLadder(s):
    allPrevWords = ''
    # seperate the string to words
    seperateList = s.split('-')
    
    # check one word / no word
    if len(seperateList) <= 1:
        return False
    
    # check repeated words
    for eachWord in seperateList:
        if seperateList.count(eachWord) > 1:
            return False
    
    # check every pair of two words
    word = seperateList[0]
    allPrevWords += word + '-'
    for index in range(len(seperateList) - 1):
        newWord = seperateList[index + 1]
        # if True, add the word and the dash to allPrevWords
        if isDifferByOneLetter(word, newWord) == True:
            allPrevWords += newWord + '-'
        word = newWord
    
    # check is allPrevWords match with the original string
    s += '-'
    if s == allPrevWords:
        return True
    else:
        return False

# @testFunction
# def testIsDifferByOneLetter():
#     assert(isDifferByOneLetter('hey', 'hyy') == True)
#     assert(isDifferByOneLetter('hy', 'hyy') == False)
#     assert(isDifferByOneLetter('heyy', 'hyy') == False)
#     assert(isDifferByOneLetter('hey', 'hey') == False)

# @testFunction
# def testIsWordLadder():
#     assert(isWordLadder('dog-cog-cot-cat') == True)
#     assert(isWordLadder('cat-bat') == True)
#     assert(isWordLadder('cold-cord-card-ward-warm') == True)
#     assert(isWordLadder('toggle-goggle-google') == True)
#     assert(isWordLadder('cold-cord-card-warm') == False)
#     assert(isWordLadder('cat-bat-cat') == False) # duplicate word
#     assert(isWordLadder('cat-bat-') == False)
#     assert(isWordLadder('cat-cats') == False)
#     assert(isWordLadder('cat-cabs') == False)
#     assert(isWordLadder('cat') == False) # just one word
#     assert(isWordLadder('') == False) # no words
#     assert(isWordLadder('-') == False) # no words

# def main():
#     testIsDifferByOneLetter()
#     testIsWordLadder()

# main()

```

### stripComments

Write the function stripComments(code) which takes a multiline string of python code, and returns a new multiline string with the comments removed.

Note: if a line contains a comment, and once that comment is removed the line is either empty or is only whitespace, then ignore the line entirely (do not include it in the result).


```python
# from cmu_cs3_utils import testFunction

def stripComments(code):
    result = ''
    for line in code.splitlines():
        index = line.find('#')
        if index == -1:
            if len(line) != 0:
                result += line
                result += '\n'
        else:
            item = line.split('#')
            if item[0].isspace():
                result = result
            elif len(item[0]) != 0:
                result += item[0]
                result += '\n'
    return result

# @testFunction
# def testStripComments():
#     code = '''\
# # here's a comment!
# def foo(x):
#     return x + 1    # here's another one
# '''
#     result = '''\
# def foo(x):
#     return x + 1    
# '''
#     assert(stripComments(code) == result)

#     code = '''\
# def g(x):
# # Here are some comments
# # which must be removed
# # by stripComments
#     return  x * 7
# '''
#     result = '''\
# def g(x):
#     return  x * 7
# '''
#     assert(stripComments(code) == result)

#     code = """\
# def doIHaveAnyComments():
#     return 'No'
# """
#     result = """\
# def doIHaveAnyComments():
#     return 'No'
# """
#     assert(stripComments(code) == result)

#     code = '''\
# def f(x):
#     #This function returns x + 5
#     return x + 5
# '''
#     result = '''\
# def f(x):
#     return x + 5
# '''
#     assert(stripComments(code) == result)

#     assert(stripComments('') == '')

# def main():
#     testStripComments()

# main()

```

### egyptianMultiplication

Note: This exercise builds on your solution to sumOfPowersOf2(). You should briefly review that exercise before continuing here.

Background: Ancient Egyptians developed a way to multiply two positive integers x and y quickly using only a small number of additions. Their approach relied on the fact that any positive integer x can be uniquely expressed as a sum of powers of 2. For example, to multiply 11*13, they would do this:

Let's use Egyptian Multiplication to compute 11*13 only using addition:

Step 1: Express 11 as a sum of powers of 2:

`11 = 1 + 2 + 8`

Step 2: Express 11*13 as a sum of powers of 2 times 13:

`11*13 = 1*13 + 2*13 + 8*13`

Step 3: Use addition to find the required powers of 2 times 13:

`1*13 = 13
2*13 = 1*13 + 1*13 = 13 + 13 = 26
4*13 = 2*13 + 2*13 = 26 + 26 = 52
8*13 = 4*13 + 4*13 = 52 + 52 = 104`

Step 4: Add these to get our answer:

`1*13 + 2*13 + 8*13 = 13 + 26 + 104 = 143`

So: 11*13 = 143, only using addition!


In this way, we found 11*13 using only 5 total additions. Remarkable!

Note that if x is itself a power of 2, then the process is shortened just a bit. For example, we can multiply 8*13 like so:

Let's use Egyptian Multiplication to compute 8*13 only using addition:

Step 1: Note that 8 is a power of 2

Step 2: (skip this step for powers of 2)

Step 3: Use addition to find the required powers of 2 times 13:

`1*13 = 13
2*13 = 1*13 + 1*13 = 13 + 13 = 26
4*13 = 2*13 + 2*13 = 26 + 26 = 52
8*13 = 4*13 + 4*13 = 52 + 52 = 104`

So: 8*13 = 104, only using addition!

With this in mind, write the function egyptianMultiplication(x, y), which takes two positie integers x and y, and returns a multiline string that performs Egyptian Multiplication just as described.

Important notes:
1. You may not use the builtin Python function eval() here. In general, we do not allow the use of eval() in your code, since its use often leads to bugs and security problems in real-world code.

2. Keep in mind that you should not simply print the output of egyptianMultiplication(). Instead, you should build up a multiline result string which is returned from the function.

3. While you can solve this however you wish, we found it very helpful to first write a helper function which takes the integer x and returns a string representing x as a sum of powers of 2. For example, getSumOfPowersOf2(11) would return '1 + 2 + 8'. Then, we repeatedly used s.split(' + ') to loop over each of the powers of 2 in that sum. If you do this, remember that the values will be strings, so use int() to convert them to ints.


```python
from cmu_cs3_utils import testFunction
import math

def maxPowerOf2UpToN(n):
    result = 1
    while 2*result <= n:
        result *= 2
    return result

def sumOfPowersOf2(n):
    if n <= 0:
        return f'{n} is not positive.'
    
    powerOf2 = maxPowerOf2UpToN(n)
    if powerOf2 == n:
        return f'{n}'
    
    sumSoFar = 0
    result = ''
    while sumSoFar < n:
        if sumSoFar + powerOf2 <= n:
            sumSoFar += powerOf2
            result += f'{powerOf2} + '
        powerOf2 //= 2
    result = result[:-3]
    return result

def egyptianMultiplication(x, y):
    # step 1
    result = '''Let's use Egyptian Multiplication to compute''' 
    result += '\n'
    result += (f'''{x}*{y} only using addition:''')
    result += '\n\n'
    s = sumOfPowersOf2(x).split(' + ')
    # special case
    if len(s) == 1:
        result += f'Step 1: Note that {x} is a power of 2'
        result += '\n\n'
        result += 'Step 2: (skip this step for powers of 2)'
        result += '\n\n'
        
    else:
        result += f'''Step 1: Express {x} as a sum of powers of 2:''' 
        result += '\n\n'
        getSumOfPowersOf2 = ''
        for i in range(1, len(s)+1):
            getSumOfPowersOf2 += f'''{s[-i]} + '''
        getSumOfPowersOf2 = getSumOfPowersOf2[:-3]
        result += (f'{x} = ' + getSumOfPowersOf2 +'\n\n')
    
    # step 2
    if len(s) != 1:
        s = getSumOfPowersOf2.split(' + ')
        result+=f'Step 2: Express {x}*{y} as a sum of powers of 2 times {y}:'
        result += '\n\n'
        sumOfPowersOf2TimesY = ''
        for i in range(len(s)):
            sumOfPowersOf2TimesY += f'''{s[i]}*{y} + '''
        sumOfPowersOf2TimesY = sumOfPowersOf2TimesY[:-3]
        result += (f'{x}*{y}' + ' = ' + sumOfPowersOf2TimesY + '\n\n')
    
    # step 3
    result+=f'Step 3: Use addition to find the required powers of 2 times {y}:'
    result += '\n'
    line2AndAfter = ''
    n = int(math.log(s[-1],2))
    line1 = ('\n' + f'{1}*{y} = {y}' + '\n')
    for i in range(1, n+1):
        line2AndAfter += (f'{2**i}*{y} = {2**(i-1)}*{y} + {2**(i-1)}*{y} =' + 
        f' {2**(i-1)*y} + {2**(i-1)*y} = {2**(i-1)*y + 2**(i-1)*y}' + '\n')
    result += line1 + line2AndAfter + '\n'
        
    # step 4
    # special case
    if len(s) == 1:
        result += f'So: {x}*{y} = {x*y}, only using addition!'
        result += '\n'
    # general case
    else:
        result += 'Step 4: Add these to get our answer:' + '\n'
        result += '\n'
        finalExpression = sumOfPowersOf2TimesY + ' = '
        for i in range(len(s)):
            finalExpression += f'{int(s[i])*y} + '
        finalExpression = finalExpression[:-3]
        finalExpression += ' = ' + f'{x*y}'
        result += finalExpression 
        result += '\n\n'
        
        result += f'So: {x}*{y} = {x*y}, only using addition!'
        result += '\n'
    
    return result

# @testFunction
# def testEgyptianMultiplication():
#     assert(egyptianMultiplication(11, 5) == '''\
# Let's use Egyptian Multiplication to compute
# 11*5 only using addition:

# Step 1: Express 11 as a sum of powers of 2:

# 11 = 1 + 2 + 8

# Step 2: Express 11*5 as a sum of powers of 2 times 5:

# 11*5 = 1*5 + 2*5 + 8*5

# Step 3: Use addition to find the required powers of 2 times 5:

# 1*5 = 5
# 2*5 = 1*5 + 1*5 = 5 + 5 = 10
# 4*5 = 2*5 + 2*5 = 10 + 10 = 20
# 8*5 = 4*5 + 4*5 = 20 + 20 = 40

# Step 4: Add these to get our answer:

# 1*5 + 2*5 + 8*5 = 5 + 10 + 40 = 55

# So: 11*5 = 55, only using addition!
# ''')

#     assert(egyptianMultiplication(5, 11) == '''\
# Let's use Egyptian Multiplication to compute
# 5*11 only using addition:

# Step 1: Express 5 as a sum of powers of 2:

# 5 = 1 + 4

# Step 2: Express 5*11 as a sum of powers of 2 times 11:

# 5*11 = 1*11 + 4*11

# Step 3: Use addition to find the required powers of 2 times 11:

# 1*11 = 11
# 2*11 = 1*11 + 1*11 = 11 + 11 = 22
# 4*11 = 2*11 + 2*11 = 22 + 22 = 44

# Step 4: Add these to get our answer:

# 1*11 + 4*11 = 11 + 44 = 55

# So: 5*11 = 55, only using addition!
# ''')

#     assert(egyptianMultiplication(8, 11) == '''\
# Let's use Egyptian Multiplication to compute
# 8*11 only using addition:

# Step 1: Note that 8 is a power of 2

# Step 2: (skip this step for powers of 2)

# Step 3: Use addition to find the required powers of 2 times 11:

# 1*11 = 11
# 2*11 = 1*11 + 1*11 = 11 + 11 = 22
# 4*11 = 2*11 + 2*11 = 22 + 22 = 44
# 8*11 = 4*11 + 4*11 = 44 + 44 = 88

# So: 8*11 = 88, only using addition!
# ''')

# def main():
#     testEgyptianMultiplication()

# main()

```

### isFencedNumber and nthFencedNumber

Note: You may not use strings when you solve this exercise!

Background: We will say that a number is "fenced" (a coined term) if it is at least 4 digits, contains no zeroes, and the sum of the outer digits (the first and last digits) equals the sum of the inner digits ( all but the first and last digits).

For example, consider 1649. The sum of the outer digits is 1 + 9 == 10, and the sum of the inner digits is 6 + 4 == 0. Since these are equal, 1649 is a fenced number. Here are the first 10 fenced numbers: [1111, 1122, 1133, 1144, 1155, 1166, 1177, 1188, 1199, 1212]

With this in mind, write two functions. First, write isFencedNumber(n) which takes a possibly-negative integer and returns True if it is fenced and False otherwise. Next, write nthFencedNumber(n) which takes a non-negative integer and returns the nth fenced number, starting from 0, so nthFencedNumber(0) returns 1111.


```python
# from cmu_cs3_utils import testFunction

def isFencedNumber(n):
    nStr = str(n)
    if len(nStr) < 4:
        return False
    if '0' in nStr:
        return False
    lastDigit = n % 10
    
    firstDigit = n // (10 ** (len(nStr) - 1))
    sumOfOuterDigits = lastDigit + firstDigit
    
    newNStr = nStr[1:len(nStr) - 1]
    sumOfInnerDigits = 0
    for digit in newNStr:
        digit = int(digit)
        sumOfInnerDigits += digit
    
    if sumOfOuterDigits == sumOfInnerDigits:
        return True
    else:
        return False

def nthFencedNumber(n):
    count = 0
    guess = 0
    while count <= n:
        guess += 1
        if isFencedNumber(guess) == True:
            count += 1
            print(count)
    return guess

# @testFunction
# def testIsFencedNumber():
#     assert(isFencedNumber(1111) == True)
#     assert(isFencedNumber(12348) == True)
#     assert(isFencedNumber(12349) == False)
#     assert(isFencedNumber(2110) == False)  # no zeros allowed
#     assert(isFencedNumber(1201) == False)  # no zeros allowed
#     assert(isFencedNumber(0) == False)     # < 1000
#     assert(isFencedNumber(-1111) == False) # < 1000

# @testFunction
# def testNthFencedNumber():
#     assert(nthFencedNumber(0)  == 1111)
#     assert(nthFencedNumber(1)  == 1122)
#     assert(nthFencedNumber(2)  == 1133)
#     assert(nthFencedNumber(3)  == 1144)
#     assert(nthFencedNumber(9)  == 1212)
#     assert(nthFencedNumber(10) == 1223)

# def main():
#     testIsFencedNumber()
#     testNthFencedNumber()

# main()

```

### getTopScore

Each line starts with a name, followed by 1 or more comma-separated scores. You may assume that each name is unique, and each score is a non-negative integer, and that there is at least one line of data. With this in mind, write the function getTopScore(grades) which takes a string as described, and returns a tuple of the top score and the name of the person who scored it. In the example above, this would be (92, 'Ben'). If more than one person got the top score, list all of them in a single comma-separated string, with the names in the same order they appear in the grades. 

Hint: you may want to use both s.splitlines() and s.split() here.


```python
# from cmu_cs3_utils import testFunction

def getTopScore(grades):
    champScore = ''
    champScorer = ''
    grades = grades.splitlines()
    for line in grades:
        firstCommaIndex = line.find(',')
        currScorer = line[0:firstCommaIndex]
        scores = line[firstCommaIndex + 1:]
        
        currScore = -1
        for score in scores.split(','):
            if int(score) > currScore:
                currScore = int(score)
        
        champScore += f'{currScore}' + ','
        champScorer += currScorer + ','
    
    champScore = champScore[:-1].split(',')
    #print(champScore)
    champScorer = champScorer[:-1].split(',')
    #print(champScorer)
    currScore = -1
    for score in champScore:
        tieChampScoreIndex = ''
        tieChampScorer = ''
        tie = False
        if int(score) == currScore:
            tie = True
            tieChampScoreIndex = champScore.index(f'{currScore}')
            tieChampScorer += champScorer[tieChampScoreIndex] + ','
            print(tieChampScorer)
            
            currScore = int(score)
            tieChampScoreIndex += champScore.index(f'{currScore}')
            tieChampScore = currScore
            print(tieChampScoreIndex)
            tieChampScorer += champScorer[tieChampScoreIndex-1]
            
        
        if int(score) > currScore:
            currScore = int(score)
    # tie
    if tie == True:
        return (tieChampScore, tieChampScorer)
    
    else:
    # not tie
        champScoreIndex = champScore.index(f'{currScore}')
        champScore = currScore
        champScorer = champScorer[champScoreIndex]
        return (champScore, champScorer)

# @testFunction
# def testGetTopScore():
#     grades1 = '''\
# Amy,81,79,91
# Jake,63,82
# Ben,71,77,92,89
# Zoe,90,91'''
#     assert(getTopScore(grades1) == (92, 'Ben'))

#     grades2 = '''\
# Amy,81,79,91
# Jake,63,82
# Ben,71,77,92,89
# Zoe,90,91,92'''
#     assert(getTopScore(grades2) == (92, 'Ben,Zoe'))

# def main():
#     testGetTopScore()

# main()

```

### encode + decode

Background: Here is a simple scheme for encoding a word with a key, both of which you may assume are non-empty and only contain uppercase letters. Say that the word is 'CGXYZ' and the key is 'DAB'. We encode the ith letter in the word using the ith letter in the key. Take the offset of the key character from 'A' and add that to the offset of the word character, wrapping around back to 'A' if you pass 'Z'. If you run out of key letters, just repeat the key as necessary. So, for this example:

- encode 'C' with 'D'
    - since 'D' is 3 past 'A', we shift 'C' by 3 to get 'F'
- encode 'G' with 'A'
    - since 'A' is 0 past 'A', we shift 'G' by 0 to get 'G'
- encode 'X' with 'B'
    - since 'B' is 1 past 'A', we shift 'X' by 1 to get 'Y'
- encode 'Y' with 'D' (we repeated the key)
    - since 'D' is 3 past 'A', we shift 'Y' by 3 with wraparound to get 'B'
- encode 'Z' with 'A'
    - since 'A' is 0 past 'A', we shift 'Z' by 0 to get 'Z'

So we see that when we encode 'CGXYZ' with the key 'DAB' we get 'FGYBZ'. Decoding works the same way in reverse, so when we decode 'FGYBZ' with the key 'DAB' we get the original word 'CGXYZ'. With this in mind, write the function encode(word, key) which takes a word and a key as described above, and returns the encoded word. Also write the function decode(encodedWord, key) which takes the encoded word and the key, and returns the original word.


```python
from cmu_cs3_utils import testFunction

def encode(word, key):
    result = ''
    wordSplit = []
    for char in word:
        wordSplit += char
    indexOfCurrChar = 0
    while len(wordSplit) > 0:
        
        # baseChar = 'a' if char.islower() else 'A'
        # return chr(ord(baseChar) + (ord(char) - ord(baseChar) + shift) % 26)
        
        currChar = wordSplit[0]
        indexOfCurrChar = indexOfCurrChar % len(key)
        baseChar = 'A'
        shift = ord(key[indexOfCurrChar]) - ord(baseChar)
        encodedChar=chr(ord(baseChar)+(ord(currChar) - ord(baseChar)+shift)% 26)
        result += encodedChar
        
        indexOfCurrChar += 1
        wordSplit = wordSplit[1:]
        
    return result

def decode(encodedWord, key):
    result = ''
    indexOfCurrChar = 0
    while len(encodedWord) > 0:
        
        # baseChar = 'a' if char.islower() else 'A'
        # return chr(ord(baseChar) + (ord(char) - ord(baseChar) + shift) % 26)
        
        currChar = encodedWord[0]
        indexOfCurrChar = indexOfCurrChar % len(key)
        baseChar = 'A'
        shift = ord(key[indexOfCurrChar]) - ord(baseChar)
        encodedChar=chr(ord(baseChar)+(ord(currChar) - ord(baseChar)-shift)% 26)
        result += encodedChar
        
        indexOfCurrChar += 1
        encodedWord = encodedWord[1:]

    return result
    
# @testFunction
# def testEncode():
#     assert(encode('CGXYZ', 'DAB') == 'FGYBZ')
#     assert(encode('ABCDZ', 'B')   == 'BCDEA')
#     assert(encode('ABCZ',  'ZZZZZZZ') == 'ZABY')

# @testFunction
# def testDecode():
#     assert(decode('FGYBZ', 'DAB') == 'CGXYZ')
#     assert(decode('BCDEA', 'B')   == 'ABCDZ')
#     assert(decode('ZABY',  'ZZZZZZZ') == 'ABCZ')

# def main():
#     testEncode()
#     testDecode()

# main()

```

### isAddableNumber and nthAddableNumber

Note: You may not use strings when you solve this exercise!

Background: We will say that a positive integer is "addable" (a coined term) if it is at least 1000, and for every three consecutive digits abc in the number, the c is the ones digit of the sum a+b. For example, consider the number 1673. We see:

- We first check 167, and 1+6 is 7, and the ones digit of 7 is 7.
- We next check 673, and 6+7 is 13, and the ones digit of 13 is 3.

We are then out blocks of three consecutive digits, so 1673 is an addable number. Here are the first 10 addable numbers: [1011, 1123, 1235, 1347, 1459, 1561, 1673, 1785, 1897, 1909]

With this in mind, write two functions. First, write isAddableNumber(n) that takes a possibly-negative integer and returns True if it is addable and False otherwise. Next, write nthAddableNumber(n) that takes a non-negative integer and returns the nth addable number, starting from 0, so nthAddableNumber(0) returns 1011. '''


```python
# from cmu_cs3_utils import testFunction
import math

def digitCount(n):
    if n==0:
        return 1
    return 1+math.floor(math.log10(abs(n)))

def isAddableNumber(n):
    originalN = n
    if n < 1000:
        return False
    result = True
    while n > 100:
        firstDigit = int(n // 10 ** (digitCount(n) - 1))
        secondDigit = int((n // 10 ** (digitCount(n) - 2)) % 10)
        thirdDigit = int((n // 10 ** (digitCount(n) - 3)) % 10)
        
        if (firstDigit + secondDigit) % 10 != thirdDigit:
            result = False
            break
        if (firstDigit == thirdDigit and secondDigit != 0) or \
            (secondDigit==thirdDigit and firstDigit != 0):
            result = False
            break
        n %= 10 ** (digitCount(n) - 1)
    
    if 10 <= n <= 99:
        if n % 10 == 0:
            result = False
        
    if (originalN // 100) % 10 == 0:
        if n // 10 != n % 10:
            result = False
    
    return result 
    
def nthAddableNumber(n):
    count = 0
    guess = 1000
    while count <= n:
        guess += 1
        if isAddableNumber(guess) == True:
            count += 1
    return guess

# @testFunction
# def testIsAddableNumber():
#     assert(isAddableNumber(1010) == False)
#     assert(isAddableNumber(1011) == True)
#     assert(isAddableNumber(1012) == False)
#     assert(isAddableNumber(1909) == True)
#     assert(isAddableNumber(1122) == False)
#     assert(isAddableNumber(1908) == False)
#     assert(isAddableNumber(1910) == False)
#     assert(isAddableNumber(12358314) == True)
#     assert(isAddableNumber(112) == False) # < 1000
#     assert(isAddableNumber(0) == False)   # < 1000
#     assert(isAddableNumber(-1011) == False) # < 1000

# @testFunction
# def testNthAddableNumber():
#     assert(nthAddableNumber(0) == 1011)
#     assert(nthAddableNumber(1) == 1123)
#     assert(nthAddableNumber(2) == 1235)
#     assert(nthAddableNumber(3) == 1347)
#     assert(nthAddableNumber(4) == 1459)
#     assert(nthAddableNumber(5) == 1561)
#     assert(nthAddableNumber(6) == 1673)

# def main():
#     testIsAddableNumber()
#     testNthAddableNumber()

# main()

```

### getGameReport


```python
# from cmu_cs3_utils import testFunction

def stripComments(code):
    result = ''
    for line in code.splitlines():
        index = line.find('#')
        if index == -1:
            if len(line) != 0:
                result += line
                result += '\n'
        else:
            item = line.split('#')
            if item[0].isspace():
                result = result
            elif len(item[0]) != 0:
                result += item[0]
                result += '\n'
    return result

def getGameReport(gameData):
    result = ''
    gameData = stripComments(gameData)
    for line in gameData.splitlines():
        roundNumberIndex = line.find(',')
        roundNumber = line[:roundNumberIndex]
        data = line[roundNumberIndex+1:]
        name1 = None
        name2 = None
        score1 = 0
        score2 = 0
        for eachGame in data.split(','):
            nameIndex = eachGame.find(' ')
            name = eachGame[:nameIndex]
            for char in eachGame.split(): 
                if char.isdigit(): 
                    scoreIndex = eachGame.find(char)
                    break
            score = eachGame[scoreIndex:]
            if name1 == None or name1 == name:
                name1 = name
                score1 += int(score)
            if name != name1:
                name2 = name
                score2 += int(score)
        if score1 > score2:
            result += f'{roundNumber}: {name1} won, {score1}-{score2}' + '\n'
        if score1 == score2:
            result += f'{roundNumber}: Tie, {score1}-{score2}' + '\n'
        if score2 > score1:
            result += f'{roundNumber}: {name2} won, {score2}-{score1}' + '\n'
    
    name1 = None
    name2 = None
    finalscore1 = 0
    finalscore2 = 0
    for lines in result.splitlines():
        index = lines.find(' won')
        if index == -1:
            continue
        name = lines[lines.find(': ')+2:lines.find(' won')]
        if name1 == None or name1 == name:
            name1 = name
            finalscore1 += 1
        if name != name1:
            name2 = name
            finalscore2 += 1
    
    if finalscore1 > finalscore2:
        result += f'{name1} won the game, {finalscore1} rounds to {finalscore2}'
    if score2 > score1:
        result += f'{name2} won the game, {finalscore2} rounds to {finalscore1}'
    
    return result 
    
# @testFunction
# def testGetGameReport():
    
#     gameData1 = '''\
# Round 1,Bob scored 3,Bob scored 5,Amy scored 7 # Round 1: Bob won, 8-7
# Round 2,Amy scored 14,Bob scored 3,Amy scored 1 # Round 2: Amy won, 15-3
# Round 3,Amy scored 17,Bob scored 17
# Round 4,Bob scored 7,Amy scored 2,Amy scored 8'''

#     gameReport1 = '''\
# Round 1: Bob won, 8-7
# Round 2: Amy won, 15-3
# Round 3: Tie, 17-17
# Round 4: Amy won, 10-7
# Amy won the game, 2 rounds to 1'''

#     assert(getGameReport(gameData1) == gameReport1)

#     gameData2 = '''\
# Round 1,Joe scored 6,Janet scored 8 # Round 1: Janet won, 8-6
# Round 2,Janet scored 1'''

#     gameReport2 = '''\
# Round 1: Janet won, 8-6
# Round 2: Janet won, 1-0
# Janet won the game, 2 rounds to 0'''

#     assert(getGameReport(gameData2) == gameReport2)

#     gameData3 = '''\
# Round 1,Zoe scored 5 # Round 1: Zoe won, 5-0
# Round 2,Zoe scored 8,Zoe scored 3'''

#     gameReport3 = '''\
# Round 1: Zoe won, 5-0
# Round 2: Zoe won, 11-0
# Zoe won the game, 2 rounds to 0'''

#     assert(getGameReport(gameData3) == gameReport3)

#     gameData4 = '''\
# Round 1,Cal scored 1 # Round 1: Cal won, 1-0
# Round 2,Cal scored 1,Stan scored 1 # Round 2: Tie, 1-1
# Round 3,Stan scored 5,Stan scored 1
# Round 4,Cal scored 1,Stan scored 1,Cal scored 1
# # Cal won the game, 2 rounds to 1'''

#     gameReport4 = '''\
# Round 1: Cal won, 1-0
# Round 2: Tie, 1-1
# Round 3: Stan won, 6-0
# Round 4: Cal won, 2-1
# Cal won the game, 2 rounds to 1'''
#     assert(getGameReport(gameData4) == gameReport4)


# def main():
#     testGetGameReport()

# main()

```
