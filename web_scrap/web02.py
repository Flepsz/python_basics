from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Web:
    def __init__(self):
        self.site = 'https://asloterias.com.br/resultados-da-mega-sena-2022'
        self.map = {
            'sorteio': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[%jacare%]'
            },
            'numero': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/span[%largatixa%]'
            }
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.abrir_site()

    def abrir_site(self):
        self.driver.get(self.site)
        sleep(5)
        k = 0
        for i in range(110):
            print(self.driver.find_element(By.XPATH, self.map['sorteio']['xpath'].replace('%jacare%', f'{i+4}')).text, end='   ')
            for j in range(6):
                print(self.driver.find_element(By.XPATH, self.map['numero']['xpath'].replace('%largatixa%', f'{k+1}')).text, end=' ')
                k += 1
            print('')

