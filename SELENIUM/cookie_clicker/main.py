from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# run
path = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)
cookie = driver.find_element_by_id("bigCookie")
number_of_cookies = driver.find_element_by_id("cookies")
items_to_buy = [driver.find_element_by_id(
    "productPrice" + str(x)) for x in range(1, -1, -1)]
# create chain
actions = ActionChains(driver)


def main():
    # plan action
    actions.click(cookie)

    for i in range(100):
        # do action
        actions.perform()
        my_cookies = int(number_of_cookies.text.split()[0])
        for item in items_to_buy:
            value = int(item.text)
            if value <= my_cookies:
                upgrades = ActionChains(driver)
                upgrades.move_to_element(item)
                upgrades.click()
                upgrades.perform()


if __name__ == '__main__':
    main()
