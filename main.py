from selenium import webdriver

from pages.rpa_challenge_page import BasePage
from pages.start_challenge_page import StarChallenge

from time import sleep

import logging
from settings.log import setup_logging


logger = logging.getLogger(__name__)

URL = 'https://rpachallenge.com/'
btn_start = '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button'

def main():
    
    setup_logging()

    driver = webdriver.Firefox()
    
    # Abrir URL
    rpa_challenge = BasePage(driver)
    rpa_challenge.open_url(URL)

    # Startar desafio
    start_challenge = StarChallenge(driver, btn_start)
    start_challenge.start_challenge()

    sleep(2)

    driver.quit()


if __name__ == '__main__':
    main()