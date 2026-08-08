from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait



class BasePage:
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
            self.driver.get(self.url)

        except Exception as e:
            raise