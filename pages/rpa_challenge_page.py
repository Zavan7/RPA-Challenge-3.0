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
    def __init__(
        self,
        driver: WebDriver,
        timeout: int = 4
    ) ->None:

        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)


    def open_url(self, url: str):

        '''
        Responsável por acessar a página inicial da aplicação, recendo a URL

        Args:
            url (str): Endereço da página que será acessada

        Tenta acessar a URL, caso não esteja disponível, retoirnando um
        Warning via Log
        '''

        try:

            logger.info('Abrindo URL da página')

            if url is None:
                logger.warning('URL indisponível')
                return


            self.driver.get(url)

        except Exception as e:
            logger.error(f'Erro ao abrir link: {e}')
            raise