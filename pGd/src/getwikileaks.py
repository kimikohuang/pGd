# -*- coding: utf-8 -*-  

import http.client
import os
import sys
import ftplib
import re


from html.parser import HTMLParser
import time
import random
import subprocess
import urllib.request, urllib.error, urllib.parse
import time


def getKimiHtml(kimiUrl):
    http.client.HTTPConnection.debuglevel = 1
    #request = urllib2.Request('http://diveintomark.org/xml/atom.xml')
#    request = urllib2.Request('http://213.251.145.96/reldate/2010-12-08_0.html')
    request = urllib.request.Request(kimiUrl)
    
    request.add_header('Accept-encoding', 'gzip')        
    opener = urllib.request.build_opener()
    f = opener.open(request)
    compresseddata = f.read()
    len(compresseddata)
    
    import io
    compressedstream = io.StringIO(compresseddata)   
    
    import gzip
    gzipper = gzip.GzipFile(fileobj=compressedstream)      
    data = gzipper.read()                                  
    return data

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.htmlData = []
        self.found = False
        self.stop = False
        self.findDataStart = 'start'
        self.findDataStop = 'end'
 
    def handle_starttag(self, tag, attrs):
#        print "Encountered the beginning of a %s tag" % tag
        #if tag == "a":
        if self.found and not(self.stop):
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "href":
                        self.links.append(value)
                        
#    def handle_endtag(self, tag):
#        print "Encountered the end of a %s tag" % tag
        
    def handle_data(self, data):  
        """處理標籤以外的資料，也就是網頁中的文字"""  
  
        data = data.strip()  
  
        # 如果台中地區已出現過，就記錄天氣資訊  
#        if hasattr(self, 'found') and data:  
        if data and self.found and not(self.stop):
            # 到了彰化地區，中止解析  
#            if data == u'Browse by creation':  
            if data == self.findDataStop:  
                
                print('the stop string was found!: '+ data)
                self.stop = True  
                return  
            self.htmlData.append(data)  
            print(data)
  
        # 出現台中地區  
        # 設定旗標以通知後面幾次呼叫記下資訊  
#        if data == u'Browse latest releases':  
        if data == self.findDataStart:  
            self.found = True  
            self.htmlData = []  
#            self.htmlData.append(data)  
  
        
if __name__ == "__main__":
    NumGetDays = 2
    idxTotalFile = 0
    sleepSecMin = 0
    sleepSecMax =3
#    
#    html_code = """
#    <a href="www.google.com"> google.com</a>
#    <A Href="www.pythonclub.org"> PythonClub </a>
#    <A HREF = "www.sina.com.cn"> Sina </a>
#    """
    file = 'wikileaks.txt'
#    conn = httplib.HTTPConnection("213.251.145.96")
##    request = urllib2.Request('http://213.251.145.96/reldate/2010-12-08_0.html')
##    request.add_header("Accept", "text/plain")
##    headers = {"Accept": }  
#
#    #conn.request("GET", "/reldate/2010-12-08_0.html")
##    conn.request("GET", "/cablegate.html")
#    conn.putrequest("GET", "/cablegate.html")
#
##    conn.request.add_header
#
#    conn.putheader("Content-Type", "text/xml; charset=\"utf-8\"")
##    conn.putheader("Content-Length", str(len(data)))
#    conn.endheaders()
#    
#    response = conn.getresponse()
#    lHeaders = response.getheaders()
#    print lHeaders
#    html_code = response.read()
    
    
    
#    conn.close()
    html_code = getKimiHtml('http://213.251.145.96/cablegate.html')
    print(html_code)
#    exit()
    

    
    #filename = str(os.path.abspath(os.path.dirname(sys.argv[0])) + "\\"+file) #Create file
    FILE = open(file,"w") #Open file ready for writing
    FILE.writelines(html_code) #Write 'data' to file
    FILE.close() #Close file

    
    hp = MyHTMLParser()
    hp.findDataStart = 'Browse latest releases'
    hp.findDataStop = 'Browse by creation'
    hp.feed(html_code)
    hp.close()
    print("hp.links: ")
    print(hp.links)
    print("htmlData: ")
    print(hp.htmlData)
#    exit()
#===============================================================================
#    for myDate in hp.links[2:3]:
#    for myDate in hp.links[0:NumGetDays]:

#    myDateTmp = []
#    for w in hp.links[0:]:
#        print 'w: ', w, len(w)
#        if len(w)==10:
#            myDateTmp.append(w)
#        print 'myDateTmp:', myDateTmp
#        exit()
#    myDateTmp = [w for w in hp.links[0:] if len(w)==26]
#    content = [wnl.lemmatize(t) for t in tokensTmp]
#    print 'myDateTmp: ', myDateTmp
#    for myDate in hp.links[0:]:
    for myDate in [w for w in hp.links[0:] if len(w)==26]:
#    for myDate in myDateTmp:
        print('myDate: ', myDate)
#        conn = httplib.HTTPConnection("213.251.145.96")
#        #conn.request("GET", "/reldate/2010-12-08_0.html")
#        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
##        conn.request.add_header( "Accept-Encoding", "identity" )
##        conn.putheader(header, value)
##        conn.request("GET", myDate,headers)
#        conn.request("GET", myDate)
#
#
#        
#        response = conn.getresponse()
#        lHeaders = response.getheaders()
#        html_code = response.read()
#
#
#        conn.close()
        html_code = getKimiHtml('http://213.251.145.96'+myDate)
#        html_code = getKimiHtml('http://213.251.145.96/cablegate.html')

#        print "html_code: " + html_code
        
##        hp = MyHTMLParser()
#        del hp
        hp = MyHTMLParser()
        hp.findDataStart = 'Browse by '+myDate[9:13]+'/'+myDate[14:16]+'/'+myDate[17:19]
        print("hp.findDataStart: " + hp.findDataStart)
        hp.findDataStop = "Reference ID"

        try:
            hp.feed(html_code)
        except:
            print(html_code)
            raise
        print("hp.links: ")
        print(hp.htmlData)
        print("htmlData: ")
        numKeep = 1
        for i in hp.htmlData:
            if (i.isdigit() and int(i)>numKeep):
                numKeep = int(i)
        print("max numKeep: ", numKeep)
#        lReleaseDate = hp.htmlData 
#        print lReleaseDate
#        exit()
        hp.close()
        del hp
#===============================================================================
        for idxPage in range(0,numKeep):
#        for idxPage in [1:int(lReleaseDate[-1])]:
#            conn = httplib.HTTPConnection("213.251.145.96")
#            #conn.request("GET", "/reldate/2010-12-08_0.html")
            myUrl = myDate[0:-6]+str(idxPage)+'.html'
#            print 'myUrl: ' + myUrl
#            conn.request("GET", myUrl)
##            conn.request("GET", myDate[0:-6]+str(idxPage)+'.html')
#            
#            response = conn.getresponse()
#            lHeaders = response.getheaders()
#            html_code = response.read()
##            print "html_code: " + html_code
#    
#            conn.close()
            html_code = getKimiHtml('http://213.251.145.96'+myUrl)
#            html_code = getKimiHtml('http://213.251.145.96/cablegate.html')
            
    #        print html_code
            print('start parser record: ')
            hp = MyHTMLParser()
#            hp.reset
            hp.findDataStart = 'Created'
            hp.findDataStop = ".."
            hp.feed(html_code)
            print("hp.links record: ")
            print(hp.links)
#            exit()
#            tokensTmp = [w for w in tokens if w.isalpha() and (w.lower() not in myStopwords)]
#       
            lCableLinks = [i for i in hp.links if i[0:7]=="/cable/"]
            print("lCalbeLinks: ", lCableLinks)
#            print "htmlData: "
#            print hp.htmlData
            hp.close()
            time.sleep(random.randint(sleepSecMin,sleepSecMax))
            #===============================================================================
            
#            for myUrl2 in lCableLinks:
#                print myUrl2  
            for myUrl2 in lCableLinks:
                print('myUrl2: ', myUrl2)
#                FileNameTraining = '.'+myUrl2[0:-5]+'.txt'
                FileNameTraining = '/home/kimiko'+myUrl2[0:-5]+'.txt'
                print("FileNameTraining: ", FileNameTraining)
                if os.path.isfile(FileNameTraining):
                    print(FileNameTraining, 'Already exist: ', myUrl2)
                    continue
                FileNameTrainingTmp = '/home/kimiko/cable_'+time.strftime("%y%m%d")+myUrl2[0:-5]+'.txt'
                print("FileNameTrainingTmp: ", FileNameTrainingTmp)
#                exit()
#                conn = httplib.HTTPConnection("213.251.145.96")
#                print 'New article myUrl: ' + myUrl2
#                conn.request("GET", myUrl2)
#    #            conn.request("GET", myDate[0:-6]+str(idxPage)+'.html')
#                
#                response = conn.getresponse()
#                lHeaders = response.getheaders()
#                html_code = response.read()
#    #            print "html_code: " + html_code
#        
#                conn.close()
        #        print html_code
                html_code = getKimiHtml('http://213.251.145.96'+myUrl2)
#                html_code = getKimiHtml('http://213.251.145.96/cablegate.html')

                print('start parser record: ')
                hp = MyHTMLParser()
    #            hp.reset

                hp.findDataStart = 'Released'
                print("hp.findDataStart: " + hp.findDataStart)
                hp.findDataStop = "NO END Text"

                hp.feed(html_code)
#                print 'hp.htmlData: ', hp.htmlData
                hp.close()

                myText = ' '.join(hp.htmlData).replace('¶','\n')
#                if (myText.lower().find('taiwan')==-1 or myText.lower().find('taipei')==-1 or myText.lower().find('dpp')==-1 or myText.lower().find('kmt')==-1):
#                    continue
                
                #----------------------------------------------------------------
#                SubDataDir = os.getcwd()+myUrl2[0:15]
#                os.path.dirname(FileNameTraining)
#                print 'SubDataDir: ', SubDataDir
#                if not(os.path.isdir(SubDataDir)):
##                    os.mkdir(SubDataDir)
#                    subprocess.call(['mkdir', '-p', SubDataDir])

                if not(os.path.isdir(os.path.dirname(FileNameTraining))):
                    subprocess.call(['mkdir', '-p', os.path.dirname(FileNameTraining)])


#                SubDataDir = os.getcwd()+os.path.basename(dfile)[0:len(os.path.basename(dfile))-4]+'/'
                
                with open(FileNameTraining, 'w') as eachFile:
#                    eachFile.write('%d\n' % number)
                    eachFile.write(myText)


                if not(os.path.isdir(os.path.dirname(FileNameTrainingTmp))):
                    subprocess.call(['mkdir', '-p', os.path.dirname(FileNameTrainingTmp)])

                with open(FileNameTrainingTmp, 'w') as eachFile:
                    eachFile.write(myText)
#                    eachFile.write(' '.join(hp.htmlData).replace('¶','\n'))
#                    eachFile.write(hp.htmlData.encode("utf-8"))
                idxTotalFile = idxTotalFile+1
                print('save file number: '+ str(idxTotalFile))

                print('sleep!')
                time.sleep(random.randint(sleepSecMin,sleepSecMax))
exit()
