"""
This class models the dunzo category order page.
The page consists of base page and create task objects
"""
from .Base_Page import Base_Page
from .dunzo_create_task_object import Dunzo_Create_Task_Object
from utils.Wrapit import Wrapit

class Dunzo_Category_Order_Page(Base_Page,Dunzo_Create_Task_Object):
    "Page Object for the Dunzo's main page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'order/send-packages/'
        self.open(url)