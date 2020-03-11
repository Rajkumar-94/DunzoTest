"""
This class models the dunzo partner page.
URL: www.dunzo.com/partner
The page consists of base page, header page, footer page and partner page objects
"""
from .Base_Page import Base_Page
from .dunzo_partner_object import Dunzo_Partner_Object
from .dunzo_header_object import Dunzo_Header_Object
from .dunzo_footer_object import Dunzo_Footer_Object
from utils.Wrapit import Wrapit

class Dunzo_Partner_Page(Base_Page,Dunzo_Partner_Object,Dunzo_Header_Object,Dunzo_Footer_Object):
    "Page Object for the Dunzo's partner page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'partner'
        self.open(url)