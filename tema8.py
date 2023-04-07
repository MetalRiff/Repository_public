"""
Tema 8 - SELECTORS
"""

"""
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 7 și ia notițe în caz că ți-a scăpat ceva.
Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
ajut.
Dacă stai blocat > 30 min, cere indiciu.
"""

"""
Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Alege-ți unul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri

- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.
Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
"""

"""
Exerciții extra - Opțional
https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sh
eet/
"""


# Importam libraria webdriver din framework-ul selenium

from selenium import  webdriver

# importam modului time
import time

# importam clasa By

from selenium.webdriver.common.by import By

# Deschidem un browser chrome

chrome = webdriver.Chrome()

# Deschidem un site

chrome.get("https://formy-project.herokuapp.com/autocomplete")

# Pentru a vedea ce se intampla introducem un time delay

time.sleep(5)

# Cand lucram cu browserul recomandarea e sa maximizam fereastra

chrome.maximize_window()
time.sleep(5)

# Identificare dupa ID

elementul1 = chrome.find_element(By.ID, 'street_number')
elementul2 = chrome.find_element(By.ID, 'route')
elementul3 = chrome.find_element(By.ID, 'locality')

# Trimitem text/completam inputul elementului

elementul1.send_keys(By.ID, '23')
time.sleep(2)
elementul2.send_keys(By.ID, 'Strada Mica, nr.4')
time.sleep(2)
elementul3.send_keys(By.ID, 'Buzau')
time.sleep(2)


# Identificare dupa LINK_TEXT

chrome.get("https://formy-project.herokuapp.com")
time.sleep(5)


el4 = chrome.find_element(By.LINK_TEXT,'Buttons')
el4.click()
time.sleep(2)

chrome.back()
time.sleep(2)

el5 = chrome.find_element(By.LINK_TEXT,'Checkbox')
el5.click()
time.sleep(10)

chrome.back()
time.sleep(2)

el6 = chrome.find_element(By.LINK_TEXT,'Datepicker')
el6.click()
time.sleep(2)

chrome.back()
time.sleep(2)

# Identificare dupa PARTIAL LINK TEXT

el7 = chrome.find_elements(By.PARTIAL_LINK_TEXT,'Dr')
el7[0].click()
time.sleep(2)

chrome.back()
time.sleep(2)

el8 = chrome.find_elements(By.PARTIAL_LINK_TEXT,'C')
el8[1].click()
time.sleep(2)

chrome.back()
time.sleep(2)

el9 = chrome.find_elements(By.PARTIAL_LINK_TEXT,'D')
el9[2].click()
time.sleep(2)

# Identificare dupa NAME

chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(2)

el10 = chrome.find_element(By.NAME,'firstname').send_keys('Maria')
time.sleep(5)

el11 = chrome.find_element(By.NAME,'lastname').send_keys('Constantin')
time.sleep(5)

el12 = chrome.find_element(By.NAME,'continents').send_keys('Europe')
time.sleep(5)

# Identificare dupa TAG

chrome.get("https://formy-project.herokuapp.com/autocomplete")
time.sleep(2)

el13 = chrome.find_elements(By.TAG_NAME,'input')
el13[0].send_keys('Adresa completa')
time.sleep(2)

el131 = chrome.find_elements(By.CLASS_NAME,'dismissButton')
el131[0].click()

el14 = chrome.find_elements(By.TAG_NAME,'input')
el14[1].send_keys('Street address')
time.sleep(2)

el15 = chrome.find_elements(By.TAG_NAME,'input')
el15[2].send_keys('Street address 2')
time.sleep(2)

# Identificare dupa CLASS NAME

chrome.get("https://formy-project.herokuapp.com/autocomplete")
time.sleep(2)

el16 = chrome.find_elements(By.CLASS_NAME, 'form-control')
el16[1].send_keys('Street address TEST')
time.sleep(2)

# Identificare dupa CSS dupa ID

el17 = chrome.find_element(By.CSS_SELECTOR, '#street_number').send_keys('Numarul strazii')
time.sleep(2)

# Identificare dupa CSS dupa CLASS

el18 = chrome.find_elements(By.CSS_SELECTOR, '.form-control')
el18[0].send_keys('Adresa completa')
time.sleep(2)


# Identificare dupa CSS dupa atribut valoare partiala

el19 = chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Street address"]').send_keys('Modifica adresa')

time.sleep(2)