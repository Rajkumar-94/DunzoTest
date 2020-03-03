import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
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

        #2. Click on create task in the home page
        result_flag = test_obj.click_restaurants()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked the create task\n",
                            negative="Failed to click on create task \nOn url: %s"%test_obj.get_current_url(),
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

        test_dunzo_task(test_obj)
                
        #teardowm
        test_obj.wait(3)
        test_obj.teardown() 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())