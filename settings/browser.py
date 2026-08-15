from selenium.webdriver.firefox.options import Options

from settings.paths import DOWNLOAD_DIR


def get_firefox_options() -> Options:

    '''
    Configuração do browser
    '''

    options = Options()

    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", str(DOWNLOAD_DIR))
    options.set_preference("browser.download.useDownloadDir", True)
    options.set_preference(
        "browser.download.manager.showWhenStarting",
        False,
    )

    options.set_preference(
        "browser.helperApps.neverAsk.saveToDisk",
        ",".join(
            [
                "application/pdf",
                "text/csv",
                "application/vnd.ms-excel",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ]
        ),
    )

    return options