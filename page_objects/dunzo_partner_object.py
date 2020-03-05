"""
This class models the sign up form for the dunzo partners 
The form consists of some input fields and submit buttons
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import time

class Dunzo_Partner_Object():
    "Page object for partner page"

    #locators
    click_partner_button = locators.partner_button
    sign_up_click = locators.sign_me_up
    name_field = locators.name_field
    city_field = locators.city_field
    number_field = locators.number_field
    submit_button = locators.submit_button
    enter_valid_num_message = locators.phone_number_message
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_partners(self):
        "Close the popup if present  on the main page"
        if self.check_element_present(self.popup_close):
            self.click_element(self.popup_close)
        "Click on Dunzo partner button"
        result_flag = self.click_element(self.click_partner_button)
        self.conditional_write(result_flag,
            positive='Clicked on the Dunzo partner button',
            negative='Failed to click on Dunzo partner button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_sign_up(self):
        "Click on Sign me up"
        result_flag = self.click_element(self.sign_up_click)
        self.conditional_write(result_flag,
            positive='Clicked on Sign me up',
            negative='Failed to click on Sign me up',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_name(self,name):
        time.sleep(3)
        "Set the name on the form sign up form"
        result_flag = self.set_text(self.name_field,name)
        self.conditional_write(result_flag,
            positive='Set the name to: %s'%name,
            negative='Failed to set the name field in the sign up form',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_city(self,city):
        time.sleep(3)
        "Set the city on the form sign up form"
        result_flag = self.set_text(self.city_field,city)
        self.conditional_write(result_flag,
            positive='Set the city field to: %s'%city,
            negative='Failed to set the city field in the sign up form',
            level='debug')

        return result_flag 

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_number(self,number):
        time.sleep(3)
        "Set the number on the form sign up form"
        result_flag = self.set_text(self.number_field,number)
        self.conditional_write(result_flag,
            positive='Set the number to: %d'%number,
            negative='Failed to set the number in the sign up form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_on_submit(self):
        "Click on submit button"
        
        result_flag = self.click_element(self.submit_button)
        time.sleep(5)
        self.conditional_write(result_flag,
            positive='Clicked on the Submit button',
            negative='Failed to click on Submit button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def submit_form(self,name,city,number):
        "Submit the form"
        result_flag = self.set_name(name)
        result_flag &= self.set_city(city)
        result_flag &= self.set_number(number)
        result_flag &= self.click_on_submit()  
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_phone_num_alert_msg(self):
        "Check alret message"
        result_flag = self.check_element_present(self.enter_valid_num_message)
        self.conditional_write(result_flag,
            positive='prompt to enter valid message',
            negative='Did not prompt to enter valid message',
            level='debug')

        return result_flag