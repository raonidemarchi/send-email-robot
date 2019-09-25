from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('./chromedriver.exe')
wait = WebDriverWait(driver, 10)

driver.get('https://gmail.com')

# fill and submit username
driver.find_element_by_css_selector('#identifierId').send_keys('raoni.demarchi.iv2@gmail.com')
driver.find_element_by_css_selector('#identifierNext').click()

# fill and submit password
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#password input')))
driver.find_element_by_css_selector('#password input').send_keys('r15210986')

wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#passwordNext')))
driver.find_element_by_css_selector('#passwordNext').click()

# Click compose button
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.oo [role=button]')))
driver.find_element_by_css_selector('.oo [role=button]').click()

# fill the "To"
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.vO')))
driver.find_element_by_css_selector('.vO').send_keys('cliente-xyzxyz@gmail.com')

# fill the "subject"
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[name=subjectbox]')))
driver.find_element_by_css_selector('[name=subjectbox]').send_keys('Sua encomenda está a caminho!')

# compose the email body
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[contenteditable][role=textbox]')))
driver.find_element_by_css_selector('[contenteditable][role=textbox]').send_keys(
  'Olá!',
  Keys.ENTER, Keys.ENTER,
  'Já enviamos sua encomenda e ela deve chegar até dia 20 de janeiro.',
  Keys.ENTER, Keys.ENTER,
  'Você pode acompanhar por esse link https://acompanhe.iv2.com.br.',
  Keys.ENTER, Keys.ENTER,
  'Um abraço! (:',
  Keys.ENTER,
  'Equipe iv2.'
)

# send e-mail
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.dC [role=button]')))
driver.find_element_by_css_selector('.dC [role=button]').click()

# show sent e-mail
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#link_vsm')))
driver.find_element_by_css_selector('#link_vsm').click()
