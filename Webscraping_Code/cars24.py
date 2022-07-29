from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "C:\\Users\\ADMIN\\Desktop\\Selenium\\drivers\\chromedriver.exe" )
driver.get(url="https://www.cars24.com/buy-used-car?sort=P&storeCityId=5&pinId=122001")

time.sleep(1)
#previous_height = driver.execute_script('return document.body.scrollHeight')

elem = driver.find_element_by_tag_name("body")

no_of_pagedowns = 200

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_of_pagedowns-=1

'''
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')

    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == previous_height:
        print('reached maximum height')
        break
    previous_height == new_height
'''
#html = driver.execute_script("return document.body.innerHTML;")
#with open("login.html","w") as f:
#    f.write(html)

'''
post_elems = driver.find_elements_by_class_name("col-4")


for post in post_elems:
    print(post.text)
'''
file = open('DS_Gurgaon.html', 'w',encoding="utf-8")
file.write(driver.page_source)
file.close()