from lxml import html

parser = html.etree.HTMLParser()
tree = html.etree.parse("jd.html",parser=parser)
res = tree.xpath("/html")



print(res)

