"""This class models the https://www.dunzo.com/ header as a Page Object.
The header consists of the Dunzo logo and the Dunzo main options
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Dunzo_Header_Object():
    "Page Object for the header class"

    #locators
    dunzo_home_header_logo = locators.home_header_logo
    dunzo_redirect_header_logo = locators.redirect_header_logo

    @Wrapit._exceptionHandler
    def check_home_page_logo_present(self):
        "Check if a logo is present in home page"
        return self.check_element_present(self.dunzo_home_header_logo)

    @Wrapit._exceptionHandler
    def check_redirect_logo(self):
        "Check whether logo is present in the redirected page "
        return self.check_element_displayed(self.dunzo_redirect_header_logo)


