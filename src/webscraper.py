from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

path_to_driver = './chromedriver.exe'

class Scraper:
    def __init__(self):
        self.driver_options = Options()
        self.driver_options.headless = True
        self.driver_options.add_argument("--log-level=3")
        self.driver_options.add_argument("--mute-audio")
        self.driver_options.add_argument('--disable-gpu')
        self.driver_options.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(path_to_driver, options=self.driver_options) 


    def find_time_from_me(self, url, click_XPATH, time_xpath):
        self.driver.get(url)
        self.driver.find_element(By. XPATH, click_XPATH).click()
        time.sleep(0.3)
        e = self.driver.find_element(By. XPATH, time_xpath)
        return e.text

    def open_instance_get_id(self, url, desired_XPATH):
        self.driver.get(url)
        e = self.driver.find_element(By. XPATH, desired_XPATH)
        return int(e.get_attribute('data-vacancy-id'))


########################################################################################################
#   Copyright (C) 2022  Rhydian Davies
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
