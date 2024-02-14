import pytest

from All_POM_Packages.Watch_Demo_Page_POM.Watch_Demo_Page_POM import Watch_Demo_Page_Pom
from Base_Package.Web_Driver import web_driver

from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=1)
class Test_Watch_Demo_Page_Test_Cases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Watch_Demo_Page (Order - 1) Begin ********")
    print("******** Watch_Demo_Page (Order - 1) Begin ********")

    @pytest.mark.p1
    def test_Watch_Demo_TC01(self):
        if Watch_Demo_Page_Pom().verify_user_able_to_hit_the_url():
            assert True
        else:
            assert False

    def test_Watch_Demo_TC02(self):
        if Watch_Demo_Page_Pom().verify_user_is_able_to_fill_the_watch_demo_form():
            assert True
        else:
            assert False

    def test_Watch_Demo_TC03(self):
        if Watch_Demo_Page_Pom().verify_watch_demo_button_is_enable_and_clickable():
            assert True
        else:
            assert False

    def test_Watch_Demo_TC04(self):
        if Watch_Demo_Page_Pom().verify_when_user_click_on_watch_demo_button_then_redirect_on_watch_demo_page():
            assert True
        else:
            assert False





