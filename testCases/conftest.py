import pytest
from selenium import webdriver

chrom_option = webdriver.ChromeOptions()
# chrom_option.add_argument("--headless")


# Multiple browser Testing
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome(options=chrom_option)
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    # driver.implicitly_wait(5)
    yield driver
    driver.quit()
