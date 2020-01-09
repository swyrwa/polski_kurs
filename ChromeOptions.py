from selenium import webdriver

class ChromeOptions:

   def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("useAutomationExtension", False)