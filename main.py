import math

def is_perfect(n):
    
    if n < 2:
        return False
    
    sum_divs = 1
    
    limit = int(math.sqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            sum_divs += i
            
            if i * i != n:
                sum_divs += n // i
                
    return sum_divs == n

n = int(input())

if is_perfect(n):
    print("YES")
else:
    print("NO")