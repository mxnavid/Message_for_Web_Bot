from selenium import webdriver
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome("chromedriver")


def main():
    driver.get("https://messages.google.com/web/authentication")
    time.sleep(10)
    csvReader = csv.reader(open("contacts.csv"))
    messageReader = open("message.txt", "r")
    message = messageReader.read()
    print(message)
    for row in csvReader:
        phone = row[1]
        print(phone)
        initpage(phone, message)
        # initpage(phone, message)


def initpage(phoneNumber, message):

    driver.find_element(By.CSS_SELECTOR, ".fab-label").click()
    element = driver.find_element(
        By.CSS_SELECTOR, ".ng-star-inserted:nth-child(1) > .list-item")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    driver.find_element(By.CSS_SELECTOR, ".input").send_keys(phoneNumber)
    driver.find_element(By.CSS_SELECTOR, ".input").send_keys(Keys.ENTER)
    print("number input done")
    time.sleep(3)
    act2 = ActionChains(driver)
    act2.send_keys(message)
    act2.perform()
    act2.send_keys(Keys.ENTER)
    act2.perform()
    driver.refresh()
    time.sleep(3)
    print("Successfully sent message to " + str(phoneNumber))

    return True

    # textBox = driver.find_elements_by_xpath(
    #     "/html/body/mw-app/div/main/mw-main-container/div[1]/mw-conversation-container/div/div/mws-message-compose/div/div[2]/div/mws-autosize-textarea/textarea")
    # textBox.send_keys("adfadsdasda")
    time.sleep(20)
    # driver.close()


main()
