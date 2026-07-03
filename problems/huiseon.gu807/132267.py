def solution(a, b, n):
    total_received = 0
    while n >= a:
        new_coke = (n//a)*b
        
        remain_empty_coke = n % a
        
        total_received += new_coke
        
        n = new_coke + remain_empty_coke
        
    return total_received