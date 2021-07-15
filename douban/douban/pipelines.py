from itemadapter import ItemAdapter
import os
import time
import xlwt
import xlrd
from xlutils.copy import copy


class DoubanPipeline:

    # def __init__(self):
    #     self.filename = 'output'
    #     if not os.path.exists(self.filename):
    #         os.mkdir(self.filename)
    #
    # def process_item(self, item, spider):
    #
    #     now = time.strftime('%Y%m%d',time.localtime())
    #     jsonfile = 'douban_' + now + '.json'
    #
    #     try:
    #         with open(self.filename + os.sep + jsonfile,'a') as f:
    #             data = json.dumps(dict(item),ensure_ascii=False) + '\n'
    #             f.write(data)
    #     except:
    #         print('error')
    # 构造方法：创建一个excel文件以及内容模板
    def __init__(self):

        foldname = 'output'
        now = time.strftime('%Y-%m-%d', time.localtime())
        fliename = 'douban_excle_' + now + '.xls'

        # 最终文件路径
        self.exclepath = foldname + '/' + fliename

        # 构建workbook工作簿
        self.workbook = xlwt.Workbook(encoding = 'UTF-8')

        # 创建sheet工作页
        self.sheet = self.workbook.add_sheet(u'豆瓣电影')

        # 设置excel内容标题
        headers = ['排名', '电影名称']

        # 设置标题文字样式
        headstyle = xlwt.easyxf('font:color-index black,bold on')

        # for循环写入标题内容
        for colindex in range(0, len(headers)):

            # 按照规定好的字体样式将标题内容写入
            self.sheet.write(0, colindex, headers[colindex], headstyle)

        # 保存创建好的excel文件
        self.workbook.save(self.exclepath)

        # 全局变量行数
        self.rowindex = 1

    def process_item(self, item, spider):

        # 读取已经创建好的excel文件
        oldwb = xlrd.open_workbook(self.exclepath, formatting_info=True)
        # 拷贝一个副本
        newwb = copy(oldwb)
        # 获取到excel要操作的sheet工作页
        sheet = newwb.get_sheet(0)
        # 将采集到的数据转换成一个list列表
        line = [item['rank'], item['title']]
        # 使用for循环遍历excel中的每一个cell格（行，列）
        for colindex in range(0, len(item)):
            # 将数据写入到指定的行列中去
            sheet.write(self.rowindex, colindex, line[colindex])

        # 完毕后保存excel文件，自动覆盖原有的文件
        newwb.save(self.exclepath)

        print('完成写入！')
        # 全局的行变量自增1
        self.rowindex = self.rowindex + 1
        return item
