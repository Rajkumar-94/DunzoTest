"""
This class models the options available on the dunzo main page 
The options can be selected only after selecting the location
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import time

class Dunzo_Options_Object():
    "Page object for Options"

    #locators
    popup_close = locators.popup_close
    restaurant_option = locators.restaurant
    alert_message = locators.alert_message
    location = locators.bangalore_location
    restaurants = locators.bangalore_restaurants

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_restaurant(self):
        "Close the popup if present  on the main page"
        if self.check_element_present(self.popup_close):
            self.click_element(self.popup_close) 

        "Click on Restaurant_option"
        result_flag = self.click_element(self.restaurant_option)
        self.conditional_write(result_flag,
            positive='Clicked on the Restaurant',
            negative='Failed to click on Restaurant',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_alert_msg(self):
        "Check alret message"
        result_flag = self.check_element_present(self.alert_message)
        self.conditional_write(result_flag,
            positive='Alert message is present',
            negative='Alert message is not present',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_location(self):
        "Click on Bangalore location"
        result_flag = self.click_element(self.location)
        self.conditional_write(result_flag,
            positive='Clicked on the given location',
            negative='Failed to click on the given location',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_restaurants(self):
        "Check whether naviagted to Restaurants screen"
        result_flag = self.check_element_present(self.restaurants)
        self.conditional_write(result_flag,
            positive='Navigated to bangalore restaurants page',
            negative='Did not navigated to bangalore restaurants page',
            level='debug')

        return result_flag