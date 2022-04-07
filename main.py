import json
from cProfile import run
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run():
    with open('DATA.json', 'r') as file:
        data = json.load(file)

    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    driver.get('https://srvcnpc.policia.gov.co/PSC/frm_cnp_consulta.aspx')
    select_element = driver.find_element(By.ID, value='ctl00_ContentPlaceHolder3_ddlTipoDoc')
    for option in select_element.find_elements(By.TAG_NAME, value='option'):
        if option.text == 'CÉDULA DE CIUDADANÍA':
            option.click() # select() in earlier versions of webdriver
            break

    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00$ContentPlaceHolder3$txtFechaexp")))
    print(element)

    input_id = driver.find_element(By.ID, value='ctl00_ContentPlaceHolder3_txtExpediente')
    input_id.send_keys(data['id'])

    input_expedition_date = driver.find_element(By.NAME, value='ctl00$ContentPlaceHolder3$txtFechaexp')
    input_expedition_date.send_keys(data['date_expedition'])

    search_button = driver.find_element(By.ID, value='ctl00_ContentPlaceHolder3_btnConsultar2')
    search_button.click()

    print_button = driver.find_element(By.ID, value='ctl00_ContentPlaceHolder3_btnImprimir')
    print_button.click()

if __name__ == "__main__":
    run()