from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

# BOT GERADOR DE GUIAS DE PARCELAMENTOS NO CADPREV

class BotGerador:
    def __init__(self, username, password):
        # Corrigindo problema do Chrome fechando sozinho
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        self.username = username
        self.password = password
        service=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=options, service=service)

    # Entra no site do Cadprev e loga
    def login(self):
        try:
            driver = self.driver
            driver.get('https://cadprev.previdencia.gov.br/Cadprev/pages/login.xhtml')
            
            time.sleep(1)
            
            username_element = driver.find_element(By.XPATH, '//input[@name="form:cpf"]')
            #username_element.clear()
            username_element.send_keys(self.username)
            password_element = driver.find_element(By.XPATH, '//input[@name="form:senha"]')
            #password_element.clear()
            password_element.send_keys(self.password)
            password_element.send_keys(Keys.RETURN)
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
    
        # Entra na tela de geração das guias
        time.sleep(1)
        pyautogui.click(137,441, duration=1.5)
        pyautogui.click(137,528, duration=1.5)
        pyautogui.click(131,567, duration=1.5)
        pyautogui.click(508,295, duration=1.5)
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.click(526,376, duration=3)

        # Seleciona o parcelamento
        driver.find_element(By.XPATH, '//input[@name="formTabela:tabPARC:12:j_id682"]').click()

        # Gera as guias
        for guia in range(14, 241):
            n_guia_element = driver.find_element(By.XPATH, '//input[@name="form:parcelaInicial"]')
            n_guia_element.clear()
            n_guia_element.send_keys(guia)

            data_guia_element = driver.find_element(By.XPATH, '//input[@name="form:dataPagamento"]')
            data_guia_element.clear()
            data_guia_element.send_keys('31012024')
            
            driver.find_element(By.XPATH, '//input[@name="form:j_id617"]').click()
            time.sleep(5)

iniciar = BotGerador('CPF', 'SENHA')
iniciar.login()
