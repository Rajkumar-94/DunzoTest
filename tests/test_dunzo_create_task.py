"""
This is an automated test to verify the following features to create a task for shipping for Dunzo web application
    #Open https://www.dunzo.com/
    #Click on create a task
    #Verify if redirected to send package page
    #Set the pick up and drop address 
    #Get the estimated shipping amount for the created task based on the provided address
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.dunzo_address_conf as dunzo_address
import pytest


@pytest.mark.GUI
def test_dunzo_task(test_obj):
    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
    
        # Turn on the highlighting feature
        test_obj.turn_on_highlight()

        #1. Create a test object and create the task.
        test_obj = PageFactory.get_page_object("dunzo main page") 

        #Set start_time with current time
        start_time = int(time.time())
        
        #2. Click on create task in the home page
        result_flag = test_obj.click_on_create_task()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked the create task\n",
                            negative="Failed to click on create task \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #3. Verify if re-directed to the correct page i.e send package page
        if result_flag is True:
            result_flag = test_obj.check_redirect()
        test_obj.log_result(result_flag,
                            positive="Redirected correctly to the create task page!!\n",
                            negative="Fail: Redirection to the create task page failed!")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #4. Get details from conf file
        pick_address = dunzo_address.partial_pick_address
        pick_up_flat_num = dunzo_address.pick_house_num
        drop_address = dunzo_address.partial_drop_address
        drop_flat_num = dunzo_address.drop_house_num

        #5. Set the pick up address
        result_flag = test_obj.set_pick_up_address(pick_address,pick_up_flat_num)
        test_obj.log_result(result_flag,
                            positive="Successfully set the pick up address",
                            negative="Failed to set the pick up address:\nOn url: %s\n"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #6. set the drop address
        result_flag = test_obj.set_drop_address(drop_address,drop_flat_num)
        test_obj.log_result(result_flag,
                            positive="Successfully set the drop address",
                            negative="Failed to set the drop address \nOn url: %s\n"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #7. Get the estimated amount for the shipping
        result_flag = test_obj.get_price()
        test_obj.log_result(result_flag,
                            positive="Successfully fetched the price",
                            negative="Failed to fetch the price \nOn url: %s\n"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #8. Print out the result
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