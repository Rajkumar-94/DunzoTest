"""
This class models the dunzo business page.
URL: www.dunzo.com/business
The page consists of base page, header page, footer page and business page objects
"""
from .Base_Page import Base_Page
from .dunzo_business_object import Dunzo_Business_Object
from .dunzo_header_object import Dunzo_Header_Object
from .dunzo_footer_object import Dunzo_Footer_Object
from utils.Wrapit import Wrapit

class Dunzo_Business_Page(Base_Page,Dunzo_Header_Object,Dunzo_Footer_Object,Dunzo_Business_Object):
    "Page Object for the Dunzo's partner page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'business'
        self.open(url)