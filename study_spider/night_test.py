from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# 无头浏览器
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")

web = Chrome(options=opt)

web.get("https://www.lagou.com")


el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[4]/a')\

el.click()
time.sleep(3)

web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)
li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')

for li in li_list:

    job_name = li.find_element_by_tag_name('h3').text
    job_price = li.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[2]/div/span').text
    print(job_name, job_price)
