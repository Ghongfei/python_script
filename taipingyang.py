import re
import os
import urllib.request
import time
import random


# 创建 A——Z文件夹
def createLetterfile(name):
    path = 'E:/taipingyang/' + name
    isExists=os.path.exists(path)
    if not isExists:
        os.mkdir(path) 
    else:
        return False


#创建字母里的文件夹
def createLettertypefile(letter, name):
    path = 'E:/taipingyang/' + letter + '/' + name
    isExists=os.path.exists(path)
    if not isExists:
        os.mkdir(path) 
    else:
        return False


#创建字母里的文件夹的文件夹
def createLettertypefilee(letter, letter2, name2):
    path = 'E:/taipingyang/' + letter + '/' + letter2 + '/' + name2
    isExists=os.path.exists(path)
    if not isExists:
        os.mkdir(path) 
    else:
        return False


#创建字母里的文件夹的文件夹
def createLettertypefileee(letter, letter2, name2, name3):
    path = 'E:/taipingyang/' + letter + '/' + letter2 + '/' + name2 + '/' + name3
    isExists=os.path.exists(path)
    if not isExists:
        os.mkdir(path) 
    else:
        return False

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
cou = 1

f = open('E:/taipingyang/taipingyang.txt',mode='r',encoding='UTF-8')
data = f.read()
f.close()

letterslist = re.findall('<li class="pictreeTit">(.*?)</li>',data)
#print(letterslist)

lettera = re.findall('treeTit">(.*?)</li><li class="pic',data)

z = 'Z</li><li class="closeChild" id="pictree_307"><a onclick="switchSmallTypeFrame(\'307\');return false;" class="emBox"><i></i></a><a name="VA" id="pictext_a_307" title="众泰" href="//price.pcauto.com.cn/cars/nb307/" class="ppLink"><em class="logo"><img src="//www.pcauto.com.cn/blank.gif" src2="//img.pcauto.com.cn/images/upload/upc/tx/auto5/1811/02/c16/117317344_1541140894111_50x50.png" alt="" width="30" height="30"></em><em class="sname">众泰</em><span class="snum"> (36876) </span></a><ul id="subTable307" class="subTable"></ul></li><li class="closeChild" id="pictree_104"><a onclick="switchSmallTypeFrame(\'104\');return false;" class="emBox"><i></i></a><a name="VA" id="pictext_a_104" title="中华" href="//price.pcauto.com.cn/cars/nb104/" class="ppLink"><em class="logo"><img src="//www.pcauto.com.cn/blank.gif" src2="//img2.pcauto.com.cn/pcauto/1011/29/1328212_zhonghua.png" alt="" width="30" height="30"></em><em class="sname">中华</em><span class="snum"> (17085) </span></a><ul id="subTable104" class="subTable"></ul></li><li class="closeChild" id="pictree_929"><a onclick="switchSmallTypeFrame(\'929\');return false;" class="emBox"><i></i></a><a name="VA" id="pictext_a_929" title="知豆" href="//price.pcauto.com.cn/cars/nb929/" class="ppLink"><em class="logo"><img src="//www.pcauto.com.cn/blank.gif" src2="//img.pcauto.com.cn/images/upload/upc/tx/auto5/1712/01/c17/68320453_1512113322181_50x50.png" alt="" width="30" height="30"></em><em class="sname">知豆</em><span class="snum"> (2423) </span></a><ul id="subTable929" class="subTable"></ul></li><li class="closeChild" id="pictree_125"><a onclick="switchSmallTypeFrame(\'125\');return false;" class="emBox"><i></i></a><a name="VA" id="pictext_a_125" title="中兴" href="//price.pcauto.com.cn/cars/nb125/" class="ppLink"><em class="logo"><img src="//www.pcauto.com.cn/blank.gif" src2="//img2.pcauto.com.cn/pcauto/1011/29/1328156_zhongxing.png" alt="" width="30" height="30"></em><em class="sname">中兴</em><span class="snum"> (2043) </span></a><ul id="subTable125" class="subTable"></ul></li><li class="closeChild" id="pictree_506"><a onclick="switchSmallTypeFrame(\'506\');return false;" class="emBox"><i></i></a><a name="VA" id="pictext_a_506" title="中欧" href="//price.pcauto.com.cn/cars/nb506/" class="ppLink"><em class="logo"><img src="//www.pcauto.com.cn/blank.gif" src2="//img2.pcauto.com.cn/pcauto/1010/19/1289002_zhongo.jpg" alt="" width="30" height="30"></em><em class="sname">中欧</em><span class="snum"> (933) </span></a><ul id="subTable506" class="subTable"></ul></li><li class="closeChild" id="pictree_7281"><a onclick="switchSmallTypeFrame(\'7281\');return false;" class="emBox"><i></i></a><a name="VA" id="pictext_a_7281" title="正道汽车" href="//price.pcauto.com.cn/cars/nb7281/" class="ppLink"><em class="logo"><img src="//www.pcauto.com.cn/blank.gif" src2="//img.pcauto.com.cn/images/upload/upc/tx/auto5/1704/24/c18/44435450_1493020900520_50x50.png" alt="" width="30" height="30"></em><em class="sname">正道汽车</em><span class="snum"> (180) </span></a><ul id="subTable7281" class="subTable"></ul></li><li class="closeChild" id="pictree_325"><a onclick="switchSmallTypeFrame(\'325\');return false;" class="emBox"><i></i></a><a name="VA" id="pictext_a_325" title="中顺" href="//price.pcauto.com.cn/cars/nb325/" class="ppLink"><em class="logo"><img src="//www.pcauto.com.cn/blank.gif" src2="//img3.pcauto.com.cn/pcauto/1011/29/1328198_zs.png" alt="" width="30" height="30"></em><em class="sname">中顺</em><span class="snum"> (33) </span></a><ul id="subTable325" class="subTable"></ul></li><li class="closeChild" id="pictree_866"><a onclick="switchSmallTypeFrame(\'866\');return false;" class="emBox"><i></i></a><a name="VA" id="pictext_a_866" title="之诺" href="//price.pcauto.com.cn/cars/nb866/" class="ppLink"><em class="logo"><img src="//www.pcauto.com.cn/blank.gif" src2="//img0.pcauto.com.cn/pcauto/1311/08/3375004_5050png.png" alt="" width="30" height="30"></em><em class="sname">之诺</em><span class="snum"> (173) </span></a><ul id="subTable866" class="subTable"></ul></li><li class="closeChild" id="pictree_1043"><a onclick="switchSmallTypeFrame(\'1043\');return false;" class="emBox"><i></i></a><a name="VA" id="pictext_a_1043" title="Zenvo" href="//price.pcauto.com.cn/cars/nb1043/" class="ppLink"><em class="logo"><img src="//www.pcauto.com.cn/blank.gif" src2="//img.pcauto.com.cn/images/upload/upc/tx/auto5/1503/05/c22/3522517_1425548851752_50x50.png" alt="" width="30" height="30"></em><em class="sname">Zenvo</em><span class="snum"> (54) </span></a><ul id="subTable1043" class="subTable"></ul>'

lettera.append(z)
letterbb = []
letterccc = []
#print(lettera)
for index0,a in enumerate(lettera):
    #if index0 == 0:
    letter = a[0]
    #createLetterfile(letter)
    letterb = re.findall('<a name="VA" id="pictext_.*?" title="(.*?)" href=".*?" class="ppLink">',a)
    #for b in letterb:
        #createLettertypefile(letter, b)
    letterblink = re.findall('<a name="VA" id="pictext_.*?" title=".*?" href="(.*?)" class="ppLink">',a)
    #print(letterblink)
    for index,blink in enumerate(letterblink):
        #if index >= 1:
        time.sleep(random.random()*2)
        blink = 'http:'+ blink
        try:
            req4 = urllib.request.Request(blink, headers=header)
            bPage=urllib.request.urlopen(req4)
        except Exception:
            pass
        bdata = bPage.read()
        bdata = bdata.decode('gb2312','ignore')
        bdata = bdata.replace('\n', '')
        bdata = bdata.replace('\r', '')
        letterc = re.findall('<div class="modA">(.*?)</div></div>',bdata)
        for c in letterc:
            lettercc = re.findall('<em class="mark">(.*?)</em>',c)[0].strip()
            #print(lettercc)
            #createLettertypefilee(letter, letterb[index], lettercc)

            letterd = re.findall('<p title=".*?">(.*?)<em>.*?</em></p>',c)
            if letterd[-3:] == '...':
                letterd = letterd[:-3]
            #for d in letterd:
                #d = d.replace('/','-').replace(':', '').strip()
                #createLettertypefileee(letter, letterb[index], lettercc, d)
            
            letterdlink = re.findall('<li class="picCen"><a href="(.*?)"><img src=', c)
            #print(letterdlink)
            for index1,dlink in enumerate(letterdlink):
                if letterd[index1][-3:] == '...':
                    letterd[index1] = letterd[index1][:-3]
                dlink = 'http://price.pcauto.com.cn/' + dlink[:-1] + '-o1-1-10/#picScroll'
                
                req3 = urllib.request.Request(dlink, headers=header)
                dPage=urllib.request.urlopen(req3)
                ddata = dPage.read()
                ddata = ddata.decode('gb2312','ignore')
                ddata = ddata.replace('\n', '')
                ddata = ddata.replace('\r', '')
                ddlink = re.findall('<li class="picCen"><a target="_blank" href="(.*?)"><div class="imgWrap">',ddata)
                for ddd in ddlink:
                    ddd = 'http://price.pcauto.com.cn/' + ddd
                    #print(ddd)
                    req2 = urllib.request.Request(ddd, headers=header)
                    ddPage=urllib.request.urlopen(req2)
                    dddata = ddPage.read()
                    dddata = dddata.decode('gb2312','ignore')
                    dddata = dddata.replace('\n', '')
                    dddata = dddata.replace('\r', '')
                    print(dddata)
                    dddlink = re.findall("picurl01='(.*?)',picurl02",dddata)
                    print(dddlink)
                    dddlink = dddlink[0]
                    if dddlink[0:3] != 'htt':
                        dddlink = 'http:'+dddlink
                    dddtitle = re.findall('<p class="name fz14">(.*?)</p><span class="price vam">',dddata)
                    if dddtitle != []:
                        dddtitle = dddtitle[0].replace(' ','-')
                    else:
                        dddtitle = re.findall('<p class="name fz14">(.*?)</p></dd></dl>',dddata)[0].replace(' ','-')
                    #print(dddlink)
                    req1 = urllib.request.Request(dddlink, headers=header)
                    itdata = 1
                    try:
                        with urllib.request.urlopen(req1) as web:
                            itdata = web.read()
                    except Exception as e:
                            page = e.partial
                            itdata = page
                    imggname = 'E:/taipingyang/taipingyang/'+letter+'/'+letterb[index]+ '/'+lettercc+'/'+ letterd[index1] +'/'+str(cou)+'_'+dddtitle+'.jpg'
                    print(imggname)
                    if os.path.exists(imggname) == True:
                        cou += 1
                        print('allready in the fire')
                        continue
                    else:
                        f = open(imggname,"wb")
                        cou += 1
                        f.write(itdata)
                        f.close()
                        print('ok')
                cou = 1
