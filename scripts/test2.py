# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva


# completam username in functie de atribut=valoare
chrome.find_element(By.XPATH,'//input[@name="username"]').send_keys('tomsmith')


# completam password in functie de atribut=valoare
chrome.find_element(By.XPATH,'//*[@id="password"]').send_keys('SuperSecretPassword!')


# dam click pe elemental selenium link in functie de textul elementului
chrome.find_element(By.XPATH,'//a[text()="Elemental Selenium"]').click()


# dam click pe login in functie de textul elementului
chrome.find_element(By.XPATH,'//*[text()=" Login"]').click()

# verificam daca am ajuns pe pagina corecta
expected = 'https://the-internet.herokuapp.com/secure'
actual = chrome.current_url
assert expected == actual, 'Incorect URL'

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')