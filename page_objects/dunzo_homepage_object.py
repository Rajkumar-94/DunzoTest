"""
This class models the objects available on dunzo main page 
The dunzo home page has some input fields and buttons
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import time

class Dunzo_Homepage_Object():
    "Page object for home page"

    #locators
    dunzo_partner_button = locators.dunzo_partner_button
    dunzo_business_button = locators.dunzo_business_button
    app_link = locators.app_link
    sign_in = locators.sign_in
    location_input = locators.location_input
    proceed_button = locators.proceed_button
    available_locations = locators.available_locations
    available_options = locators.available_options
    download_app = locators.download_app
    google_play_link = locators.google_play_link
    apple_store_link = locators.apple_store_link
    mobile_num = locators.mobile_num
    get_app_link_button = locators.get_app_link_button
    become_dunzo_partner_button = locators.become_dunzo_partner_button
    get_dunzo_business_button = locators.get_dunzo_business_button
    dunzo_feedback = locators.dunzo_feedback
    partner_title = "Dunzo"
    business_url = "www.dunzo.com/business"

    @Wrapit._exceptionHandler
    def check_partner_button(self):
        if self.check_element_displayed(self.popup_close):
            self.click_element(self.popup_close)
        "Check whether Dunzo for partner button is present"
        result_flag = self.check_element_displayed(self.dunzo_partner_button)
        self.conditional_write(result_flag,
            positive='Dunzo Partner button is present in Home page',
            negative='Failed to detect Dunzo Partner button in Home page',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    def check_business_button(self):
        "Check whether Dunzo for business button is present"
        result_flag = self.check_element_displayed(self.dunzo_business_button)
        self.conditional_write(result_flag,
            positive='Dunzo Business button is present in Home page',
            negative='Failed to detect Dunzo Business button in Home page',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    def check_app_link(self):
        "Check whether app link option is present"
        result_flag = self.check_element_displayed(self.app_link)
        self.conditional_write(result_flag,
            positive='Get App link option is present in Home page',
            negative='Failed to detect Get App link option in Home page',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    def check_sign_in_option(self):
        "Check whether sign option is present"
        result_flag = self.check_element_displayed(self.sign_in)
        self.conditional_write(result_flag,
            positive='Sign in option is present in Home page',
            negative='Failed to detect Sign in option in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_location_input(self):
        "Check whether location input option is present"
        result_flag = self.check_element_displayed(self.location_input)
        self.conditional_write(result_flag,
            positive='Location input option is present in Home page',
            negative='Failed to detect Location input option in Home page',
            level='debug')

        return result_flag
    
    @Wrapit._exceptionHandler
    def check_proceed_button(self):
        "Check whether proceed button is present"
        result_flag = self.check_element_displayed(self.proceed_button)
        self.conditional_write(result_flag,
            positive='Proceed button option is present in Home page',
            negative='Failed to detect Proceed button in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_available_location(self):
        "Check whether available locations are present"
        result_flag = self.check_element_displayed(self.available_locations)
        self.conditional_write(result_flag,
            positive='Available locations are present in Home page',
            negative='Failed to detect Available locations in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_download_app_option(self):
        "Check whether download app option is present"
        result_flag = self.check_element_displayed(self.download_app)
        self.conditional_write(result_flag,
            positive='Download app option is present in Home page',
            negative='Failed to detect Download app option in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_google_play_link(self):
        "Check whether Google Play link is present"
        result_flag =self.check_element_displayed(self.google_play_link)
        self.conditional_write(result_flag,
            positive='Google Play link is present in Home page',
            negative='Failed to detect Google Play link in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_apple_store_link(self):
        "Check whether apple store link is present"
        result_flag = self.check_element_displayed(self.apple_store_link)
        self.conditional_write(result_flag,
            positive='Apple store link is present in Home page',
            negative='Failed to detect Apple store link in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_mobile_num_input(self):
        "Check whether input for mobile number option is present"
        result_flag = self.check_element_displayed(self.mobile_num)
        self.conditional_write(result_flag,
            positive='Input space for mobile number is present in Home page',
            negative='Failed to detect Input space for mobile number in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_get_app_link_button(self):
        "Check whether Get app link button is present"
        result_flag = self.check_element_displayed(self.get_app_link_button)
        self.conditional_write(result_flag,
            positive='Get app link option is present in Home page',
            negative='Failed to detect Get app link option in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_become_dunzo_partner_button(self):
        "Check whether become Dunzo Partner button is present"
        result_flag = self.check_element_displayed(self.become_dunzo_partner_button)
        self.conditional_write(result_flag,
            positive='Become Dunzo Partner button is present in Home page',
            negative='Failed to detect Become Dunzo Partner button in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_get_dunzo_business_button(self):
        "Check whether Get your business on Dunzo button is present"
        result_flag = self.check_element_displayed(self.get_dunzo_business_button)
        self.conditional_write(result_flag,
            positive='Get your business on Dunzo button is present in Home page',
            negative='Failed to detect Get your business on Dunzo button in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_dunzo_feedback_division(self):
        "Check whether Dunzo feedback is present"
        result_flag = self.check_element_displayed(self.dunzo_feedback)
        self.conditional_write(result_flag,
            positive='Dunzo feedback is present in Home page',
            negative='Failed to detect Dunzo feedback in Home page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_home_page_elements(self):
        "Check's all home page web elements"
        result_flag = self.check_partner_button()
        result_flag &= self.check_business_button()
        result_flag &= self.check_app_link()
        result_flag &= self.check_sign_in_option()
        result_flag &= self.check_location_input()
        result_flag &= self.check_proceed_button()
        result_flag &= self.check_available_location()
        result_flag &= self.check_download_app_option()
        result_flag &= self.check_google_play_link()
        result_flag &= self.check_apple_store_link()
        result_flag &= self.check_mobile_num_input()
        result_flag &= self.check_get_app_link_button()
        result_flag &= self.check_become_dunzo_partner_button()
        result_flag &= self.check_get_dunzo_business_button()
        result_flag &= self.check_dunzo_feedback_division()

        return result_flag 

    @Wrapit._exceptionHandler
    def click_partners(self):
        "Close the popup if present  on the main page"
        if self.check_element_present(self.popup_close):
            self.click_element(self.popup_close)
        "Click on Dunzo partner button"
        result_flag = self.click_element(self.dunzo_partner_button)
        self.conditional_write(result_flag,
            positive='Clicked on the Dunzo partner button',
            negative='Failed to click on Dunzo partner button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def click_business(self):
        "Close the popup if present  on the main page"
        if self.check_element_present(self.popup_close):
            self.click_element(self.popup_close)
        "Click on Dunzo business button"
        result_flag = self.click_element(self.dunzo_business_button)
        self.conditional_write(result_flag,
            positive='Clicked on the Dunzo business button',
            negative='Failed to click on Dunzo business button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect_to_partner_page(self):
        "Check if we have been redirected to the partner page"
        result_flag = False
        if self.partner_title in self.driver.title:
            result_flag = True
            self.switch_page("partner page")
        
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect_to_business_page(self):
        "Check if we have been redirected to the partner page"
        result_flag = False
        if self.business_url in self.driver.current_url:
            result_flag = True
            self.switch_page("business page")
        
        return result_flag



    



    



