from selenium import webdriver

from pages.rpa_challenge_page import BasePage




def main():
    
    URL = 'https://rpachallenge.com/'

    driver = webdriver.Firefox()
    
    rpa_challenge = BasePage(driver, URL)

    rpa_challenge.open_url()

    driver.quit()


if __name__ == '__main__':
    main()