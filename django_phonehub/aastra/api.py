'''
Created on 01/03/2012

@author: ogonbat
'''
class AastraIPPhoneTextMenu():
    root_name = "AastraIPPhoneTextMenu"
    xmlRoot = ""
    xmlRoot_Content = ""
    def __init__(self, defaultIndex = None, destroyOnExit = "no", style = "numbered", Beep="no", Timeout = None, LockIn = "no", 
                 allowAnswer="no", allowDrop="no", allowXfer="no", allowConf="no", cancelAction=None, wrapList="no", scrollConstrain="no", 
                 unitScroll="no",scrollUp=None, scrollDown=None, numberLaunch="no"):
        self.xmlRoot = '<%s' % (self.root_name)
        if defaultIndex != None:
            self.xmlRoot += ' defaultIndex="%s"' % (defaultIndex)
        self.xmlRoot += ' destroyOnExit="%s"' % (destroyOnExit)
        self.xmlRoot += ' style="%s"' % (style)
        self.xmlRoot += ' Beep="%s"' % (Beep)
        if Timeout != None:
            self.xmlRoot += ' Timeout="%s"' % (Timeout)
        self.xmlRoot += ' LockIn="%s"' % (LockIn)
        self.xmlRoot += ' allowAnswer="%s"' % (allowAnswer)
        self.xmlRoot += ' allowDrop="%s"' % (allowDrop)
        self.xmlRoot += ' allowXfer="%s"' % (allowXfer)
        self.xmlRoot += ' allowConf="%s"' % (allowConf)
        if cancelAction != None:
            self.xmlRoot += ' cancelAction="%s"' % (cancelAction)
        self.xmlRoot += ' wrapList="%s"' % (wrapList)
        self.xmlRoot += ' scrollConstrain="%s"' % (scrollConstrain)
        self.xmlRoot += ' unitScroll="%s"' % (unitScroll)
        if scrollUp != None:
            self.xmlRoot += ' scrollUp="%s"' % (scrollUp)
        if scrollDown != None:
            self.xmlRoot += ' scrollDown="%s"' % (scrollDown)
        self.xmlRoot += ' numberLaunch="%s"' % (numberLaunch)
        self.xmlRoot = '>'
    def addTitle(self,text="",wrap="no"):
        self.xmlRoot_Content += '<Title wrap="%s">%s</Title>' % (wrap,text)
    def addMenuItem(self,item):
        if isinstance(item, MenuItem):
            for i in item.getItems():
                self.xmlRoot_Content += i
        else:
            raise TypeError, "Item not a MenuItem class Instance "
    def addIconList(self,icon):
        if isinstance(icon, IconList):
            for i in icon.getIcons():
                self.xmlRoot_Content += i
        else:
            raise TypeError, "Icon not a IconList class Instance "
    def addSoftKeys(self,softkey_item):
        if isinstance(softkey_item, SoftKey):
            for i in softkey_item.getSoftKey():
                self.xmlRoot_Content += i
        else:
            raise TypeError, "SoftKey Item not a SoftKey class Instance "
    def render(self):
        self.xmlRoot += self.xmlRoot_Content
        self.xmlRoot += '</%s>' % (self.root_name)
        return self.xmlRoot

class SoftKey():
    _softkey_list = []
    _content = ''
    def addSoftKey(self,soft_key_item,label,URI,index=None,icon_index=None):
        self._content = '<SoftKey'
        if index != None:
            self._content += ' index="%s"'%(index)
        if icon_index != None:
            self._content += ' icon="%s"'%(icon_index)
        self._content += '>'
        self._content += '<Label>%s</Label>'%(label)
        self._content += '<URI>%s</URI>'%(URI)
        self._content += '</SoftKey>'
        self._softkey_list.append(self._content)
    def getSoftKey(self):
        for i in self._softkey_list:
            yield i

class IconList():
    _icons_list = []
    _content = ''
    def addIcon(self,iconName,index=None):
        self._content = '<Icon'
        if index != None:
            self._content += ' index="%s"'%(index)
        self._content += '>%s</Icon>'%(iconName)
        self._icons_list.append(self._content)
    def getIcons(self):
        for i in self._icons_list:
            yield i
    
class MenuItem():
    _items_list = []
    def addItem(self,Prompt,URI,base=None,icon=None,Dial=None,Selection=None):
        item = _Item(Prompt,URI,base,icon,Dial,Selection)
        content = ''
        content += '<MenuItem'
        if base != None:
            content += ' base="%s"' % ( base )
        if icon != None:
            content += ' icon="%s"' % ( icon )
        content += '>%s</MenuItem>'%(item)
        self._items_list.append(content)
    def getItems(self):
        for item in self._items_list:
            yield item
            
class _Item():
    _content = ''
    def __init__(self,Prompt,URI,Dial=None,Selection=None):
        self._content = '<Prompt>%s</Prompt>' % (Prompt)
        self._content += '<URI>%s</URI>' % (URI)
        if Dial != None:
            if type(Dial) is dict and all(k in Dial for k in ("line","content")):
                self._content +=  '<Dial line="%s">%s</Dial>' % (Dial['line'],Dial['content'])
            else:
                self._content += '<Dial>%s</Dial>' % (Dial)
        if Selection != None:
            self._content += '<Selection>%s</Selection>' % ( Selection)
        return self._content
                