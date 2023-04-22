"""
OBLIGATORIU - grad de dificultate: Usor spre Mediu


1. Implementează o clasă Login care să moștenească unittest.TestCase.

In metoda de setUp():
- seteaza driver-ul (instanta de browser)
- acceseaza site-ul 'https://the-internet.herokuapp.com/'
- click pe Form Authentication

In metoda de tearDown():
- quit la browser
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.maximize_window()
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a').click()


    def tearDown(self) -> None:
        self.chrome.quit()

# ● Test 1
# - Verifică dacă noul url e corect
#
#
    def test_1(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual)
#
# # ● Test 2
# # - Verifică dacă page title e corect (page title este tag-ul title din <head>)
# #
    def test_2(self):
        actual = self.chrome.find_element(By.XPATH, '/html/head/title').text
        expected = 'The Internet'
        self.assertEqual(expected, actual)
#
# # ● Test 3
# # - Verifică daca textul de pe elementul xpath=//h2 e corect
# #
    def test_3(self):
        actual = self.chrome.find_element(By.XPATH, '//h2').text
        expected = 'Login Page'
        self.assertEqual(expected,actual)
#
# # ● Test 4
# # - Verifică dacă butonul de login este displayed

    def test_4(self):
        actual = self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i')
        self.assertEqual(actual.is_displayed(), True)

# ● Test 5
# - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
#
    def test_5(self):
        actual = self.chrome.find_element(By.LINK_TEXT, 'Elemental Selenium').get_attribute('href')
        expected = "http://elementalselenium.com/"
        self.assertEqual(actual, expected)

# ● Test 6
# - Lasă goale user și pass
# - Click login
# - Verifică dacă eroarea e displayed

    def test_6(self):
        self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        expected = self.chrome.find_element(By.ID, 'flash-messages').is_displayed()

        self.assertEqual(expected, True)
#
# ● Test 7
# - Completează cu user și pass invalide
# - Click login
# - Verifică dacă mesajul de pe eroare e corect
# - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
# expected = 'Your username is invalid!'
# self.assertTrue(expected in actual, 'Error message text is
# incorrect')
#
    def test_7(self):
        self.chrome.find_element(By.XPATH, '//*[@id="username"]').send_keys('Ana')
        self.chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys('123')
        self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        actual = self.chrome.find_element(By.XPATH, '//*[@id="flash"]').text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

# ● Test 8
# - Lasă goale user și pass
# - Click login
# - Apasă x la eroare
# - Verifică dacă eroarea a dispărut

    def test_8(self):
        self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        self.chrome.find_element(By.XPATH, '//*[@id="flash"]/a').click()
        time.sleep(2)
        with self.assertRaises(NoSuchElementException):
            actual = self.chrome.find_element(By.XPATH, '//*[@id="flash"]')
#
# ● Test 9
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi

    def test_9(self):
        lista = self.chrome.find_elements(By.XPATH, '//label')
        username_actuala = lista[0].text
        password_actuala = lista[1].text

        username_expected = 'Username'
        password_expected = 'Password'

        self.assertEqual(username_expected,username_actuala)
        self.assertEqual(password_expected,password_actuala)

# ● Test 10
# - Completează cu user și pass valide
# - Click login
# - Verifică ca noul url CONTINE /secure
# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
#
# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
    def test_10(self):
        self.chrome.find_element(By.XPATH, '//*[@id="username"]').send_keys('tomsmith')
        self.chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(expected_url, actual_url)
        WebDriverWait(self.chrome, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@class="flash success"]')))
        element = self.chrome.find_element(By.XPATH, '//*[@class="flash success"]')
        self.assertTrue(element.is_displayed(), True)

        actual = element.text
        expected = 'secure area!'
        self.assertTrue(expected in actual)

#
# ● Test 11
# - Completează cu user și pass valide
# - Click login
# - Click logout
# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_11(self):
        self.chrome.find_element(By.XPATH, '//*[@id="username"]').send_keys('tomsmith')
        self.chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        time.sleep(2)
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/a').click()

#
# OPTIONAL - grad de dificultate: Mediu spre greu: may need Google
# ● Test 12 - brute force password hacking
# - Completează user tomsmith
# - Găsește elementul //h4
# - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
# potențială parolă.
# - Folosește o structură iterativă prin care să introduci rând pe rând
# parolele și să apeși pe login.
# - La final testul trebuie să îmi printeze fie
# ‘Nu am reușit să găsesc parola’
# ‘Parola secretă este [parola]’