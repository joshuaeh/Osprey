# imports
import topSecretInfo

import datetime

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from twilio.rest import Client

#TODO Look at other websites

class BBbird:
    def __init__(self, name, url, headless_browser, multithreading, text_alerts):
        # Multithreading

        # Identifying stuff
        self.name = name
        self.url = url

        # Twilio Stuff
        self.text_alerts = text_alerts
        self.client = Client(topSecretInfo.twilio_sid, topSecretInfo.twilio_token)

        # Chrome options
        caps = webdriver.DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "eager"
        chrome_options = ChromeOptions()
        chrome_options.headless = headless_browser
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("disable-alerts")
        self._driver = webdriver.Chrome(desired_capabilities=caps, options=chrome_options)

    def open_page(self):
        self._driver.get(self.url)
        self._driver.execute_script("window.onbeforeunload = function() {};")

    def text_alert(self, text):
        message = self.client.messages.create(
            messaging_service_sid='MG3e9a0ad3158a41e5b962b49f90eea3d0',
            body=f'Osprey:\n'+text,
            to=topSecretInfo.phone_number
        )
        print('Message sent. ID:', message.sid)

    def checkout(self):
        isComplete = False
        while not isComplete:
            # Wait for Add To Cart Button to Be clickable
            try:
                print(f'{timestamp()}[{self.name}]Attempting to add to cart')
                atc_button = WebDriverWait(self._driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button")))
            except Exception as e:
                # confirm out of stock
                try:
                    # locate atc button
                    atc_button = WebDriverWait(self._driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart-button")))
                    print(f'{timestamp()}[{self.name}]Cart Error: {atc_button.text}')
                    self._driver.refresh()
                except Exception as err:
                    print(f'{timestamp()}[{self.name}] ***** Could not locate Cart after 2 attempts *****')
                    print(f'{timestamp()}[{self.name}] First Error: {e}')
                    print(f'{timestamp()}[{self.name}] Second Error: {err}')
                continue

            print("Add to cart Button Found")
            if self.text_alerts:
                self.text_alert(f'{timestamp()}[{self.name}]ATC Available: {self.url}')

            # Try To check out
            try:
                # add to cart
                # TODO ERROR HANDLING FOR ERROR ADDING TO CART
                atc_button.click()

                # Go to cart and checkout as guest
                self._driver.get("https://www.bestbuy.com/cart")

                # wait for checkout button
                checkout_button = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "checkout-buttons__checkout")))

                checkout_button.click()

                print(f'{timestamp()}[{self.name}]Successfully added to cart - beginning check out')

                # Sign in
                email_field = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.ID, "fld-e"))
                )
                email_field.send_keys(topSecretInfo.email)

                pass_field = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.ID, "fld-p1"))
                )
                pass_field.send_keys(topSecretInfo.password)

                sign_in_button = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "cia-form__controls__submit"))
                )
                sign_in_button.click()

                print(f'{timestamp()}[{self.name}]Signed In')

                # Enter CCV
                ccv_button = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "credit-card-form__cvv--warn"))
                )
                ccv_button.send_keys(topSecretInfo.ccv)

                # Place Order
                order_button = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "button__fast-track"))
                )
                #order_button.click()

                isComplete=True
                print(f'{timestamp()}[{self.name}]Order Placed Successfully')


            except Exception as e:
                print(f'{timestamp()}[{self.name}]Error:')
                print(f'{timestamp()}[{self.name}]{e}')
                print(f'{timestamp()}[{self.name}]Restarting Bot')
                self._driver.get(self.url)

    def close(self):
        self._driver.close()

    def quit(self):
        self._driver.quit()


def timestamp():
    local_time = datetime.datetime.now()
    return local_time.strftime('%H:%M:%S')