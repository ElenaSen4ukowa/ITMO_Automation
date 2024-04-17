from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()          # создаем объект драйвера
driver.get("https://demoqa.com/")    # метод get() - метод входа на страницу

# поиск элемента
icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')
