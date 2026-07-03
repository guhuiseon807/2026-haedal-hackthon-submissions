def solution(n):
    a=0
    b=1
    for _ in range(2, n+1):
        a,b = b, (a+b) % 1234567
    return b