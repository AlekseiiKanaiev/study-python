 nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
#     # if startPriceOld > startPriceNew: return [0, startPriceOld-startPriceNew]
#     pc = 1-percentLossByMonth/100
#     m = 0
#     # print(pc)
#     # startPriceOld *= pc
#     # startPriceNew *= pc
#     while startPriceOld+savingperMonth*m < startPriceNew:
#         m += 1
#         print(m, pc)
#         startPriceOld *= pc
#         startPriceNew *= pc
#         pc -= 0.25/100
#         print('old: ',startPriceOld+savingperMonth*m)
#         print('new: ',startPriceNew)
#     print([m, startPriceOld+savingperMonth*m - startPriceNew])
#     return 