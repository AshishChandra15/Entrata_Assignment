


This is Test Framework created by @Demo for Entrata \
This Automation Test Project Is Only For Demo purpose.
>> before running script please be sure all requirements are met and test environment is created. \
>> Re-verify conftest.py file inside All-Test-Cases-Package. \
>> Re-verify 
>> # Watch Demo Page
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