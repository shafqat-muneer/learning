#! /usr/bin/env python3

# TablePrinter.py - Take list of lists of strings and display
# it in well-organized table.


'''
For practice, write a program that does the following.

Table Printer
Write a function named print_table() that takes a list of lists of strings and
displays it in a well-organized table with each column right-justified. Assume
that all the inner lists will contain the same number of strings.For example,
the value could look like this:
             tableData =    [['apples', 'oranges', 'cherries', 'banana'],
                            ['Alice', 'Bob', 'Carol', 'David'],
                            ['dogs', 'cats', 'moose', 'goose']]
Your print_table() function would print the following:
                apples Alice  dogs
               oranges   Bob  cats
              cherries Carol moose
                banana David goose
'''

table_data = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]


def print_table():
    col_width = [0] * len(table_data)
    for index in range(len(table_data)):
        col_width[index] = find_max_length(table_data[index])
    right_justified_table(max(col_width))
    
    
def right_justified_table(col_width):
    for inner_list in table_data:
        for str_item in inner_list:
            print(str_item.rjust(col_width)+' ', end='')
        print()
    

def find_max_length(listItems):
    # It will first find maximum size string
    # After taking that maximum size string, we are taking lenght of that string
    return len(max(listItems, key=len))
        

print_table()
