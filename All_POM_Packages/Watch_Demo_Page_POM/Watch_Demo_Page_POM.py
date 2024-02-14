import time
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

from All_Config_Packages.Watch_Demo_Page.Watch_Demo_Page_read_INI import watch_demo_page_read_ini
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


class Watch_Demo_Page_Pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def click_on_accept_cookies(self):

        accept_cookies = self.explicit_wait(10, "XPATH", watch_demo_page_read_ini().accept_cookies(), self.d)
        accept_cookies.click()

    def verify_user_able_to_hit_the_url(self):
        try:
            self.open_url(self.d)
            return self.d.title == watch_demo_page_read_ini().home_page_title()
        except Exception as ex:
            print(ex)

    def verify_watch_demo_button_is_enable_and_clickable(self):
        try:
            self.open_url(self.d)
            watch_demo_button = self.explicit_wait(10, "XPATH", watch_demo_page_read_ini().watch_demo_button(), self.d)
            return watch_demo_button.is_enabled()
        except Exception as ex:
            print(ex)

    def verify_when_user_click_on_watch_demo_button_then_redirect_on_watch_demo_page(self):
        try:
            self.open_url(self.d)

            watch_demo_button = self.explicit_wait(10, "XPATH", watch_demo_page_read_ini()
                                                   .watch_demo_button(), self.d)
            watch_demo_button.click()

            watch_demo_submit_button = self.explicit_wait(10, "XPATH", watch_demo_page_read_ini()
                                                          .watch_demo_submit_button(), self.d)
            return watch_demo_submit_button.is_displayed()
        except Exception as ex:
            print(ex)

    def verify_user_is_able_to_fill_the_watch_demo_form(self):
        try:
            self.open_url(self.d)
            self.click_on_accept_cookies()
            watch_demo_button = self.explicit_wait(10, "XPATH", watch_demo_page_read_ini()
                                                   .watch_demo_button(), self.d)
            # watch_demo_button.click()
            self.d.execute_script("arguments[0].click();", watch_demo_button)

            first_name = self.d.find_element(By.XPATH, watch_demo_page_read_ini().first_name())
            first_name.send_keys(watch_demo_page_read_ini().first_name_data())

            last_name = self.d.find_element(By.XPATH, watch_demo_page_read_ini().last_name())
            last_name.send_keys(watch_demo_page_read_ini().last_name_data())

            email_id = self.d.find_element(By.XPATH, watch_demo_page_read_ini().email_id())
            email_id.send_keys(watch_demo_page_read_ini().email_id_data())

            company_name = self.d.find_element(By.XPATH, watch_demo_page_read_ini().company_name())
            company_name.send_keys(watch_demo_page_read_ini().company_name_data())

            phone_number = self.d.find_element(By.XPATH, watch_demo_page_read_ini().phone_number())
            phone_number.send_keys(watch_demo_page_read_ini().phone_number_data())

            unit_count = self.d.find_element(By.XPATH, watch_demo_page_read_ini().unit_count())
            unit_count.send_keys(watch_demo_page_read_ini().unit_count_data())

            job_title = self.d.find_element(By.XPATH, watch_demo_page_read_ini().job_title())
            job_title.send_keys(watch_demo_page_read_ini().job_title_data())

            watch_demo_submit_button = self.d.find_element(By.XPATH,
                                                           watch_demo_page_read_ini().watch_demo_submit_button())
            return watch_demo_submit_button.is_displayed()
        except Exception as ex:
            print(ex)

    def verify_without_filling_the_mandatory_information_validation_message_should_be_displayed_This_is_field_is_required(
            self):
        try:
            self.open_url(self.d)
            self.click_on_accept_cookies()
            watch_demo_button = self.explicit_wait(10, "XPATH", watch_demo_page_read_ini()
                                                   .watch_demo_button(), self.d)
            # watch_demo_button.click()
            self.d.execute_script("arguments[0].click();", watch_demo_button)

            watch_demo_submit_button = self.d.find_element(By.XPATH,
                                                           watch_demo_page_read_ini().watch_demo_submit_button())
            watch_demo_submit_button.click()

            first_name = self.explicit_wait(10, "XPATH", watch_demo_page_read_ini().validation_text_firstname(), self.d)
            return first_name.is_displayed()
        except Exception as ex:
            print(ex)

        ##################################### Reusable Methods #################################

    def open_url(self, d):
        try:
            self.d = d
            self.d.get(watch_demo_page_read_ini().get_url())
            self.d.maximize_window()
            time.sleep(web_driver.two_second)

        except Exception as ex:
            self.logger.error(ex)
