from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Scraper:
    def __init__(self):
        self.driver_options = Options()
        self.driver_options.headless(True)
        self.driver = webdriver.Chrome('..\chromedriver.exe', options=self.driver_options) 


    def open_instance(self, url):
        self.driver.get(url)


    def find_element_byXPATH(self, desired_XPATH):
        self.driver.find_element(By. XPATH, desired_XPATH)


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
