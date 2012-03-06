'''
Created on 01/03/2012

@author: ogonbat
'''
from phonehub.aastra.items import ExecuteItem, MessageItem, inputItem,\
    LineItem, URIItem, MenuItem, IconItem, SoftKeyItem, ConfigurationItem
class AastraIPPhoneBase():
    root_name = None
    _content = ''
    _list_root_options = []
    
    def setDefaultIndex(self,val):
        self._list_root_options.append(' defaultIndex="%s"' % (val))
        
    def setDestroyOnExit(self,val):
        self._list_root_options.append(' destroyOnExit="%s"'%(val))
    
    def setStyle(self,val):
        self._list_root_options.append(' style="%s"' % (val))
        
    def setBeep(self,val):
        self._list_root_options.append(' Beep="%s"' % (val))
   
    def setTimeout(self,val):
        self._list_root_options.append(' Timeout="%s"' % (val))
    
    def setLockIn(self,val):
        self._list_root_options.append(' LockIn="%s"' % (val))
    
    def setAllowAnswer(self,val):
        self._list_root_options.append(' allowAnswer="%s"' % (val))
    
    def setAllowDrop(self,val):
        self._list_root_options.append(' allowDrop="%s"' % (val))
    
    def setAllowXfer(self,val):
        self._list_root_options.append(' allowXfer="%s"' % (val))
    
    def setAllowConf(self,val):
        self._list_root_options.append(' allowConf="%s"' % (val))
        
    def setAllowDTMF(self,val):
        self._list_root_options.append(' allowDTMF="%s"' % (val))
    
    def setCancelAction(self,val):
        self._list_root_options.append(' cancelAction="%s"' % (val))
        
    def setDoneAction(self,val):
        self._list_root_options.append(' doneAction="%s"' % (val))
    
    def setWrapList(self,val):
        self._list_root_options.append(' wrapList="%s"' % (val))
    
    def setScrollConstrain(self,val):
        self._list_root_options.append(' scrollConstrain="%s"' % (val))
    
    def setUnitScroll(self,val):
        self._list_root_options.append(' unitScroll="%s"' % (val))
    
    def setScrollUp(self,val):
        self._list_root_options.append(' scrollUp="%s"' % (val))
    
    def setScrollDown(self,val):
        self._list_root_options.append(' scrollDown="%s"' % (val))
    
    def setScrollLeft(self,val):
        self._list_root_options.append(' scrollLeft="%s"' % (val))
    
    def setScrollRight(self,val):
        self._list_root_options.append(' scrollRight="%s"' % (val))
    
    def setNumberLaunch(self,val):
        self._list_root_options.append(' numberLaunch="%s"' % (val))
        
    def content(self):
        return self._content
    
    def addSoftKeysItems(self,softkey_item):
        if isinstance(softkey_item, SoftKeyItem):
            for i in softkey_item.getItem():
                self._content += i
        else:
            raise TypeError, "SoftKey Item not a SoftKey() class Instance"
    def addIconListItems(self,icon):
        if isinstance(icon, IconItem):
            self._content += '<IconList>'
            for i in icon.getItem():
                self._content += i
            self._content += '</IconList>'
        else:
            raise TypeError, "Icon not a IconList() class Instance"
    
    def getXMLRender(self):
        self._xmlRoot = '<%s' % (self.root_name)
        for option in self._list_root_options:
            self._xmlRoot += option
        self._xmlRoot += '>'
        self._xmlRoot += self._content
        self._xmlRoot += '</%s>' % (self.root_name)
        del self._list_root_options[:]
        return self._xmlRoot
    
class AastraIPPhoneTextMenu(AastraIPPhoneBase):
    
    def __init__(self):
        self.root_name = "AastraIPPhoneTextMenu"
        
    def addTitle(self,text,wrap="no"):
        self._content += '<Title wrap="%s">%s</Title>' % (wrap,text)
        
    def addMenuItems(self,item):
        if isinstance(item, MenuItem):
            for i in item.getItem():
                self._content += i
        else:
            raise TypeError, "Item not a MenuItem() class Instance"
             
class AastraIPPhoneImageScreen(AastraIPPhoneBase):
    def __init__(self):
        self.root_name = "AastraIPPhoneImageScreen"
        
    def setImageAction(self,val):
        self._list_root_options.append(' imageAction="%s"' % (val))
        
    def setMode(self,val):
        self._list_root_options.append(' mode="%s"' % (val))
        
    def addImageItem(self,content,height,width,verticalAlign='middle',horizontalAlign='middle'):
        self._content += '<Image'
        self._content += ' verticalAlign="%s" horizontalAlign="%s" height="%s" width="%s">'
        self._content += content
        self._content += '</Image>'

class AastraIPPhoneImageMenu(AastraIPPhoneImageScreen):
    def __init__(self):
        self.root_name = "AastraIPPhoneImageMenu"
        
    def addURLListItem(self,URIlist):
        if isinstance(URIlist, URIItem):
            self._content += '<URIList%s'%(URIlist.getBase())
            self._content += '>'
            for i in URIlist.getItem():
                self._content += i
            self._content += '</URIList>'
        else:
            raise TypeError, "URI List not a URIList() class Instance"
        
class AastraIPPhoneTextScreen(AastraIPPhoneBase):
    
    def __init__(self):
        self.root_name = "AastraIPPhoneTextScreen"
        
    def addTitle(self,text,wrap="no"):
        self._content += '<Title wrap="%s">%s</Title>' % (wrap,text)
                                                          
    def addText(self,text):
        self._content += '<Text>%s</Text>' % (text)

class AastraIPPhoneFormattedScreen(AastraIPPhoneBase):
    
    def __init__(self):
        self.root_name = "AastraIPPhoneFormattedScreen"
        
    def addLineItems(self,line):
        if isinstance(line,LineItem):
            for i in line.getItem():
                self._content += i
        else:
            raise TypeError, "line not a Line() class Instance"
        
    def addScrollLineItems(self,line,height=None): 
        if isinstance(line,LineItem):
            self._content += '<Scroll'
            if height != None:
                self._content += ' Height="%s"'%(height)
            self._content += '>'
            for i in line.getItem():
                self._content += i
            self._content += '</Scroll>'
        else:
            raise TypeError, "line not a Line() class Instance"
        
class AastraIPPhoneInputScreen(AastraIPPhoneBase):
    def __init__(self):
        self.root_name = "AastraIPPhoneInputScreen"
        
    def setLanguage(self,val="English"):
        if val != "English":
            self._list_root_options.append(' inputLanguage="%s"' % (val))
            
    def setType(self,val="string", is_password=False):
        if val != "string":
            self._list_root_options.append(' type="%s"' % (val))
        if is_password != False:
            self._list_root_options.append(' password="yes"')
            
    def addInputItem(self,prompt,URL,parameter,default,title=None,title_wrap="no"):
        if title != None:
            self._content += '<Title'
            if title_wrap != "no":
                self._content += ' wrao="%s"'%(title_wrap)
            self._content += '>%s</Title>'%(title)
        self._content += '<Prompt>%s</Prompt>'%(prompt)
        self._content += '<URL>%s</URL>'%(URL)
        self._content += '<Parameter>%s</Parameter>'%(parameter)
        self._content += '<Default>%s</Default>'%(default)
                
class AastraIPPhoneMultiInputScreen(AastraIPPhoneBase):
    def __init__(self):
        self.root_name = "AastraIPPhoneInputScreen"
    
    def setDisplayMode(self,val="normal"):
        if val != "normal":
            self._list_root_options.append(' displayMode="condensed"')
    
    def setEditable(self,val="yes"):
        if val != "yes":
            self._list_root_options.append(' editable="no"')
    
    def setType(self,val="string", is_password=False):
        if val != "string":
            self._list_root_options.append(' type="%s"' % (val))
        if is_password != False:
            self._list_root_options.append(' password="yes"')
    
    def addInputItems(self,item):
        if isinstance(item, inputItem):
            for i in inputItem.getItem():
                self._content += i

class AastraIPPhoneStatus(AastraIPPhoneBase):
    def __init__(self):
        self.root_name = "AastraIPPhoneStatus"
        
    def setTriggerDestroyOnExit(self,val="no"):
        if val != "no":
            self._list_root_options.append(' triggerDestroyOnExit="yes"')
            
    def addMessageItems(self,messageItem,Session=None):
        if Session != None:
            self._content = '<Session>%s</Session>'%(Session)
        if isinstance(messageItem,MessageItem):
            for i in messageItem.getItem():
                self._content += i
        else:
            raise TypeError, "Item Message Variable not a MessageItem() class Instance"

class AastraIPPhoneExecute(AastraIPPhoneBase):
    
    def __init__(self):
        self.root_name = "AastraIPPhoneExecute"
        
    def setTriggerDestroyOnExit(self,val="no"):
        if val != "no":
            self._list_root_options.append(' triggerDestroyOnExit="yes"')
    
    def addExecuteItems(self,item):
        if isinstance(item, ExecuteItem):
            for i in item.getItem():
                self._content += i
        else:
            raise TypeError, "Item Execute Variable not a ExecuteItem() class Instance"

class AastraIPPhoneConfiguration(AastraIPPhoneBase):
    def __init__(self):
        self.root_name = "AastraIPPhoneConfiguration"
        
    def setTriggerDestroyOnExit(self,val="no"):
        if val != "no":
            self._list_root_options.append(' triggerDestroyOnExit="yes"')
            
    def setType(self,val="remote"):
        if val != "remote":
            self._list_root_options.append(' setType="%s"' % (val))
    
    def addConfigurationItems(self,item):
        if isinstance(item, ConfigurationItem):
            for i in item.getItem():
                self._content += i
        else:
            raise TypeError, "Item Configuration Variable not a ConfigurationItem() class Instance"