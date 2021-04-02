#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ans = 0
    for val in [len(list(group)) for key, group in groupby(sorted(ar))]:
        ans = ans + int(val/2)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
