# -*- coding: utf-8 -*-
"""COSC2347_ASM1 (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-1qhFsCiCn6F2VCgYxOhfoR2eZK7rrPb

# COSC2347 - Assignment 1
In this assignment, you will review the language with input, output, control structure, loop, and function in Python. You will also learn how to arrange your software into modules with abstractions of parts of your software's functionalities into functions. As a first assignment, we will take the guided approach here. Therefore, we have prepared the main flow of this application, and you are about to replace the <code># CODE_HERE</code> place holers with your codes. Specifically, you will implement an application with functions to find the cube root of a number if it is a perfect cube or to approximate it otherwise. Here is the main description of the application:

Step 1: Input
* Ask the user to input a number

Step 2: Perfect cube
* Try to find an integer cube root for this number if it is a perfect cube and display it and the number of guesses before finding this.

* If cannot find it (the input number is not a perfect cube), print out a message "The input number is not a perfect cube, would you like to approximate its cube root (yes/no)".
* If the user inputs no, then finish the program
* If the user inputs yes, then continue to Step 3
* If the user inputs a wrong message, inform the user and ask again

Step 3: Approximation
* Ask the user to input the approximation error tolerance (epsilon)
* Validate this tolerance (e.g., ask the user to input again if it is not a number)
* Perform the approximation and display the approximated result and number of guesses if found.
* If not found, inform the user and stop

Note:
1. In Python, you can use x**(1/3) to find the root cube of x. However, you cannot use that operation here but write functions to do these tasks.
2. There should be at least two functions in this program. One for finding the root cube of a perfect cube (integer root cube) and another one for approximation. (-20 if not using functions for these two tasks).
3. All functions should work with positive and also negative numbers. The approximation function should work with numbers that are in the -1 to 1 range too. (-10 if your solution doesn't work with negative numbers, -10 it doesn't work with values in the range -1 to 1).
4. Please use the bisection method to improve performance for both perfect cube and approximation cases. (-5 if use the guess and check approach for the perfect cube, -5 if use the guess and check approach for the approximation).
5. Bonuses are given to improvements of the specified logic (but the total point does not exceed 100).
* +5 for the case the program asks for a number, validate that users must input a number. Otherwise, inform the user and ask the user to input again.
* +5 for extracting the input for the number task into a new function (because this function is reusable in different places). This function should validate that the input is actually a number or prompt for inputting again otherwise.

# Perfect cube root
"""

def find_perfect_cube_root(x):
  cube = abs(x)
  guesses = 1
  low = # CODE_HERE
  high = # CODE_HERE
  guess = # CODE_HERE
  while guess**3 != cube and guess <= cube and low <= high:
    # CODE_HERE
  # switch sign if the input is negative
  if x < 0:
    # CODE_HERE
  if guess**3 == x:
    print(f"Found root cube as {guess} for perfect cube {x} after {guesses}")
    return True
  else:
    print(f"Input number {x} is not a perfect cube")
    return False

"""## Test cases
Each of the following test cases is worth 3 points. Note: Passing test cases do not guarantee correctness (e.g., students may just fix the output). Therefore, the TA has the right to refuse to give marks if the implementation in the code chunk above is incorrect.
"""

# test 1
find_perfect_cube_root(0)

# test 2
find_perfect_cube_root(-1)

# test 3
find_perfect_cube_root(1)

# test 4
find_perfect_cube_root(27)

# test 5
find_perfect_cube_root(-27)

# test 6
find_perfect_cube_root(9)

# test 7
find_perfect_cube_root(0.5)

# test 8
find_perfect_cube_root(-0.5)

# test 9
find_perfect_cube_root(1000)

# test 10
find_perfect_cube_root(-1000)

"""# Approximate cube root
Switching from positive to negative is easy (just work for positive and switch the sign if the input is negative).

So, we can now focus on positive input.

* Now, for the input in the range of [0, 1], start guessing from the input value itself up to 1.

* For the input that is > 1, then start guessing from 1 up to cube.
"""

def approximate_cube_root(x, epsilon=0.01):
  cube = abs(x)
  # for cube > 1
  if cube > 1:
    low = # CODE_HERE
    high = # CODE_HERE
  # for cube <= 1
  else:
    low = # CODE_HERE
    high = # CODE_HERE
  guess = (low + high)/2 # do not convert to int
  guesses = 1
  while abs(guess**3 - cube) > epsilon and low <= high:
    # CODE_HERE
  if x < 0:
    # CODE_HERE
  if abs(guess**3 - x) > epsilon:
    print("Couldn't approximate with this precision, please increase epsilon")
    return False
  else:
    print(f"Found root cube as {guess} for {x} after {guesses} guesses")
    return True

"""# Test cases
Each of the following test cases is worth 3 points. Note: Passing test cases do not guarantee correctness (e.g., students may just fix the output). Therefore, the TA has the right to refuse to give marks if the implementation in the code chunk above is incorrect.
"""

# test 1
approximate_cube_root(8, 0.01)

# test 2
approximate_cube_root(-8, 0.01)

# test 3
approximate_cube_root(9, 0.01)

# test 4
approximate_cube_root(-9, 0.01)

# test 5
approximate_cube_root(1, 0.01)

# test 6
approximate_cube_root(-1, 0.01)

# test 7
approximate_cube_root(0.2, 0.01)

# test 8
approximate_cube_root(-0.2, 0.01)

# test 9
approximate_cube_root(0.9, 0.01)

# test 10
approximate_cube_root(-0.9, 0.01)

"""# User interaction"""

def user_interaction():
  # ask user to input a number and convert it to float.
  # the message is "Please input a number: "
  x = # CODE_HERE
  # try perfect cube root first
  found = find_perfect_cube_root(x)
  if not found:
    # ask user to input option
    # the message is "The input number is not a perfect cube, would you like to approximate its cube root (yes/no): "
    cont = # CODE_HERE
    # if wrong it put keep asking again with a new message as "Please input as yes/no: "
    # CODE_HERE

    if cont == "yes":
      # Ask to input tolerance and convert to float
      epsilon = # CODE_HERE
      found = approximate_cube_root(x, epsilon)

"""# User interaction test cases
Please perform the following test cases and validate the correctness of your program. In the following test cases means actions for <code>[i1, i2, i2]</code>, where:
* i1: means the input number in the first prompt
* i2: means the input option for yes/no to continue approximation.
* i3: means the value for the tolerance (epsilon)
* For each of these options, an underscore (_) means not applicable. Furthermore, if action is written as (a1, a2) and so on. It means the user inputs a1 and is wrong and asked to input again, then the user inputs a2.

Each of the following test cases is worth 4 points (except the first one that is completed for you as an example). Note: Passing test cases do not guarantee correctness (e.g., students may just fix the output). Therefore, the TA has the right to refuse to give marks if the implementation in the code chunk above is incorrect.

## Cases

0. [10, (what?, yes), 0.01]
1. [8, _, _]
2. [-8, _, _]
3. [9, (blah, no), _]
4. [9, yes, 0.01]
5. [-9, yes, 0.01]
6. [1, _, _]
7. [0.9, yes, 0.01]
8. [-0.9, yes, 0.01]
9. [0.5, yes, 0.001]
10. [-0.5, yes, 0.001]

## Example:
Following is an example of executing with the first test case (case 0).

"""

user_interaction()

