def solution(n):
    answer = []
    d = 2
    
    temp = n
    while d <= temp :
        if temp % d ==0:
            if d not in answer:
               answer.append(d)
            temp //=d
        else:
            d+=1
            
    return answer