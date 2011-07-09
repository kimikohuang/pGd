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
    
def fAvePrc(ndaGoldHis,i,idxMyDays,ifCountSelf):
    if i == 0:
        return ndaGoldHis[i][3]
    if i+1 <= idxMyDays:
        return numpy.mean(ndaGoldHis[0:i+ifCountSelf],axis=0)[3]
    else:
        return numpy.mean(ndaGoldHis[i-idxMyDays+ifCountSelf:i+ifCountSelf],axis=0)[3]
    
def fAvePrcNrl(ndaGoldHis,i,idxMyDays,ifCountSelf):
    if i == 0:
        return ndaGoldHis[i]
    if i+1 <= idxMyDays:
        return numpy.mean(ndaGoldHis[0:i+ifCountSelf],axis=0)
    else:
        return numpy.mean(ndaGoldHis[i-idxMyDays+ifCountSelf:i+ifCountSelf],axis=0)

def fgetByNum(idxCdHis,listCnt,listAcnt,forByRatio):
    myTotalAccount = numpy.sum(listAcnt[0][0:idxCdHis])+listAcnt[0][-1]
#    print 'myTotalAccount:', myTotalAccount
#    exit()
    if myTotalAccount/ndaGoldHis[idxCdHis][3]*forByRatio>=1:
        return round(myTotalAccount/ndaGoldHis[idxCdHis][3]*forByRatio)
    else:
        return 0

def fGetSlNum(idxCdHis,listCnt,listAcnt,forSlRatio):
    myTotalCount = numpy.sum(listCnt[0][0:idxCdHis])
#    print 'myTotalCount:', myTotalCount
#    exit()
    if myTotalCount*forSlRatio>=1:
        return round(myTotalCount*forSlRatio)
    else:
        return 0
    
ndaGoldHis = numpy.loadtxt('/home/kimiko/Documents/gold.csv',dtype='float',delimiter=',')   # 4 is the best 30-201096, False
print ndaGoldHis.shape
print ndaGoldHis[0:10]
exit
ndaGoldHis2 = numpy.concatenate((ndaGoldHis[1:],numpy.array([[0,0,0,0]])), axis=0)
print ndaGoldHis2[0:10]
#ndaGoldHis2m1 = ndaGoldHis2 - ndaGoldHis
ndaG3 = ndaGoldHis[1:]-ndaGoldHis[0:-1]
print ndaG3.shape
print ndaG3[0:10]
#print ndaGoldHis2m1.shape
#if (ndaG3-ndaGoldHis2m1[0:-1]).all:
#    print 'OK'

#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

mu, sigma = 100, 15
#x = mu + sigma*np.random.randn(10000)
x = ndaG3[:,3]
print 'x:',x, min(x), max(x),max(x)-min(x)
#exit()
#print len(x)
#exit()
# the histogram of the data
#n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
n, bins, patches = plt.hist(x, 44, normed=0, facecolor='green')

## add a 'best fit' line
#y = mlab.normpdf( bins, mu, sigma)
#l = plt.plot(bins, y, 'r--', linewidth=1)
#
#plt.xlabel('Smarts')
#plt.ylabel('Probability')
#plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
#plt.grid(True)

plt.show()



exit()
print ndaGoldHis2m1
print '------------------------'
print numpy.round(ndaGoldHis2m1, 0)
exit()
# 4,False, 52-246470, True, 50-236978, 3, 26-202786
#ndaGoldHis = numpy.loadtxt('/home/kimiko/Documents/goldNy1.csv',dtype='float',delimiter=',')
#ndaGoldHis = numpy.loadtxt('/home/kimiko/Documents/goldNy2.csv',dtype='float',delimiter=',')
#ndaGoldHis = numpy.loadtxt('/home/kimiko/Documents/gold250_3.csv',dtype='float',delimiter=',')
# gold250_1.csv gold250_2.csv gold250_3.csv 3 is the best


lenCdHis = len(ndaGoldHis)
print 'ndaGoldHis:',len(ndaGoldHis) 
print ndaGoldHis
#exit()
mylist = []

spamReader = csv.reader(open('/home/kimiko/Documents/gold.csv', 'rb'), dialect='excel')

#for row in spamReader:
#    mylist.append([int(row[2]),int(row[3])])
#    listT.append(float(row[0]))
#    listX.append(float(row[3]))
listT = []
listX = []    
for idxRow in range(0,len(ndaGoldHis)):
    mylist.append([int(ndaGoldHis[idxRow][2]),int(ndaGoldHis[idxRow][3])])
#    listT.append(float(ndaGoldHis[idxRow][0]))
    listT.append(idxRow)
    listX.append(float(ndaGoldHis[idxRow][3]))
    
#     '----'
#    qq=polyfit(listT[0:idxRow+1],listX[0:idxRow+1],4)
#    xr=polyval(qq,listT)
#    listNewX = (listX-xr)
#    print 'listNewX, listT ,listX :', listNewX, listT[0:idxRow+1], listX[0:idxRow+1]
#    time.sleep(1)
    
#    exit()
n=len(listX)

#(ar,br)=polyfit(listT,listX,2)
#xr=polyval([ar,br],listT)

print '----'
qq=polyfit(listT,listX,10)
xr=polyval(qq,listT)

err=sqrt(sum((xr-listX)**2)/n)
print 'err:', err

print '----'
listNewX = (listX-xr)
print listNewX[0:10]
#exit()
#matplotlib ploting
title('Linear Regression Example')
plot(listT,listNewX,'g.--')
plot(listT,listX,'k.')
plot(listT,xr,'r.-')

#legend(['listX','xr'])

show()

for row in spamReader:
    mylist.append([int(row[2]),int(row[3])])
#    print ', '.join(row)
#    print row[0]
#    print row[3], type(int(row[3]))
print 'mylist[0]:', mylist[0][1]
print 'mylist[-1]:', mylist[-1]
print type(mylist), mylist
#exit()


print 'type(ndaGoldHis):', type(ndaGoldHis)
#exit()
#print numpy.mean(ndaGoldHis[0:5],axis=0)[3]
#
#print numpy.mean(ndaGoldHis[0:5],axis=0)
#print numpy.mean(ndaGoldHis[0:5],axis=0)[3]
#print ndaGoldHis[1][1]
#idxMyDays = 6
maxFinalTotal = 0
maxByRatio = 0.0
maxSlRatio = 0.0
ifCountSelf = True

dicNewX = {}
listStdNewX = []

for idxCdHis in range(0,lenCdHis):
#                qq=polyfit(listT[0:idxCdHis+1],listX[0:idxCdHis+1],4)
#    qq=polyfit(listT[0:idxCdHis+1],listX[0:idxCdHis+1],max(1,int(numpy.log10(idxCdHis+1)+1)))
    qq=polyfit(listT[0:idxCdHis+1],listX[0:idxCdHis+1],4)
    xr=polyval(qq,range(0,idxCdHis+1))
    listNewX = (listX[0:idxCdHis+1]-xr)
#    print 'listNewX:', listNewX
    if not dicNewX.has_key(idxCdHis):
        dicNewX[idxCdHis]=[]
    dicNewX[idxCdHis]=listNewX
    listStdNewX.append(numpy.std(listNewX))
#numpy.savetxt('listStdNewX.csv',listStdNewX,fmt="%9.2f")
#exit()
#    print listStdNewX[0:100] 
    #    print dicNewX
#    if idxCdHis == 50:
##        exit()
#        continue
print listStdNewX[0:10]
print numpy.mean(numpy.array(listStdNewX))
print numpy.std(numpy.array(listStdNewX))
print '---- idxRow OK!'

    
ftByRatioMax = 1
ftByRatioStep = -0.1

ftSlRatioMax = 1
ftSlRatioStep = -0.1

ftStdEachNrm100XStart = -5
ftStdEachNrm100XStop = -15
ftStdEachNrm100XStep = -1

initialNumber = 100000

MaxMyDays=lenCdHis
MaxMyDays = 50
myCsvWriter = csv.writer(open('result2.csv', 'wb'), dialect='excel')
ndaResult = numpy.ndarray(shape=(MaxMyDays,ftByRatioMax/(-ftByRatioStep)+1,ftSlRatioMax/(-ftSlRatioStep)+1,(ftStdEachNrm100XStart-ftStdEachNrm100XStop)/(-ftStdEachNrm100XStep)+1), dtype=float)

listStdNrm100X = list(range(ftStdEachNrm100XStart,ftStdEachNrm100XStop+ftStdEachNrm100XStep,ftStdEachNrm100XStep))
print 'listStdNrm100X:', listStdNrm100X
#exit()
listMyDays = range(1,MaxMyDays+1)
listByRatio = list(numpy.arange(ftByRatioMax,-0.1,ftByRatioStep))
listSlRatio = list(numpy.arange(ftSlRatioMax,-0.1,ftSlRatioStep))

myFilename = '/home/kimiko/result4_'+str(ftStdEachNrm100XStart)+'_'+str(-ftStdEachNrm100XStep)+'_'+str(MaxMyDays)+'.csv'
with open(myFilename, 'w') as resultfile:
    print 'open '+myFilename
#    for forStdEachNrm100X in numpy.arange(-ftStdEachNrm100XStop,ftStdEachNrm100XStop+ftStdEachNrm100XStep,ftStdEachNrm100XStep):
    print '---- start forStdEachNrm100X:'
    for forStdEachNrm100X in listStdNrm100X:
        print 'forStdEachNrm100X:', forStdEachNrm100X
        for idxMyDays in listMyDays:
            print '  idxMyDays:', idxMyDays
            for forByRatio in listByRatio:  
                
                for forSlRatio in listSlRatio:    
                    
                    listCnt = numpy.zeros((1,lenCdHis))
                    listAcnt = numpy.zeros((1,lenCdHis+1))
                    listAcnt[0][-1]=initialNumber
                    
        #            print 'listAcnt[0]):',numpy.sum(listAcnt[0])+numpy.sum(listCnt[0])*ndaGoldHis[idxCdHis][2]
                    
                    for idxCdHis in range(0,lenCdHis):
                        
        #                print 'idxCdHis:', idxCdHis
                        
                    #    if idxCdHis == 10:
                    #        exit()
                            
        #                print 'idxMyDays:', idxMyDays, 'idxbyRatio10:', idxbyRatio10, 'mySlRaio10:', mySlRaio10, 'idxCdHis:', idxCdHis
        #                print 'ndaGoldHis[idxCdHis][3]:', ndaGoldHis[idxCdHis][3]
                    #    print 'fAvePrc:', fAvePrc(ndaGoldHis,idxCdHis,idxMyDays,ifCountSelf)
        
        
        #                qq=polyfit(listT[0:idxCdHis+1],listX[0:idxCdHis+1],4)
        #                qq=polyfit(listT[0:idxCdHis+1],listX[0:idxCdHis+1],int(numpy.log10(idxCdHis+1)+1))
        #                xr=polyval(qq,range(0,idxCdHis+1))
        #                listNewX = (listX[0:idxCdHis+1]-xr)
        #                print 'listNewX, listT ,listX :', listNewX, listT[0:idxRow+1], listX[0:idxRow+1]
        #                time.sleep(1)
                        
        #                myAvePrc = fAvePrc(ndaGoldHis,idxCdHis,idxMyDays,ifCountSelf)
        #                myAvePrc = fAvePrcNrl(listNewX,idxCdHis,idxMyDays,ifCountSelf)
        
                        myAvePrc = fAvePrcNrl(dicNewX[idxCdHis],idxCdHis,idxMyDays,ifCountSelf)
        
        #                print 'myAvePrc:', myAvePrc
        #                if ndaGoldHis[idxCdHis][3]<myAvePrc:
        #                if listNewX[3] > myAvePrc: # 3-246, 4-248, 5-218168
        #                if listNewX[idxCdHis] < myAvePrc: # 
        #                print 'dicNewX[idxCdHis][idxCdHis]:', dicNewX[idxCdHis][idxCdHis]
        #                exit()
        #                if dicNewX[idxCdHis][idxCdHis] < myAvePrc: # <138, >100
                        meanDicNewX = numpy.mean(dicNewX[idxCdHis])
        #                print 'meanDicNewX:', meanDicNewX, '|  myAvePrc:', myAvePrc
                        if meanDicNewX+round(forStdEachNrm100X/100.0,2)*listStdNewX[idxCdHis] < myAvePrc: # <136015-
        
        #               if listNewX[5] > myAvePrc:
        #                if numpy.mean(listNewX) > myAvePrc:
        #                if numpy.mean(listNewX[0:idxCdHis]) < myAvePrc: # > 72-223271, < 50-153431
        #                if numpy.mean(listNewX[0:max(1,idxCdHis-10)]) < myAvePrc: # 136015
        #                if listNewX[idxCdHis] < myAvePrc:
        #                if myAvePrcLong > myAvePrc: # >44-203743, 10>73-223271
        
                            
        #                    print 'Try by'
                            listCnt[0][idxCdHis]=fgetByNum(idxCdHis,listCnt,listAcnt,forByRatio)
                            listAcnt[0][idxCdHis]=-listCnt[0][idxCdHis]*ndaGoldHis[idxCdHis][3]
                        else:
        #                    print 'Try Sl'
                            listCnt[0][idxCdHis]=-fGetSlNum(idxCdHis,listCnt,listAcnt,forSlRatio)
                            listAcnt[0][idxCdHis]=-listCnt[0][idxCdHis]*ndaGoldHis[idxCdHis][2]
        #                print 'listCount[0][idx1]:', listCount[0][idx1]
        #                print 'listAccount[0][idx1]:', listAccount[0][idx1]
                    
        #            print 'numpy.sum(listAccount[0,idx1]):', numpy.sum(listAccount[0])
        #            print 'numpy.sum(listCount[0][idx1]):', numpy.sum(listCount[0])
        #            print 'numpy.sum(listCount[0][idx1]):', numpy.sum(listCount[0])*ndaPhiStd[-1][2]
                    finalTotal = numpy.sum(listAcnt[0])+numpy.sum(listCnt[0])*ndaGoldHis[-1][2]
#                    print type(ndaResult)
#                    print idxMyDays, forByRatio, forSlRatio, forStdEachNrm100X
#                    print 'listMyDays.index(idxMyDays):', listMyDays.index(idxMyDays)
#                    exit()
                    if finalTotal/initialNumber > 1.5:
                        print 'len(listMyDays):', len(listMyDays), idxMyDays, listMyDays.index(idxMyDays)
                        print 'len(listByRatio):', len(listByRatio), forByRatio, listByRatio.index(forByRatio)
                        print 'len(listSlRatio):', len(listSlRatio), forSlRatio, listSlRatio.index(forSlRatio)
                        print 'len(listStdNrm100X):', len(listStdNrm100X), forStdEachNrm100X, listSlRatio.index(forSlRatio)
                        ndaResult[listMyDays.index(idxMyDays)][listByRatio.index(forByRatio)][listSlRatio.index(forSlRatio)][listStdNrm100X.index(forStdEachNrm100X)] = int(finalTotal)
                        line = ','.join([str(int(finalTotal)),str(round(forStdEachNrm100X/100.0,2))+' X',str(idxMyDays)+' days',str(forByRatio)+' by',str(forSlRatio)+' Sl']) + '\n'
                        resultfile.write(line)
        #            myCsvWriter.writerow(str(finalTotal))
        #            print 'finalTotal:', finalTotal, '| idxMyDays:', idxMyDays, '| idxByRatio10:', idxByRatio10, '| mySlRaio10:', mySlRaio10, '| idxCdHis:', idxCdHis
                    if finalTotal > maxFinalTotal:
                        maxFinalTotal_SlRatio=maxFinalTotal = finalTotal
                        theMaxmyDays_SlRatio=theMaxmyDays = idxMyDays
                        maxByRatio_SlRatio = maxByRatio = forByRatio
                        maxSlRatio_SlRatio = maxSlRatio = forSlRatio
    #        print 'Days:', idxMyDays, '| maxByR:', maxByRatio, '| maxSlRatio:', maxSlRatio, '| maxFinalTotal:', maxFinalTotal
#            print 'Days:', idxMyDays, '| maxByRatio:', maxByRatio, '| maxSlRatio:', maxSlRatio, '| maxFinalTotal:', maxFinalTotal, '|  forStdEachNrm100X:', forStdEachNrm100X
#print 'start idxMyDays:', idxMyDays, '| maxByRatio:', maxByRatio, '| maxSlRatio:', maxSlRatio, '| maxFinalTotal:', maxFinalTotal, '|  forStdEachNrm100X:', forStdEachNrm100X
#ndaResult.tofile('result.csv', sep=",", format="%d")
#numpy.savetxt('result3.csv', ndaResult, fmt='%d')
print 'lenCdHis:', lenCdHis
print 'ndaGoldHis[0][3]):', ndaGoldHis[0][3], ndaGoldHis[0][3]*lenCdHis
print 'ndaGoldHis[-1][2]:', ndaGoldHis[-1][2], ndaGoldHis[-1][2]*lenCdHis
print '(ndaGoldHis[-1][2]-ndaGoldHis[0][3]):', (ndaGoldHis[-1][2]-ndaGoldHis[0][3])
print (ndaGoldHis[-1][2]-ndaGoldHis[0][3])/ndaGoldHis[0][3]
print lenCdHis*(ndaGoldHis[-1][2]-ndaGoldHis[0][3])
#exit()

print 'numpy.amax(ndaResult):', numpy.amax(ndaResult)


print 'maxFinalTotal:', maxFinalTotal
#print 'theMaxmyDays', theMaxmyDays
print 'maxByRatio:', maxByRatio
print 'maxSlRatio:', maxSlRatio
print (lenCdHis*ndaGoldHis[-1][2]-lenCdHis*ndaGoldHis[0][3])/lenCdHis*ndaGoldHis[0][3]