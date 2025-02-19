import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login_chrome(self,setup):
        self.driver= setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME, "Submit").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()


    def test_login_firefox(self,setup):
        self.driver= setup
        from selenium.webdriver.firefox.service import Service
        self.serv_obj = Service("E:\python\drivers\geckodriver.exe")
        self.driver = webdriver.Firefox(service=self.serv_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME, "Submit").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

