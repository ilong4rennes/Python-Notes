### removeRowAndCol (mutating and nonmutating)

Write the function mutatingRemoveRowAndCol(L, targetRow, targetCol) which takes a 2d list L and two integers representing a row and column that will be removed. Your function should mutate the original list to remove the given row and column.

For example, if L is the following list:

[[1,  2,  3,  4],
 [5,  6,  7,  8],
 [9, 10, 11, 12]]
 
Then after calling mutatingRemoveRowAndCol(L, 1, 2), L should be:
[[1,  2,  4],
 [9, 10, 12]]
 
In the example above, row 1 and column 2 are removed from L. As with most mutating functions, this function returns None.
Also write the function nonmutatingRemoveRowAndCol(L, targetRow, targetCol), which works the same as the previous function, only this version is non-mutating. It does not modify L, and it returns a new list with the given row and column removed.

Note: You may not simply call mutatingRemoveRowAndCol(L, targetRow, targetCol) in nonmutatingRemoveRowAndCol(L, targetRow, targetCol). Instead, you need to build up a new list from scratch in the non-mutating version.


```python
# from cmu_cs3_utils import testFunction
import copy

def mutatingRemoveRowAndCol(L, targetRow, targetCol):
    L.pop(targetRow)
    for rowList in L:
        rowList.pop(targetCol)

def nonmutatingRemoveRowAndCol(L, targetRow, targetCol):
    result = []
    for row in range(len(L)):
        if row != targetRow:
            newRow = []
            for col in range(len(L[0])):
                if col != targetCol:
                    newRow.append(L[row][col])
            result.append(newRow)
    return result

# @testFunction
def testMutatingRemoveRowAndCol():
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    mutatingRemoveRowAndCol(L, 1, 2)
    assert(L == [[1,  2,  4],
                 [9, 10, 12]])

    L = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    mutatingRemoveRowAndCol(L, 0, 0)
    assert(L == [[5, 6],
                 [8, 9]])

    L = [[1, 2],
         [3, 4]]
    mutatingRemoveRowAndCol(L, 0, 1)
    assert(L == [[3]])

    L = [[1, 2, 3]]
    mutatingRemoveRowAndCol(L, 0, 1)
    assert(L == [])

# @testFunction
def testNonmutatingRemoveRowAndCol():
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    assert(nonmutatingRemoveRowAndCol(L, 1, 2) == [[1,  2,  4],
                                                   [9, 10, 12]])

    L = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    assert(nonmutatingRemoveRowAndCol(L, 0, 0) == [[5, 6],
                                                   [8, 9]])

    L = [[1, 2],
         [3, 4]]
    assert(nonmutatingRemoveRowAndCol(L, 0, 1) == [[3]])

    L = [[1, 2, 3]]
    assert(nonmutatingRemoveRowAndCol(L, 0, 1) == [])

    # Verify that the function is non-mutating
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    nonmutatingRemoveRowAndCol(L, 1, 2)
    assert(L == [[1,  2,  3,  4],
                 [5,  6,  7,  8],
                 [9, 10, 11, 12]])

def main():
    testMutatingRemoveRowAndCol()
    testNonmutatingRemoveRowAndCol()

main()

```

### isLatinSquare

Background: A list L is a Latin Square if it has the following properties:

1. L is 2d, non-empty, and square (it has the same number of rows and columns).
2. L contains n unique integers, where n is the number of rows (and because L is square, n is also the number of columns).
3. Each of the n integers appears exactly once in each row and exactly once in each column of L. This restriction does not apply to diagonals.

For example, the following list is a Latin Square because it is a square list, and the numbers 1, 5, and 7 appear exactly once in each row and once in each column:

[[5, 7, 1],
 [1, 5, 7],
 [7, 1, 5]]
 
However, the following list is not a Latin Square, because 7 appears twice in column 2:

[[1, 5, 7],
 [5, 1, 7],
 [1, 7, 5]]
 
With this in mind, write the function isLatinSquare(L) which takes a list L, which may or may not be a 2d list, and if it is a 2d list it may or may not be square, and returns True if L is a Latin Square and False otherwise.


```python
# from cmu_cs3_utils import testFunction

def is2D(L):
    for row in range(len(L)):
        if type(L[row]) != list:
            return False
    return True

def isNonEmpty(L):
    return True if L != [] else False
    
def isSquare(L):
    rows, cols = len(L), len(L[0])
    for row in range(rows):
        if len(L[row]) != rows:
            return False
    return True

def haveDuplicates(L):
    for v in L:
        if L.count(v) != 1:
            return True
    return False

def appearOnce(L1, L2):
    return sorted(L1) == sorted(L2)

def isLatinSquare(L):
    if not (is2D(L) and isSquare(L) and isNonEmpty(L)):
        return False
    if haveDuplicates(L):
        return False
    targetList = L[0]
    length = len(L)
    for i in range(length):
        rowList = L[i]
        colList = [L[row][i] for row in range(length)]
        if (not appearOnce(rowList, targetList) or 
            not appearOnce(colList, targetList)):
                return False
    return True
    

# @testFunction
def testIsLatinSquare():
    L = [[5, 7, 1],
         [1, 5, 7],
         [7, 1, 5]]
    assert(isLatinSquare(L) == True)
    # Verify that the function is non-mutating
    assert(L == [[5, 7, 1],
                 [1, 5, 7],
                 [7, 1, 5]])

    L = [[1, 5, 7],
         [5, 1, 7],
         [1, 7, 5]]
    assert(isLatinSquare(L) == False)

    L = [[1, 2, 3],
         [3, 1, 2],
         [4, 3, 1, 2]]
    assert(isLatinSquare(L) == False)

    L = [[0, 1],
         [1, 0]]
    assert(isLatinSquare(L) == True)

    L = [[1, 4],
         [2, 1]]
    assert(isLatinSquare(L) == False)

    L = [1, 2, 3]
    assert(isLatinSquare(L) == False)

    L = [[1]]
    assert(isLatinSquare(L) == True)

def main():
    testIsLatinSquare()

main()

```

### wordSearch

Write the function wordSearch(board, word) which takes a rectangular 2d list board, where each value in the board is a single lowercase letter, and word, which is a string of lowercase letters, and returns True if the given word can be found anywhere on the board -- starting at any location, and heading in any direction -- and False otherwise.

For example, consider this board:

board = [ [ 'd', 'o', 'g' ],
          [ 't', 'a', 'c' ],
          [ 'w', 'a', 't' ],
          [ 'u', 'r', 'b' ] ]
          
We see:
- 'dog' is on the board, starting at (0, 0) and heading to the right.
- 'cat' is on the board, starting at (1, 2) and heading to the left.
- 'bat' is on the board, starting at (3, 2) and heading on a diagonal to the upper-left.
- 'tab' is on the board, starting at (1, 0) and heading on a diagonal to the lower-right.
- 'wag' is on the board, starting at (2, 0) and heading on a diagonal to the upper-right.
- 'cow' is not on the board.
Thus, we have the following for this board:
`assert(wordSearch(board, 'dog') == True)
assert(wordSearch(board, 'cat') == True)
assert(wordSearch(board, 'bat') == True)
assert(wordSearch(board, 'tab') == True)
assert(wordSearch(board, 'wag') == True)
assert(wordSearch(board, 'cow') == False)`


```python
# from cmu_cs3_utils import testFunction

def wordSearch(board, word):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if wordSearchFromCell(board, word, row, col):
                return True
    return False

def wordSearchFromCell(board, word, startRow, startCol):
    rows, cols = len(board), len(board[0])
    for dRow in [-1,0,1]:
        for dCol in [-1,0,1]:
            if not (dRow == 0 and dCol == 0):
                if wordSearchFromCellInDirection(board, word, 
                                                 startRow, startCol,
                                                 dRow, dCol):
                    return True
    return False

def wordSearchFromCellInDirection(board, word, startRow, startCol, dRow, dCol):
    rows, cols = len(board), len(board[0])
    for i in range(len(word)):
        nextRow = startRow + i*dRow
        nextCol = startCol + i*dCol
        if (nextRow < 0 or nextRow >= rows or
            nextCol < 0 or nextCol >= cols or
            board[nextRow][nextCol] != word[i]):
                return False
    return True


# @testFunction
def testWordSearch():
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'w', 'a', 't' ],
              [ 'u', 'r', 'b' ] ]
    assert(wordSearch(board, 'dog') == True)
    assert(wordSearch(board, 'cat') == True)
    assert(wordSearch(board, 'bat') == True)
    assert(wordSearch(board, 'tab') == True)
    assert(wordSearch(board, 'wag') == True)
    assert(wordSearch(board, 'cow') == False)
    assert(wordSearch(board, 'dab') == False)
    assert(wordSearch(board, 'goat') == False)

def main():
    testWordSearch()

main()

```

### betterWordSearch1

Background: This version of wordSearch(board, word) returns more information about each word -- the function returns a string that includes whether the word was found, where the word was found, and in what direction. Here are some examples:

`
board = [ [ 'd', 'o', 'g' ],
          [ 't', 'a', 'c' ],
          [ 'w', 'a', 't' ],
          [ 'u', 'r', 'b' ] ]
assert(wordSearch(board, 'dog') ==
    "'dog' is at (0, 0) heading right")
assert(wordSearch(board, 'cat') ==
    "'cat' is at (1, 2) heading left")
assert(wordSearch(board, 'bat') ==
    "'bat' is at (3, 2) heading up-left")
assert(wordSearch(board, 'tab') ==
    "'tab' is at (1, 0) heading down-right")
assert(wordSearch(board, 'wag') ==
    "'wag' is at (2, 0) heading up-right")
assert(wordSearch(board, 'cow') == "'cow' not found")
assert(wordSearch(board, 'dab') == "'dab' not found")
assert(wordSearch(board, 'goat') == "'goat' not found")
`

If a word occurs more than once on the board, you can choose whichever one you want to return.
With this in mind, write the function wordSearch(board, word), which takes a rectangular 2d list board, where each value in the board is a single lowercase letter, and word, which is a string of lowercase letters, and returns a string as outlined above.

Hint: We found it helpful to put the names of the directions in a 2d list like so:

`
dirNames = [ [ 'up-left'  ,  'up' , 'up-right'   ],
             [ 'left'     ,   ''  , 'right'      ],
             [ 'down-left', 'down', 'down-right' ] ]`


```python
# from cmu_cs3_utils import testFunction

def wordSearch(board, word):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if wordSearchFromCell(board, word, row, col) != False:
                direction, startCell = wordSearchFromCell(board, word, row, col)
                result = f''''{word}' is at {startCell} heading {direction}'''
                return result
            else:
                result = f''''{word}' not found'''
    return result

def wordSearchFromCell(board, word, startRow, startCol):
    for dRow in [-1,0,1]:
        for dCol in [-1,0,1]:
            if wordSearchFromCellInDirection(board, word, 
                                             startRow, startCol, 
                                             dRow, dCol) != False:
                if dRow == -1 and dCol == -1:  direction = 'up-left'
                elif dRow == -1 and dCol == 0: direction = 'up'
                elif dRow == -1 and dCol == 1: direction = 'up-right'
                elif dRow == 0 and dCol == -1: direction = 'left'
                elif dRow == 0 and dCol == 1:  direction = 'right'
                elif dRow == 1 and dCol == -1: direction = 'down-left'
                elif dRow == 1 and dCol == 0:  direction = 'down'
                elif dRow == 1 and dCol == 1:  direction = 'down-right'
                return (direction, wordSearchFromCellInDirection(board, word, 
                                                          startRow, startCol, 
                                                                dRow, dCol))
    return False

def wordSearchFromCellInDirection(board, word, startRow, startCol, dRow, dCol):
    rows, cols = len(board), len(board[0])
    for i in range(len(word)):
        nextRow = startRow +i*dRow
        nextCol = startCol +i*dCol
        if (nextRow < 0 or nextRow >= rows or
            nextCol < 0 or nextCol >= cols or
            board[nextRow][nextCol] != word[i]):
                return False
    return (startRow, startCol)


# @testFunction
def testWordSearch():
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'w', 'a', 't' ],
              [ 'u', 'r', 'b' ] ]
    assert(wordSearch(board, 'dog') == "'dog' is at (0, 0) heading right")
    assert(wordSearch(board, 'cat') == "'cat' is at (1, 2) heading left")
    assert(wordSearch(board, 'bat') == "'bat' is at (3, 2) heading up-left")
    assert(wordSearch(board, 'tab') == "'tab' is at (1, 0) heading down-right")
    assert(wordSearch(board, 'wag') == "'wag' is at (2, 0) heading up-right")
    assert(wordSearch(board, 'cow') == "'cow' not found")
    assert(wordSearch(board, 'dab') == "'dab' not found")
    assert(wordSearch(board, 'goat') == "'goat' not found")

def main():
    testWordSearch()

main()

```

### betterWordSearch2

Background: This version of wordSearch(board, word) builds on betterWordSearch1. Now we also allow for wildcards. In particular, the board and the word can each contain '?' characters, which match any single character. For example, 'c?t' matches 'cat' or 'cot' but not 'cart' or 'act'.

Here is a sample board with wildcards, and some sample words with wildcards:

board = [ [ 'd', '?', 'g' ],
          [ 't', '?', 'c' ],
          [ 'w', 'a', 't' ],
          [ 'u', 'r', 'b' ] ]
          
assert(wordSearch(board, 'dog') == 
    "'dog' is at (0, 0) heading right")
assert(wordSearch(board, 'dig') == 
    "'dig' is at (0, 0) heading right")
assert(wordSearch(board, 'ant') == 
    "'ant' is at (2, 1) heading up")
assert(wordSearch(board, 'cat') == 
    "'cat' is at (1, 2) heading left")
assert(wordSearch(board, 'u?b') == 
    "'u?b' is at (3, 0) heading right")
assert(wordSearch(board, 'wag') == 
    "'wag' is at (2, 0) heading up-right")
assert(wordSearch(board, 'cow') == "'cow' not found")
assert(wordSearch(board, 'dab') == "'dab' not found")
assert(wordSearch(board, 'goat') == "'goat' not found") 

With this in mind, write the function wordSearch(board, word), which takes a rectangular 2d list board, where each value in the board is a single lowercase letter or a wildcard letter, and word, which is a string of lowercase letters possibly containing a wildcard letter, and returns a descriptive string as outlined above.


```python
# from cmu_cs3_utils import testFunction

def wordSearch(board, word):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if wordSearchFromCell(board, word, row, col) != False:
                direction, startCell = wordSearchFromCell(board, word, row, col)
                result = f''''{word}' is at {startCell} heading {direction}'''
                return result
            else:
                result = f''''{word}' not found'''
    return result

def wordSearchFromCell(board, word, startRow, startCol):
    for dRow in [-1,0,1]:
        for dCol in [-1,0,1]:
            if not (dRow == 0 and dCol == 0):
                if wordSearchFromCellInDirection(board, word, 
                                                 startRow, startCol, 
                                                 dRow, dCol) != False:
                    if dRow == -1 and dCol == -1:  direction = 'up-left'
                    elif dRow == -1 and dCol == 0: direction = 'up'
                    elif dRow == -1 and dCol == 1: direction = 'up-right'
                    elif dRow == 0 and dCol == -1: direction = 'left'
                    elif dRow == 0 and dCol == 1:  direction = 'right'
                    elif dRow == 1 and dCol == -1: direction = 'down-left'
                    elif dRow == 1 and dCol == 0:  direction = 'down'
                    elif dRow == 1 and dCol == 1:  direction = 'down-right'
                    return (direction, wordSearchFromCellInDirection(board, 
                                        word, startRow, startCol, dRow, dCol))
    return False

def wordSearchFromCellInDirection(board, word, startRow, startCol, dRow, dCol):
    rows, cols = len(board), len(board[0])
    for i in range(len(word)):
        nextRow = startRow +i*dRow
        nextCol = startCol +i*dCol
        if not (nextRow < 0 or nextRow >= rows or
                nextCol < 0 or nextCol >= cols):
            if (board[nextRow][nextCol] != word[i] and
                board[nextRow][nextCol] != '?' and
                word[i] != '?'):
                    return False
        else: 
            return False
    return (startRow, startCol)


# @testFunction
def testWordSearch():
    board = [ [ 'd', '?', 'g' ],
              [ 't', '?', 'c' ],
              [ 'w', 'a', 't' ],
              [ 'u', 'r', 'b' ] ]
    assert(wordSearch(board, 'dog') == "'dog' is at (0, 0) heading right")
    assert(wordSearch(board, 'dig') == "'dig' is at (0, 0) heading right")
    assert(wordSearch(board, 'ant') == "'ant' is at (2, 1) heading up")
    assert(wordSearch(board, 'cat') == "'cat' is at (1, 2) heading left")
    assert(wordSearch(board, 'u?b') == "'u?b' is at (3, 0) heading right")
    assert(wordSearch(board, 'wag') == "'wag' is at (2, 0) heading up-right")
    assert(wordSearch(board, 'cow') == "'cow' not found")
    assert(wordSearch(board, 'dab') == "'dab' not found")
    assert(wordSearch(board, 'goat') == "'goat' not found")

def main():
    testWordSearch()

main()

```

### betterWordSearch3

Background: This version of wordSearch(board, cell) also builds on betterWordSearch1. Now we allow for wraparound. That is, as we head off the board on one edge, we re-enter the board on the opposite edge.

For example:

board = [ [ 'g', 'd', 'o' ],
          [ 'c', 't', 'a' ],
          [ 'w', 'a', 't' ],
          [ 'r', 'a', 'b' ] ]
The word 'dog' is on this board, because as we head off the board to the right, we re-enter on the left and keep going. Thus:
assert(wordSearch(board, 'dog') ==
    "'dog' is at (0, 1) heading right")
assert(wordSearch(board, 'cat') ==
    "'cat' is at (1, 0) heading left")
assert(wordSearch(board, 'tag') ==
    "'tag' is at (2, 2) heading down-left")
assert(wordSearch(board, 'tact') ==
    "'tact' is at (1, 1) heading right")
assert(wordSearch(board, 'boat') ==
    "'boat' is at (3, 2) heading down")
assert(wordSearch(board, 'tow') == "'tow' not found")

With this in mind, write the function wordSearch(board, word), which takes a rectangular 2d list board, where each value in the board is a single lowercase letter, and word, which is a string of lowercase letters, and returns a string as outlined above.


```python
# from cmu_cs3_utils import testFunction

def wordSearch(board, word):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if wordSearchFromCell(board, word, row, col) != False:
                direction, startCell = wordSearchFromCell(board, word, row, col)
                result = f''''{word}' is at {startCell} heading {direction}'''
                return result
            else:
                result = f''''{word}' not found'''
    return result

def wordSearchFromCell(board, word, startRow, startCol):
    for dRow in [-1,0,1]:
        for dCol in [-1,0,1]:
            if wordSearchFromCellInDirection(board, word, 
                                             startRow, startCol, 
                                             dRow, dCol) != False:
                if dRow == -1 and dCol == -1:  direction = 'up-left'
                elif dRow == -1 and dCol == 0: direction = 'up'
                elif dRow == -1 and dCol == 1: direction = 'up-right'
                elif dRow == 0 and dCol == -1: direction = 'left'
                elif dRow == 0 and dCol == 1:  direction = 'right'
                elif dRow == 1 and dCol == -1: direction = 'down-left'
                elif dRow == 1 and dCol == 0:  direction = 'down'
                elif dRow == 1 and dCol == 1:  direction = 'down-right'
                return (direction, wordSearchFromCellInDirection(board, word, 
                                                          startRow, startCol, 
                                                                dRow, dCol))
    return False

def wordSearchFromCellInDirection(board, word, startRow, startCol, dRow, dCol):
    rows, cols = len(board), len(board[0])
    for i in range(len(word)):
        nextRow = (startRow +i*dRow) % rows
        nextCol = (startCol +i*dCol) % cols
        if (nextRow < 0 or nextRow >= rows or
            nextCol < 0 or nextCol >= cols or
            board[nextRow][nextCol] != word[i]):
                return False
    return (startRow, startCol)
    

# @testFunction
def testWordSearch():
    board = [ [ 'g', 'd', 'o' ],
              [ 'c', 't', 'a' ],
              [ 'w', 'a', 't' ],
              [ 'r', 'a', 'b' ] ]
    assert(wordSearch(board, 'dog') == "'dog' is at (0, 1) heading right")
    assert(wordSearch(board, 'cat') == "'cat' is at (1, 0) heading left")
    assert(wordSearch(board, 'tag') == "'tag' is at (2, 2) heading down-left")
    assert(wordSearch(board, 'tact') == "'tact' is at (1, 1) heading right")
    assert(wordSearch(board, 'boat') == "'boat' is at (3, 2) heading down")
    assert(wordSearch(board, 'tow') == "'tow' not found")

def main():
    testWordSearch()

main()

```

### insertRowAndCol (mutating and nonmutating)

Write the function mutatingInsertRowAndCol(L, row, col, val) which takes a rectangular 2d list L, and inserts one new row and one new column at the locations specified by row and col. The cells in the new row and column are all set to val.

For example, if L is the following list:

[[1,  2,  3,  4],
 [5,  6,  7,  8],
 [9, 10, 11, 12]]
 
Then after calling mutatingInsertRowAndCol(L, 1, 2, 42), L should be equal to:

[[ 1,  2, 42,  3,  4],
 [42, 42, 42, 42, 42],
 [ 5,  6, 42,  7,  8],
 [ 9, 10, 42, 11, 12]]
 
In the example above, a row is inserted at index 1, and a column is inserted at index 2. All the values in the inserted row and column are set to 42. As with most mutating functions, this function returns None.
You are guaranteed that row and col will be valid indexes for L.

Also write the function nonmutatingInsertRowAndCol(L, row, col, val), which works the same as the previous function, only this version is non-mutating. It does not modify L, and it returns a new list with the specified row and column added.

Note: You may not call mutatingInsertRowAndCol(L, row, col, val) in nonmutatingInsertRowAndCol(L, row, col, val). Instead, you need to build up a new list from scratch in the non-mutating version.


```python
# from cmu_cs3_utils import testFunction

def mutatingInsertRowAndCol(L, row, col, val):
    rows, cols = len(L), len(L[0])
    L.insert(row, [val] * cols)
    for row in range(rows+1):
        L[row].insert(col, val)

def nonmutatingInsertRowAndCol(L, rowToAdd, colToAdd, val):
    rows, cols = len(L), len(L[0])
    result = []
    for rowIndex in range(rows):
        newRow = []
        for colIndex in range(cols):
            if colIndex == colToAdd:
                newRow.append(val)
            newRow.append(L[rowIndex][colIndex])
        if colToAdd == cols:
            newRow.append(val)
            
        newCols = len(newRow)
        if rowIndex == rowToAdd:
            result.append([val] * newCols)
        result.append(newRow)
    
    return result 
    
    
# @testFunction
def testMutatingInsertRowAndCol():
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    mutatingInsertRowAndCol(L, 1, 2, 42)
    assert(L == [[ 1,  2, 42,  3,  4],
                 [42, 42, 42, 42, 42],
                 [ 5,  6, 42,  7,  8],
                 [ 9, 10, 42, 11, 12]])

    L = [[1, 2, 3],
         [4, 5, 6]]
    mutatingInsertRowAndCol(L, 0, 0, 5)
    assert(L == [[5, 5, 5, 5],
                 [5, 1, 2, 3],
                 [5, 4, 5, 6]])

    L = [[1, 2, 3],
         [4, 5, 6]]
    mutatingInsertRowAndCol(L, 1, 3, 5)
    assert(L == [[1, 2, 3, 5],
                 [5, 5, 5, 5],
                 [4, 5, 6, 5]])

# @testFunction
def testNonmutatingInsertRowAndCol():
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    assert(nonmutatingInsertRowAndCol(L, 1, 2, 42) == [[ 1,  2, 42,  3,  4],
                                                      [42, 42, 42, 42, 42],
                                                      [ 5,  6, 42,  7,  8],
                                                      [ 9, 10, 42, 11, 12]])

    L = [[1, 2, 3],
         [4, 5, 6]]
    assert(nonmutatingInsertRowAndCol(L, 0, 0, 5) == [[5, 5, 5, 5],
                                                      [5, 1, 2, 3],
                                                      [5, 4, 5, 6]])

    L = [[1, 2, 3],
         [4, 5, 6]]
    assert(nonmutatingInsertRowAndCol(L, 1, 3, 5) == [[1, 2, 3, 5],
                                                      [5, 5, 5, 5],
                                                      [4, 5, 6, 5]])

    # Verify that the function is non-mutating
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    nonmutatingInsertRowAndCol(L, 1, 2, 42)
    assert(L == [[1,  2,  3,  4],
                 [5,  6,  7,  8],
                 [9, 10, 11, 12]])

def main():
    testMutatingInsertRowAndCol()
    testNonmutatingInsertRowAndCol()

main()

```

### makeEdits

Background: Say we have this 2d list M:

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
     
Also, we have this list of strings describing non-mutating edits to make on M:

E = ['swap row 0 and row 1',
     'swap col 1 and col 2',
     'swap row 0 and row 2']
     
To make the first edit, we swap row 0 and row 1 on the original list, to get:

[[4, 5, 6],
 [1, 2, 3],
 [7, 8, 9]]
 
To make the second edit, we swap col 1 and col 2 on that list, to get:

[[4, 6, 5],
 [1, 3, 2],
 [7, 9, 8]]
 
Finally, to make the last edit, we swap row 0 and row 2 on that list, to get:

[[7, 9, 8],
 [1, 3, 2],
 [4, 6, 5]]
 
With this in mind, write the function makeEdits(M, E), which takes a rectangular (but not necessarily square) 2d list M and a 1d list of edits E, and non-mutatingly returns the 2d list that results from making the edits in E on M.

You may assume that all the edits are of the form described above, and always contain legal indexes. Note that the list can be larger than 10x10, so the rows or columns you are supposed to swap are not necessarily one digit numbers.

Hints:

You may want to use s.split().
You may want to use copy.deepcopy(M).


```python
# from cmu_cs3_utils import testFunction
import copy

def makeEdits(M, E):
    R = copy.deepcopy(M)
    for line in E:
        s = line.split()
        swapRow = True if 'row' in s else False
        for element in s:
            if element in '0123456789':
                index1 = int(element)
                break
        index2 = int(s[-1])
        if swapRow:
            R[index1], R[index2] = R[index2], R[index1]
        else: # swap columns
            for rowList in R:
                rowList[index1],rowList[index2]=rowList[index2],rowList[index1]
    return R
    
# @testFunction
# def testMakeEdits():
#      M = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#     E = ['swap row 0 and row 1',
#           'swap col 1 and col 2',
#           'swap row 0 and row 2']
#      R = [[7, 9, 8],
#           [1, 3, 2],
#           [4, 6, 5]]
#     assert(makeEdits(M, E) == R)

#      M = [[1, 2, 3, 4],
#           [5, 6, 7, 8]]
#     E = ['swap row 0 and row 1',
#           'swap row 1 and row 0']
#      R = [[1, 2, 3, 4],
#           [5, 6, 7, 8]]
#     assert(makeEdits(M, E) == R)

#      M = [[1, 2, 3, 4],
#           [5, 6, 7, 8]]
#     E = ['swap col 0 and col 1',
#           'swap row 1 and row 1',
#           'swap col 3 and col 0']
#      R = [[4, 1, 3, 2],
#           [8, 5, 7, 6]]
#     assert(makeEdits(M, E) == R)

#      M = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
#     E = ['swap col 0 and col 10']
#      R = [[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 12]]
#     assert(makeEdits(M, E) == R)

#      # Verify that the function is non-mutating
#     M = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#      E = ['swap row 0 and row 1',
#           'swap col 1 and col 2',
#           'swap row 0 and row 2']
#     makeEdits(M, E)
#      assert(M == [[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]])
#     assert(E == ['swap row 0 and row 1',
#                   'swap col 1 and col 2',
#                   'swap row 0 and row 2'])

# def main():
#     testMakeEdits()

# main()

```

### isKingsTour

Background: In Chess, a King can move one square in any of the 8 possible directions (up, down, left right, and the 4 diagonals).

A King's Tour is a series of legal King moves such that every square in the board is visited exactly once. We can represent a King's Tour as an NxN 2d list where the numbers indicate what order the squares are visited in, going from 1 to N2. So the King starts where the 1 is located, then moves to the 2, then the 3, etc.

For example, this is a valid King's Tour:

[[1, 5, 6],
 [4, 2, 7],
 [3, 8, 9]]
 
However, this is not a valid King's Tour because there is no way for a King to legally move from the 7 to the 8:

[[3, 2, 1],
 [7, 4, 8],
 [6, 5, 9]]
 
Also, this is not a valid King's tour because it contains a 0, which is out of range:

[[3, 2, 1],
 [6, 4, 0],
 [5, 7, 8]]
 
With this in mind, write the function isKingsTour(board), which takes a 2d list of integers, and returns True if it represents a legal King's Tour, and False otherwise. You may assume that the 2d list is square.


```python
# from cmu_cs3_utils import testFunction

def outOfRange(board):
    length = rows = cols = len(board)
    maxNumber = length ** 2
    sum = (1 + maxNumber) * maxNumber // 2
    for row in range(rows):
        for col in range(cols):
            if board[row][col] not in range(1, maxNumber+1):
                return True
            else: 
                sum -= board[row][col]
    return False if sum == 0 else True

def canMoveStep(board, currRow, currCol):
    rows, cols = len(board), len(board[0])
    for nextRow in range(currRow-1, currRow+2):
        for nextCol in range(currCol-1, currCol+2):
            if (nextRow < 0 or nextRow >= rows or 
                nextCol < 0 or nextCol >= cols):
                    continue
            if board[nextRow][nextCol] - board[currRow][currCol] == 1:
                return True
    return False

def isKingsTour(board):
    if outOfRange(board):
        return False
    
    length = rows = cols = len(board)
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == length ** 2:
                continue
            if not canMoveStep(board, row, col):
                return False
    return True

# @testFunction
def testIsKingsTour():
    board = [[1, 5, 6],
             [4, 2, 7],
             [3, 8, 9]]
    assert(isKingsTour(board) == True)

    board = [[3, 2, 1],
             [7, 4, 8],
             [6, 5, 9]]
    assert(isKingsTour(board) == False)

    board = [[3, 2, 1],
             [6, 4, 0],
             [5, 7, 8]]
    assert(isKingsTour(board) == False)

    board = [[ 7,  8,  9, 10],
             [ 6,  3,  2, 11],
             [ 4,  5,  1, 12],
             [16, 15, 14, 13]]
    assert(isKingsTour(board) == True)

def main():
    testIsKingsTour()

main()

```

### matrixMultiply

Background: We can represent a matrix as a rectangular 2d list of integers. We can multiply two matrices using a dot product. A dot product takes two sequences (lists of integers, in this case) of equal length, and combines them to make a single integer. To take the dot product of two lists of size 3, for example, we multiply the values at indexes 0, 1, and 2 of each list and then add them together. We can expand that process for lists of any length.

Consider the following matrices:

[[1, 2, 3],
 [4, 5, 6]]
[[ 7,  8],
 [ 9, 10],
 [11, 12]]
 
To multiply the two matrices, we take the dot product of each row in the first matrix and each column in the second matrix. This value goes into the corresponding row and column of the result matrix.

So, for row 0 and column 0, we get the following:

[1, 2, 3] * [7, 9, 11]
= 1 * 7 + 2 * 9 + 3 * 11
= 7 + 18 + 33
= 58

In our result matrix, the value at (0, 0) is 58. We'll then repeat this for row 0 and column 1:

[1, 2, 3] * [8, 10, 12]
= 1 * 8 + 2 * 10 + 3 * 12
= 8 + 20 + 36
= 64

Row 1 and column 0:

[4, 5, 6] * [7, 9, 11]
= 4 * 7 + 5 * 9 + 6 * 11
= 139

Row 1 and column 1:

[4, 5, 6] * [8, 10, 12]
= 4 * 8 + 5 * 10 + 6 * 12
= 154

Putting those numbers together, our resulting matrix is:

[[ 58,  64],
 [139, 154]]
 
Note that in order to multiply two matrices, the number of columns in the first matrix must equal the number of rows in the second matrix. The resulting matrix will have the same number of rows as the first matrix and the same number of columns as the second matrix.

With this in mind, write the function matrixMultiply(m1, m2), which takes two rectangular 2d lists of integers, and returns their product. If the matrices cannot be multipled, return None.

Hint: It will be useful to start with a 2d list with the correct dimensions and filled with all 0s.


```python
# from cmu_cs3_utils import testFunction

def matrixMultiply(m1, m2):
    if len(m1[0]) == len(m2):
        equalLength = len(m1[0])
        result = []
        for rowList in m1:
            resultRow = []
            for col in range(len(m2[0])):
                ans = 0
                colList = [m2[row][col] for row in range(len(m2))]
                for i in range(equalLength):
                    ans += rowList[i] * colList[i] 
                resultRow.append(ans)
            result.append(resultRow)
        return result

# @testFunction
def testMatrixMultiply():
    m1 = [[1, 2, 3],
          [4, 5, 6]]
    m2 = [[ 7,  8],
          [ 9, 10],
          [11, 12]]
    assert(matrixMultiply(m1, m2) == [[ 58,  64],
                                      [139, 154]])
    m1 = [[-1, 0, 1]]
    m2 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    assert(matrixMultiply(m1, m2) == [[6, 6, 6]])

    m1 = [[1, 2, 3],
          [4, 5, 6]]
    m2 = [[1, 2, 3]]
    assert(matrixMultiply(m1, m2) == None)

def main():
    testMatrixMultiply()

main()

```

### isAlmostMagicSquare

Background: A list L is a magic square if it has the following properties:

1. L is 2d and square (it has the same number of rows and columns).
2. L contains only integers, and no integer appears more than once in L. Note that the integers don't need to be in a specific range.
3. Each row, each column, and each of the 2 diagonals sum to the same total.

For example, the following list is a magic square because it is a square list, and each row, column, and diagonal sums to 21:

[[ 4, 9,  8],
 [11, 7,  3],
 [ 6, 5, 10]]
 
However, the following list is not a magic square because there are numbers which appear more than once in the list:

[[1, 5, 3],
 [5, 3, 1],
 [3, 1, 5]]
 
We will say that a list L is an almost-magic square (a coined term) if it is not a magic square, but swapping two values in L will make it a magic square.

For example, the following list is an almost-magic square because swapping the 5 and the 8 would make it a magic square:

[[ 4, 9,  5],
 [11, 7,  3],
 [ 6, 8, 10]]
 
With this in mind, write the function isAlmostMagicSquare(L), which takes a list L which may or may not be a 2d list, and if it is a 2d list it may or may not be square, and returns True if L is an almost-magic square and False otherwise.

Hint: It will be helpful to write a helper function isMagicSquare(L) which takes a list L and returns True if L is a magic square, and False otherwise.


```python
# from cmu_cs3_utils import testFunction

def is2D(L):
    for rowList in L:
        if type(rowList) != list:
            return False
    return True

def isSquare(L):
    row = len(L)
    for rowList in L:
        col = len(rowList)
        if row != col:
            return False
    return True

def haveDuplicate(L):
    length = rows = cols = len(L)
    for row in range(rows):
        for col in range(cols):
            for altRow in range(rows):
                for altCol in range(cols):
                    if row == altRow and col == altCol:
                        continue
                    if L[row][col] == L[altRow][altCol]:
                        return True
    return False

def isMagicSquare(L):
    if not isSquare(L): 
        return False
    length = rows = cols = len(L)
    total = sum(L[0])
    rowTotal = 0
    colTotal = 0
    leftDiagonalTotal = 0
    rightDiagonalTotal = 0
    
    # test for col
    for col in range(cols):
        for row in range(rows):
            colTotal += L[row][col]
        if colTotal != total:
            return False
        colTotal = 0
    
    # test for row
    for rowList in L:
        rowTotal = sum(rowList)
        if rowTotal != total:
            return False
        rowTotal = 0
    
    # test for diagonal 
    for index in range(length):
        leftDiagonalTotal += L[index][index]
        rightDiagonalTotal += L[index][length-1-index]
    if leftDiagonalTotal != total or rightDiagonalTotal != total: 
        return False
    return True
    
def isAlmostMagicSquare(L):
    if not is2D(L) or not isSquare(L):
        return False
        
    if haveDuplicate(L):
        return False
        
    if isMagicSquare(L):
        return False
        
    # Check if swapping two values make it a magic square
    length = rows = cols = len(L)
    for row in range(rows):
        for col in range(cols):
            for altR in range(rows):
                for altC in range(cols):
                    if row == altR and col == altC:
                        continue
                    L[row][col],L[altR][altC]=L[altR][altC],L[row][col]
                    if isMagicSquare(L):
                        return True
                    else: 
                        L[row][col],L[altR][altC]=L[altR][altC],L[row][col]
    return False

# @testFunction
def testIsAlmostMagicSquare():
    # Swapping the 5 and 8 make this a magic square
    L = [[ 4, 9,  5],
         [11, 7,  3],
         [ 6, 8, 10]]
    assert(isAlmostMagicSquare(L) == True)

    # Swapping the 7 and 13 make this a magic square
    L = [[ 4, 14, 15,  1],
         [ 9, 13,  6, 12],
         [ 5, 11, 10,  8],
         [16,  2,  3,  7]]
    assert(isAlmostMagicSquare(L) == True)

    # This is a magic square, so it's not an almost-magic square
    L = [[ 4, 9,  8],
         [11, 7,  3],
         [ 6, 5, 10]]
    assert(isAlmostMagicSquare(L) == False)

    # Almost-magic squares can't have duplicates
    L = [[1, 5, 3],
         [5, 3, 5],
         [3, 1, 1]]
    assert(isAlmostMagicSquare(L) == False)

    # Not square
    L = [[1, 2, 3],
         [4, 5]]
    assert(isAlmostMagicSquare(L) == False)

    # Not a 2d list
    L = [1, 2, 3]
    assert(isAlmostMagicSquare(L) == False)

def main():
    testIsAlmostMagicSquare()

main()

```

### hasNoPrimes

Write the function hasNoPrimes(L) which takes a 2d list L of integers, and returns True if L does not contain any primes, and False otherwise.


```python
# from cmu_cs3_utils import testFunction, rounded

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maxFactor = rounded(n ** 0.5)
    for i in range(3, maxFactor + 1, 2):
        if n % i == 0:
            return False
    return True

def hasNoPrimes(L):
    rows, cols = len(L), len(L[0])
    for row in range(rows):
        for col in range(cols):
            if isPrime(L[row][col]):
                return False
    return True

# @testFunction
def testHasNoPrimes():
    L = [[4, 6, 8], 
         [12, 9, 14]]
    assert(hasNoPrimes(L) == True)
    assert(hasNoPrimes([[10, 16, 20]]) == True)
    L = [[3, 6, 9], 
         [8, 22, 4]]
    assert(hasNoPrimes(L) == False)
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    assert(hasNoPrimes(L) == False)
    assert(hasNoPrimes([[21, 33, 85], [4, 76, 14], [55, 48, 16], 
        [18, 51, 60], [9, 22, 20]]) == True)

def main():
    testHasNoPrimes()

# main()

```

### isRectangular

Background: We say a 2d list is rectangular if every row is the same length. For example, a 2d list with 3 rows that each have 2 elements is rectangular.

With this in mind, write the function isRectangular(L) which takes a possibly-2d (or possibly not) list L and returns True if the list is 2d and also rectangular. Return False otherwise.


```python
# from cmu_cs3_utils import testFunction

def is2D(L):
    rows = len(L)
    for row in range(rows):
        if type(L[row]) != list:
            return False
    return True

def isRectangular(L):
    if not is2D(L): return False
    rows, cols = len(L), len(L[0])
    for row in range(rows):
        if len(L[row]) != cols:
            return False
    return True

# @testFunction
def testIsRectangular():
    L = [[1, 2, 3], 
         [4, 5, 6]]
    assert(isRectangular(L) == True)
    L = [[1, 2], 
         [4, 5, 6]]
    assert(isRectangular(L) == False)
    L = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    assert(isRectangular(L) == True)
    assert(isRectangular([1, 2, 3]) == False)
    assert(isRectangular([[1], 2]) == False)

def main():
    testIsRectangular()

main()

```

### hasDuplicates

Write the function hasDuplicates(L) which takes a 2d list L of integers, and returns True if L contains any duplicate values (that is, if any two values in L are equal to each other), and False otherwise.


```python
# from cmu_cs3_utils import testFunction

def is2D(L):
    rows = len(L)
    for row in range(rows):
        if type(L[row]) != list:
            return False
    return True

def hasDuplicates(L):
    if not is2D(L): return False
    rows, cols = len(L), len(L[0])
    for row in range(rows):
        for col in range(cols):
            currNum = L[row][col]
            for checkRow in range(rows):
                for checkCol in range(cols):
                    if row == checkRow and col == checkCol: 
                        continue
                    else:
                        checkNum = L[checkRow][checkCol]
                        if currNum == checkNum:
                            return True
    return False

# @testFunction
def testHasDuplicates():
    L = [[1, 2, 3],
         [9, 3, 4]]
    assert(hasDuplicates(L) == True)
    L = [[3, 3],
         [0, 6]]
    assert(hasDuplicates(L) == True)
    L = [[5, 9, 1],
         [7, 6, 8]]
    assert(hasDuplicates(L) == False)
    L = [[2, 1],
         [0, 4]]
    assert(hasDuplicates(L) == False)

def main():
    testHasDuplicates()

main()

```

### isKnightsTour

Background: Knights in chess move in “L” shapes. One move consists of 2 squares in one direction and 1 square in another direction. For example, a knight could move 1 square right and 2 squares up, or 1 square down and 2 squares left, etc.

A "knight's tour" is a sequence of legal knight moves such that the knight visits every square exactly once. We will represent a possible knight's tour as an NxN list of the integers from 1 to N2 listing the positions in order that the knight occupied on the tour. If it is a legal knight's tour, then all the numbers from 1 to N2 will be included.

With this in mind, write the function isKnightsTour(board) which takes a 2d list of integers and returns True if it represents a legal knight's tour, and False otherwise.

For example, below is a legal 5x5 knight's tour as the 2d list includes every number from 1 to 52 (25), where each of the moves from 1 to 25 is a legal knight move.

[[1, 6, 15, 10, 21], 
[14, 9, 20, 5, 16], 
[19, 2, 7, 22, 11], 
[8, 13, 24, 17, 4], 
[25, 18, 3, 12, 23]]


```python
# from cmu_cs3_utils import testFunction

def isSquare(board):
    rows, cols = len(board), len(board[0])
    return rows == cols

def isValidValue(board):
    rows, cols = len(board), len(board[0])
    sideLength = len(board)
    largestNum = sideLength ** 2
    sum = (1 + largestNum) * largestNum // 2
    for row in range(rows):
        for col in range(cols):
            sum -= board[row][col]
    return sum == 0

def canMoveStep(row, col, board):
    rows, cols = len(board), len(board[0])
    sideLength = len(board)
    largestNum = sideLength ** 2
    for nextRow in [row-2, row+2]:
        for nextCol in [col-1, col+1]:
            if (nextRow < 0 or nextRow >= rows or
                nextCol < 0 or nextCol >= cols):
                    continue
            if board[row][col] + 1 == board[nextRow][nextCol]:
                return True
                        
    for nextRow in [row-1, row+1]:
        for nextCol in [col-2, col+2]:
            if (nextRow < 0 or nextRow >= rows or
                nextCol < 0 or nextCol >= cols):
                    continue
            if board[row][col] + 1 == board[nextRow][nextCol]:
                return True
    return False

def isKnightsTour(board):
    if not isValidValue(board):
        return False
    
    rows, cols = len(board), len(board[0])
    sideLength = len(board)
    largestNum = sideLength ** 2
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == largestNum:
                continue
            if not canMoveStep(row, col, board):
                return False
    return True

# @testFunction
def testIsKnightsTour():
    board = [[1, 6, 15, 10, 21], 
             [14, 9, 20, 5, 16], 
             [19, 2, 7, 22, 11], 
             [8, 13, 24, 17, 4], 
             [25, 18, 3, 12, 23]]
    assert(isKnightsTour(board) == True)

    board1 = [[1, 30, 33, 22, 25, 12], 
              [34, 21, 26, 13, 32, 23], 
              [29, 2, 31, 24, 11, 14],
              [20, 35, 18, 27, 8, 5], 
              [17, 28, 3, 6, 15, 10], 
              [36, 19, 16, 9, 4, 7]]
    assert(isKnightsTour(board1) == True)

    board2 = [[2, 5, 9], 
              [7, 8, 3], 
              [4, 1, 6]]
    assert(isKnightsTour(board2) == False)

    board3 = [[2, 5, 0], 
              [7, 0, 3], 
              [4, 1, 6]]
    assert(isKnightsTour(board3) == False)

    board4 = [[1, 4, 7, 10], 
              [12, 9, 2, 5], 
              [3, 6, 11, 8]]
    assert(isKnightsTour(board4) == False)

def main():
    testIsKnightsTour()

main()

```

### isLegalSudoku


```python
# from cmu_cs3_utils import testFunction, rounded
import copy

def isLegal(L):
    seen = []
    for value in L:
        if type(value) != int:
            return False
        
        if value < 0 or value > len(L):
            return False
        
        if value != 0 and value in seen:
            return False
        
        seen.append(value)
    return True

def isLegalRow(grid, row):
    return isLegal(grid[row])

def isLegalCol(grid, col):
    rows, cols = len(grid), len(grid[0])
    colList = []
    for row in range(rows):
        colList.append(grid[row][col])
    return isLegal(colList)

def isLegalBlock(grid, block):
    n = len(grid)
    blockSize = round(n**0.5)
    startRow = block // blockSize * blockSize
    startCol = block % blockSize * blockSize
    value = []
    for drow in range(blockSize):
        for dcol in range(blockSize):
            row, col = startRow + drow, startCol + dcol
            value.append(grid[row][col])
    return isLegal(value)


def isLegalSudoku(grid):
    rows, cols = len(grid), len(grid[0])
    if (rows != 4) and (rows != 9):
        return False
    if rows != cols:
        return False
    
    for row in range(rows):
        if not isLegalRow(grid, row):
            return False
    
    for col in range(cols):
        if not isLegalCol(grid, col):
            return False
    
    blocks = rows # or cols
    for block in range(blocks):
        if not isLegalBlock(grid, block):
            return False
    
    return True

# @testFunction
def testIsLegalSudoku():
    okGrid1 = [
     [ 3, 0, 4, 0 ],
     [ 0, 1, 0, 2 ],
     [ 0, 4, 0, 3 ],
     [ 2, 0, 1, 0 ]
    ]

    okGrid2 = [
     [ 3, 2, 4, 1 ],
     [ 4, 1, 3, 2 ],
     [ 1, 4, 2, 3 ],
     [ 2, 3, 1, 4 ]
    ]

    badGrid1 = copy.deepcopy(okGrid1)
    badGrid1[3][3] = 1

    badGrid2 = copy.deepcopy(okGrid2)
    badGrid2[2][2] = 4

    # not 4x4 or 9x9
    badGrid3 = [
     [ 3, 0, 4, 0 ],
     [ 0, 1, 0, 2 ],
     [ 0, 4, 0, 3 ]
    ]

    # contains an integer that is out of range (5)
    badGrid4 = [
     [ 3, 0, 4, 0 ],
     [ 0, 1, 0, 2 ],
     [ 0, 4, 0, 3 ],
     [ 2, 0, 1, 5 ]
    ]

    # contains a non-integer
    badGrid5 = [
     [ 3, 0, 4, 0 ],
     [ 0, 1, 0, 2 ],
     [ 0, 4, 0, 3 ],
     [ 2, 0, 1, 'do not crash!' ]
    ]

    assert(isLegalSudoku(okGrid1) == True)
    assert(isLegalSudoku(okGrid2) == True)
    assert(isLegalSudoku(badGrid1) == False)
    assert(isLegalSudoku(badGrid2) == False)
    assert(isLegalSudoku(badGrid3) == False)
    assert(isLegalSudoku(badGrid4) == False)
    assert(isLegalSudoku(badGrid5) == False)

    # now test 9x9 boards
    okGrid3 = [
     [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
     [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
     [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
     [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
     [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
     [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
     [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
     [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
     [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
    ]

    badGrid6 = copy.deepcopy(okGrid3)
    badGrid6[0][0] = 7

    assert(isLegalSudoku(okGrid3) == True)
    assert(isLegalSudoku(badGrid6) == False)

def main():
    testIsLegalSudoku()

main()

```

### samePolygons

Background: We can represent a polygon as a list of points -- that is, (x,y) tuples -- that are guaranteed to be either in clockwise or counter-clockwise order. For example, [(0, 0), (1, 1), (2, 0), (1, -1)].

Note that the same polygon can be represented in multiple ways. The previous example can start from any of the points. So these are all the same polygon:

[(0, 0), (1, 1), (2, 0), (1, -1)]
[(1, 1), (2, 0), (1, -1), (0, 0)]
[(2, 0), (1, -1), (0, 0), (1, 1)]
[(1, -1), (0, 0), (1, 1), (2, 0)]

Also, those point lists are all in clockwise order. The same polygon can be listed in counter-clockwise order. So these are also all the same polygon:

[(0, 0), (1, -1), (2, 0), (1, 1)]
[(1, -1), (2, 0), (1, 1), (0, 0)]
[(2, 0), (1, 1), (0, 0), (1, -1)]
[(1, 1), (0, 0), (1, -1), (2, 0)]

Importantly, order still matters, and the list must match in either clockwise or counter-clockwise order. Thus, the following is not the same polygon, even though it contains the same points:

[(0, 0), (2, 0), (1, -1), (1, 1)]

Finally, you should ignore duplicated points -- that is, where the same point occurs consecutively in the list, you should only use the first such point. This is also the case when a point is repeated at the beginning and the end of the list, since the points are still consecutive. Thus, the following are also all the same polygon:

[(0, 0), (1, 1), (2, 0), (1, -1)]
[(0, 0), (0, 0), (1, 1), (2, 0), (1, -1)]
[(0, 0), (1, 1), (2, 0), (1, -1), (0, 0)]

With this in mind, write the function samePolygons(p1, p2) which takes two polygons (that is, lists of (x,y) points) and returns True if they are the same polygon, and False otherwise.

Note: You may assume that both polygons have at least 3 unique points in them.


```python
# from cmu_cs3_utils import testFunction
import copy

def clockwiseRotate(p1, p2, i):
    p2 = copy.deepcopy(p2)
    if p1 == p2:
        return True
    for rotateTime in range(i):
        v = p2.pop(0)
        p2.append(v)
        if p1 == p2:
            return True
    return False

def counterclockwiseRotate(p1, p2, i):
    p2 = copy.deepcopy(p2)
    p2.reverse()
    if p1 == p2:
        return True
    for rotateTime in range(i):
        v = p2.pop()
        p2.insert(0, v)
        if p1 == p2:
            return True
    return False

def samePolygons(p1, p2):
    for value in p1:
        if p1.count(value) > 1:
            p1.remove(value)
    for value in p2:
        if p2.count(value) > 1:
            p2.remove(value)
    for i in range(len(p1)):
        if (clockwiseRotate(p1, p2, i) or 
            counterclockwiseRotate(p1, p2, i)):
            return True
    return False

# @testFunction
def testSamePolygons():
    # Test polygon against itself:
    assert(samePolygons([(0, 0), (1, 1), (2, 0), (1, -1)],
                        [(0, 0), (1, 1), (2, 0), (1, -1)]) == True)
    # Test against polygons formed from clockwise rotations of points:
    assert(samePolygons([(0, 0), (1, 1), (2, 0), (1, -1)],
                        [(1, 1), (2, 0), (1, -1), (0, 0)]) == True)
    assert(samePolygons([(0, 0), (1, 1), (2, 0), (1, -1)],
                        [(2, 0), (1, -1), (0, 0), (1, 1)]) == True)
    # Test against polygons formed from counter-clockwise rotations of points:
    assert(samePolygons([(0, 0), (1, 1), (2, 0), (1, -1)],
                        [(0, 0), (1, -1), (2, 0), (1, 1)]) == True)
    assert(samePolygons([(0, 0), (1, 1), (2, 0), (1, -1)],
                        [(1, -1), (2, 0), (1, 1), (0, 0)]) == True)
    # Test polygon against mixed-up points (not rotations):
    assert(samePolygons([(0, 0), (1, 1), (2, 0), (1, -1)],
                        [(0, 0), (2, 0), (1, 1), (1, -1)]) == False)
    assert(samePolygons([(0, 0), (1, 1), (2, 0), (1, -1)],
                        [(0, 0), (2, 0), (1, -1), (1, 1)]) == False)
    # Test polygon against polygons with wrong # of points:
    assert(samePolygons([(0, 0), (1, 1), (2, 0), (1, -1)],
                        [(0, 0), (1, 1), (2, 0)]) == False)
    # Test polygon against same polygon with duplicated points:
    assert(samePolygons([(0, 0), (0, 0), (1, 1), (2, 0), (1, -1)],
                        [(0, 0), (1, 1), (2, 0), (1, -1)]) == True)
    assert(samePolygons([(0, 0), (1, 1), (2, 0), (1, -1)],
                        [(0, 0), (1, 1), (2, 0), (1, -1), (0, 0)]) == True)
    # Test polygon against different polygon with duplicated points:
    assert(samePolygons([(0, 0), (1, 1), (2, 0), (1, -1)],
                        [(0, 0), (2, 0), (1, 1), (1, 1), (1, -1)]) == False)

def main():
    testSamePolygons()

main()

```
