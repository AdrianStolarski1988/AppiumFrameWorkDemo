from appium import webdriver

class Driver:
    def getDriverMethod(self):


        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Xiaomi'
        desired_caps['app'] = ('/home/adrian/Pobrane/Android_Demo_App.apk')
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        driver.implicitly_wait(10)

        return driver