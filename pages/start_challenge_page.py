from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from datetime import datetime

from pages.rpa_challenge_page import BasePage

import logging

logger = logging.getLogger(__name__)


class StarChallenge(BasePage):
    
    def __init__(self,
        driver: WebDriver,
        seletor_start_challenge: str,
        timeout: int = 4
    ) -> None:

        self.seletor_start_page = seletor_start_challenge
        super().__init__(driver, timeout)


    def start_challenge(self) -> None:

        try:
            hora_inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            logger.info(f'Iniciando desafio as: {hora_inicio}')

            seletor_start = self.driver.find_element(
                By.XPATH,
                self.seletor_start_page
            )
            if not seletor_start.is_enabled:
                logger.warning('Seletor de start indisponível')
                return


            seletor_start.click()

            logger.info('Desafio iniciado')

        except Exception as e:
            logger.error(f'Erro na aplicação: {e}')
            raise