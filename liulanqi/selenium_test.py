from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys


#创建浏览器对象
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#打印页面标题“百度一下你就知道”
# print(driver.title)

#生成当前页面快照
# driver.save_screenshot("baidu.png")

# id="kw"是百度搜索框，输入字符串“微博”，跳转到搜索中国页面
driver.find_element_by_id("kw").send_keys(u"微博")

# id="su"是百度搜索按钮，click() 是模拟点击
driver.find_element_by_id("su").click()

# 获取新的页面快照
# driver.save_screenshot(u"微博.png")
#
# 打印网页渲染后的源代码
# print(driver.page_source)
#
# 获取当前页面Cookie
# print(driver.get_cookies())
#
# ctrl+a 全选输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
#
# ctrl+x 剪切输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
#
# 输入框重新输入内容
# driver.find_element_by_id("kw").send_keys("test")
#
# 模拟Enter回车键
# driver.find_element_by_id("su").send_keys(Keys.RETURN)
#
# 清除输入框内容
# driver.find_element_by_id("kw").clear()


# 生成新的页面快照
# driver.save_screenshot("test.png")
#
# 获取当前url
print(driver.current_url)
#
# 关闭当前页面，如果只有一个页面，会关闭浏览器
driver.close()
#
# 关闭浏览器
driver.quit()