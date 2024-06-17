import tkinter as tk
from tkinter import messagebox
import random

def show_info(info):
    info_text.config(state=tk.NORMAL)
    info_text.delete(1.0, tk.END)
    info_text.insert(tk.END, info)
    info_text.config(state=tk.DISABLED)

w = tk.Tk()
w.geometry("1920x1080")
w.title("Python Tutorial")

title_label = tk.Label(w, text="PYTHON TUTORIAL", font=("Arial", 24))
title_label.pack(pady=10)

button_frame = tk.Frame(w)
button_frame.pack(side=tk.LEFT, padx=10)

buttons = [
    ("Python Variables",
     """
    Variables
    Variables are containers for storing data values.

    Creating Variables
    Python has no command for declaring a variable.

    A variable is created the moment you first assign a value to it.

    ExampleGet your own Python Server
    x = 5
    y = "John"
    print(x)
    print(y)
    Variables do not need to be declared with any particular type, and can even change type after they have been set.

    Example
    x = 4       # x is of type int
    x = "Sally" # x is now of type str
    print(x)
    Casting
    If you want to specify the data type of a variable, this can be done with casting.

    Example
    x = str(3)    # x will be '3'
    y = int(3)    # y will be 3
    z = float(3)  # z will be 3.0
    Get the Type
    You can get the data type of a variable with the type() function.

    Example
    x = 5
    y = "John"
    print(type(x))
    print(type(y))
    You will learn more about data types and casting later in this tutorial.
    Single or Double Quotes?
    String variables can be declared either by using single or double quotes:

    Example
    x = "John"
    # is the same as
    x = 'John'
    Case-Sensitive
    Variable names are case-sensitive.

    Example
    This will create two variables:

    a = 4
    A = "Sally"
    #A will not overwrite a
    """),

    ("Python Data Types",
     """
     Python Data Types
     Built-in Data Types
     In programming, data type is an important concept.
 
     Variables can store data of different types, and different types can do different things.
 
     Python has the following data types built-in by default, in these categories:
 
     Text Type:	str
     Numeric Types:	int, float, complex
     Sequence Types:	list, tuple, range
     Mapping Type:	dict
     Set Types:	set, frozenset
     Boolean Type:	bool
     Binary Types:	bytes, bytearray, memoryview
     None Type:	NoneType
     Getting the Data Type
     You can get the data type of any object by using the type() function:
 
     ExampleGet your own Python Server
     Print the data type of the variable x:
 
     x = 5
     print(type(x))
     Setting the Data Type
     In Python, the data type is set when you assign a value to a variable:
 
     Example	Data Type	Try it
     x = "Hello World"	str	
     x = 20	int	
     x = 20.5	float	
     x = 1j	complex	
     x = ["apple", "banana", "cherry"]	list	
     x = ("apple", "banana", "cherry")	tuple	
     x = range(6)	range	
     x = {"name" : "John", "age" : 36}	dict	
     x = {"apple", "banana", "cherry"}	set	
     x = frozenset({"apple", "banana", "cherry"})	frozenset	
     x = True	bool	
     x = b"Hello"	bytes	
     x = bytearray(5)	bytearray	
     x = memoryview(bytes(5))	memoryview	
     x = None	NoneType	
     Setting the Specific Data Type
     If you want to specify the data type, you can use the following constructor functions:
 
     Example	Data Type	Try it
     x = str("Hello World")	str	
     x = int(20)	int	
     x = float(20.5)	float	
     x = complex(1j)	complex	
     x = list(("apple", "banana", "cherry"))	list	
     x = tuple(("apple", "banana", "cherry"))	tuple	
     x = range(6)	range	
     x = dict(name="John", age=36)	dict	
     x = set(("apple", "banana", "cherry"))	set	
     x = frozenset(("apple", "banana", "cherry"))	frozenset	
     x = bool(5)	bool	
     x = bytes(5)	bytes	
     x = bytearray(5)	bytearray	
     x = memoryview(bytes(5))	memoryview	
     """),

    ("Python Strings",
     """
     Python Strings
     Strings
     Strings in python are surrounded by either single quotation marks, or double quotation marks.
 
     'hello' is the same as "hello".
 
     You can display a string literal with the print() function:
 
     ExampleGet your own Python Server
     print("Hello")
     print('Hello')
     Quotes Inside Quotes
     You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
 
     Example
     print("It's alright")
     print("He is called 'Johnny'")
     print('He is called "Johnny"')
     Assign String to a Variable
     Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
 
     Example
     a = "Hello"
     print(a)
     Multiline Strings
     You can assign a multiline string to a variable by using three quotes:
 
     Example
     You can use three double quotes:
 
     a = ""Lorem ipsum dolor sit amet,
     consectetur adipiscing elit,
     sed do eiusmod tempor incididunt
     ut labore et dolore magna aliqua.""
     print(a)
     Or three single quotes:
 
     Example
     a = '''Lorem ipsum dolor sit amet,
     consectetur adipiscing elit,
     sed do eiusmod tempor incididunt
     ut labore et dolore magna aliqua.'''
     print(a)
     Note: in the result, the line breaks are inserted at the same position as in the code.
 
     Strings are Arrays
     Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
 
     However, Python does not have a character data type, a single character is simply a string with a length of 1.
 
     Square brackets can be used to access elements of the string.
 
     Example
     Get the character at position 1 (remember that the first character has the position 0):
 
     a = "Hello, World!"
     print(a[1])
     Looping Through a String
     Since strings are arrays, we can loop through the characters in a string, with a for loop.
 
     Example
     Loop through the letters in the word "banana":
 
     for x in "banana":
     print(x)
     Learn more about For Loops in our Python For Loops chapter.
 
     String Length
     To get the length of a string, use the len() function.
 
     Example
     The len() function returns the length of a string:
 
     a = "Hello, World!"
     print(len(a))
     Check String
     To check if a certain phrase or character is present in a string, we can use the keyword in.
 
     Example
     Check if "free" is present in the following text:
 
     txt = "The best things in life are free!"
     print("free" in txt)
     Use it in an if statement:
 
     Example
     Print only if "free" is present:
 
     txt = "The best things in life are free!"
     if "free" in txt:
     print("Yes, 'free' is present.")
     Learn more about If statements in our Python If...Else chapter.
 
     Check if NOT
     To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
 
     Example
     Check if "expensive" is NOT present in the following text:
 
     txt = "The best things in life are free!"
     print("expensive" not in txt)
     """),

    ("Python Lists",
     """
    Python Lists
    mylist = ["apple", "banana", "cherry"]
    List
    Lists are used to store multiple items in a single variable.

    Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

    Lists are created using square brackets:

    ExampleGet your own Python Server
    Create a List:

    thislist = ["apple", "banana", "cherry"]
    print(thislist)
    List Items
    List items are ordered, changeable, and allow duplicate values.

    List items are indexed, the first item has index [0], the second item has index [1] etc.

    Ordered
    When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

    If you add new items to a list, the new items will be placed at the end of the list.

    Note: There are some list methods that will change the order, but in general: the order of the items will not change.

    Changeable
    The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

    Allow Duplicates
    Since lists are indexed, lists can have items with the same value:

    Example
    Lists allow duplicate values:

    thislist = ["apple", "banana", "cherry", "apple", "cherry"]
    print(thislist)
    List Length
    To determine how many items a list has, use the len() function:

    Example
    Print the number of items in the list:

    thislist = ["apple", "banana", "cherry"]
    print(len(thislist))
    List Items - Data Types
    List items can be of any data type:

    Example
    String, int and boolean data types:

    list1 = ["apple", "banana", "cherry"]
    list2 = [1, 5, 7, 9, 3]
    list3 = [True, False, False]
    A list can contain different data types:

    Example
    A list with strings, integers and boolean values:

    list1 = ["abc", 34, True, 40, "male"]
    type()
    From Python's perspective, lists are defined as objects with the data type 'list':

    <class 'list'>
    Example
    What is the data type of a list?

    mylist = ["apple", "banana", "cherry"]
    print(type(mylist))
    The list() Constructor
    It is also possible to use the list() constructor when creating a new list.

    Example
    Using the list() constructor to make a List:

    thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
    print(thislist)
    Python Collections (Arrays)
    There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
    """),

    ("Python Tuples",
     """
    Python Tuples
    mytuple = ("apple", "banana", "cherry")
    Tuple
    Tuples are used to store multiple items in a single variable.

    Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

    A tuple is a collection which is ordered and unchangeable.

    Tuples are written with round brackets.

    ExampleGet your own Python Server
    Create a Tuple:

    thistuple = ("apple", "banana", "cherry")
    print(thistuple)
    Tuple Items
    Tuple items are ordered, unchangeable, and allow duplicate values.

    Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

    Ordered
    When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

    Unchangeable
    Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

    Allow Duplicates
    Since tuples are indexed, they can have items with the same value:

    Example
    Tuples allow duplicate values:

    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    print(thistuple)
    Tuple Length
    To determine how many items a tuple has, use the len() function:

    Example
    Print the number of items in the tuple:

    thistuple = ("apple", "banana", "cherry")
    print(len(thistuple))
    Create Tuple With One Item
    To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

    Example
    One item tuple, remember the comma:

    thistuple = ("apple",)
    print(type(thistuple))

    #NOT a tuple
    thistuple = ("apple")
    print(type(thistuple))
    Tuple Items - Data Types
    Tuple items can be of any data type:

    Example
    String, int and boolean data types:

    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1, 5, 7, 9, 3)
    tuple3 = (True, False, False)
    A tuple can contain different data types:

    Example
    A tuple with strings, integers and boolean values:

    tuple1 = ("abc", 34, True, 40, "male")
    type()
    From Python's perspective, tuples are defined as objects with the data type 'tuple':

    <class 'tuple'>
    Example
    What is the data type of a tuple?

    mytuple = ("apple", "banana", "cherry")
    print(type(mytuple))
    The tuple() Constructor
    It is also possible to use the tuple() constructor to make a tuple.

    Example
    Using the tuple() method to make a tuple:

    thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
    print(thistuple)
    Python Collections (Arrays)
    There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
    """),

    ("Python Sets",
     """
    Python Sets
    myset = {"apple", "banana", "cherry"}
    Set
    Sets are used to store multiple items in a single variable.

    Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

    A set is a collection which is unordered, unchangeable*, and unindexed.

    * Note: Set items are unchangeable, but you can remove items and add new items.

    Sets are written with curly brackets.

    ExampleGet your own Python Server
    Create a Set:

    thisset = {"apple", "banana", "cherry"}
    print(thisset)
    Note: Sets are unordered, so you cannot be sure in which order the items will appear.

    Set Items
    Set items are unordered, unchangeable, and do not allow duplicate values.

    Unordered
    Unordered means that the items in a set do not have a defined order.

    Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

    Unchangeable
    Set items are unchangeable, meaning that we cannot change the items after the set has been created.

    Once a set is created, you cannot change its items, but you can remove items and add new items.

    Duplicates Not Allowed
    Sets cannot have two items with the same value.

    Example
    Duplicate values will be ignored:

    thisset = {"apple", "banana", "cherry", "apple"}

    print(thisset)
    Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

    Example
    True and 1 is considered the same value:

    thisset = {"apple", "banana", "cherry", True, 1, 2}

    print(thisset)
    Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

    Example
    False and 0 is considered the same value:

    thisset = {"apple", "banana", "cherry", False, True, 0}

    print(thisset)
    Get the Length of a Set
    To determine how many items a set has, use the len() function.

    Example
    Get the number of items in a set:

    thisset = {"apple", "banana", "cherry"}

    print(len(thisset))
    Set Items - Data Types
    Set items can be of any data type:

    Example
    String, int and boolean data types:

    set1 = {"apple", "banana", "cherry"}
    set2 = {1, 5, 7, 9, 3}
    set3 = {True, False, False}
    A set can contain different data types:

    Example
    A set with strings, integers and boolean values:

    set1 = {"abc", 34, True, 40, "male"}
    type()
    From Python's perspective, sets are defined as objects with the data type 'set':

    <class 'set'>
    Example
    What is the data type of a set?

    myset = {"apple", "banana", "cherry"}
    print(type(myset))
    The set() Constructor
    It is also possible to use the set() constructor to make a set.

    Example
    Using the set() constructor to make a set:

    thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
    print(thisset)
    Python Collections (Arrays)
    There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
    """),

    ("Python Dictionaries",
     """
    Python Dictionaries
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    Dictionary
    Dictionaries are used to store data values in key:value pairs.

    A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

    As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

    Dictionaries are written with curly brackets, and have keys and values:

    ExampleGet your own Python Server
    Create and print a dictionary:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(thisdict)
    Dictionary Items
    Dictionary items are ordered, changeable, and do not allow duplicates.

    Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

    Example
    Print the "brand" value of the dictionary:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(thisdict["brand"])
    Ordered or Unordered?
    As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

    When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

    Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

    Changeable
    Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

    Duplicates Not Allowed
    Dictionaries cannot have two items with the same key:

    Example
    Duplicate values will overwrite existing values:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
    }
    print(thisdict)
    Dictionary Length
    To determine how many items a dictionary has, use the len() function:

    Example
    Print the number of items in the dictionary:

    print(len(thisdict))
    Dictionary Items - Data Types
    The values in dictionary items can be of any data type:

    Example
    String, int, boolean, and list data types:

    thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
    }
    type()
    From Python's perspective, dictionaries are defined as objects with the data type 'dict':

    <class 'dict'>
    Example
    Print the data type of a dictionary:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(type(thisdict))
    The dict() Constructor
    It is also possible to use the dict() constructor to make a dictionary.

    Example
    Using the dict() method to make a dictionary:

    thisdict = dict(name = "John", age = 36, country = "Norway")
    print(thisdict)
    Python Collections (Arrays)
    There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
    """),

    ("Python If ... Else",
     """
    Python If ... Else
    Python Conditions and If statements
    Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
    These conditions can be used in several ways, most commonly in "if statements" and loops.

    An "if statement" is written by using the if keyword.

    ExampleGet your own Python Server
    If statement:

    a = 33
    b = 200
    if b > a:
    print("b is greater than a")
    In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

    Indentation
    Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

    Example
    If statement, without indentation (will raise an error):

    a = 33
    b = 200
    if b > a:
    print("b is greater than a") # you will get an error
    Elif
    The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

    Example
    a = 33
    b = 33
    if b > a:
    print("b is greater than a")
    elif a == b:
    print("a and b are equal")
    In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".

    Else
    The else keyword catches anything which isn't caught by the preceding conditions.

    Example
    a = 200
    b = 33
    if b > a:
    print("b is greater than a")
    elif a == b:
    print("a and b are equal")
    else:
    print("a is greater than b")
    In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".

    You can also have an else without the elif:

    Example
    a = 200
    b = 33
    if b > a:
    print("b is greater than a")
    else:
    print("b is not greater than a")
    Short Hand If
    If you have only one statement to execute, you can put it on the same line as the if statement.

    Example
    One line if statement:

    if a > b: print("a is greater than b")
    Short Hand If ... Else
    If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

    Example
    One line if else statement:

    a = 2
    b = 330
    print("A") if a > b else print("B")
    This technique is known as Ternary Operators, or Conditional Expressions.

    You can also have multiple else statements on the same line:

    Example
    One line if else statement, with 3 conditions:

    a = 330
    b = 330
    print("A") if a > b else print("=") if a == b else print("B")
    And
    The and keyword is a logical operator, and is used to combine conditional statements:

    Example
    Test if a is greater than b, AND if c is greater than a:

    a = 200
    b = 33
    c = 500
    if a > b and c > a:
    print("Both conditions are True")
    Or
    The or keyword is a logical operator, and is used to combine conditional statements:

    Example
    Test if a is greater than b, OR if a is greater than c:

    a = 200
    b = 33
    c = 500
    if a > b or a > c:
    print("At least one of the conditions is True")
    Not
    The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

    Example
    Test if a is NOT greater than b:

    a = 33
    b = 200
    if not a > b:
    print("a is NOT greater than b")
    Nested If
    You can have if statements inside if statements, this is called nested if statements.

    Example
    x = 41

    if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
    The pass Statement
    if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

    Example
    a = 33
    b = 200

    if b > a:
    pass
    """),

    ("Python While Loops",
     """
    Python While Loops
    Python Loops
    Python has two primitive loop commands:

    while loops
    for loops
    The while Loop
    With the while loop we can execute a set of statements as long as a condition is true.

    ExampleGet your own Python Server
    Print i as long as i is less than 6:

    i = 1
    while i < 6:
    print(i)
    i += 1
    Note: remember to increment i, or else the loop will continue forever.

    The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

    The break Statement
    With the break statement we can stop the loop even if the while condition is true:

    Example
    Exit the loop when i is 3:

    i = 1
    while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
    The continue Statement
    With the continue statement we can stop the current iteration, and continue with the next:

    Example
    Continue to the next iteration if i is 3:

    i = 0
    while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    The else Statement
    With the else statement we can run a block of code once when the condition no longer is true:

    Example
    Print a message once the condition is false:

    i = 1
    while i < 6:
    print(i)
    i += 1
    else:
    print("i is no longer less than 6")
    """),

    ("Python For Loops",
     """
    Python For Loops
    A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

    This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-oriented programming languages.

    With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

    ExampleGet your own Python Server
    Print each fruit in a fruit list:

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
    print(x)
    The for loop does not require an indexing variable to set beforehand.

    Looping Through a String
    Even strings are iterable objects, they contain a sequence of characters:

    Example
    Loop through the letters in the word "banana":

    for x in "banana":
    print(x)
    The break Statement
    With the break statement we can stop the loop before it has looped through all the items:

    Example
    Exit the loop when x is "banana":

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
    print(x)
    if x == "banana":
        break
    Example
    Exit the loop when x is "banana", but this time the break comes before the print:

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
    if x == "banana":
        break
    print(x)
    The continue Statement
    With the continue statement we can stop the current iteration of the loop, and continue with the next:

    Example
    Do not print banana:

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
    if x == "banana":
        continue
    print(x)
    The range() Function
    To loop through a set of code a specified number of times, we can use the range() function,
    The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

    Example
    Using the range() function:

    for x in range(6):
    print(x)
    Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

    The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

    Example
    Using the start parameter:

    for x in range(2, 6):
    print(x)
    The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

    Example
    Increment the sequence with 3 (default is 1):

    for x in range(2, 30, 3):
    print(x)
    Else in For Loop
    The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

    Example
    Print all numbers from 0 to 5, and print a message when the loop has ended:

    for x in range(6):
    print(x)
    else:
    print("Finally finished!")
    Note: The else block will NOT be executed if the loop is stopped by a break statement.

    Example
    Break the loop when x is 3, and see what happens with the else block:

    for x in range(6):
    if x == 3: break
    print(x)
    else:
    print("Finally finished!")
    Nested Loops
    A nested loop is a loop inside a loop.

    The "inner loop" will be executed one time for each iteration of the "outer loop":

    Example
    Print each adjective for every fruit:

    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
    for y in fruits:
        print(x, y)
    The pass Statement
    for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

    Example
    for x in [0, 1, 2]:
    pass
    """),

    ("Python Functions",
     """
    Python Functions
    A function is a block of code which only runs when it is called.

    You can pass data, known as parameters, into a function.

    A function can return data as a result.

    Creating a Function
    In Python, a function is defined using the def keyword:

    ExampleGet your own Python Server
    def my_function():
    print("Hello from a function")
    Calling a Function
    To call a function, use the function name followed by parenthesis:

    Example
    def my_function():
    print("Hello from a function")

    my_function()
    Arguments
    Information can be passed into functions as arguments.

    Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

    The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

    Example
    def my_function(fname):
    print(fname + " Refsnes")

    my_function("Emil")
    my_function("Tobias")
    my_function("Linus")
    Arguments are often shortened to args in Python documentations.

    Parameters or Arguments?
    The terms parameter and argument can be used for the same thing: information that is passed into a function.

    From a function's perspective:

    A parameter is the variable listed inside the parentheses in the function definition.

    An argument is the value that is sent to the function when it is called.

    Number of Arguments
    By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

    Example
    This function expects 2 arguments, and gets 2 arguments:

    def my_function(fname, lname):
    print(fname + " " + lname)

    my_function("Emil", "Refsnes")
    If you try to call the function with 1 or 3 arguments, you will get an error:
    Example
    This function expects 2 arguments, but gets only 1:

    def my_function(fname, lname):
    print(fname + " " + lname)

    my_function("Emil")
    Arbitrary Arguments, *args
    If you do not know how many arguments will be passed into your function, add a * before the parameter name in the function definition.

    This way, the function will receive a tuple of arguments and can access the items accordingly:

    Example
    If the number of arguments is unknown, add a * before the parameter name:

    def my_function(*kids):
    print("The youngest child is " + kids[2])

    my_function("Emil", "Tobias", "Linus")
    Arbitrary Arguments are often shortened to *args in Python documentations.

    Keyword Arguments
    You can also send arguments with the key = value syntax.

    This way, the order of the arguments does not matter.

    Example
    def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

    my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
    The phrase Keyword Arguments is often shortened to kwargs in Python documentations.

    Arbitrary Keyword Arguments, **kwargs
    If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name in the function definition.

    This way, the function will receive a dictionary of arguments and can access the items accordingly:

    Example
    If the number of keyword arguments is unknown, add a double ** before the parameter name:

    def my_function(**kid):
    print("His last name is " + kid["lname"])

    my_function(fname = "Tobias", lname = "Refsnes")
    Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentations.

    Default Parameter Value
    The following example shows how to use a default parameter value.

    If we call the function without an argument, it uses the default value:

    Example
    def my_function(country = "Norway"):
    print("I am from " + country)

    my_function("Sweden")
    my_function("India")
    my_function()
    my_function("Brazil")
    Passing a List as an Argument
    You can send any data types of argument to a function (string, number, list, dictionary, etc.), and it will be treated as the same data type inside the function.

    E.g. if you send a List as an argument, it will still be a List when it reaches the function:

    Example
    def my_function(food):
    for x in food:
        print(x)

    fruits = ["apple", "banana", "cherry"]

    my_function(fruits)
    Return Values
    To let a function return a value, use the return statement:

    Example
    def my_function(x):
    return 5 * x

    print(my_function(3))
    print(my_function(5))
    print(my_function(9))
    The pass Statement
    Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

    Example
    def myfunction():
    pass
    Positional-Only Arguments
    You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

    To specify that a function can have only positional arguments, add , / after the arguments:

    Example
    def my_function(x, /):
    print(x)

    my_function(3)
    Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

    Example
    def my_function(x):
    print(x)

    my_function(x = 3)
    But when adding the , / you will get an error if you try to send a keyword argument:

    Example
    def my_function(x, /):
    print(x)

    my_function(x = 3)
    Keyword-Only Arguments
    To specify that a function can have only keyword arguments, add *, before the arguments:

    Example
    def my_function(*, x):
    print(x)

    my_function(x = 3)
    Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:

    Example
    def my_function(x):
    print(x)

    my_function(3)
    But when adding the *, / you will get an error if you try to send a positional argument:

    Example
    def my_function(*, x):
    print(x)

    my_function(3)
    Combine Positional-Only and Keyword-Only
    You can combine the two argument types in the same function.

    Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

    Example
    def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

    my_function(5, 6, c = 7, d = 8)
    Recursion
    Python also accepts function recursion, which means a defined function can call itself.

    Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

    The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

    In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

    To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

    Example
    Recursion Example

    def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

    print("\n\nRecursion Example Results")
    tri_recursion(6)
    """),

    ("Python Classes and Objects",
     """
    Python Classes and Objects
    Python is an object-oriented programming language.

    Almost everything in Python is an object, with its properties and methods.

    A Class is like an object constructor, or a "blueprint" for creating objects.

    Create a Class
    To create a class, use the keyword class:

    ExampleGet your own Python Server
    class MyClass:
    x = 5
    Create Object
    Now we can use the class named MyClass to create objects:

    Example
    Create an object named p1, and print the value of x:

    p1 = MyClass()
    print(p1.x)
    The __init__() Function
    The examples above are classes and objects in their simplest form, and are not really useful in real-life applications.

    To understand the meaning of classes, we have to understand the built-in __init__() function.

    All classes have a function called __init__(), which is always executed when the class is being initiated.

    Use the __init__() function to assign values to object properties, or perform other operations that are necessary when the object is being created:

    Example
    Create a class named Person, use the __init__() function to assign values for name and age:

    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    p1 = Person("John", 36)

    print(p1.name)
    print(p1.age)
    Note: The __init__() function is called automatically every time the class is used to create a new object.

    The __str__() Function
    The __str__() function controls what should be returned when the class object is represented as a string.

    If the __str__() function is not set, the string representation of the object is returned:

    Example
    The string representation of an object WITHOUT the __str__() function:

    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    p1 = Person("John", 36)

    print(p1)
    Example
    The string representation of an object WITH the __str__() function:

    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    p1 = Person("John", 36)

    print(p1)
    Object Methods
    Objects can also contain methods. Methods in objects are functions that belong to the object.

    Let us create a method in the Person class:

    Example
    Insert a function that prints a greeting, and execute it on the p1 object:

    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

    p1 = Person("John", 36)
    p1.myfunc()
    Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

    The self Parameter
    The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

    It does not have to be named self; you can call it whatever you like, but it has to be the first parameter of any function in the class:

    Example
    Use the words mysillyobject and abc instead of self:

    class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello, my name is " + abc.name)

    p1 = Person("John", 36)
    p1.myfunc()
    Modify Object Properties
    You can modify properties on objects like this:

    Example
    Set the age of p1 to 40:

    p1.age = 40
    Delete Object Properties
    You can delete properties on objects using the del keyword:

    Example
    Delete the age property from the p1 object:

    del p1.age
    Delete Objects
    You can delete objects using the del keyword:

    Example
    Delete the p1 object:

    del p1
    The pass Statement
    Class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error:

    Example
    class Person:
    pass
""")
]

for (text, info) in buttons:
    button = tk.Button(button_frame, text=text, command=lambda info=info: show_info(info))
    button.pack(fill=tk.X, pady=5)

info_frame = tk.LabelFrame(w, text="SHOW INFORMATION", font=("Arial", 18))
info_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill="both", expand=True)

info_text_frame = tk.Frame(info_frame)
info_text_frame.pack(fill="both", expand=True)

info_text = tk.Text(info_text_frame, wrap="word")
info_text.pack(side=tk.LEFT, fill="both", expand=True)

scrollbar = tk.Scrollbar(info_text_frame, command=info_text.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

info_text.config(yscrollcommand=scrollbar.set)
info_text.config(state=tk.DISABLED)

exit_button = tk.Button(w, text="Exit", command=w.quit)
exit_button.pack(side=tk.BOTTOM, pady=10)

w.mainloop()