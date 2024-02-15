
This is Test Framework created for @Demo Entrata \
This Automation Test Project Is Only For Demo purpose.
>> before running script please be sure all requirements are met and test environment is created. \
>> Re-verify conftest.py file inside All-Test-Cases-Package. \
>> Re-verify 

# Pre-requisites
>> Selenium with Python Project \
>This project demonstrates how to use Selenium with Python for automated web testing.

> ## Overview
>Selenium is a powerful tool for automating web browsers.It provides a simple API for interacting with web pages, 
allowing you to simulate user actions such as clicking buttons, filling out forms, and navigating between pages.
This project showcases how to set up Selenium with Python and provides examples of common tasks such as web scraping and automated testing.

> ## Requirements
> Python 3.x \
> Selenium WebDriver \
> Web browser (Chrome, Firefox, etc.)

> ## Installation
>1. Clone this repository: \
    git clone https://github.com/AshishChandra15/Entrata_Assignment.git

>2. Install Python dependencies: \
>pip install -r requirements.txt

>## Usage to run the script
> pytest --html=report.html 

>> ## Watch Demo Page
>> Update Locators:\
>> [Common_Data]\
>> url = https://www.entrata.com/ \

>> [watch_demo_locator] \
>accept_cookies = //button[@class='button-default dark-cookie-button cookie-accept-button'] \
>watch_demo_button = (//a[@class='button-default solid-dark-button'])[1] \
>first_name = //input[@id='FirstName'] \
>last_name = //input[@id='LastName'] \
>email_id = //input[@name='Email'] \
>company_name = //input[@name='Company'] \
>phone_number  = //input[@name='Phone'] \
>unit_count = //select[@name='Unit_Count__c'] \
>job_title = //input[@name='Title'] \
>watch_demo_submit_button = //button[text()='Watch Demo'] \

>> [validation_data] \
>home_page_title = Property Management Software | Entrata \

>> [data] \
>first_name_data = First Name \
>last_name_data = Last Name \
>email_id_data = Email@gmail.com \
>company_name_data = Company Name \
>phone_number_data = 9876543210 \
>unit_count_data = 11-100 \
>job_title_data = Demo Test \

>> ******* Execute Suite *******\
> pytest --html=report.html

>> ***** Reports Path ******\
> report.html

>> ****** Loggers ******\
> Application_Logs
