from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import time


service = Service(executable_path='/home/yan/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275')
time.sleep(5)

select_1 = Select(driver.find_element(By.ID, 'comboUnidade'))

for i in range(1, len(select_1.options)):
    select_1 = Select(driver.find_element(By.ID, 'comboUnidade'))
    select_1.select_by_index(i)
    time.sleep(0.5)
    select_2 = Select(driver.find_element(By.ID, 'comboCurso'))

    for j in range(1, len(select_2.options)):
        select_2 = Select(driver.find_element(By.ID, 'comboCurso'))
        time.sleep(0.5)
        select_2.select_by_index(j)
        time.sleep(0.5)

        try:
            driver.find_element(By.ID, 'enviar').click()
            time.sleep(2)
            driver.find_element(By.ID, 'step4-tab').click()
            grade = driver.find_element(By.ID, 'step4')
            time.sleep(3)
        except:
            driver.get('https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275')
            time.sleep(1)
            select_1 = Select(driver.find_element(By.ID, 'comboUnidade'))
            time.sleep(1)
            select_1.select_by_index(i)
            print(f"Grade indisponivel.\n")
            continue

        html = grade.get_attribute('outerHTML')
        time.sleep(1)

        with open("grades/grade" + f"{i}" +"-"+ f"{j}" + ".html", "w", encoding="utf-8", errors='ignore') as f:
            f.write(html)

        driver.get('https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275')
        time.sleep(1)
        select_1 = Select(driver.find_element(By.ID, 'comboUnidade'))
        time.sleep(1)
        select_1.select_by_index(i)

driver.quit()