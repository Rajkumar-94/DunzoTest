"""
Super hero test for Dunzo Web App - will only fight super-villans
Our automated test will do the following:
    #1.  Launch the Dunzo main page
    #2.  Validates main page logo
    #3.  Checks whether all elemensts are present in home page
    #4.  Validates footer section
    #5.  Clicks on Dunzo Partner button
    #6.  Checks whether redirected to partner page
    #7.  Validates partner page logo
    #8.  Checks whether all elemensts are present in partner page
    #9.  Validates partner page footer section and redirectes to home page
    #10. Clicks on Dunzo Business button
    #11. Checks whether redirected to business page
    #12. Validates business page logo
    #13. Checks whether all elemensts are present in business page
    #14. Validates business page footer section and redirectes to home page

"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import pytest

@pytest.mark.GUI
def test_dunzo_superhero(test_obj):
    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #Set start_time with current time
        start_time = int(time.time())

        #1. Create a test object.
        test_obj = PageFactory.get_page_object("dunzo main page") 

        #2. Validate logo is present
        result_flag = test_obj.check_home_page_logo_present()
        test_obj.log_result(result_flag,
                            positive="Dunzo Logo is present in home page\n",
                            negative="Failed to load Dunzo Logo on home page \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #3. Validate all home page web elements
        result_flag = test_obj.check_home_page_elements()
        test_obj.log_result(result_flag,
                            positive="Checked all home page elements\n",
                            negative="Failed to check all home page elements\nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #4. Validates home page footer section
        result_flag = test_obj.check_home_page_footer_div()
        test_obj.log_result(result_flag,
                            positive="checked home page footer_division\n",
                            negative="Failed to load home page footer_division\nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #5. Clicks on Dunzo Partner button
        result_flag = test_obj.click_partners()    
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Dunzo for Partners button\n",
                            negative="\nFailed to click on Dunzo for Partners button \n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #6. Checks whether redirected to partner page
        result_flag = test_obj.check_redirect_to_partner_page()    
        test_obj.log_result(result_flag,
                            positive="Successfully redirected to partner page\n",
                            negative="\nFailed to redirect to partner page \n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #7. Validate logo is present in Partner page
        result_flag = test_obj.check_redirect_logo()
        test_obj.log_result(result_flag,
                            positive="Dunzo Logo is present in partner page\n",
                            negative="Failed to load Dunzo Logo on partner page \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))


        #8. Checks whether all elemensts are present in partner page
        result_flag = test_obj.check_partner_page_elements()
        test_obj.log_result(result_flag,
                            positive="Checked all partner page elements\n",
                            negative="Failed to check all partner page elements\nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #9. Validates partner page footer section and redirectes to home page
        result_flag = test_obj.check_redirect_page_footer_div()
        test_obj.log_result(result_flag,
                            positive="checked partner page footer_division\n",
                            negative="Failed to load partner page footer_division\nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #10. Clicks on Dunzo Business button
        result_flag = test_obj.click_business()    
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Dunzo for Business button\n",
                            negative="\nFailed to click on Dunzo for Business button \n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #11. Checks whether redirected to business page
        result_flag = test_obj.check_redirect_to_business_page()    
        test_obj.log_result(result_flag,
                            positive="Successfully redirected to business page\n",
                            negative="\nFailed to redirect to business page \n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #12. Validate logo is present in Business page
        result_flag = test_obj.check_redirect_logo()
        test_obj.log_result(result_flag,
                            positive="Dunzo Logo is present in business page\n",
                            negative="Failed to load Dunzo Logo on business page \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #13. Checks whether all elemensts are present in business page
        result_flag = test_obj.check_business_page_elements()
        test_obj.log_result(result_flag,
                            positive="Checked all elements in business page\n",
                            negative="Failed to check all business page elements\nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #14. Validates business page footer section and redirectes to home page
        result_flag = test_obj.check_redirect_page_footer_div()
        test_obj.log_result(result_flag,
                            positive="Business page footer division is present\n",
                            negative="Failed to load Business page footer_division\nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #15. Print out the result
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
        test_dunzo_superhero(test_obj)
                
        #teardowm
        test_obj.wait(3)
        test_obj.teardown() 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())