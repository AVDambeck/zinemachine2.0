#!/usr/bin/env python3
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.by import By
from .config import Config

driver = None
timeout = 2

def initialize():
            global driver
            if Config.DRIVER_TYPE == "chrome":
                        driver = webdriver.Chrome()
            elif Config.DRIVER_TYPE == "firefox":
                        driver = webdriver.Firefox()


def convert(htmlpath, pdfpath):
            driver.get(htmlpath)
            # Boofed from pyhtml2pdf
            try:
                        WebDriverWait(driver, timeout).until(
                                    staleness_of(driver.find_element(by=By.TAG_NAME, value="html"))
                        )
            except TimeoutException:
                        print_options: dict = {},
                        calculated_print_options = {
                                    "landscape": False,
                                    "displayHeaderFooter": False,
                                    "printBackground": True,
                                    "preferCSSPageSize": True,
                        }
                        calculated_print_options.update(print_options)

def deinitialize():
            driver.quit()
