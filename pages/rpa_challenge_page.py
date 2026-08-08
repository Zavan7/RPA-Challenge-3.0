from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

import logging

logger = logging.getLogger(__name__)

class BasePage:
    '''
    Classe base para todas as páginas da automação.

    Armazena a instância da página do Selenium (WebDriver) e o tempo padrão
    de espera, utilizado pelas classes filhas
    '''
    
    def __init__(self,
        driver: WebDriver,
        url: str,
        timeout: int = 4
    ) ->None:

        self.driver = driver
        self.timeout = timeout
        self.url = url
        self.wait = WebDriverWait(driver, timeout)


    def open_url(self):

        try:

            logger.info('Abrindo URL da página')

            if self.url is None:
                return


            self.driver.get(self.url)

        except Exception as e:
            logger.error(f'Erro ao abrir link: {e}')
            raise