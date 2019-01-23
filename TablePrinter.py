#! /usr/bin/env python3

# TablePrinter.py - Take list of lists of strings and display
# it in well-organized table.


'''
For practice, write a program that does the following.

Table Printer
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings.For example, the value could look like this:
             tableData =    [['apples', 'oranges', 'cherries', 'banana'],
                            ['Alice', 'Bob', 'Carol', 'David'],
                            ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:
                apples Alice  dogs
               oranges   Bob  cats
              cherries Carol moose
                banana David goose
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    colWidth = [0] * len(tableData)
    for index in range(len(tableData)):
        colWidth[index] = findMaxLength(tableData[index])
    rightJustifiedTable(max(colWidth))
    
    
def rightJustifiedTable(colWidth):
    for innerList in tableData:
        for strItem in innerList:
            print(strItem.rjust(colWidth)+' ', end='')
        print()
    

def findMaxLength(listItems):
    # It will first find maximum size string
    # After taking that maximum size string, we are taking lenght of that string
    return len(max(listItems, key=len))
        

printTable()
