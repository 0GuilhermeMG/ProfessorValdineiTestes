# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testFALSE(self):
        self.driver.get("https://aluno.unidombosco.edu.br/")
        self.driver.set_window_size(945, 1020)
        self.driver.find_element(By.ID, "MATRICULA").click()
        self.driver.find_element(By.ID, "MATRICULA").send_keys("userCorretoCensurado")
        self.driver.find_element(By.ID, "SENHA").click()
        self.driver.find_element(By.ID, "SENHA").send_keys("senhaCorretaCensurada")
        self.driver.find_element(By.XPATH, "//button[contains(.,\'       Acessar\')]").click()

