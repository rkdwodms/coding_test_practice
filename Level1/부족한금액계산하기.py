def solution(price, money, count):
    sum = 0
    for i in range(1,count+1):
        sum = sum +(price * i) 
        
    if sum <= money:
        return 0
    else:
        return (sum - money)
    

    return 0


solution(3,20,4)
