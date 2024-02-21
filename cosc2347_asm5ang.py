# -*- coding: utf-8 -*-
"""COSC2347_ASM5ANG.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N9-PyrQfF0HN7TMeh_9VB5gtBiTiGjIu

# Tribonacci number
The Tribonacci sequence $T_n$ is defined as follows:

$T_0 = 0$, $T_1 = 1$, $T_2 = 1$, and $T_{n} = T_{n-1} + T_{n-2} + T_{n-3}$ for $n >= 3$.

Given n, return the value of $T_n$.

## Exercise 1. Recursive (easy) approach
Implement this algorithm using recursive approach.
"""

def tribo_recur(n):

    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return tribo_recur(n-1) + tribo_recur(n-2) + tribo_recur(n-3)

def test(func, i, o):
  try:
    assert func(i) == o
    print("Passed")
  except:
    print("Failed")

# test case 1 (10 pt)
test(tribo_recur, 0, 0)
test(tribo_recur, 2, 1)
test(tribo_recur, 1, 1)

# test case 2 (10 pt)
test(tribo_recur, 3, 2)
test(tribo_recur, 4, 4)
test(tribo_recur, 5, 7)

"""## "Wall clock" counting for Exercise 1
You can use these two code cells to have a sense (just a sense of) how the time changes compare to the input change
"""

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# tribo_recur(10)

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# tribo_recur(30)

"""## Reflection on Exercise 1
Please answers the following questions (by typing the answer) in the following code cell.
- from 30 values to 10, what is the rate (ratio, order of growth) of input size change?
- from your execution, what is the rate (ratio, order of growth) of the execution time. Instruction: Take the time displayed, convert to the same unit, do the division and print the rate.


What is the time complexity O(?) of this implementation. Please print your answer as either one of the following
- "constant" (if it is O(1))
- "logarithmic" (if it is O(logn))
- "linear" (if it is O(n))
- "log linear" if it is O(nlogn)
- "quadratic" if it is O(n^2)
- "exponential" if it is O(3^n)
"""

input_size_change_ratio = 30 / 10
print(f'input change ratio {input_size_change_ratio}')

execution_time_30 = 11
execution_time_10 = 61.1
execution_time_change_ratio = execution_time_30 / execution_time_10
print(f'time change ratio {execution_time_change_ratio}')

print('time complexity type exponential')

"""## Exercise 2. Dynamic programming using dictionary (memoization)
Implement this algorithm using recursive approach and memoization.
"""

def tribo_recur_mem(n):
    def helper(n, mem):
        key = n

        if key not in mem:

            if n == 0:
                ret = 0
            elif n == 1 or n == 2:
                ret = 1
            else:
                ret = helper(n-1, mem) + helper(n-2, mem) + helper(n-3, mem)

            mem[key] = ret

        return mem[key]

    return helper(n, {})

# test case 1 (10 pt)
test(tribo_recur_mem, 0, 0)
test(tribo_recur_mem, 1, 1)
test(tribo_recur_mem, 2, 1)

# test case 2 (10 pt)
test(tribo_recur_mem, 3, 2)
test(tribo_recur_mem, 4, 4)
test(tribo_recur_mem, 5, 7)

"""## "Wall clock" counting for Exercise 2
You can use these two code cells to have a sense (just a sense of) how the time changes compare to the input change
"""

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# tribo_recur_mem(10)

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# tribo_recur_mem(30)

"""## Reflection on Exercise 2
Please answers the following questions (by typing the answer) in the following code cell.
- from 30 values to 10, what is the rate (ratio, order of growth) of input size change?
- from your execution, what is the rate (ratio, order of growth) of the execution time. Instruction: Take the time displayed, convert to the same unit, do the division and print the rate.


What is the time complexity O(?) of this implementation. Please print your answer as either one of the following
- "constant" (if it is O(1))
- "logarithmic" (if it is O(logn))
- "linear" (if it is O(n))
- "log linear" if it is O(nlogn)
- "quadratic" if it is O(n^2)
- "exponential" if it is O(3^n)
"""

execution_time_30 = 6.4


execution_time_10 = 23


input_size_change_ratio = 30 / 10
print(f'input change ratio {input_size_change_ratio}')

execution_time_change_ratio = execution_time_30 / execution_time_10
print(f'time change ratio {execution_time_change_ratio}')


print('time complexity type linear')

"""# Exercise 3. Dynamic programming using list
Recursive and memoization has linear complexity with the trade off of some space. However, it still involves linear number of recursive calls. Thus, we can make use of a list to avoid recursive calls.
"""

def tribo_dp(n):

    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]

# test case 1
test(tribo_dp, 0, 0)
test(tribo_dp, 1, 1)
test(tribo_dp, 2, 1)

# test case 2
test(tribo_dp, 3, 2)
test(tribo_dp, 4, 4)
test(tribo_dp, 5, 7)

"""## "Wall clock" counting for Exercise 3
You can use these two code cells to have a sense (just a sense of) how the time changes compare to the input change
"""

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# tribo_dp(10)

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# tribo_dp(30)

"""## Reflection on Exercise 3
Please answers the following questions (by typing the answer) in the following code cell.
- from 30 values to 10, what is the rate (ratio, order of growth) of input size change?
- from your execution, what is the rate (ratio, order of growth) of the execution time. Instruction: Take the time displayed, convert to the same unit, do the division and print the rate.


What is the time complexity O(?) of this implementation. Please print your answer as either one of the following
- "constant" (if it is O(1))
- "logarithmic" (if it is O(logn))
- "linear" (if it is O(n))
- "log linear" if it is O(nlogn)
- "quadratic" if it is O(n^2)
- "exponential" if it is O(3^n)
"""

execution_time_30 = 9.19


execution_time_10 = 2.23

input_size_change_ratio = 30 / 10
print(f'input change ratio {input_size_change_ratio}')


execution_time_change_ratio = execution_time_30 / execution_time_10
print(f'time change ratio {execution_time_change_ratio}')


print('time complexity type linear')

"""# Exercise 4. Iterative approach
Both dynamic approaches (using list and using dictionary) are linear in terms of time and complexity O(n). The linear approach is better that it doesn't require the space for storing all the outputs. Specifically, we do not need the whole sequence from 1 to n but want only the last one. Thus, we can use iterative approach to save space. This approach is like using 4 pointers at at time. One for the current value, one for the -1 step value, one for -2 steps value, one for -3 steps value.
"""

def tribo_iter(n):

    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:

        p0, p1, p2 = 0, 1, 1

        for i in range(3, n + 1):

            p = p0 + p1 + p2

            p0, p1, p2 = p1, p2, p

        return p

# test case 1
test(tribo_iter, 0, 0)
test(tribo_iter, 1, 1)
test(tribo_iter, 2, 1)

# test case 2
test(tribo_iter, 3, 2)
test(tribo_iter, 4, 4)
test(tribo_iter, 5, 7)

"""## "Wall clock" counting for Exercise 4
You can use these two code cells to have a sense (just a sense of) how the time changes compare to the input change
"""

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# tribo_iter(10)

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# tribo_iter(30)

"""## Reflection on Exercise 4
Please answers the following questions (by typing the answer) in the following code cell.
- from 30 values to 10, what is the rate (ratio, order of growth) of input size change?
- from your execution, what is the rate (ratio, order of growth) of the execution time. Instruction: Take the time displayed, convert to the same unit, do the division and print the rate.


What is the time complexity O(?) of this implementation. Please print your answer as either one of the following
- "constant" (if it is O(1))
- "logarithmic" (if it is O(logn))
- "linear" (if it is O(n))
- "log linear" if it is O(nlogn)
- "quadratic" if it is O(n^2)
- "exponential" if it is O(3^n)
"""

execution_time_30 = 3.11


execution_time_10 = 2.13


input_size_change_ratio = 30 / 10
print(f'input change ratio {input_size_change_ratio}')


execution_time_change_ratio = execution_time_30 / execution_time_10
print(f'time change ratio {execution_time_change_ratio}')


print('time complexity type linear')

"""# Reflection
By now, you should have mastered main techniques to perform some algorithms, namely:
- Recursive approach
- Dynamic programming using dictionary or memoization
- Dynamic programming using list
- Iterative approach

You should be able to analyze the pros and cons of each approach and how to move from one to another.
"""

