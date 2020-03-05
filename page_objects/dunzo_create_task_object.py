"""
This class models the create task on the dunzo main page 
The create task option has some input fields and buttons
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import time

class Dunzo_Create_Task_Object():
    "Page object for Create Task"

    #locators
    popup_close = locators.popup_close
    create_task_button = locators.create_task
    pick_up_click = locators.pick_up_click
    address = locators.partial_address
    area_loc = locators.area_location
    flat_num = locators.flat_number
    pick_continue = locators.pick_adress_continue_button
    drop_click = locators.drop_click
    partial_drop_address = locators.partial_drop_address
    drop_area_loc = locators.drop_area_location
    drop_flat_num = locators.drop_flat_number
    drop_continue = locators.drop_adress_continue_button
    amount_to_pay = locators.amount_to_pay
    redirect_title = "Category Order"

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_on_create_task(self):
        "Close the popup if present  on the main page"
        if self.check_element_present(self.popup_close):
            self.click_element(self.popup_close)

        "Click on Create task button"
        result_flag = self.click_element(self.create_task_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "create task" button',
            negative='Failed to click on "create task" button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect(self):
        "Check if redirected to the send package page"
        result_flag = False

        if self.redirect_title in self.driver.title:
            result_flag = True
            self.switch_page("dunzo category order page")
            
        return result_flag        

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_on_pick_up_address(self):
        "Click on 'Create pick up address"

        result_flag = self.click_element(self.pick_up_click)
        self.conditional_write(result_flag,
            positive='Clicked on the "pick up address" button',
            negative='Failed to click on "pick up address" button',
            level='debug')
        
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_partial_address(self,pick_address):
        "Set the partial pick up location"
        result_flag = self.set_text(self.address,pick_address)
        self.conditional_write(result_flag,
            positive='Set the pick up address to: %s'%pick_address,
            negative='Failed to set the pick up address in the form',
            level='debug')
        
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_area_location(self):
        "Click on the given location"
        result_flag = self.click_element(self.area_loc)
        self.conditional_write(result_flag,
            positive='Clicked on the "pick up area" button',
            negative='Failed to click on "pick up area" button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_flat_num(self,house_num):
        "Set the pick up house number"
        result_flag = self.set_text(self.flat_num,house_num)
        self.conditional_write(result_flag,
            positive='Set the pick up house number to: %s'%house_num,
            negative='Failed to set the house number in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_continue(self):
        "Click on continue after pick up address is set"
        result_flag = self.click_element(self.pick_continue)
        self.conditional_write(result_flag,
            positive='Clicked on the "continue" while filling the pick up address',
            negative='Failed to click on "continue" while filling the pick up address',
            level='debug')

        return result_flag
        
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_pick_up_address(self,pick_address,house_num):
        "Set the pick up address at once"
        result_flag = self.click_on_pick_up_address()
        result_flag &= self.set_partial_address(pick_address)
        result_flag &= self.click_area_location()
        result_flag &= self.set_flat_num(house_num)
        result_flag &= self.click_continue()
        return result_flag   

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_on_drop_address(self):
        "Click on drop address"
        result_flag = self.click_element(self.drop_click)
        self.conditional_write(result_flag,
            positive='Clicked on the "drop address" button',
            negative='Failed to click on "drop address" button',
            level='debug')
        
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_partial_drop_address(self,drop_address):
        "Set the partial drop location"
        result_flag = self.set_text(self.address,drop_address)
        self.conditional_write(result_flag,
            positive='Set the drop address to: %s'%drop_address,
            negative='Failed to set the drop address in the form',
            level='debug')
        
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_drop_area_location(self):
        "Click on the given location"
        result_flag = self.click_element(self.drop_area_loc)
        self.conditional_write(result_flag,
            positive='Clicked on the "pick up area" button',
            negative='Failed to click on "pick up area" button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_drop_flat_num(self,house_num2):
        "Set the drop house number"
        result_flag = self.set_text(self.flat_num,house_num2)
        self.conditional_write(result_flag,
            positive='Set the drop house number to: %s'%house_num2,
            negative='Failed to set the drop house number in the form',
            level='debug')
            
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def drop_click_continue(self):
        "Click on continue after drop address is set"
        result_flag = self.click_element(self.drop_continue)
        self.conditional_write(result_flag,
            positive='Clicked on the "continue" while filling the drop address',
            negative='Failed to click on "continue" while filling the drop address',
            level='debug')

        return result_flag
        
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_drop_address(self,drop_address,house_num2):
        "Set the drop address at once"
        result_flag = self.click_on_drop_address()
        result_flag &= self.set_partial_drop_address(drop_address)
        result_flag &= self.click_drop_area_location()
        result_flag &= self.set_drop_flat_num(house_num2)
        result_flag &= self.drop_click_continue()

        return result_flag 

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def get_price(self):
        "Get the expected shipment price"
        price = self.get_text(self.amount_to_pay)
        price=int(price.split()[-1])
        result_flag = False
        if price is not None:
            result_flag = True
            self.conditional_write(result_flag,
            positive='The expected shipment price is: %d'%price,
            negative='Failed to get the shipment price',
            level='debug')
        
        return result_flag
    



