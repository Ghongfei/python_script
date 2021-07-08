import urllib.request
import re
import os

url = 'https://car.autohome.com.cn'

rooturl = 'https://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx?typeId=2%20&brandId=0%20&fctId=0%20&seriesId=0'
webPage=urllib.request.urlopen(rooturl)
data = webPage.read()
data = data.decode('gb2312','ignore')
#print(data)


k = re.split(r"<div class='cartree-letter'>",data)
k = k[1:-1]
#print(k)

# 创建 A——Z文件夹
def createLetterfile(name):
    path = 'E:/carpic1/' + name
    isExists=os.path.exists(path)
    if not isExists:
        os.mkdir(path) 
    else:
        return False


#创建字母里的文件夹
def createLettertypefile(letter, name):
    path = 'E:/carpic1/' + letter + '/' + name
    isExists=os.path.exists(path)
    if not isExists:
        os.mkdir(path) 
    else:
        return False



#创建字母里的文件夹的文件夹
def createLettertypefilee(letter, letter2, name2):
    path = 'E:/carpic1/' + letter + '/' + letter2 + '/' + name2
    isExists=os.path.exists(path)
    if not isExists:
        os.mkdir(path) 
    else:
        return False


        


cou = 1

for index1,letterlist in enumerate(k):
    # 创建 A——Z文件夹
    #createLetterfile(letterlist[0])
    
    l = re.split(r"<li id=",letterlist)
    for index2,lettertype in enumerate(l):
        
         ltype = re.search(r"icon10-sjr'></i>(.*?)<em>", lettertype).group(1)
         #创建字母里的文件夹
         #createLettertypefile(letterlist[0],ltype)
         
         ltypealink = re.search(r"<a href='(.*?)'><i ", lettertype).group(1)
         alink = url + ltypealink
         webPage2 = urllib.request.urlopen(alink)
         data2 = webPage2.read()
         data2 = data2.decode('gb2312','ignore')
         k2 = re.search(r'<div class="uibox-con carpic-list02"><ul>(.*?)</ul></div></div></div></div>', data2).group(1)
         lik2 = k2.split('<li>')[1:]
         for lik22 in lik2:
             piclistlink = url + re.search(r'</a><div><span class="fn-left"><a href="(.*?)"  title=".*?图片">.*?</a>(.*?张)',lik22).group(1)
             piclistname = re.search(r'</a><div><span class="fn-left"><a href=".*?"  title=".*?图片">(.*?)</a>(.*?张)',lik22).group(1)
             piclistname = piclistname.replace('/','-').replace(':', '').strip()
             #createLettertypefilee(letterlist[0],ltype,piclistname)
             #print(piclistlink)
             webPage3 = urllib.request.urlopen(piclistlink)
             data3 = webPage3.read()
             data3 = data3.decode('gb2312','ignore')
             #print(data3)
             data3 = data3.replace(' ', '')
             data3 = data3.replace('\n', '')
             data3 = data3.replace('\r', '')
             k3 = re.search(r'<divclass="cartab-title">(.*?)<divclass="choise-contma-b-10">', data3).group(1)
             #print(k3)
             
             moreone = k3.split('更多')[0]
             #print(moreone)
             try:
                 moreone = url + re.search(r'</span><ahref="(.*?)"class="more"', moreone).group(1)
             except Exception:
                continue
             webPage4 = urllib.request.urlopen(moreone)
             data4 = webPage4.read()
             data4 = data4.decode('gb2312','ignore')
             data4 = data4.replace(' ', '')
             data4 = data4.replace('\n', '')
             data4 = data4.replace('\r', '')
             
             k4 = re.search(r'<divclass="cartab-title">(.*?)<divclass="choise-contma-b-10">', data4).group(1)
             #print(k4)
             moreone1 = k4.split('<li><ahref="')[1:]
             #print(moreone1)
             for aaa in moreone1:
                 #print(aaa)
                 #bbb = aaa.split()
                 moreonelink = url + re.search(r'</a><div><ahref="(.*?)"title=".*?"target="_blank">.*?</a></div>', aaa).group(1)
                 print(moreonelink)
                 moreonetitle = re.search(r'</a><div><ahref=".*?"title=".*?"target="_blank">(.*?)</a></div>', aaa).group(1)
                    
                 

                 webPage5 = urllib.request.urlopen(moreonelink)
                 data5 = webPage5.read()
                 data5 = data5.decode('gb2312','ignore')
                 k5 = re.search(r'<img id="img" src="(.*?)" onside="-1" />', data5).group(1)
                    
                 finnallink = 'https:' + k5
                 #print(finnallink)
                 web = urllib.request.urlopen(finnallink)
                 itdata = web.read()
                 imggname = 'E:/carpic1/'+letterlist[0]+'/'+ltype+ '/'+piclistname+'/'+str(cou)+'_'+moreonetitle.replace(' ','-')+'.jpg'
                 if os.path.exists(imggname) == True:
                      continue
                 else:
                      f = open(imggname,"wb")
                      cou += 1
                      f.write(itdata)
                      f.close()
                      print(imggname)

'''
            typealink.append(alink)
            webPage2 = urllib.request.urlopen(alink)
            data2 = webPage2.read()
            data2 = data2.decode('gb2312','ignore')
            data2 = data2.replace(' ', '')
            data2 = data2.replace('\n', '')
            data2 = data2.replace('\r', '')
            k2 = re.search(r'height:1500px;"><scripttype="text/javascript"src="(.*?)"></script><divid="carBottom"style="height:800px;">', data2)
            
            url3 = url + k2.group(1)
            webPage3 = urllib.request.urlopen(url3)
            data3 = webPage3.read()
            data3 = data3.decode('gb2312','ignore')
            k3 = re.split(r'<dd>', data3)
            k3 = k3[1:]
            
            for k3name in k3:
                k3nameitem = re.search(r"<a id='series_.*?' href='/pic/series/.*?.html'>(.*?)<em>.*?</em></a></dd>", k3name)
                detailtype.append(k3nameitem.group(1))
                k3nameitem1 = re.search(r"<a id='series_.*?' href='(.*?)'>.*?<em>.*?</em></a></dd>", k3name)

                url4 = url + k3nameitem1.group(1)
                
                webPage4 = urllib.request.urlopen(url4)
                data4 = webPage4.read()
                data4 = data4.decode('gb2312','ignore')

                k4 = re.search(r'<li class="last"><a href="(.*?)"><i class=', data4)
                
                if k4 == None:
                    data4 = data4.replace(' ', '')
                    data4 = data4.replace('\n', '')
                    data4 = data4.replace('\r', '')

                    kdata4 = re.search(r'<divclass="cartab-title"><h2class="fn-leftcartab-title-name">(.*?)</a></div></li></ul></div></div>', data4)
                    zuzonglink1 = kdata4.group(1).split('<li>')
                    zuzonglink1 = zuzonglink1[1:]
                    for zzlink1 in zuzonglink1:
                        zzonglink1 = re.search(r'<ahref="(.*?)"title=".*?"target="_blank"><img', zzlink1)
                        zzongtitle1 = re.search(r'<ahref=".*?"title="(.*?)"target="_blank"><img', zzlink1)
                        url6 = url + zzonglink1.group(1)
                        
                        webPage6 = urllib.request.urlopen(url6)
                        data6 = webPage6.read()
                        data6 = data6.decode('gb2312','ignore')

                        imglinkk1 = re.search(r'<img id="img" src="(.*?)" onside="-1" />', data6)

                        imglinkkk1 = 'https:'+ imglinkk1.group(1)
                        
                        
                        web = urllib.request.urlopen(imglinkkk1)
                        itdata = web.read()

                        imggname = 'E:/carpic/'+letterlists[-1]+'/'+lettertypes[-1]+ '/'+detailtype[-1].strip()+'/'+str(cou)+'_'+zzongtitle1.group(1).replace(' ','-')+'.jpg'
                        if os.path.exists(imggname) == True:
                            continue
                        else:
                            f = open(imggname,"wb")
                               
                            cou += 1
                                
                            f.write(itdata)
                            f.close()
                            print(imggname)
                        
                else:
                    url5 = url + k4.group(1)
                   
                    
                    webPage5 = urllib.request.urlopen(url5)
                    data5 = webPage5.read()
                    data5 = data5.decode('gb2312','ignore')

                    k5 = re.search(r'<div class="uibox-con carpic-list03 border-b-solid"><ul>(.*?)</li></ul></div></div>', data5)
                    if k5 == None:
                        continue
                    zuzonglink = k5.group(1).split('<li>')
                    zuzonglink = zuzonglink[1:]
                    for zzlink in zuzonglink:
                        zzonglink = re.search(r'<a href="(.*?)" title=".*?" target="_blank"><img', zzlink)
                        zzongtitle = re.search(r'<a href=".*?" title="(.*?)" target="_blank"><img', zzlink)
                        url7 = url + zzonglink.group(1)
                        
                        webPage7 = urllib.request.urlopen(url7)
                        data7 = webPage7.read()
                        data7 = data7.decode('gb2312','ignore')

                        imglinkk = re.search(r'<img id="img" src="(.*?)" onside="-1" />', data7)

                        imglinkkk = 'https:'+imglinkk.group(1)
                        
                        
                        web = urllib.request.urlopen(imglinkkk)
                        itdata = web.read()

                        imggname1 = 'E:/carpic/'+letterlists[-1]+'/'+lettertypes[-1]+ '/'+detailtype[-1].strip()+'/'+str(cou)+'_'+zzongtitle.group(1).replace(' ','-')+'.jpg'
                        if os.path.exists(imggname1) == True:
                            continue
                        else:
                            f = open(imggname1,"wb")
                               
                            cou += 1
                                
                            f.write(itdata)
                            f.close()
                            print(imggname1)
                 
           
            print(detailtype)
            try:
                createLettertypefilee(letterlists[-1],lettertypes[-1],detailtype)
            except Exception:
                pass
            
            detailtype = []
            
        #createLettertypefile(letterlists[index1],lettertypes)
        #lettertypes = []
        

#print(typealink)    
'''








