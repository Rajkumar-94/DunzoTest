"""
This is an automated test to verify the following features to check the options like Restaurant on the Dunzo web application
    #Open https://www.dunzo.com/
    #Click on Restaurant option
    #Check if the alert message to choose location is prompted
    #Select the location
    #Clcik on Restaurants again
    #Verify if it is navigated to Restaurants page for the given location
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import pytest

@pytest.mark.GUI
def test_dunzo_options(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
    
        # Turn on the highlighting feature
        test_obj.turn_on_highlight()

        #1. Create a test object.
        test_obj = PageFactory.get_page_object("dunzo main page") 

        #2. Click on Restaurant option on the home page
        result_flag = test_obj.click_restaurant()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Restaurant\n",
                            negative="Failed to click on Restaurant \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")

        #3. Check whether alert message is saying to select a location before proceeding
        if result_flag is True:
            result_flag = test_obj.check_alert_msg()
        test_obj.log_result(result_flag,
                            positive="Select location message appeared when clicked on Restaurant!\n",
                            negative="Fail: Select location message message did not appear when clicked on Restaurant!")
        
        #4. Select location to click on any options like restaurant/grocery etc..
        if result_flag is True:
            result_flag = test_obj.click_location()
            test_obj.log_result(result_flag,
                            positive="Successfully clicked on Bangalore location\n",
                            negative="Failed to click on Bangalore location \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")

        #5. Click on Restaurant option for the given location
        result_flag = test_obj.click_restaurant()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Restaurant\n",
                            negative="Failed to click on Restaurant \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")

        #6. Check if it is navigated to Restaurants page for the given location
        result_flag = test_obj.check_restaurants()
        test_obj.log_result(result_flag,
                            positive="Successfully switched to Bangalore Restaurants page\n",
                            negative="Failed to switch to Bangalore Restaurant page \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")

        #7. Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter        

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))
    
    assert expected_pass == actual_pass, "Test failed: %s"%__file__


    #---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_obj = PageFactory.get_page_object("Zero",base_url=options.url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag,options.os_name,options.os_version,options.browser,options.browser_version,options.remote_project_name,options.remote_build_name)

        test_dunzo_task(test_obj)
                
        #teardowm
        test_obj.wait(3)
        test_obj.teardown() 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())