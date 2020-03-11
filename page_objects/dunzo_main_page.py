"""
This class models the dunzo main page.
URL: https://www.dunzo.com/
The page consists of base page and create task obejects
"""
from .Base_Page import Base_Page
from .dunzo_create_task_object import Dunzo_Create_Task_Object
from .dunzo_options_object import Dunzo_Options_Object
from .dunzo_partner_object import Dunzo_Partner_Object
from .dunzo_business_object import Dunzo_Business_Object
from .dunzo_header_object import Dunzo_Header_Object
from .dunzo_homepage_object import Dunzo_Homepage_Object
from .dunzo_footer_object import Dunzo_Footer_Object
from utils.Wrapit import Wrapit

class Dunzo_Main_Page(Base_Page,Dunzo_Create_Task_Object,Dunzo_Options_Object,Dunzo_Partner_Object,Dunzo_Business_Object,Dunzo_Header_Object,Dunzo_Homepage_Object,Dunzo_Footer_Object):
    "Page Object for the Dunzo's main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = ' '
        self.open(url)