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
    sign_up = locators.sign_me_up
    name_field = locators.name_field
    city_field = locators.city_field
    number_field = locators.number_field
    submit_button = locators.submit_button
    enter_valid_num_message = locators.phone_number_message
    partner_specification = locators.partner_specification
    partner_feedback = locators.partner_feedback
    partner_sign_up_form = locators.partner_sign_up_form

    @Wrapit._exceptionHandler
    def check_sign_up_button(self):
        "Check whether sign me up button is present"
        result_flag =  self.check_element_displayed(self.sign_up)
        self.conditional_write(result_flag,
            positive='Sign up button is present in the Partner page',
            negative='Failed to detect Sign up button in the Partner page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_partner_specification(self):
        "Check whether partner specification is present"
        result_flag =  self.check_element_displayed(self.partner_specification)
        self.conditional_write(result_flag,
            positive='Partner specification is present in the Partner page',
            negative='Failed to detect Partner specification in the Partner page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_partner_feedback(self):
        "Check whether partner feedback is present"
        result_flag =  self.check_element_displayed(self.partner_feedback)
        self.conditional_write(result_flag,
            positive='Partner feedback is present in the Partner page',
            negative='Failed to detect Partner feedback in the Partner page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_partner_sign_up_form(self):
        "Check whether Partner sign-up form is present"
        result_flag =  self.check_element_displayed(self.partner_sign_up_form)
        self.conditional_write(result_flag,
            positive='Partner sign-up form is present in the Partner page',
            negative='Failed to detect Partner sign-up form in the Partner page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_partner_page_elements(self):
        "Check's all Partner page web elements"
        result_flag = self.check_sign_up_button()
        result_flag &= self.check_partner_specification()
        result_flag &= self.check_partner_feedback()
        result_flag &= self.check_partner_sign_up_form()

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_sign_up(self):
        "Click on Sign me up"
        result_flag = self.click_element(self.sign_up)
        self.conditional_write(result_flag,
            positive='Clicked on Sign me up',
            negative='Failed to click on Sign me up',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_name(self,name):
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
        #time.sleep(5)
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

