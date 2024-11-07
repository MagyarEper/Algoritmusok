import math
import os
import random
import re
import sys

def unboundedKnapsack(k, arr):
    seged = [0] * (k + 1)
        
    for j in range(1, k + 1):
        for aktualis in arr:
            if aktualis <= j:
                seged[j] = max(seged[j], aktualis + seged[j - aktualis])
    
    return seged[k]
    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    results = ''
    for i in range(0, t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        arr = list(map(int, input().rstrip().split()))

        results += str(unboundedKnapsack(k, arr)) + '\n'

    print(results)
    fptr.write(results)

    fptr.close()