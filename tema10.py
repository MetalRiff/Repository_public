import unittest
import HtmlTestRunner

from Sesiunea9.Tema.tema_9 import Login

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


"""
Tema 10 - VERIFICARI EXTRA
Exerciții Recomandate - grad de dificultate: Ușor
1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
intalnirea 10 (care au clasa). Generati raportul.

"""
class TestSuite(unittest.TestCase):
    def test_suite(self):

        # stabilim si adaugam intr-o suita testele pe care vrem sa le rulam
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
         unittest.defaultTestLoader.loadTestsFromTestCase(Login)
        ])

 # cream un runner
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True, # vrem sa generam un singur raport cu toate testele
            report_title="Test Execution Report",
            report_name="Login"
        )

        runner.run(teste_de_rulat)

"""

2. Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi firefox in loc de chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).

https://www.phptravels.net/
http://automationpractice.com/index.php
https://formy-project.herokuapp.com/
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html
Sau puteti alege voi ce pagina doriti

"""
class SwitchWindow(unittest.TestCase):
    def setUp(self) -> None:
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.get('https://formy-project.herokuapp.com/')
        self.firefox.find_element(By.XPATH, '/html/body/div/div/li[13]/a').click()
    def tearDown(self) -> None:
        self.firefox.quit()

# Test 1 verifica noul url
    def test_1(self):
        actual = self.firefox.current_url
        expected = 'https://formy-project.herokuapp.com/switch-window'
        self.assertEqual(actual, expected)

# Test 2 verifica butonul Open new tab

    def test_2(self):
        self.firefox.find_element(By.XPATH, '//*[@id="new-tab-button"]').click()
        self.firefox.switch_to.window(self.firefox.window_handles[1]) # schimba focusul pe noul Tab deschis
        actual = self.firefox.current_url
        expected = 'https://formy-project.herokuapp.com/'
        self.assertEqual(actual, expected)

# Test 3 verifica butonul Open alert

    def test_3(self):
        self.firefox.find_element(By.XPATH, '//*[@id="alert-button"]').click()
        alerta = self.firefox.switch_to.alert
        actual = alerta.text
        expected = 'This is a test alert!'

        self.assertEqual(actual,expected)



