import sys

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]
    return l

def DutchFlagPartition(v, i):
    l = v.copy()
    pivot = l[i]

    (smaller, equal, larger) = (0, 0, len(l)-1)

    while (equal <= larger):
        if l[equal] < pivot:
            smaller += 1
            equal += 1
            swap(l, smaller, equal)
        elif l[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            swap(l, equal, larger)

    return l


v = [-3, 0, -1, 1, 1, 1, 4, 2]

print('input list: ',v)

print(DutchFlagPartition(v, 2))



def BuyAndSellStockOnce(prices):
    #min_price_so_far = sys.maxsize
    min_price_so_far = prices[0]
    max_profit = 0

    daily_profit = []

    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        daily_profit.append(max_profit_sell_today)

        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)

    print('xxxx daily_profit: ', daily_profit)

    return max_profit


prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

print('xxxx prices: ', prices)
print(BuyAndSellStockOnce(prices))

