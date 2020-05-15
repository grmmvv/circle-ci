import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions


def test_google():
    desired_caps = {}
    options = ChromeOptions()
    driver = selenium.webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        desired_capabilities=desired_caps,
        options=options,
    )

    driver.get('https://google.com')
