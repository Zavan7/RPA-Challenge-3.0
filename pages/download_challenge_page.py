from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from datetime import datetime

from pages.rpa_challenge_page import BasePage

import logging

logger = logging.getLogger(__name__)


class DownloadChallenge(BasePage):

    def __init__(
        self,
        driver: WebDriver,
        btn_download_seletor: str,
        timeout: int=4
    ) -> None:

        super().__init__(driver, timeout)
        self.btn_download_seletor = btn_download_seletor
        
        
    def download_click(self) -> None:
        
        btn_download = self.driver.find_element(
            By.XPATH,
            self.btn_download_seletor
        )
        try:

            if not btn_download.is_enabled():
                raise

            btn_download.click()

        except Exception as e:
            return
            