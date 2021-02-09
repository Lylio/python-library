import getpass
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

r1 = "http://localhost:8081/#admin/repository/repositories:maven-central"
r2 = "http://localhost:8081/#admin/repository/repositories:nuget.org-proxy"

repos = [r1, r2]

log = logging.getLogger(__name__)


def run():
    driver.get(r1)
    time.sleep(1)
    username_box = driver.find_element_by_id("textfield-1173-inputEl")
    username_box.send_keys(username)
    password_box = driver.find_element_by_id("textfield-1174-inputEl")
    password_box.send_keys(password)
    time.sleep(1)
    password_box.send_keys(Keys.RETURN)
    time.sleep(1)

    for repo in repos:
        check_repo(repo)


def check_repo(repo):
    driver.get(repo)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "x-btn-nx-plain-small"))).click()
    time.sleep(2)
    cert_status = driver.find_element_by_css_selector(
        '.x-btn-button.x-btn-button-nx-primary-small.x-btn-text.x-btn-icon.x-btn-icon-left.x-btn-button-center')
    log.info("cert status: " + cert_status.text)
    repo = repo.replace("http://localhost:8081/#admin/repository/repositories:", "")
    if "Remove" in cert_status.text:
        print(repo + " : Certificate OK")
    elif "Add" in cert_status.text:
        print(repo + " : Certificate MISSING")
        driver.find_element_by_css_selector(
            '.x-btn-button.x-btn-button-nx-primary-small.x-btn-text.x-btn-icon.x-btn-icon-left.x-btn-button-center').click()
        print("** certificate for " + repo + " has now been added **")
    else:
        print(repo + " : MANUAL CHECK REQUIRED (cannot determine cert status)")
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


if __name__ == '__main__':
    username = input("Enter Nexus username: ")
    password = getpass.getpass("Enter Nexus password: ")
    DRIVER_PATH = '/usr/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    # logging.basicConfig(level=logging.INFO)

    run()
    driver.quit()

