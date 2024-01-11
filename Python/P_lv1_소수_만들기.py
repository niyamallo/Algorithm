import math
from itertools import combinations

def is_prime_number(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def solution(nums):
    num_3 = list(map(sum, combinations(nums, 3)))
    answer = 0
    for num in num_3:
        if is_prime_number(num):
            answer += 1
    
    return answer