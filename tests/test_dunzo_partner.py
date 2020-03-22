"""
This is an automated test to verify the following features to check Dunzo partner sign up feature on the Dunzo web application
    #Open https://www.dunzo.com/
    #Click on Dunzo partner 
    #Click on sign up and fill the form details
    #Verify the prompted message
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.dunzo_partner_conf as partner_conf
import pytest

@pytest.mark.GUI
def test_dunzo_partner(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
    
        # Turn on the highlighting feature
        #test_obj.turn_on_highlight()

        #1. Create a test object and fill the Dunzo partner sign up form
        test_obj = PageFactory.get_page_object("dunzo main page")

        #2. Click on Dunzo for partners
        result_flag = test_obj.click_partners()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Dunzo for Partners\n",
                            negative="Failed to click on Dunzo for Partners \nOn url: %s"%test_obj.get_current_url(),
                            level="critical") 

        #2. Click on sign me up
        result_flag = test_obj.click_sign_up()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Sign me up\n",
                            negative="Failed to click on Sign me up\nOn url: %s"%test_obj.get_current_url(),
                            level="critical") 

        #3. Get the test details from the conf file
        name = partner_conf.name
        city = partner_conf.city
        number = partner_conf.number

        #4. Set the form details and submit the form
        result_flag = test_obj.submit_form(name,city,number)
        test_obj.log_result(result_flag,
                            positive="Successfully submitted the form\n",
                            negative="Failed to submit the form \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")

        #5. Verify if it has prompted the message
        result_flag = test_obj.check_phone_num_alert_msg()
        test_obj.log_result(result_flag,
                            positive="Successfully prompted to enter valid phone number\n",
                            negative="Failed to prompt to enter valid phone number \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")

        #6. Print out the result
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

        test_dunzo_partner(test_obj)
                
        #teardowm
        test_obj.wait(3)
        test_obj.teardown() 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())