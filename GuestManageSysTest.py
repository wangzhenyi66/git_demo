import unittest
from ddt import ddt

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.get("http://150.109.156.47:8000/")

#  元素层
class Login:
    username = "username"
    password = "password"

class AddEvent:
    eventname = "eventname"
    eventaddress = "eventaddress"
    eventnum = "eventnum"
    eventdata = "eventdata"

class AddGuest:
    guestEvent = "guestEvent"
    guestname = "guestname"
    guestphone = "guestphone"
    guestmail = "guestmail"


#  操作层
class loginAction:
    def __init__(self, driver):
        self.driver = driver

    def inputUsername(self, username):
        driver.find_element(By.NAME, "username").send_keys(username)

    def inputPassword(self, password):
        driver.find_element(By.NAME, "password").send_keys(password)


class addEventAction:
    def __init__(self, driver):
        self.driver = driver

    def inputEventName(self, name):
        driver.find_element(By.NAME, "name").send_keys(name)

    def inputEventAddress(self, address):
        driver.find_element(By.NAME, "address").send_keys(address)

    def inputEventNum(self, number):
        driver.find_element(By.NAME, "number").send_keys(number)

    def inputEventData(self, start_time):
        driver.find_element(By.NAME, "start_time").send_keys(start_time)

class addGuestAction:
    def __init__(self, driver):
        self.driver = driver

    def selectguestEvent(self, value):
        event = driver.find_element(By.NAME, "event")
        select = Select(event)
        select.select_by_value(value)
        select.select_by_visible_text('text')

    def inputGuestPhone(self, phone):
        driver.find_element(By.NAME, "phone").send_keys(phone)

    def inputGuestMail(self, email):
        driver.find_element(By.NAME, "email").send_keys(email)

    def inputGuestName(self, name):
        driver.find_element(By.NAME, "name").send_keys(name)


#  数据层
login_data = []

add_event_data = []

add_guest_data = []

#  用例层
class LoginTest(unittest.TestCase):

