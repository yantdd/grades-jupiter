from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import time
from tqdm import tqdm

def scraper(n_unidades, sistema_jupiter=None):
    if n_unidades > 47:
        print(f"\nNúmero de unidades selecionadas ({n_unidades}) é maior que o número de unidades disponíveis (47).")
        return 1
    elif n_unidades <= 0:
        print("\nNúmero de unidades selecionadas deve ser maior que 0.")
        return 1
    
    print("Analisando grades curriculares, isso pode levar alguns minutos...")
    service = Service(executable_path='/home/yan/Downloads/chromedriver-linux64/chromedriver')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275')
    time.sleep(5)
    
    select_1 = Select(driver.find_element(By.ID, 'comboUnidade'))


    for i in range(1, n_unidades + 1):
        select_1 = Select(driver.find_element(By.ID, 'comboUnidade'))
        select_1.select_by_index(i)
        time.sleep(0.5)
        select_2 = Select(driver.find_element(By.ID, 'comboCurso'))
        for j in tqdm(range(1, len(select_2.options)), desc=f"Unidade {f'{i}/{n_unidades}':>5}", ncols=50, bar_format="{desc}: {percentage:3.0f}% | {n}/{total}"):
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
                continue
    
            html = grade.get_attribute('outerHTML')
            time.sleep(1)

            if sistema_jupiter:
                try:
                    sistema_jupiter.processar_grade(html)
                except Exception as e:
                    pass
           
            driver.get('https://uspdigital.usp.br/jupiterweb/jupCarreira.jsp?codmnu=8275')
            time.sleep(1)
            select_1 = Select(driver.find_element(By.ID, 'comboUnidade'))
            time.sleep(2)
            select_1.select_by_index(i)
    
    driver.quit()
    return 0