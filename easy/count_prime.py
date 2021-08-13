'''
Problem:
Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0

Constraints:

0 <= n <= 5000000
'''

# Solution

class Solution:
    def count_primes(self, n: int) -> int:
        is_prime = True
        primes_list = []
        if n < 2:
            return len(primes_list)
        elif n == 2:
            return 1
        for i in range (2, n + 1, 1): 
            for j in range (1, i, 1):
                if i % j == 0 and j != 1:
                    is_prime = False
            if is_prime == True:
                primes_list.append(i)
            is_prime = True
        return len(primes_list)