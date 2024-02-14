import sys
import colorsys
import subprocess
from pathlib import Path
import datetime
import pytest


if __name__ == "__main__":
    # ************* Report Path *********************
    Regression_suit = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Regression_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p1_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p2_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p2_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p3_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p3_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p4_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p4_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p5_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p5_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"

    # ************* Module Wise Report Path **********
    p1_report_path_pl = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\protal_login_p1_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_ng = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Notification_Groups_p1_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_events = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Events_p2_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_enrollments = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Enrollments_p1_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_detect_faces = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Detect_Faces_p1_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_tags = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Tags_p1_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_ie = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\I&E_Module_p1_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_vs = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\_7_Visitor_Search_Module_p3_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_vsj = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\_8_Visitor_Search_Jobs_Module_p3_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_notes = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\_14_Notes_Module_p1_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_Sys_level = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\System_Level_Module_p1_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path_alr = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\ALR_Module_p1_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"

    # ************* test suite path ******************
    test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\"
    test_suite_path_vs = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_7_Visitor_Search_Module\\"
    test_suite_path_ng = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_6_Notification_Groups_Module\\"
    test_suite_path_pl = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_1_Portal_Login_Module"
    test_suite_path_alr = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_16_Audit_Log_Report_Module"
    test_suite_path_vsj = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_8_Visitor_Search_Jobs_Module"
    test_suite_path_IE = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_12_Idntify_and_Enroll_Module"
    test_suite_path_events = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_10_Events_Module"
    test_suite_path_tags = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_13_tags_Module"
    test_suite_path_enrollments = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_9_Enrollment_Module"
    test_suite_path_sys_level = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_9_Enrollment_Module"
    test_suite_path_detect_faces = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_11_Detect_Faces_Module"
    test_suite_path_notes = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_14_Notes_Module"

    # ********************** Commands to Run Test Suite **********************

    # ************************** Module Wise Test Run *********************************
    # pytest.main(['-s', '-q', '-m', 'p1', f'{test_suite_path_alr}', '--html', f'{p1_report_path_alr}'])
    # pytest.main(['-s', '-q', '-m', 'p1', f'{test_suite_path_events}', '--html', f'{p1_report_path_events}'])
    # pytest.main(['-s', '-q', '-m', 'p1', f'{test_suite_path_detect_faces}', '--html', f'{p1_report_path_detect_faces}'])
    # pytest.main(['-s', '-q', '-m', 'p1', f'{test_suite_path_tags}', '--html', f'{p1_report_path_tags}'])
    # pytest.main(['-s', '-q', '-m', 'p2', f'{test_suite_path_ng}', '--html', f'{p2_report_path}'])
    # pytest.main(['-s', '-q', '-m', 'p3', f'{test_suite_path_enrollments}', '--html', f'{p2_report_path_enrollments}'])
    # pytest.main(['-s', '-q', '-m', 'p1', f'{test_suite_path_vs}', '--html', f'{p1_report_path_vs}'])
    # pytest.main(['-s', '-q', '-m', 'p5', f'{test_suite_path_ng}', '--html', f'{p5_report_path}'])
    # pytest.main(['-s', '-q', '-m', 'p1', f'{test_suite_path_notes}', '--html', f'{p1_report_path_notes}'])
    # pytest.main(['-s', '-q', '-m', 'p1', f'{test_suite_path_IE}', '--html', f'{p1_report_path_ie}'])

    # ************************** P1 Priority Test Run *********************************
    pytest.main(['-s', '-q', '-m', 'p1', f'{test_suite_path}', '--html', f'{p1_report_path}'])

    # ************************** P2 Priority Test Run *********************************
    # pytest.main(['-s', '-q', '-m', 'p2', f'{test_suite_path}', '--html', f'{p2_report_path}'])

    # ************************** P3 Priority Test Run *********************************
    # pytest.main(['-s', '-q', '-m', 'p3', f'{test_suite_path}', '--html', f'{p3_report_path}'])

    # ************************** P4 Priority Test Run *********************************
    # pytest.main(['-s', '-q', '-m', 'p4', f'{test_suite_path}', '--html', f'{p4_report_path}'])

    # ************************** P5 Priority Test Run *********************************
    # pytest.main(['-s', '-q', '-m', 'p5', f'{test_suite_path}', '--html', f'{p5_report_path}'])

    # ************************** Regression Suite Test Run *********************************
    # pytest.main(['-s', '-q', f'{test_suite_path}', '--html', f'{Regression_suit}'])
# ******************************************************************************************************************
