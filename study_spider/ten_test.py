import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client

# 防止滑块拖拽失败,去掉webdriver
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)

# 超级鹰帐号密码
chaojiying = Chaojiying_Client('ghfGHF', '960213', '919345')

# 打开12306
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(3)

# 点击帐号密码登录
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(3)

# 获取验证码图片
img = web.find_element_by_xpath('//*[@id="J-loginImg"]')
dic = chaojiying.PostPic(img.screenshot_as_png, 9004)

result = dic['pic_str']
rs_list = result.split("|")
print(rs_list)

for rs in rs_list:
    # 获取验证码的坐标
    p_temp = rs.split(",")
    x = int(p_temp[0])
    y = int(p_temp[1])

    # 点击验证码坐标钉位置
    ActionChains(web).move_to_element_with_offset(img, x, y).click().perform()

time.sleep(2)

# 登录
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('18666056460')
time.sleep(1)
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('000000')
time.sleep(1)
web.find_element_by_xpath('//*[@id="J-login"]').click()

# 拖拽
time.sleep(1)
btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()