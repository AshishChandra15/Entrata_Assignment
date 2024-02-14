import configparser
from pathlib import Path

file_path = (f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Watch_Demo_Page\\Data_From_INI"
             f"\\Watch_Demo_Page.ini")
print("configure filepath: ", file_path)
common_test_data_ini_file_path = (f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data"
                                  f"\\common_test_data.ini")


class watch_demo_page_read_ini:
    def __init__(self):
        self.config = configparser.RawConfigParser()

        self.common_test_data_config = configparser.RawConfigParser()
        self.common_test_data_config.read(common_test_data_ini_file_path)
        try:
            self.config.read(file_path)
        except Exception as ex:
            print(ex)

    def get_url(self):
        try:
            url = self.common_test_data_config.get("Common_Data", "url")
            print("url: ", url)
            return url
        except Exception as ex:
            print(ex)

    def accept_cookies(self):
        try:
            accept_cookies = self.config.get("watch_demo_locator", "accept_cookies")
            print("accept_cookies: ", accept_cookies)
            return accept_cookies
        except Exception as ex:
            print(ex)

    def watch_demo_button(self):
        try:
            watch_demo_button = self.config.get("watch_demo_locator", "watch_demo_button")
            print("watch_demo_button: ", watch_demo_button)
            return watch_demo_button
        except Exception as ex:
            print(ex)

    def first_name(self):
        try:
            first_name = self.config.get("watch_demo_locator", "first_name")
            print("first_name: ", first_name)
            return first_name
        except Exception as ex:
            print(ex)

    def last_name(self):
        try:
            last_name = self.config.get("watch_demo_locator", "last_name")
            print("last_name: ", last_name)
            return last_name
        except Exception as ex:
            print(ex)

    def email_id(self):
        try:
            email_id = self.config.get("watch_demo_locator", "email_id")
            print("email_id: ", email_id)
            return email_id
        except Exception as ex:
            print(ex)

    def company_name(self):
        try:
            company_name = self.config.get("watch_demo_locator", "company_name")
            print("watch_demo_button: ", company_name)
            return company_name
        except Exception as ex:
            print(ex)

    def phone_number(self):
        try:
            phone_number = self.config.get("watch_demo_locator", "phone_number")
            print("phone_number: ", phone_number)
            return phone_number
        except Exception as ex:
            print(ex)

    def unit_count(self):
        try:
            unit_count = self.config.get("watch_demo_locator", "unit_count")
            print("unit_count: ", unit_count)
            return unit_count
        except Exception as ex:
            print(ex)

    def job_title(self):
        try:
            job_title = self.config.get("watch_demo_locator", "job_title")
            print("watch_demo_button: ", job_title)
            return job_title
        except Exception as ex:
            print(ex)

    def watch_demo_submit_button(self):
        try:
            watch_demo_submit_button = self.config.get("watch_demo_locator", "watch_demo_submit_button")
            print("watch_demo_button: ", watch_demo_submit_button)
            return watch_demo_submit_button
        except Exception as ex:
            print(ex)

    def home_page_title(self):
        try:
            home_page_title = self.config.get("validation_data", "home_page_title")
            print("home_page_title: ", home_page_title)
            return home_page_title
        except Exception as ex:
            print(ex)

    def first_name_data(self):
        try:
            first_name_data = self.config.get("data", "first_name_data")
            print("first_name_data: ", first_name_data)
            return first_name_data
        except Exception as ex:
            print(ex)

    def last_name_data(self):
        try:
            last_name_data = self.config.get("data", "last_name_data")
            print("last_name_data: ", last_name_data)
            return last_name_data
        except Exception as ex:
            print(ex)

    def email_id_data(self):
        try:
            email_id_data = self.config.get("data", "email_id_data")
            print("email_id_data: ", email_id_data)
            return email_id_data
        except Exception as ex:
            print(ex)

    def company_name_data(self):
        try:
            company_name_data = self.config.get("data", "company_name_data")
            print("company_name_data: ", company_name_data)
            return company_name_data
        except Exception as ex:
            print(ex)

    def phone_number_data(self):
        try:
            phone_number_data = self.config.get("data", "phone_number_data")
            print("phone_number_data: ", phone_number_data)
            return phone_number_data
        except Exception as ex:
            print(ex)

    def unit_count_data(self):
        try:
            unit_count_data = self.config.get("data", "unit_count_data")
            print("first_name_data: ", unit_count_data)
            return unit_count_data
        except Exception as ex:
            print(ex)

    def job_title_data(self):
        try:
            job_title_data = self.config.get("data", "job_title_data")
            print("first_name_data: ", job_title_data)
            return job_title_data
        except Exception as ex:
            print(ex)




