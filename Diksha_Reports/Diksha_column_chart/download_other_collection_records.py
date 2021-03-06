




import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class others_records_download():

    def __init__(self, driver):
        self.driver = driver
        self.filename = ''

    def test_download_csv(self):
        self.data = GetData()
        self.p = pwd()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        colltype = Select(self.driver.find_element_by_name('collection_type'))
        colltype.select_by_visible_text(' Others ')
        self.data.page_loading(self.driver)
        if ' No Data Available ' in self.driver.page_source:
            print("This is not having collection records")
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(4)
            self.filename = self.p.get_download_dir() + '/collectionType_textbook_data.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            os.remove(self.filename)
            return file


