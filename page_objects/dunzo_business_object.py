"""
This class models the objects present in the dunzo business page
The business page consists of buttons and business specification divisions
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import time

class Dunzo_Business_Object():
    "Page object for Business page"

    #locators
    about_dunzo_business = locators.about_dunzo_business
    sign_up_button = locators.sign_up_button
    business_specification = locators.business_specification
    video_feedback_section = locators.video_feedback_section
    business_feedback_section = locators.business_feedback_section

    @Wrapit._exceptionHandler
    def check_about_dunzo_business_present(self):
        "Check whether about dunzo business is present"
        result_flag =  self.check_element_displayed(self.about_dunzo_business)
        self.conditional_write(result_flag,
            positive='About Dunzo business is present in the business page',
            negative='Failed to detect About Dunzo business in the business page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_sign_up_button(self):
        "Check whether sign up button is present"
        result_flag =  self.check_element_displayed(self.sign_up_button)
        self.conditional_write(result_flag,
            positive='Sign up button is present in the business page',
            negative='Failed to detect Sign up button in the business page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_business_specification(self):
        "Check whether business specification is present"
        result_flag =  self.check_element_displayed(self.business_specification)
        self.conditional_write(result_flag,
            positive='Business Specification is present in the business page',
            negative='Failed to detect Business Specification in the business page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_video_feedback_section(self):
        "Check whether Video Feedback division is present"
        result_flag =  self.check_element_displayed(self.video_feedback_section)
        self.conditional_write(result_flag,
            positive='Video Feedback division is present in the business page',
            negative='Failed to detect Video Feedback division in the business page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_business_feedback_section(self):
        "Check whether Business Feedback division is present"
        result_flag =  self.check_element_displayed(self.business_feedback_section)
        self.conditional_write(result_flag,
            positive='Business Feedback division is present in the business page',
            negative='Failed to detect Business Feedback division in the business page',
            level='debug')

        return result_flag
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_business_page_elements(self):
        "Check's all Business page web elements"
        result_flag = self.check_about_dunzo_business_present()
        result_flag &= self.check_sign_up_button()
        result_flag &= self.check_business_specification()
        result_flag &= self.check_video_feedback_section()
        result_flag &= self.check_business_feedback_section()

        return result_flag

