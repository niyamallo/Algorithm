import sys
import copy
input = sys.stdin.readline

def permutation(arr, n):

    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        
        if len(chosen) == n and not found:
            checkTotal(chosen, n)
            return
        
        if found:
            return
            
	
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

def checkTotal(arr, n):

    global found
    
    tmp = copy.deepcopy(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            tmp[j] = tmp[j] + tmp[j+1]
    if tmp[0] == f:
        found = True
        print(*arr)
        return

n, f = map(int, input().split())
nums = [x for x in range(1,n+1)]
found = False

permutation(nums, n)