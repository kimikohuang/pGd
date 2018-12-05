#!/usr/bin/python

import csv
import time
import numpy
from scipy import polyfit, polyval, sqrt
from pylab import plot, title, legend, show
import warnings

warnings.simplefilter('ignore', numpy.RankWarning)
#def kimikodecision(mylist, dayPeriod):
#    for 
    
def fAvePrc(ndaGoldHis_4_columns,i,idxMyDays,ifCountSelf):
    if i == 0:
        return ndaGoldHis_4_columns[i][3]
    if i+1 <= idxMyDays:
        return numpy.mean(ndaGoldHis_4_columns[0:i+ifCountSelf],axis=0)[3]
    else:
        return numpy.mean(ndaGoldHis_4_columns[i-idxMyDays+ifCountSelf:i+ifCountSelf],axis=0)[3]
    
def f_average_price_idx_DAY_WINDOW_1(listPirceDiffHis,i,idx_DAY_WINDOW_1,ifCountSelf):
    if i == 0:
        return listPirceDiffHis[i]
    if i+1 <= idx_DAY_WINDOW_1:
        return numpy.mean(listPirceDiffHis[0:i+ifCountSelf],axis=0)
    else:
        return numpy.mean(listPirceDiffHis[i-idx_DAY_WINDOW_1+ifCountSelf:i+ifCountSelf],axis=0)

def f_get_buy_unit_qty(idxCdHis,nda_buy_unit_idx,nda_balance_idx,forByRatio):
    myTotalAccount = numpy.sum(nda_balance_idx[0][0:idxCdHis])+nda_balance_idx[0][-1]
#    print 'myTotalAccount:', myTotalAccount
#    exit()
    if myTotalAccount/ndaGoldHis_4_columns[idxCdHis][3]*forByRatio>=1:
        return round(myTotalAccount/ndaGoldHis_4_columns[idxCdHis][3]*forByRatio)
    else:
        return 0

def f_get_sell_unit_qty(idxCdHis,nda_buy_unit_idx,nda_balance_idx,forSlRatio):
    myTotalCount = numpy.sum(nda_buy_unit_idx[0][0:idxCdHis])
#    print 'myTotalCount:', myTotalCount
#    exit()
    if myTotalCount*forSlRatio>=1:
        return round(myTotalCount*forSlRatio)
    else:
        return 0
    
ndaGoldHis_4_columns = numpy.loadtxt('/home/kimiko/Documents/GoldPassbook_745.csv',dtype='float',delimiter=',')   # 4 is the best 30-201096, False
print('Type(ndaGoldHis_4_columns): ', type(ndaGoldHis_4_columns))
# 4,False, 52-246470, True, 50-236978, 3, 26-202786
#ndaGoldHis_4_columns = numpy.loadtxt('/home/kimiko/Documents/goldNy1.csv',dtype='float',delimiter=',')
#ndaGoldHis_4_columns = numpy.loadtxt('/home/kimiko/Documents/goldNy2.csv',dtype='float',delimiter=',')
#ndaGoldHis_4_columns = numpy.loadtxt('/home/kimiko/Documents/gold250_3.csv',dtype='float',delimiter=',')
# gold250_1.csv gold250_2.csv gold250_3.csv 3 is the best


lenGoldHis = len(ndaGoldHis_4_columns)
print('len(ndaGoldHis_4_columns):',lenGoldHis) 
print(ndaGoldHis_4_columns)
#exit()
# mylist = []
# 
# spamReader = csv.reader(open('/home/kimiko/Documents/gold.csv', 'rb'), dialect='excel')

#for row in spamReader:
#    mylist.append([int(row[2]),int(row[3])])
#    list_idxGoldHis.append(float(row[0]))
#    list_GoldPrice.append(float(row[3]))
# list_idxGoldHis = []
# list_GoldPrice = []    
list_idxGoldHis = list(range(0,lenGoldHis))
print('len(list_idxGoldHis): ', len(list_idxGoldHis))

list_GoldPrice = ndaGoldHis_4_columns[:,3].tolist()
print('len(list_GoldPrice): ', len(list_GoldPrice)) 
# for idxRow in range(0,lenGoldHis):
# #    mylist.append([int(ndaGoldHis_4_columns[idxRow][2]),int(ndaGoldHis_4_columns[idxRow][3])])
# #    list_idxGoldHis.append(float(ndaGoldHis_4_columns[idxRow][0]))
#     list_idxGoldHis.append(idxRow)
#     list_GoldPrice.append(float(ndaGoldHis_4_columns[idxRow][3]))
    
#     '----'
#    polyfit_idx_price=polyfit(list_idxGoldHis[0:idxRow+1],list_GoldPrice[0:idxRow+1],4)
#    polyval_idx_price=polyval(polyfit_idx_price,list_idxGoldHis)
#    list_Price_Diff = (list_GoldPrice-polyval_idx_price)
#    print 'list_Price_Diff, list_idxGoldHis ,list_GoldPrice :', list_Price_Diff, list_idxGoldHis[0:idxRow+1], list_GoldPrice[0:idxRow+1]
#    time.sleep(1)
    
#    exit()
n=len(list_GoldPrice)

#(ar,br)=polyfit(list_idxGoldHis,list_GoldPrice,2)
#polyval_idx_price=polyval([ar,br],list_idxGoldHis)

print('----')

for idx in range(1,51):
    polyfit_idx_price=polyfit(list_idxGoldHis,list_GoldPrice,idx)
    polyval_idx_price=polyval(polyfit_idx_price,list_idxGoldHis)

    err=sqrt(sum((polyval_idx_price-list_GoldPrice)**2)/n)
    print('idx - err: ', idx, ' - ', err)

my_degree = 50    
polyfit_idx_price=polyfit(list_idxGoldHis,list_GoldPrice,my_degree)
polyval_idx_price=polyval(polyfit_idx_price,list_idxGoldHis)

err=sqrt(sum((polyval_idx_price-list_GoldPrice)**2)/n)
print('err:', err)

print('----')
list_Price_Diff = (list_GoldPrice-polyval_idx_price)
print(list_Price_Diff[0:10])
#exit()
#matplotlib ploting
title('Linear Regression Example')
plot(list_idxGoldHis,list_Price_Diff,'g.--')
plot(list_idxGoldHis,list_GoldPrice,'k.')
plot(list_idxGoldHis,polyval_idx_price,'r.-')

#legend(['list_GoldPrice','polyval_idx_price'])

show()

# for row in spamReader:
#     mylist.append([int(row[2]),int(row[3])])
# #    print ', '.join(row)
# #    print row[0]
# #    print row[3], type(int(row[3]))
# print('mylist[0]:', mylist[0][1])
# print('mylist[-1]:', mylist[-1])
# print(type(mylist), mylist)
#exit()


print('type(ndaGoldHis_4_columns): ', type(ndaGoldHis_4_columns))
#exit()
#print numpy.mean(ndaGoldHis_4_columns[0:5],axis=0)[3]
#
#print numpy.mean(ndaGoldHis_4_columns[0:5],axis=0)
#print numpy.mean(ndaGoldHis_4_columns[0:5],axis=0)[3]
#print ndaGoldHis_4_columns[1][1]
#idx_DAY_WINDOW_1 = 6
maxFinalTotal = 0
maxByRatio = 0.0
maxSlRatio = 0.0

dic_listPriceDiff = {}
list_Std_Price_Diff = []

print('lenGoldHis: ', lenGoldHis)
idxGdHis = 2
print('idxGdHis, list_idxGoldHis[0:idxGdHis+1]: ', idxGdHis, list_idxGoldHis[0:idxGdHis+1])
print('idxGdHis, list_GoldPrice[0:idxGdHis+1]: ', idxGdHis, list_GoldPrice[0:idxGdHis+1])

print('len(range(0,lenGoldHis)): ', len(range(0,lenGoldHis)), '; ', range(0,lenGoldHis))
for idxGdHis in range(0,lenGoldHis):
#                polyfit_idx_price=polyfit(list_idxGoldHis[0:idxGdHis+1],list_GoldPrice[0:idxGdHis+1],4)
#    polyfit_idx_price=polyfit(list_idxGoldHis[0:idxGdHis+1],list_GoldPrice[0:idxGdHis+1],max(1,int(numpy.log10(idxGdHis+1)+1)))
    print('idxGdHis: ', idxGdHis)
    print('list_idxGoldHis[0:idxGdHis+1]: ', list_idxGoldHis[0:idxGdHis+1])
    print('list_GoldPrice[0:idxGdHis+1]: ', list_GoldPrice[0:idxGdHis+1])
    
    if idxGdHis == 0:
        list_Price_Diff = [0]
    else:
        polyfit_idx_price=polyfit(list_idxGoldHis[0:idxGdHis+1],list_GoldPrice[0:idxGdHis+1],4)
        polyval_idx_price=polyval(polyfit_idx_price,list(range(0,idxGdHis+1)))
        list_Price_Diff = list_GoldPrice[0:idxGdHis+1]-polyval_idx_price
#    print 'list_Price_Diff:', list_Price_Diff
    if idxGdHis not in dic_listPriceDiff:
        dic_listPriceDiff[idxGdHis]=[]
    dic_listPriceDiff[idxGdHis]=list_Price_Diff
    list_Std_Price_Diff.append(numpy.std(list_Price_Diff))
#numpy.savetxt('list_Std_Price_Diff.csv',list_Std_Price_Diff,fmt="%9.2f")
#exit()
#    print list_Std_Price_Diff[0:100] 
    #    print dic_listPriceDiff
#    if idxGdHis == 50:
##        exit()
#        continue
print('len(list_Std_Price_Diff[0:10]): ', len(list_Std_Price_Diff[0:10]), ', list_Std_Price_Diff[0:10]:', list_Std_Price_Diff[0:10])
print('numpy.mean(numpy.array(list_Std_Price_Diff)): ', numpy.mean(numpy.array(list_Std_Price_Diff)))
print('numpy.std(numpy.array(list_Std_Price_Diff)): ', numpy.std(numpy.array(list_Std_Price_Diff)))
print('---- idxRow OK!')

ifCountSelf = True

BUY_RATIO_MAX = 1
BUY_RATIO_STEP = -0.2

SELL_RATIO_MAX = 1
SELL_RATIO_STEP = -0.2

ftStdEachNrm100XStart = -5
ftStdEachNrm100XStop = -15
#ftStdEachNrm100XStep = -1
ftStdEachNrm100XStep = -3

INITIAL_CAPITAL = 100000      # 100,000

DAYS_WINDOW_SIZE=lenGoldHis
DAYS_WINDOW_SIZE = 100
DAYS_WINDOW_SIZE = min(lenGoldHis, 100)

myCsvWriter = csv.writer(open('result2.csv', 'wb'), dialect='excel')
print('BUY_RATIO_MAX/(-BUY_RATIO_STEP)+1: ', type(BUY_RATIO_MAX/(-BUY_RATIO_STEP)+1), BUY_RATIO_MAX/(-BUY_RATIO_STEP)+1)
ndaResult = numpy.ndarray(shape=(DAYS_WINDOW_SIZE,int(BUY_RATIO_MAX/(-BUY_RATIO_STEP))+1,int(SELL_RATIO_MAX/(-SELL_RATIO_STEP))+1,int((ftStdEachNrm100XStart-ftStdEachNrm100XStop)/(-ftStdEachNrm100XStep))+1), dtype=float)

#exit()

listStdNrm100X = list(range(ftStdEachNrm100XStart,ftStdEachNrm100XStop+ftStdEachNrm100XStep,ftStdEachNrm100XStep))
print('len(listStdNrm100X): ', len(listStdNrm100X), ', listStdNrm100X:', listStdNrm100X)    # len(listStdNrm100X):  5 , listStdNrm100X: [-5, -8, -11, -14, -17]
#exit()
list_DAY_WINDOW_1 = list(range(1,DAYS_WINDOW_SIZE+1))
listByRatio = list(numpy.arange(BUY_RATIO_MAX,-0.1,BUY_RATIO_STEP))
print('len(listByRatio): ', len(listByRatio), ', listByRatio: ', listByRatio)

listSlRatio = list(numpy.arange(SELL_RATIO_MAX,-0.1,SELL_RATIO_STEP))
print('len(listSlRatio): ', len(listSlRatio), ', listSlRatio: ', listSlRatio)

myFilename = '/home/kimiko/result4_'+str(ftStdEachNrm100XStart)+'_'+str(-ftStdEachNrm100XStep)+'_'+str(DAYS_WINDOW_SIZE)+'.csv'
with open(myFilename, 'w') as resultfile:
    print('open '+myFilename)
#    for forStdEachNrm100X in numpy.arange(-ftStdEachNrm100XStop,ftStdEachNrm100XStop+ftStdEachNrm100XStep,ftStdEachNrm100XStep):
    print('---- start forStdEachNrm100X:')
    for forStdEachNrm100X in listStdNrm100X:
        print('forStdEachNrm100X:', forStdEachNrm100X)
        for idx_DAY_WINDOW_1 in list_DAY_WINDOW_1:
            print('  idx_DAY_WINDOW_1:', idx_DAY_WINDOW_1)
            for forByRatio_1_00 in listByRatio:  
                
                for forSlRatio in listSlRatio:    
                    
                    nda_buy_unit_idx = numpy.zeros((1,lenGoldHis))
                    nda_balance_idx = numpy.zeros((1,lenGoldHis+1))
                    nda_balance_idx[0][-1] = INITIAL_CAPITAL
                    
        #            print 'nda_balance_idx[0]):',numpy.sum(nda_balance_idx[0])+numpy.sum(nda_buy_unit_idx[0])*ndaGoldHis_4_columns[idxGdHis][2]
                    
                    for idxGdHis in range(0,lenGoldHis):
                        
        #                print 'idxGdHis:', idxGdHis
                        
                    #    if idxGdHis == 10:
                    #        exit()
                            
        #                print 'idx_DAY_WINDOW_1:', idx_DAY_WINDOW_1, 'idxbyRatio10:', idxbyRatio10, 'mySlRaio10:', mySlRaio10, 'idxGdHis:', idxGdHis
        #                print 'ndaGoldHis_4_columns[idxGdHis][3]:', ndaGoldHis_4_columns[idxGdHis][3]
                    #    print 'fAvePrc:', fAvePrc(ndaGoldHis_4_columns,idxGdHis,idx_DAY_WINDOW_1,ifCountSelf)
        
        
        #                polyfit_idx_price=polyfit(list_idxGoldHis[0:idxGdHis+1],list_GoldPrice[0:idxGdHis+1],4)
        #                polyfit_idx_price=polyfit(list_idxGoldHis[0:idxGdHis+1],list_GoldPrice[0:idxGdHis+1],int(numpy.log10(idxGdHis+1)+1))
        #                polyval_idx_price=polyval(polyfit_idx_price,range(0,idxGdHis+1))
        #                list_Price_Diff = (list_GoldPrice[0:idxGdHis+1]-polyval_idx_price)
        #                print 'list_Price_Diff, list_idxGoldHis ,list_GoldPrice :', list_Price_Diff, list_idxGoldHis[0:idxRow+1], list_GoldPrice[0:idxRow+1]
        #                time.sleep(1)
                        
        #                myAvePrice = fAvePrc(ndaGoldHis_4_columns,idxGdHis,idx_DAY_WINDOW_1,ifCountSelf)
        #                myAvePrice = f_average_price_idx_DAY_WINDOW_1(list_Price_Diff,idxGdHis,idx_DAY_WINDOW_1,ifCountSelf)
        
                        myAvePrice = f_average_price_idx_DAY_WINDOW_1(dic_listPriceDiff[idxGdHis],idxGdHis,idx_DAY_WINDOW_1,ifCountSelf)
        
        #                print 'myAvePrice:', myAvePrice
        #                if ndaGoldHis_4_columns[idxGdHis][3]<myAvePrice:
        #                if list_Price_Diff[3] > myAvePrice: # 3-246, 4-248, 5-218168
        #                if list_Price_Diff[idxGdHis] < myAvePrice: # 
        #                print 'dic_listPriceDiff[idxGdHis][idxGdHis]:', dic_listPriceDiff[idxGdHis][idxGdHis]
        #                exit()
        #                if dic_listPriceDiff[idxGdHis][idxGdHis] < myAvePrice: # <138, >100
                        mean_PriceDiff_idxGdHis = numpy.mean(dic_listPriceDiff[idxGdHis])
        #                print 'mean_PriceDiff_idxGdHis:', mean_PriceDiff_idxGdHis, '|  myAvePrice:', myAvePrice
                        if mean_PriceDiff_idxGdHis+round(forStdEachNrm100X/100.0,2)*list_Std_Price_Diff[idxGdHis] < myAvePrice: # <136015-
        
        #               if list_Price_Diff[5] > myAvePrice:
        #                if numpy.mean(list_Price_Diff) > myAvePrice:
        #                if numpy.mean(list_Price_Diff[0:idxGdHis]) < myAvePrice: # > 72-223271, < 50-153431
        #                if numpy.mean(list_Price_Diff[0:max(1,idxGdHis-10)]) < myAvePrice: # 136015
        #                if list_Price_Diff[idxGdHis] < myAvePrice:
        #                if myAvePrcLong > myAvePrice: # >44-203743, 10>73-223271
        
                            
        #                    print 'Try by'
                            nda_buy_unit_idx[0][idxGdHis] = f_get_buy_unit_qty(idxGdHis,nda_buy_unit_idx,nda_balance_idx,forByRatio_1_00)
                            nda_balance_idx[0][idxGdHis] = -nda_buy_unit_idx[0][idxGdHis]*ndaGoldHis_4_columns[idxGdHis][3]
                        else:
        #                    print 'Try Sl'
                            nda_buy_unit_idx[0][idxGdHis] = -f_get_sell_unit_qty(idxGdHis,nda_buy_unit_idx,nda_balance_idx,forSlRatio)
                            nda_balance_idx[0][idxGdHis] = -nda_buy_unit_idx[0][idxGdHis]*ndaGoldHis_4_columns[idxGdHis][2]
        #                print 'listCount[0][idx1]:', listCount[0][idx1]
        #                print 'listAccount[0][idx1]:', listAccount[0][idx1]
                    # end for idxGdHis in range(0,lenGoldHis):
                    
        #            print 'numpy.sum(listAccount[0,idx1]):', numpy.sum(listAccount[0])
        #            print 'numpy.sum(listCount[0][idx1]):', numpy.sum(listCount[0])
        #            print 'numpy.sum(listCount[0][idx1]):', numpy.sum(listCount[0])*ndaPhiStd[-1][2]
                    finalTotal = numpy.sum(nda_balance_idx[0]) + numpy.sum(nda_buy_unit_idx[0])*ndaGoldHis_4_columns[-1][2]
#                    print type(ndaResult)
#                    print idx_DAY_WINDOW_1, forByRatio_1_00, forSlRatio, forStdEachNrm100X
#                    print 'list_DAY_WINDOW_1.index(idx_DAY_WINDOW_1):', list_DAY_WINDOW_1.index(idx_DAY_WINDOW_1)
#                    exit()
                    if finalTotal/INITIAL_CAPITAL > 1.5:
                        print('len(list_DAY_WINDOW_1):', len(list_DAY_WINDOW_1), idx_DAY_WINDOW_1, list_DAY_WINDOW_1.index(idx_DAY_WINDOW_1))
                        print('len(listByRatio):', len(listByRatio), forByRatio_1_00, listByRatio.index(forByRatio_1_00))
                        print('len(listSlRatio):', len(listSlRatio), forSlRatio, listSlRatio.index(forSlRatio))
                        print('len(listStdNrm100X):', len(listStdNrm100X), forStdEachNrm100X, listSlRatio.index(forSlRatio))
                        ndaResult[list_DAY_WINDOW_1.index(idx_DAY_WINDOW_1)][listByRatio.index(forByRatio_1_00)][listSlRatio.index(forSlRatio)][listStdNrm100X.index(forStdEachNrm100X)] = int(finalTotal)
                        line = ','.join([str(int(finalTotal)),str(round(forStdEachNrm100X/100.0,2))+' X',str(idx_DAY_WINDOW_1)+' days',str(forByRatio_1_00)+' by',str(forSlRatio)+' Sl']) + '\n'
                        resultfile.write(line)
        #            myCsvWriter.writerow(str(finalTotal))
        #            print 'finalTotal:', finalTotal, '| idx_DAY_WINDOW_1:', idx_DAY_WINDOW_1, '| idxByRatio10:', idxByRatio10, '| mySlRaio10:', mySlRaio10, '| idxGdHis:', idxGdHis
                    if finalTotal > maxFinalTotal:
                        maxFinalTotal_SlRatio=maxFinalTotal = finalTotal
                        theMaxmyDays_SlRatio=theMaxmyDays = idx_DAY_WINDOW_1
                        maxByRatio_SlRatio = maxByRatio = forByRatio_1_00
                        maxSlRatio_SlRatio = maxSlRatio = forSlRatio
    #        print 'Days:', idx_DAY_WINDOW_1, '| maxByR:', maxByRatio, '| maxSlRatio:', maxSlRatio, '| maxFinalTotal:', maxFinalTotal
#            print 'Days:', idx_DAY_WINDOW_1, '| maxByRatio:', maxByRatio, '| maxSlRatio:', maxSlRatio, '| maxFinalTotal:', maxFinalTotal, '|  forStdEachNrm100X:', forStdEachNrm100X
#print 'start idx_DAY_WINDOW_1:', idx_DAY_WINDOW_1, '| maxByRatio:', maxByRatio, '| maxSlRatio:', maxSlRatio, '| maxFinalTotal:', maxFinalTotal, '|  forStdEachNrm100X:', forStdEachNrm100X
#ndaResult.tofile('result.csv', sep=",", format="%d")
#numpy.savetxt('result3.csv', ndaResult, fmt='%d')
print('lenGoldHis:', lenGoldHis)
print('ndaGoldHis_4_columns[0][3]):', ndaGoldHis_4_columns[0][3], ndaGoldHis_4_columns[0][3]*lenGoldHis)
print('ndaGoldHis_4_columns[-1][2]:', ndaGoldHis_4_columns[-1][2], ndaGoldHis_4_columns[-1][2]*lenGoldHis)
print('(ndaGoldHis_4_columns[-1][2]-ndaGoldHis_4_columns[0][3]):', (ndaGoldHis_4_columns[-1][2]-ndaGoldHis_4_columns[0][3]))
print((ndaGoldHis_4_columns[-1][2]-ndaGoldHis_4_columns[0][3])/ndaGoldHis_4_columns[0][3])
print(lenGoldHis*(ndaGoldHis_4_columns[-1][2]-ndaGoldHis_4_columns[0][3]))
#exit()

print('numpy.amax(ndaResult):', numpy.amax(ndaResult))


print('maxFinalTotal:', maxFinalTotal)
#print 'theMaxmyDays', theMaxmyDays
print('maxByRatio:', maxByRatio)
print('maxSlRatio:', maxSlRatio)
print((lenGoldHis*ndaGoldHis_4_columns[-1][2]-lenGoldHis*ndaGoldHis_4_columns[0][3])/lenGoldHis*ndaGoldHis_4_columns[0][3])