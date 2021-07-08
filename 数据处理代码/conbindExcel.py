import xlrd
import xlsxwriter
import os
filelist = os.listdir('D:/学校')
dict1 = ['珠海', '汕头', '佛山', '广州', '深圳',
         '韶关', '河源', '梅州', '惠州',  '汕尾',
         '东莞', '中山', '江门', '阳江', '湛江',
         '茂名', '肇庆', '清远', '潮州', '揭阳', '云浮']
name = ['高中', '初中', '中等职业学校', '特殊教育学校', '普通高等学校', '工读学校']
zhongxue = []
other = []
for city in dict1:
    for files1 in filelist:
        # .xlsx
        xmlname1 = os.path.splitext(files1)[1]
        xmlname0 = os.path.splitext(files1)[0]
        #print(xmlname0[-3:])
        if xmlname0[-3:] == city + ')':
            if xmlname0[:-4] == '高中' or xmlname0[:-4] == '初中':
                zhongxue.append('D:/学校/'+xmlname0+xmlname1)
            if xmlname0[:-4] == '中等职业学校' or xmlname0[:-4] == '特殊教育学校' or xmlname0[:-4] == '普通高等学校' or xmlname0[:-4] == '工读学校':
                other.append('D:/学校/'+xmlname0+xmlname1)

    print(other)
    if zhongxue != [] and other != []:
        # source_xls1 = [zhongxue[0], zhongxue[1]]
        # target_xls1 = 'D:/学校/中学('+ city +').xlsx'
        #
        # # 读取数据
        # data = []
        # for i in source_xls1:
        #     wb = xlrd.open_workbook(i)
        #     for sheet in wb.sheets():
        #         for rownum in range(sheet.nrows):
        #             data.append(sheet.row_values(rownum))
        # print(data)
        # # 写入数据
        # workbook = xlsxwriter.Workbook(target_xls1)
        # worksheet = workbook.add_worksheet()
        # font = workbook.add_format({"font_size": 11})
        # for i in range(len(data)):
        #     for j in range(len(data[i])):
        #         worksheet.write(i, j, data[i][j], font)
        # # 关闭文件流
        # workbook.close()
        # zhongxue = []



        source_xls2 = [other[0], other[1], other[2], other[3]]
        target_xls2 = 'D:/学校/其他('+ city +').xlsx'

        # 读取数据
        data = []
        for i in source_xls2:
            wb = xlrd.open_workbook(i)
            for sheet in wb.sheets():
                for rownum in range(sheet.nrows):
                    data.append(sheet.row_values(rownum))
        print(data)
        # 写入数据
        workbook = xlsxwriter.Workbook(target_xls2)
        worksheet = workbook.add_worksheet()
        font = workbook.add_format({"font_size":11})
        for i in range(len(data)):
            for j in range(len(data[i])):
                worksheet.write(i, j, data[i][j], font)
        # 关闭文件流
        workbook.close()
        other = []