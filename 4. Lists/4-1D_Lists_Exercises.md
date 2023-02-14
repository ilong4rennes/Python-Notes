## 4.2 1d Lists

### removeEvens (mutating and nonmutating)

Write the function mutatingRemoveEvens(L) which takes a list L, and removes all the even integers from L. This is a mutating function, so it directly changes the provided list. You may assume that L contains only integers. As with most mutating functions, this function returns None.

Also write the function nonmutatingRemoveEvens(L), which works the same as the previous function, only this version is non-mutating. It does not modify L, and it returns a new list without the evens.

Note: You may not simply call mutatingRemoveEvens(L) in nonmutatingRemoveEvens(L). Instead, you need to build up a new list from scratch in the non-mutating version, as we did in the notes.


```python
# from cmu_cs3_utils import testFunction
import copy

def mutatingRemoveEvens(L):
    i = 0
    while i < len(L):
        if L[i] % 2 == 0:
            L.pop(i)
        else:
            i += 1

def nonmutatingRemoveEvens(L):
    M = copy.copy(L)
    mutatingRemoveEvens(M)
    return M

# @testFunction
def testMutatingRemoveEvens():
    L = [1, 2, 3, 4, 5, 6]
    mutatingRemoveEvens(L)
    assert(L == [1, 3, 5])

    L = [9, 13, -7, 17]
    mutatingRemoveEvens(L)
    assert(L == [9, 13, -7, 17])

    L = [0, -8, -12, 6, 18]
    mutatingRemoveEvens(L)
    assert(L == [])

    L = []
    mutatingRemoveEvens(L)
    assert(L == [])

    # Verify that the function is mutating
    assert(mutatingRemoveEvens(L) == None)

# @testFunction
def testNonmutatingRemoveEvens():
    assert(nonmutatingRemoveEvens([1, 2, 3, 4, 5, 6]) == [1, 3, 5])
    assert(nonmutatingRemoveEvens([9, 13, -7, 17]) == [9, 13, -7, 17])
    assert(nonmutatingRemoveEvens([0, -8, -12, 6, 18]) == [])
    assert(nonmutatingRemoveEvens([]) == [])

    # Verify that the function is nonmutating
    L = [1, 2, 3]
    nonmutatingRemoveEvens(L)
    assert(L == [1, 2, 3])

def main():
    testMutatingRemoveEvens()
    testNonmutatingRemoveEvens()

# main()

```

### removeRepeats (mutating and nonmutating)

Write the function mutatingRemoveRepeats(L) which takes a list L, and removes all the repeated integers from L so only the first instance of each of those repeated integers remains. For example, if L = [1, 5, 2, 2, 4, 4, 2], then after a call to mutatingRemoveRepeats(L), then L == [1, 5, 2, 4].

This is a mutating function, so it directly changes the provided list. You may assume that L contains only integers. As with most mutating functions, this function returns None.

Also write the function nonmutatingRemoveRepeats(L), which works the same as the previous function, only this version is non-mutating. It does not modify L, and it returns a new list without any repeated values.

Note: You may not simply call mutatingRemoveRepeats(L) in nonmutatingRemoveRepeats(L). Thus, instead of copying the list L and then mutating that copy to get the answer, you need to build up a new list from scratch, like we did in the notes.


```python
# from cmu_cs3_utils import testFunction

def mutatingRemoveRepeats(L):
    index = 0
    while index < len(L):
        currValue = L[index]
        if index != L.index(currValue):
            L.pop(index)
        else:
            index += 1

def nonmutatingRemoveRepeats(L):
    index = 0
    result = []
    while index < len(L):
        currValue = L[index]
        if index == L.index(currValue):
            result.append(L[index])
        index += 1
    return result

# @testFunction
def testMutatingRemoveRepeats():
    L = [1, 5, 2, 2, 4, 4, 2]
    mutatingRemoveRepeats(L)
    assert(L == [1, 5, 2, 4])

    L = [-2, 15, -2, 3]
    mutatingRemoveRepeats(L)
    assert(L == [-2, 15, 3])

    L = [1, 1, 1]
    mutatingRemoveRepeats(L)
    assert(L == [1])

    L = [1, 9, 5]
    mutatingRemoveRepeats(L)
    assert(L == [1, 9, 5])

    L = []
    mutatingRemoveRepeats(L)
    assert(L == [])

    assert(mutatingRemoveRepeats(L) == None)

# @testFunction
def testNonmutatingRemoveRepeats():
    assert(nonmutatingRemoveRepeats([1, 5, 2, 2, 4, 4, 2]) == [1, 5, 2, 4])
    assert(nonmutatingRemoveRepeats([-2, 15, -2, 3]) == [-2, 15, 3])
    assert(nonmutatingRemoveRepeats([1, 1, 1]) == [1])
    assert(nonmutatingRemoveRepeats([1, 9, 5]) == [1, 9, 5])
    assert(nonmutatingRemoveRepeats([]) == [])

    # Verify that the function is nonmutating:
    L = [1, 2, 2, 3, 4, 4]
    nonmutatingRemoveRepeats(L)
    assert(L == [1, 2, 2, 3, 4, 4])

def main():
    testMutatingRemoveRepeats()
    testNonmutatingRemoveRepeats()

main()

```

### firstNEvenFibonacciNumbers

Background: The Fibonacci numbers are 1, 1, 2, 3, 5, 8, 13, 21, 34,... The first two Fibonacci numbers are both 1. Each Fibonacci number after that is the sum of the two previous Fibonacci numbers.

With this in mind, write the function firstNEvenFibonacciNumbers(n), which takes a non-negative integer n, and returns a list of the first n even Fibonacci numbers in increasing order. For example, firstNEvenFibonacciNumbers(3) returns [2, 8, 34]. Note that your function must run reasonably quickly, so you cannot write nthEvenFibonacciNumber and repeatedly call it.


```python
# from cmu_cs3_utils import testFunction
import math

def isPerfectSquare(n):
    s = int(math.sqrt(n))
    return s*s == n

def isFibonacciNumber(n):
    return isPerfectSquare(5*n**2 + 4) or isPerfectSquare(5*n**2 - 4)
    
def isEven(n):
    return True if n % 2 == 0 else False

def isEvenFibonacciNumbers(n):
    if isFibonacciNumber(n) and isEven(n):
        return True
    return False

def firstNEvenFibonacciNumbers(n):
    result = []
    lastGuess = 1
    secondLastGuess = 1
    count = 0
    while count < n:
        guess = lastGuess + secondLastGuess
        if isEvenFibonacciNumbers(guess):
            result.append(guess)
            count += 1
        lastGuess, secondLastGuess = guess, lastGuess
    return result

# @testFunction
def testFirstNEvenFibonacciNumbers():
    assert(firstNEvenFibonacciNumbers(0) == [])
    assert(firstNEvenFibonacciNumbers(1) == [2])
    assert(firstNEvenFibonacciNumbers(2) == [2, 8])
    assert(firstNEvenFibonacciNumbers(3) == [2, 8, 34])
    assert(firstNEvenFibonacciNumbers(4) == [2, 8, 34, 144])
    assert(firstNEvenFibonacciNumbers(5) == [2, 8, 34, 144, 610])

def main():
    testFirstNEvenFibonacciNumbers()

main()

```

### isNearlySorted

Background: We will say that a list is "nearly-sorted" (a coined term) if it is not sorted, but it requires exactly one swap of two of its values to become sorted from least to greatest. For example, L = [5, 9, 6, 8, 6] is nearly-sorted, since swapping L[1] and L[4] results in the sorted list [5, 6, 6, 8, 9]. However, L = [2, 3, 1] is not nearly-sorted because it requires at least two swaps to put it in sorted order. Also, L = [1, 2, 3] is not nearly-sorted since it is already sorted.

With this in mind, write the function isNearlySorted(L), which takes a list of integers L and returns False if the list is not nearly sorted. If the list is nearly sorted, the function does not return True, but instead returns the list [i, j], where i < j, and swapping the values at indices i and j would make the list sorted.

From the examples above, isNearlySorted([5, 9, 6, 8, 6]) returns [1, 4] and isNearlySorted([1, 2, 3]) returns False.

Note: Your function should be non-mutating.


```python
# from cmu_cs3_utils import testFunction
import copy

def isNearlySorted(L):
    if len(L) < 2:
        return False
    
    sortedL = sorted(L)
    
    position = []
    for i in range(len(L)):
        if L[i] != sortedL[i]:
            position.append(i)
    if len(position) != 2:
        return False
    
    return position
    
# @testFunction
def testIsNearlySorted():
    assert(isNearlySorted([5, 9, 6, 8, 6]) == [1, 4])
    assert(isNearlySorted([2, 3, 1]) == False)
    assert(isNearlySorted([1, 2, 3]) == False)
    assert(isNearlySorted([-12, 5, 0, 13]) == [1, 2])
    assert(isNearlySorted([2, 1]) == [0, 1])
    assert(isNearlySorted([3, 3]) == False)
    assert(isNearlySorted([2]) == False)
    assert(isNearlySorted([]) == False)

    # Verify that the function is non-mutating
    L = [5, 9, 6, 8, 6]
    isNearlySorted(L)
    assert(L == [5, 9, 6, 8, 6])

def main():
    testIsNearlySorted()

main()

```

### repeatingPattern

Background: We will say that a list L includes a repeating pattern if it contains at least 2 values, and there is some list M that is shorter than L, and L equals repeated copies of M.

For example, if L = [1, 2, 1, 2], then L includes the repeating pattern M = [1, 2], because L = M * 2.

It is possible for a list to contain multiple repeating patterns. For example, if L = [1, 2, 1, 2, 1, 2, 1, 2], then M = [1, 2] is a repeating pattern, because L = M * 4. But N = [1, 2, 1, 2] is also a repeating pattern, becuase L = N * 2. In this case, use the shortest such pattern. So we will say that L contains the repeating pattern [1, 2].

With this in mind, write the function repeatingPattern(L), which takes a list L and returns the shortest repeating pattern in L, if there is one. If L does not contain a repeating pattern, return None.

Hints:

If M is the repeating pattern of L, then the length of L must be a multiple of the length of M. For example, if L is of length 6, then the pattern must be of length 1, 2, or 3.
Remember that functions must be non-mutating by default. So the list L cannot be mutated by your function.


```python
# from cmu_cs3_utils import testFunction

def lengthOfPattern(n):
    result = []
    for factor in range(1, len(n), 1):
        if len(n) % factor == 0:
            result.append(factor)
    return result

def repeatingPattern(L):
    if len(L) == 0:
        return None
    for length in lengthOfPattern(L):
        currPattern = L[:length]
        numberOfRepeats = len(L) // length
        repeatedPattern = currPattern * numberOfRepeats
        if repeatedPattern == L:
            return currPattern
    return None
    

# @testFunction
def testRepeatingPattern():
    assert(repeatingPattern([1,2,1,2]) == [1, 2])
    assert(repeatingPattern([1,2,1,2,1,2,1,2])==[1,2])
    assert(repeatingPattern([]) == None)
    assert(repeatingPattern([42]) == None)
    assert(repeatingPattern([1,2]) == None)
    assert(repeatingPattern([1,1]) == [1])
    assert(repeatingPattern([1,2,1]) == None)
    assert(repeatingPattern([1,2,3,1,2,3]) == [1,2,3])
    assert(repeatingPattern([1,2,3,1,2]) == None)
    assert(repeatingPattern([1,2,2,1]) == None)
    L = [1,2,3,4]
    assert(repeatingPattern(L*20) == L)

    # Finally, verify that the function is non-mutating
    L = [1,2,1,2]
    repeatingPattern(L)
    assert(L == [1,2,1,2])

def main():
    testRepeatingPattern()

main()

```

### bowlingScore

Background: When you are bowling, you get 10 frames. In each frame you get 2 throws, where you try to knock down the 10 pins. Your score for that frame is the total number of pins you knocked down in those 2 throws. So if you knock down 3 pins on your first throw, and then 6 more on the second throw, your score in that frame is 3+6, or 9. Your total score is the sum of your score in each frame.

There are some special cases to consider:

1. If you knock down less than 10 pins on your first throw, but then you knock down the rest of the pins on your second throw, this is called a "spare". When you get a spare, your score in that frame also includes your next throw (in the next frame). So if you knock down 3 on your first throw, and 7 on your second throw, that is a spare. So you score 10 plus your next throw. Say your next throw is a 5 (in the next frame). Then your score for the spare is 15.
2. If you knock down all 10 pins on your first throw in a frame, that is called a "strike". In that case, you skip your second throw in the frame, so you only get one throw in that frame. Also, the score for the strike includes the next 2 throws. So if you get a strike, then in the next frame you get 3 on your first throw and 5 on your second throw, then the score for the strike is 10+3+5, or 18. As another example, if you get a strike, followed by another strike, followed by a 3, then the score for the first strike is 10+10+3, or 23.
3. If you get a spare in the last frame (the 10th frame), you get one more throw, and your score for that last spare includes that last throw. However, there is no 11th frame, even though you got that last throw.
4. Similarly, if you get a strike in the last frame, you get two more throws, and your score for that last strike includes both of those throws. Again, though, there is no 11th frame, even though you got both of those last throws.

So we see that the best possible score is if you get a strike in every frame, and then in the last frame you get two extra throws and both of those are strikes, too. In that case, your score is 30 in all 10 frames, so your total score is 300.

With this in mind, write the function bowlingScore(scores) which takes a list of the scores on each throw, and returns the total score for that game.

Remember that when you score a 10, that frame only has 1 throw, except the last frame, as described above.


```python
# from cmu_cs3_utils import testFunction
import copy

def bowlingScore(scores):
    i = 0
    result = 0
    finalScore = 0
    count = 0
    while count < 10:
        count += 1
        if scores[i] == 10:
            result = scores[i] + scores[i+1] + scores[i+2]
            i += 1
        elif scores[i] + scores[i+1] != 10:
            result = scores[i] + scores[i+1]
            i += 2
        elif scores[i] + scores[i+1] == 10:
            result = scores[i] + scores[i+1] + scores[i+2]
            i += 2
        finalScore += result
    return finalScore
        

# @testFunction
def testBowlingScore():
    assert(bowlingScore([10]*12)==300)
    assert(bowlingScore([7,2,8,2,10,7,1,8,2,7,3,10,10,5,4,8,2,7])==162)
    assert(bowlingScore([2,6,2,6,9,1,10,10,10,5,1,4,5,9,0,9,1,6])==147)
    assert(bowlingScore([6,4,2,7,8,1,2,4,6,3,10,6,2,1,9,6,4,10,10,10])==137)
    assert(bowlingScore([8,2,10,10,10,5,4,10,8,0,10,10,3,6])==180)

    # Finally, verify that the function is non-mutating
    L = [7,2,8,2,10,7,1,8,2,7,3,10,10,5,4,8,2,7]
    bowlingScore(L)
    assert(L == [7,2,8,2,10,7,1,8,2,7,3,10,10,5,4,8,2,7])

def main():
    testBowlingScore()

main()

```

### multiplyPolynomials

Background: We can represent a polynomial as a list of its coefficients. For example, we will represent the polynomial 2x3 + 3x2 + 4 with the list [2, 3, 0, 4].

With this in mind, write the function multiplyPolynomials(p1, p2), which takes two lists representing polynomials as described above, and returns the list representing the polynomial that is the product of p1 and p2.

For example, multiplyPolynomials([2, 3, 0, 4], [1, 5]) represents the problem (2x3 + 3x2 + 4)(x + 5). This equals 2x4 + 13x3 + 15x2 + 4x + 20. So the function would return [2, 13, 15, 4, 20].


```python
# from cmu_cs3_utils import testFunction

def multiplyPolynomials(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i+j] += int(p1[i] * p2[j])
    return result

# @testFunction
def testMultiplyPolynomials():
    assert(multiplyPolynomials([2, 3, 0, 4], [1, 5]) == [2, 13, 15, 4, 20])
    assert(multiplyPolynomials([1, 5], [2, 3, 0, 4]) == [2, 13, 15, 4, 20])
    assert(multiplyPolynomials([7, 3], [2, 4]) == [14, 34, 12])
    assert(multiplyPolynomials([-2, -1], [2, 4]) == [-4, -10, -4])
    assert(multiplyPolynomials([3], [5]) == [15])
    assert(multiplyPolynomials([0], [2, 1]) == [0, 0])

def main():
    testMultiplyPolynomials()

main()

```

### singleWildcardMatches

Background: when matching strings, we can use the wildcards '?' or '+'. The wildcard '?' matches any single character. Thus, 'a?b' matches the strings 'axb' and 'a4b' but not 'a12b' and not 'ab'. The wildcard '+' matches one or more characters. Thus, 'a+b' matches the strings 'axb', 'a4b' and 'a12b' but not 'ab' nor 'axbc'.

With this in mind, write the function singleWildcardMatches(pattern, L) that takes a pattern, which is a string with exactly one wildcard ('?' or '+'), and a list L of strings, and returns a sorted list of all the strings in L that match the pattern.

Hint: if a string s matches a pattern p, then s and p will start with the same prefix and end with the same suffix. If that is true, then you can use the lengths of s and p to determine if they are a match.


```python
# from cmu_cs3_utils import testFunction

def singleWildcardMatches(pattern, L):
    result = []
    
    # wildcard is '?'
    wildcardIndex = pattern.find('?')
    if wildcardIndex != -1:
        patternPrefix = str(pattern[:wildcardIndex])
        patternSuffix = str(pattern[wildcardIndex + 1:])
        for element in L:
            prefix = str(element[:wildcardIndex])
            suffix = str(element[wildcardIndex + 1:])
            if prefix == patternPrefix and suffix == patternSuffix:
                result.append(element)
    
    # wildcard is '+'
    if wildcardIndex == -1:
        wildcardIndex = pattern.find('+')
        patternPrefix = str(pattern[:wildcardIndex])
        patternSuffix = str(pattern[wildcardIndex + 1:])
        for element in L:
            if (element.startswith(patternPrefix) and 
                element.endswith(patternSuffix) and
                len(element) >= len(pattern)):
                    result.append(element)
                
    return sorted(result)

# @testFunction
def testSingleWildcardMatches():
    pattern1 = 'a?b'
    L1 = ['ab', 'abb', 'abc', 'acb', '', 'aBb', 'abcb', 'abcd']
    result1 = ['aBb', 'abb', 'acb']
    assert(singleWildcardMatches(pattern1, L1) == result1)

    pattern2 = 'a+b'
    L2 = ['ab', 'abc', 'acb', 'abb', '', 'aBb', 'abcb', 'abcd']
    result2 = ['aBb', 'abb', 'abcb', 'acb']
    assert(singleWildcardMatches(pattern2, L2) == result2)

    pattern3 = 'a+xyz'
    L3 = ['axyz', 'aaxyz', 'aBxyz', 'abaxyz', 'babxyz', 'abxyza']
    result3 = ['aBxyz', 'aaxyz', 'abaxyz']
    assert(singleWildcardMatches(pattern3, L3) == result3)
    
    # Verify that the function is non-mutating
    assert(L3 == ['axyz', 'aaxyz', 'aBxyz', 'abaxyz', 'babxyz', 'abxyza'])

def main():
    testSingleWildcardMatches()

main()

```

### firstNAcceptedValues

Background: This problem includes a list of rules that either require or forbid certain positive integers. For example:

['x must be a multiple of 3']

The first 6 integers that follow this rule are: [3, 6, 9, 12, 15, 18].

We can add a second rule to the list:

['x must be a multiple of 3',
 'x must not be a multiple of 9']
 
The first 6 integers that follow these rules are: [3, 6, 12, 15, 21, 24].

We can add two more rules:

['x must be a multiple of 3',
 'x must not be a multiple of 9',
 'x%2 must be a multiple of 2',
 'x%10 must not be equal to 4']

The first 6 integers that follow these rules are: [6, 12, 30, 42, 48, 60].
The rules will always have 3 parts (always in this order), each with 2 options:

1. 'x' or 'x%N', where N is a positive integer.
2. 'must be' or 'must not be'.
3. 'a multiple of M' or 'equal to M', where M is a non-negative integer.

We will only test your code on valid rules.
With this in mind, first write the helper function isAcceptedValue(x, rules), which takes a positive integer x and a list of rules, and returns True if x follows all the rules and False otherwise.

Next, write the function firstNAcceptedValues(n, rules), which takes a positive integer n and a non-empty list of rules, and returns a list containing the first n positive integers that follow all the given rules.

Hints:

- Because the format is so restricted, you can check for a few specific strings to determine which kind of command each line is.
    - To tell if we are using x or x%n, just check if '%' is anywhere in the rule.
    - To check if the condition is 'must be' or 'must not be', just check if 'not' is anywhere in the rule.
    - To check if the condition is 'a multiple of' or 'equal to', just check if 'equal' is anywhere in the rule.
- Some methods like .split() and .splitlines() return lists, which you now know how to index into.


```python
# from cmu_cs3_utils import testFunction
import copy

def isAcceptedValue(x, rules):
    for rule in rules:
        result = None
        integer = rule[-1]
        if rule.find('%') == -1:
            modifiedX = x
        else:
            factorBeginIndex = rule.find('%') + 1
            factorEndIndex = rule.find(' ')
            factor = rule[factorBeginIndex:factorEndIndex]
            modifiedX = x % int(factor)
            
        # to test multiple or not
        if rule.find('equal') == -1:
            isMultiple = True if rule.find('must not') == -1 else False
            result = True if modifiedX % int(integer) == 0 else False
            if result != isMultiple:
                return False
        
        # to test equal or not
        else:
            isEqual = True if rule.find('must not') == -1 else False
            result = True if int(modifiedX) == int(integer) else False
            if result != isEqual:
                return False
        
    return True

def firstNAcceptedValues(n, rules):
    guess = 0
    count = 1
    result = []
    while count <= n:
        guess += 1
        if isAcceptedValue(guess, rules):
            count += 1
            result.append(guess)
    return result

@testFunction
def testIsAcceptedValue():
    rules = ['x must be a multiple of 3',
             'x must not be a multiple of 9',
             'x%2 must be a multiple of 2',
             'x%10 must not be equal to 4']
    assert(isAcceptedValue(24, rules) == False)
    
    rules = ['x must be a multiple of 3']
    assert(isAcceptedValue(3, rules) == True)
    assert(isAcceptedValue(5, rules) == False)
    assert(isAcceptedValue(9, rules) == True)

    rules = ['x must be a multiple of 3',
             'x must not be a multiple of 9']
    assert(isAcceptedValue(3, rules) == True)
    assert(isAcceptedValue(5, rules) == False)
    assert(isAcceptedValue(9, rules) == False)

    rules = ['x%2 must be a multiple of 2']
    assert(isAcceptedValue(3, rules) == False)
    assert(isAcceptedValue(4, rules) == True)

    rules = ['x%10 must be equal to 9']
    assert(isAcceptedValue(19, rules) == True)
    assert(isAcceptedValue(18, rules) == False)
    

# @testFunction
def testFirstNAcceptedValues():
    rules = ['x must be a multiple of 3']
    assert(firstNAcceptedValues(0, rules) == [])
    assert(firstNAcceptedValues(3, rules) == [3, 6, 9])
    assert(firstNAcceptedValues(6, rules) == [3, 6, 9, 12, 15, 18])

    rules = ['x must be a multiple of 3',
             'x must not be a multiple of 9']
    assert(firstNAcceptedValues(6, rules) == [3, 6, 12, 15, 21, 24])

    rules = ['x must be a multiple of 3',
             'x must not be a multiple of 9',
             'x%2 must be a multiple of 2',
             'x%10 must not be equal to 4']
    assert(firstNAcceptedValues(6, rules) == [6, 12, 30, 42, 48, 60])

    rules = ['x%2 must be equal to 1',
             'x%5 must not be a multiple of 2',
             'x must not be equal to 3']
    assert(firstNAcceptedValues(6, rules) == [1, 11, 13, 21, 23, 31])

    # Verify that the function is non-mutating
    rules = ['x must be a multiple of 3']
    firstNAcceptedValues(6, rules)
    assert(rules == ['x must be a multiple of 3'] )

def main():
    testIsAcceptedValue()
    testFirstNAcceptedValues()

main()

```

### median


```python
# from cmu_cs3_utils import testFunction, almostEqual
import copy

def median(L):
    if len(L) == 0:
        return None
    N = copy.copy(L)
    N.sort()
    if len(N) % 2 == 1:
        return N[len(N) // 2]
    else: 
        return (N[len(N) // 2 - 1] + N[len(N) // 2]) / 2

# @testFunction
def testMedian():
    assert(median([42]) == 42)
    assert(almostEqual(median([1, 2]), 1.5))
    assert(median([-1.7, 3, -2, 4.2, 2]) == 2)
    assert(median([2, 3, 2, 4, 2]) == 2)
    assert(almostEqual(median([2, 3, 2, 4, 2, 3]), 2.5))
    assert(median([]) == None)

    # Verify function is non-mutating
    L = [1, 3, 2]
    assert(median(L) == 2)
    assert(L == [1, 3, 2])


def main():
    testMedian()


# main()

```

### isPalindromicList

Write the non-mutating function isPalindromicList(L) which takes a list L and returns True if it is the same forwards as backwards, and False otherwise.


```python
# from cmu_cs3_utils import testFunction
import copy

def isPalindromicList(L):
    forwards = copy.copy(L)
    backwards = list(reversed(L))
    return True if forwards == backwards else False

# @testFunction
def testIsPalindromicList():
    assert(isPalindromicList([1, 2, 2, 1]) == True)
    assert(isPalindromicList([1, 2, 3, 1]) == False)
    assert(isPalindromicList([1]) == True)
    assert(isPalindromicList([5.0, -1, True, 'hey', True, -1, 5.0]) == True)
    assert(isPalindromicList([0, 'hi', False, False, 4.0]) == False)
    assert(isPalindromicList([]) == True)

    # Verify function is non-mutating
    L = [1, 2, 1]
    assert(isPalindromicList(L) == True)
    assert(L == [1, 2, 1])

    L = [1, 9, 8]
    assert(isPalindromicList(L) == False)
    assert(L == [1, 9, 8])

def main():
    testIsPalindromicList()

main()

```

### reverseList

Write the mutating function reverseList(L) which reverses the list L.

So if L = [2, 3, 4], then after reverseList(L) is called, L == [4, 3, 2]. As is generally true of mutating functions, this function should return None.

Note: You may not use reverse or reversed here.


```python
# from cmu_cs3_utils import testFunction

def reverseList(L):
    if L == []: return None
    length = len(L)
    result = [0] * length
    for i in range(length):
        result[i] = L[-i-1]
    L.extend(result)
    while len(L) > length:
        L.pop(0)
    return L

# @testFunction
def testReverseList():
    L = [2, 3, 4]
    reverseList(L)
    assert(L == [4, 3, 2])

    L = [-1, 5, 2, 0, 9]
    reverseList(L)
    assert(L == [9, 0, 2, 5, -1])

    L = [4.0, 6, 'hi', -1, True]
    reverseList(L)
    assert(L == [True, -1, 'hi', 6, 4.0])

    L = []
    assert(reverseList(L) == None)
    assert(L == [])

def main():
    testReverseList()

main()

```

### isSorted

Write the function isSorted(L) which takes a list L of numbers and returns True if the list is sorted (either smallest-first or largest-first), and False otherwise.

Notes:

- Your function may only use one loop, which may not have more iterations than the length of L.
- You may not use sort, use sorted, or otherwise sort the list.


```python
# from cmu_cs3_utils import testFunction

def isSorted(L):
    if L == []: return True
    isAscending = True if L[0] < L[-1] else False
    
    for i in range(1, len(L)):
        if isAscending:
            if L[i-1] > L[i]: return False
        else:
            if L[i-1] < L[i]: return False
    return True

# @testFunction
def testIsSorted():
    assert(isSorted([1]) == True)
    assert(isSorted([1,1]) == True)
    assert(isSorted([1,2]) == True)
    assert(isSorted([2,1]) == True)
    assert(isSorted([5,2,1,1,0]) == True)
    assert(isSorted([-8,1,1,2.5,3,6]) == True)
    assert(isSorted([1,2,1]) == False)
    assert(isSorted([1,1,2,1]) == False)
    assert(isSorted([]) == True)

def main():
    testIsSorted()

main()

```

### alternatingSum

Write the non-mutating function alternatingSum(L) which takes a list L of integers and returns the alternating sum (where the sign alternates from positive to negative or vice versa).

For example, alternatingSum([5,3,8,-4]) == 5-3+8-(-4). If the list is empty, return 0.


```python
# from cmu_cs3_utils import testFunction

def alternatingSum(L):
    sum = 0
    for i in range(len(L)):
        if i % 2 == 0:
            sum += L[i]
        else:
            sum -= L[i]
    return sum

# @testFunction
def testAlternatingSum():
    assert(alternatingSum([5, 3, 8, -4]) == 5-3+8-(-4))
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([-1, -5]) == (-1)-(-5))
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    assert(alternatingSum([ ]) == 0)

    # Verify function is non-mutating
    L = [1, 2, 3]
    assert(alternatingSum(L) == 1-2+3)
    assert(L == [1, 2, 3])


def main():
    testAlternatingSum()


main()

```

### smallestDifference

Write the function smallestDifference(L) which takes a list L of integers and returns the smallest absolute difference between any two numbers in the list. If the list has fewer than two elements, return -1.

For example, smallestDifference([19, 2, 83, 6, 27]) == 4, since the two closest numbers in the list are 2 and 6, and their difference is 4.


```python
# from cmu_cs3_utils import testFunction

def smallestDifference(L):
    if len(L) <= 1: return -1
    diff = 10**7
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if abs(L[i]-L[j]) < diff:
                diff = abs(L[i]-L[j])
    return diff

# @testFunction
def testSmallestDifference():
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([19,2,83,6,27]) == 4)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([0]) == -1)

def main():
    testSmallestDifference()

main()

```

### vectorSum

Write the function vectorSum(L1, L2) which takes two same-length lists of integers L1 and L2, and returns a new list M where M[i] is the sum of L1[i] and L2[i].

For example, vectorSum([2, 4], [20, 30]) == [22, 34].


```python
# from cmu_cs3_utils import testFunction

def vectorSum(L1, L2):
    length = len(L1)
    result = [0] * length
    for i in range(length):
        result[i] = L1[i] + L2[i]
    return result

# @testFunction
def testVectorSum():
    assert(vectorSum([2, 4], [20, 30]) == [22, 34])
    assert(vectorSum([1, 2, 3], [4, 5, 6]) == [5, 7, 9])
    assert(vectorSum([-1, 4, 99], [2, 0, -500]) == [1, 4, -401])
    assert(vectorSum([], []) == [])

def main():
    testVectorSum()

main()

```

### dotProduct

Background: The dot product of two lists is the sum of the products of corresponding terms. 


```python
# from cmu_cs3_utils import testFunction

def dotProduct(L, M):
    length = min(len(L), len(M))
    sum = 0
    for i in range(length):
        sum += L[i] * M[i]
    return sum

# @testFunction
def testDotProduct():
    assert(dotProduct([1, 2, 3], [4, 5, 6]) == 4+10+18)
    assert(dotProduct([1, 5], [6, 2, 8, 9]) == 6+10)
    assert(dotProduct([2, 10, 9], [-1, 1]) == -2+10)
    assert(dotProduct([], [2, 4, 6]) == 0)
    assert(dotProduct([], []) == 0)
    
    # Verify function is non-mutating
    L = [1, 5, 9]
    M = [7, 1, 2]
    assert(dotProduct(L, M) == 7+5+18)
    assert(L == [1, 5, 9])
    assert(M == [7, 1, 2])

def main():
    testDotProduct()

main()

```

### isRotation


```python
# from cmu_cs3_utils import testFunction
import copy

def isRotation(L, M):
    if len(L) != len(M): return False
    if L == M: return True
    N = copy.copy(L)
    i = 0
    for i in range(len(L)):
        v = N.pop(0)
        N.insert(len(N), v)
        if N == M: 
            return True
    return False

# @testFunction
def testIsRotation():
    assert(isRotation([2, 3, 4, 5, 6], [4, 5, 6, 2, 3]) == True)
    assert(isRotation([2, 3, 4, 5, 6], [2, 3, 4, 5, 6]) == True)
    assert(isRotation([2, 3, 4, 5, 6], [2, 4, 3, 5, 6]) == False)
    assert(isRotation([1], []) == False)
    assert(isRotation([], []) == True)

def main():
    testIsRotation()

main()

```

### rotateList (mutating and nonmutating)


```python
# from cmu_cs3_utils import testFunction
import copy

def mutatingRotateList(L, n):
    if L == []: return []
    isBackwards = True if n > 0 else False
    
    for i in range(abs(n)):
        if isBackwards:
            v = L.pop(-1)
            L.insert(0, v)
        else:
            v = L.pop(0)
            L.insert(len(L), v)

def nonmutatingRotateList(L, n):
    if L == []: return []
    N = copy.copy(L)
    if n > 0: isBackwards = True
    else: isBackwards = False
    
    for i in range(abs(n)):
        if isBackwards:
            v = N.pop(-1)
            N.insert(0, v)
        else:
            v = N.pop(0)
            N.insert(len(N), v)
    return N


# @testFunction
def testMutatingRotateList():
    L = [1, 2, 3, 4]
    mutatingRotateList(L, 1)
    assert(L == [4, 1, 2, 3])

    L = [4, 3, 2, 6, 5]
    mutatingRotateList(L, 2)
    assert(L == [6, 5, 4, 3, 2])

    L = [4, 3, 2, 6, 5]
    mutatingRotateList(L, 7)
    assert(L == [6, 5, 4, 3, 2])

    L = [4, 3, 2, 6, 5]
    mutatingRotateList(L, -7)
    assert(L == [2, 6, 5, 4, 3])

    L = [1, 2, 3]
    mutatingRotateList(L, 0)
    assert(L == [1, 2, 3])
    assert(mutatingRotateList(L, -1) == None)
    assert(L == [2, 3, 1])

    L = []
    mutatingRotateList(L, 2)
    assert(L == [])

# @testFunction
def testNonmutatingRotateList():
    L = [1, 2, 3, 4]
    assert(nonmutatingRotateList(L, 1) == [4, 1, 2, 3])
    assert(L == [1, 2, 3, 4])

    L = [4, 3, 2, 6, 5]
    assert(nonmutatingRotateList(L, 2) == [6, 5, 4, 3, 2])
    assert(nonmutatingRotateList(L, 7) == [6, 5, 4, 3, 2])
    assert(nonmutatingRotateList(L, -7) == [2, 6, 5, 4, 3])
    assert(L == [4, 3, 2, 6, 5])

    L = [1, 2, 3]
    assert(nonmutatingRotateList(L, 0) == [1, 2, 3])
    assert(nonmutatingRotateList(L, -1) == [2, 3, 1])
    assert(L == [1, 2, 3])

    L = []
    assert(nonmutatingRotateList(L, 2) == [])


def main():
    testMutatingRotateList()
    testNonmutatingRotateList()

main()

```

### moveToBack

Write the mutating function moveToBack(L, M) which takes two lists of integers L and M, and modifies L so that each element of L that appears in M moves to the end of L, in the order that they appear in M. The rest of the elements in L should still be present in L, in the same order they were originally. The function should return None.

For example, if L = [2, 3, 3, 4, 1, 5] and M = [2, 3], then after moveToBack(L, M) is called, L == [4, 1, 5, 2, 3, 3].


```python
# from cmu_cs3_utils import testFunction

def moveToBack(L, M):
    for element in M:
        count = 0
        while L.count(element) != 0:
            count += 1
            index = L.index(element)
            L.pop(index)
        for i in range(count):
            L.append(element)

# @testFunction
def testMoveToBack():
    L = [2, 3, 3, 4, 1, 5]
    M = [2, 3]
    moveToBack(L, M)
    assert(L == [4, 1, 5, 2, 3, 3])

    L = [2, 3, 4, 3, 1, 5]
    M = [3]
    moveToBack(L, M)
    assert(L == [2, 4, 1, 5, 3, 3])

    L = [2, 3, 3, 4, 1, 5]
    M = [3, 2]
    moveToBack(L, M)
    assert(L == [4, 1, 5, 3, 3, 2])

    L = [5, 8, 1, 2, 2]
    M = [1, 2]
    moveToBack(L, M)
    assert(L == [5, 8, 1, 2, 2])

    L = []
    M = [1, 2, 3]
    assert(moveToBack(L, M) == None)
    assert(L == [])

def main():
    testMoveToBack()

main()

```

### binaryListToDecimal

Background: Our normal number system, the decimal system, uses base 10. In base 10, numbers can contain the digits 0-9. Also, each place represents a power of 10. For example, the number 101 in base 10 means there is 1 hundred `(10**2), 0 tens (10**1), and 1 one (10**0)`.

A binary number is a number represented in base 2. In base 2, numbers can contain the digits 0 and 1. Each place represents a power of 2, similar to how in base 10, each place represents a power of 10. For example, the number 101 in base 2 means there is 1 four `(2**2), 0 twos (2**1), and 1 one (2**0)`. Thus, 101 in base 2 is equivalent to 5 in base 10 `(1 * 2**2 + 0 * 2**1 + 1 * 2**0)`.


```python
# from cmu_cs3_utils import testFunction

def binaryListToDecimal(L):
    result = 0
    L.reverse()
    for i in range(len(L)):
        result += L[i] * 2 ** i
    return result
    
# @testFunction
def testBinaryListToDecimal():
    assert(binaryListToDecimal([1, 0]) == 2)
    assert(binaryListToDecimal([1, 0, 1, 1]) == 11)
    assert(binaryListToDecimal([1, 1, 0, 1]) == 13)
    assert(binaryListToDecimal([0, 0, 0, 0, 1]) == 1)
    assert(binaryListToDecimal([0]) == 0)
    assert(binaryListToDecimal([]) == 0)

def main():
    testBinaryListToDecimal()

main()

```

### splitString + joinList

Note: You may not use the built-in split function.

Note: You may not use the built-in join function.


```python
# from cmu_cs3_utils import testFunction

def splitString(s, delimiter):
    result = []
    index = 0
    while True:
        index = s.find(delimiter)
        if index == -1: break
        result.append(s[:index])
        s = s[index+1:]
    result.append(s)
    return result

def joinList(L, delimiter):
    result = ''
    for element in L:
        result += element + delimiter
    result = result[:-1]
    return result

# @testFunction
def testSplitString():
    assert(splitString('ab,cd,efg', ',') == ['ab', 'cd', 'efg'])
    assert(splitString('banana', 'n') == ['ba', 'a', 'a'])
    assert(splitString('raspberry', '*') == ['raspberry'])
    assert(splitString('a', 'a') == ['', ''])
    assert(splitString('abc', 'a') == ['', 'bc'])
    assert(splitString('bca', 'a') == ['bc', ''])
    assert(splitString('', '!') == [''])

# @testFunction
def testJoinList():
    assert(joinList(['ab', 'cd', 'efg'], ',') == 'ab,cd,efg')
    assert(joinList(['ba', 'a', 'a'], 'n') == 'banana')
    assert(joinList(['raspberry'], '*') == 'raspberry')
    assert(joinList([], '!') == '')


def main():
    testSplitString()
    testJoinList()

main()

```

### mostAnagrams

Background: An anagram is a word formed by rearranging the letters of another word. For example, 'bop' and 'pob' are anagrams of one another.

With this in mind, write the function mostAnagrams(wordList), which takes a possibly-unsorted list of words (all lowercase), and returns the first word alphabetically from wordList which has the most anagrams of itself in the list. If there are ties, or if there are no anagrams, still return just the first word alphabetically. If the list is empty, return None.




```python
# from cmu_cs3_utils import testFunction
import copy

def isAnagram(word1, word2):
    if len(word1) != len(word2): return False
    for element in word1:
        if word1.count(element) != word2.count(element): return False
    return True

def mostAnagrams(wordList):
    if wordList == []: return None
    champWord = ''
    champCount = 1
    for currWord in wordList:
        count = 0
        for word in wordList:
            if isAnagram(currWord, word):
                count += 1
        if count > champCount:
            champWord = currWord
            champCount = count
        elif count == champCount:
            if currWord < champWord:
                champWord = currWord
            
    if champWord == '':
        wordList.sort()
        return wordList[0]
            
    return champWord
        

# @testFunction
def testMostAnagrams():
    wordList = ['ape', 'pae', 'eap', 'pea', 'bop', 'pob']
    assert(mostAnagrams(wordList) == 'ape')

    wordList = ['hip', 'phi', 'jar', 'raj']
    assert(mostAnagrams(wordList) == 'hip')

    wordList = ['hi', 'my', 'name', 'is', 'bob']
    assert(mostAnagrams(wordList) == 'bob')
    
    assert(mostAnagrams([]) == None)

def main():
    testMostAnagrams()

main()

```

## 4.3 Tuples

### areaOfPolygon

Background: First, read the MathIsFun article here about a method to find the area of a polygon given a list of (x,y) coordinates of its vertices.

With this in mind, write the function areaOfPolygon(L), which takes a list of (x,y) coordinates of vertices that are guaranteed to be in either clockwise or counter-clockwise order around a polygon, and returns the area of that polygon, as described above.


```python
# from cmu_cs3_utils import testFunction, almostEqual

def findTrapezoidArea(x0,y0,x1,y1):
    area = (y0+y1) * (x1-x0) / 2
    return area

def areaOfPolygon(L):
    area = 0
    for i in range(len(L)):
        x1, y1 = L[i]
        x0, y0 = L[i-1]
        area += findTrapezoidArea(x0,y0,x1,y1)
    return abs(area)

# @testFunction
def testAreaOfPolygon():
    assert(almostEqual(areaOfPolygon([(1,1), (4,1), (4,3), (1,3)]), 6))
    assert(almostEqual(areaOfPolygon([(4,10), (9,7), (11,2), (2,2)]), 45.5))
    assert(almostEqual(areaOfPolygon([(9,7), (11,2), (2,2), (4, 10)]), 45.5))
    assert(almostEqual(areaOfPolygon([(0, 0), (0.5,1), (1,0)]), 0.5))
    assert(almostEqual(areaOfPolygon([(-0.5, 10), (0,-11), (0.5,10)]), 10.5))

    # Verify that the function is non-mutating
    L = [(1,1), (4,1), (4,3), (1,3)]
    areaOfPolygon(L)
    assert(L == [(1,1), (4,1), (4,3), (1,3)])

def main():
    testAreaOfPolygon()

# main()

```

### bestTimeToMeet

Background: For this problem, we will find the best time for a group of friends to meet based on their availabilities. Each block of available time will be represented by a tuple of three values: the person's name, followed by the start time and end time when they are available. We will use 24-hour time, so the start and end times are integers from 0-23 inclusive.

For example, ('David', 6, 9) means that David is available from 6am to 9am. Similarly, ('David', 14, 17) means that David is available from 2pm to 5pm.

With this in mind, write the function bestTimeToMeet(availabilities) which takes a list of tuples representing availabilities as described above and returns a tuple with the time the most people are free and the list of people available at that time in alphabetical order. If there is a tie for the time that most people are available, return the later time. You may assume that there is always at least one time when at least one person is available.

For example, say we are given these availabilities:

[('David', 6, 9),
 ('David', 14, 17),
 ('Lauren', 13, 23),
 ('Austin', 11, 18),
 ('Erin', 9, 13)]

Your function should return (16, ['Austin', 'David', 'Lauren']), since:
- There are no times when all four friends can meet.
- The hour from 16-17 is the latest time when three of the four can meet.
- The people free at that time in alphabetical order are Austin, David, and Lauren.


```python
# from cmu_cs3_utils import testFunction

def bestTimeToMeet(availabilities):
    bestResult = []
    bestCount = 0
    for time in range(24):
        count = 0
        result = []
        for name, earlyTime, lateTime in availabilities:
            if earlyTime <= time < lateTime:
                count += 1
                result.append(name)
        if count >= bestCount:
            bestTime = time
            bestResult = result
            bestCount = count
    bestResult.sort()
    return bestTime, bestResult

# @testFunction
def testBestTimeToMeet():
    assert(bestTimeToMeet([('David', 6, 9), ('David', 14, 17),
                           ('Lauren', 13, 23), ('Austin', 11, 18),
                           ('Erin', 9, 13)]) ==
                          (16, ['Austin', 'David', 'Lauren']))
                          
    assert(bestTimeToMeet([('Fred', 11, 12), ('Fred', 15, 16),
                           ('George', 12, 17), ('Bob', 10, 16),
                           ('Carl', 10, 11)]) ==
                           (15, ['Bob', 'Fred', 'George']))

    assert(bestTimeToMeet([('Fred', 10, 14), ('George', 9, 11)]) ==
                          (10, ['Fred', 'George']))

    assert(bestTimeToMeet([('Grace', 9, 10), ('Rocky', 13, 15)]) ==
                          (14, ['Rocky']))

    # Verify that the function is non-mutating
    L = [('David', 6, 9), ('David', 14, 17),
         ('Lauren', 13, 23), ('Austin', 11, 18),
         ('Erin', 9, 13)]
    bestTimeToMeet(L)
    assert(L == [('David', 6, 9), ('David', 14, 17),
                 ('Lauren', 13, 23), ('Austin', 11, 18),
                 ('Erin', 9, 13)])


def main():
    testBestTimeToMeet()

main()

```

### isClique

Background: We will start with a list of tuples that represent pairs of friends, like so:

[('Fred', 'Wilma'),
 ('Barney', 'Fred'),
 ('Wilma', 'Barney')]

We will assume that if Fred is a friend of Wilma, then Wilma is also a friend of Fred. So the list above indicates that:

- Fred and Wilma are friends
- Barney and Fred are friends
- Wilma and Barney are friends

We will say that a list of friends forms a "clique" (a real term in Computer Science) if every person in the list is a friend of every other person in the list. The list of friends above is a clique.


```python
# from cmu_cs3_utils import testFunction

def isClique(friends):
    name = []
    for name1, name2 in friends:
        if name1 not in name:
            name.append(name1)
        if name2 not in name:
            name.append(name2)
    numberOfFriends = len(name)
    numberOfConnections = numberOfFriends * (numberOfFriends - 1) // 2
    if numberOfConnections == len(friends):
        return True
    else: return False

# @testFunction
def testIsClique():
    assert(isClique([ ('Fred', 'Wilma'),
                      ('Barney', 'Fred'),
                      ('Wilma', 'Barney') ]) == True)

    assert(isClique([ ('Fred', 'Wilma'),
                      ('Barney', 'Fred'),
                      ('Wilma', 'Barney'),
                      ('Betty', 'Barney'),
                      ('Wilma', 'Betty') ]) == False)

    assert(isClique([ ('Fred', 'Wilma') ]) == True)

    assert(isClique([ ('Fred', 'Wilma'),
                      ('Betty', 'Barney') ]) == False)

def main():
    testIsClique()

main()

```

### lookAndSay + inverseLookAndSay

Background: When "reading off" the values in a list using the look-and-say method, we describe how many consecutive occurrences of each value there are in the list, in order.

For example, when reading off [3,3,8,-10,-10,-10,3] using the look-and-say method, in order from left-to-right the list contains two 3's, then one 8, then three -10's, then one 3. 


```python
# from cmu_cs3_utils import testFunction

def lookAndSay(L):
    return 42

def inverseLookAndSay(L):
    return 42

# @testFunction
def testLookAndSay():
    assert(lookAndSay([3, 3, 8, -10, -10, -10, 3]) ==
                      [(2, 3), (1, 8), (3, -10), (1, 3)])
    assert(lookAndSay([1, 1, 0, 0, 1, 1, 1]) == [(2, 1), (2, 0), (3, 1)])
    assert(lookAndSay([-5, 5]) == [(1, -5), (1, 5)])
    assert(lookAndSay([6]) == [(1, 6)])
    assert(lookAndSay([]) == [])

    # Verify that the function is non-mutating
    L = [3, 3, 8, -10, -10, -10, 3]
    lookAndSay(L)
    assert(L == [3, 3, 8, -10, -10, -10, 3])

# @testFunction
def testInverseLookAndSay():
    assert(inverseLookAndSay([(2, 3), (1, 8), (3, -10), (1, 3)]) ==
                             [3, 3, 8, -10, -10, -10, 3])
    assert(inverseLookAndSay([(2, 1), (2, 0), (3, 1)]) == [1, 1, 0, 0, 1, 1, 1])
    assert(inverseLookAndSay([(1, -5), (1, 5)]) == [-5, 5])
    assert(inverseLookAndSay([(1, 6)]) == [6])
    assert(inverseLookAndSay([]) == [])

    # Verify that the function is non-mutating
    L = [(2, 3), (1, 8), (3, -10), (1, 3)]
    inverseLookAndSay(L)
    assert(L == [(2, 3), (1, 8), (3, -10), (1, 3)])

def main():
    testLookAndSay()
    testInverseLookAndSay()

# main()

```

### satisfyExpressions

Background: We have seen how the condition in an "if" statement is a boolean expression -- that is, a value that evaluates to True or False.

Here, we will limit ourselves to boolean expressions that use two boolean variables, x and y. So each of x and y can be True or False.

For example:

(x and y)

This is a boolean expression. We will try to "satisfy" the expression. That is, we will find a list of all the values of x and y for which the expression is True. For (x and y), the expression is only True when both x and y are True, which we will represents as:

[(True, True)]

Let's look at another example:

(x or y)

This is True when either x is True, or y is True, or both x and y are True. Thus, the values that satisfy this expression are:

[(True, True), (True, False), (False, True)]

Note that the order of the (x, y) tuples matters. If (True, True) is present, it must be first. Then, (True, False), then (False, True), then (False, False).

Here is another example:

(x or (not y))

This is True when x is True, or y is False (so (not y) is True), or both. That is:

[(True, True), (True, False), (False, False)]

Another example:

((x and (not y)) or ((not x) and y))

This may take a bit of reasoning, but it is only True when exactly one of x and y is True and the other one is False. That is:

[(True, False), (False, True)]

And one last example:

((x and (not x)) and y)

This is never True. Thus, the list of values that satisifes this expression is empty:

[]

With this in mind, write the function satisfyExpression(expr), which takes a string, expr, that is a boolean expression that uses both x and y, and the function returns a (possibly-empty) list of (x,y) values that satisfy that expression.

To do this, we need to be precise about the format of expressions. Basic expressions will always be either just x or y by themselves. Complex expressions are made up of other expressions, and will always be of one of these forms:

- (expr1 and expr2)
- (expr1 or expr2)
- (not expr1)

Note: You may not use the Python builtin functions eval() or exec() here. The point is for you to evaluate the expression yourself.

Hints:

- Write a helper function, satisfiesExpression(expr, x, y), which takes an expression string, as noted above, and True/False values for each of x and y, and returns True if those values for x and y satisfy the expression (that is, make it evaluate to True). For example, satisfiesExpression('(x and y)', True, False) returns False, and satisfiesExpression('(x and y)', True, True) returns True.
- Call that function 4 times, once for each pair of values for x and y. That is, (True, True), (True, False), (False, True), and (False, False). We used two nested loops over the list [True, False] to do this.
- In satisfiesExpression(), we suggest that you first replace x and y in the string with the string 'True' or 'False', depending on their values. Next, repeatedly find a part of the string which is parenthesized, but contains no left parentheses (we will call these "inner parentheses"). This must be of a complex expression of one of these forms:
    - (expr1 and expr2)
    - (expr1 or expr2)
    - (not expr1)
- If you followed this closely, then at this point expr1 and expre2 will each be either the string 'True' or the string 'False'. So replace the whole parenthesized expression with either 'True' or 'False'. Then, keep doing this in a loop until all the parentheses are gone. At that point, you will have a single string, either 'True' or 'False'. Be sure to return a boolean value, not a string. So return True or False, not 'True' or 'False'.
- We also found it helpful to write the function findInnerParens(expr), which returns a tuple (i, j) of the indexes of the left-paren and right-paren for the first inner parentheses in expr.


```python
# from cmu_cs3_utils import testFunction

def findInnerParens(expr):
    end = expr.find(')')
    inner = expr[:end+1]
    while inner.find('(') != -1:
        start = inner.find('(')
        inner = inner[start+1:end+1]
    return '(' + inner

def satisfiesExpression(expr, x, y):
    # 1. replace x and y in the string with the string 'True' or 'False'
    while expr.find('x') != -1: 
        expr = expr.replace('x', f'{x}')
    while expr.find('y') != -1: 
        expr = expr.replace('y', f'{y}')
    
    # 2. repeatedly find innermost parenthesized expression
    while expr.find('(') != -1:
        innerExpression = findInnerParens(expr)
        
        # conjunction 'and'
        index = innerExpression.find('and')
        former = innerExpression[1:index-1]
        latter = innerExpression[index+4:-1]
        if former == 'True' and latter == 'True':
            result = True
        else:
            result = False
        
        # disjunction 'or'
        if index == -1:
            index = innerExpression.find('or')
            former = innerExpression[1:index-1]
            latter = innerExpression[index+3:-1]
            if former == 'True' or latter == 'True':
                result = True
            else: 
                result = False
        
        # negation 'not'
        if index == -1:
            index = innerExpression.find('not')
            latter = innerExpression[index+4:-1]
            if latter == 'True': result = False
            if latter == 'False': result = True
        
        expr = expr.replace(innerExpression, f'{result}')
    return True if expr == 'True' else False

def satisfyExpression(expr):
    result = []
    for x in [True, False]:
        for y in [True, False]:
            if satisfiesExpression(expr, x, y):
                result.append((x, y))
    return result

# @testFunction
def testSatisfyExpression():
    assert(satisfyExpression('(x and y)') ==
        [(True, True)])
    assert(satisfyExpression('(x or y)') ==
        [(True, True), (True, False), (False, True)])
    assert(satisfyExpression('(x or (not y))') ==
        [(True, True), (True, False), (False, False)])
    assert(satisfyExpression('((x and (not y)) or ((not x) and y))') ==
        [(True, False), (False, True)])
    assert(satisfyExpression('((x and (not x)) and y)') ==
        [])
    assert(satisfyExpression('x') ==
        [(True, True), (True, False)])

def main():
    testSatisfyExpression()

main()

```
