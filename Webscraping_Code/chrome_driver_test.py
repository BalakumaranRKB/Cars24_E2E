from selenium import webdriver

class Chrome_Driver_Windows():

    def test(self):
        driver = webdriver.Chrome(executable_path = "C:\\Users\\ADMIN\\Desktop\\Selenium\\drivers\\chromedriver.exe" )
        driver.get("http://www.letskodeit.com")

cc = Chrome_Driver_Windows()
cc.test()
