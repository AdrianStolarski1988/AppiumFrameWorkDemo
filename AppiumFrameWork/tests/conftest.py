import time
import pytest
from AppiumFrameWork.base.DriverClass import Driver
from appium import webdriver


@pytest.fixture(scope = 'class')
def beforeClass(request):
    print("before class")
    app = Driver()
    driver = app.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
    print("after class")

@pytest.fixture()
def beforeMethod():
    print("before Method")
    yield
    print("After Method ")