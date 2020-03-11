"""This class models the https://www.dunzo.com/ footer as a Page Object.
The footer consists of the Dunzo logo and the footer divisions.
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Dunzo_Footer_Object():
    "Page Object for the header class"

    #locators
    home_footer_div = locators.home_footer_division
    redirect_footer_div = locators.redirect_footer_div

    @Wrapit._exceptionHandler
    def check_home_page_footer_div(self):
        "Check whether proceed button is present"
        result_flag = self.check_element_displayed(self.home_footer_div)
        if result_flag == True:
            self.switch_page("dunzo main page")
        return result_flag

    @Wrapit._exceptionHandler
    def check_redirect_page_footer_div(self):
        "Check whether proceed button is present"
        result_flag = self.check_element_displayed(self.redirect_footer_div)
        if result_flag == True:
            self.switch_page("dunzo main page")
        return result_flag