def solution(price):
    low_store = price[0]
    high_store = 0
    for i in price:
        if i < low_store:
            low_store = i
        profit = i - low_store

        if profit > high_store:
            high_store = profit
        
    return high_store
        

prices = [7, 1, 5, 3, 6, 4]

print(solution(prices))