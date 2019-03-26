#!/usr/bin/python3.5

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    # if startPriceOld > startPriceNew: return [0, startPriceOld-startPriceNew]
    pc = 1-percentLossByMonth/100
    m = 0
    # print(pc)
    # startPriceOld *= pc
    # startPriceNew *= pc
    while startPriceOld+savingperMonth*m < startPriceNew:
        m += 1
        print(m, pc)
        if m%2 == 0: pc -= 0.5/100
        startPriceOld *= pc
        startPriceNew *= pc
        print('old: ',startPriceOld+savingperMonth*m)
        print('new: ',startPriceNew)
    print([m, startPriceOld+savingperMonth*m - startPriceNew])
    return [m, round(startPriceOld+savingperMonth*m - startPriceNew)]

# def nbMonths(oldCarPrice, newCarPrice, saving, loss):
#     months = 0
#     budget = oldCarPrice
    
#     while budget < newCarPrice:
#         months += 1
#         if months % 2 == 0:
#             loss += 0.5
        
#         oldCarPrice *= (100 - loss) / 100
#         newCarPrice *= (100 - loss) / 100
#         budget = saving * months + oldCarPrice
#     print(months, round(budget - newCarPrice))
#     return [months, round(budget - newCarPrice)]

nbMonths(2000, 8000, 1000, 1.5)
nbMonths(12000, 8000, 1000, 1.5)