'''
Created on 04/03/2012

@author: ogonbat
'''
import unittest
from django_phonehub.aastra.api import AastraIPPhoneTextMenu, MenuItem 
from django_phonehub.aastra.items import SoftKeyItem
class PhoneHubTestCase(unittest.TestCase):
    def setUp(self):
        self.textmenu = AastraIPPhoneTextMenu()
        self.textmenu.addTitle("this is a test")
        self.textmenu.setDestroyOnExit("yes")
        self.textmenu.setAllowConf('yes')
        #add menu item
        menuItem = MenuItem()
        menuItem.addItem("Prompt First Item","http://www.google.com")
        menuItem.addItem("Prompt Second Item","http://www.yahoo.com")
        self.textmenu.addMenuItems(menuItem)
        
        #add SoftKey
        softkeyitem = SoftKeyItem()
        softkeyitem.addItem("Test Softkey One", "www.aastra.com")
        softkeyitem.addItem("Test Softkey Two", "www.aastra.com")
        self.textmenu.addSoftKeysItems(softkeyitem)
        
        
    def test_aastra_text_menu(self):
        #print self.textmenu.getXMLRender()
        self.assertEqual(self.textmenu.getXMLRender(),'<AastraIPPhoneTextMenu destroyOnExit="yes" allowConf="yes"><Title wrap="no">this is a test</Title><MenuItem><Prompt>Prompt First Item</Prompt><URI>http://www.google.com</URI></MenuItem><MenuItem><Prompt>Prompt Second Item</Prompt><URI>http://www.yahoo.com</URI></MenuItem><SoftKey><Label>Test Softkey One</Label><URI>www.aastra.com</URI></SoftKey><SoftKey><Label>Test Softkey Two</Label><URI>www.aastra.com</URI></SoftKey></AastraIPPhoneTextMenu>')