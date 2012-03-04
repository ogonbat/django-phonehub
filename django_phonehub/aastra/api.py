'''
Created on 01/03/2012

@author: ogonbat
'''
class AastraIPPhoneBase():
    root_name = None
    _content = ''
    _list_root_options =[]
    
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
    
    def addSoftKeys(self,softkey_item):
        if isinstance(softkey_item, SoftKey):
            for i in softkey_item.getSoftKey():
                self._content += i
        else:
            raise TypeError, "SoftKey Item not a SoftKey() class Instance "
    def addIconList(self,icon):
        if isinstance(icon, IconList):
            self._content += '<IconList>'
            for i in icon.getIcons():
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
        return self._xmlRoot
    
class AastraIPPhoneTextMenu(AastraIPPhoneBase):
    def __init__(self):
        self.root_name = "AastraIPPhoneTextMenu"
    def addTitle(self,text,wrap="no"):
        self._content += '<Title wrap="%s">%s</Title>' % (wrap,text)
    def addMenuItem(self,item):
        if isinstance(item, MenuItem):
            for i in item.getItems():
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
    def addImage(self,content,height,width,verticalAlign='middle',horizontalAlign='middle'):
        self._content += '<Image'
        self._content += ' verticalAlign="%s" horizontalAlign="%s" height="%s" width="%s">'
        self._content += content
        self._content += '</Image>'

class AastraIPPhoneImageMenu(AastraIPPhoneImageScreen):
    def __init__(self):
        self.root_name = "AastraIPPhoneImageMenu"
    def addURLList(self,URIlist):
        if isinstance(URIlist, URIList):
            self._content += '<URIList%s'%(URIlist.getBase())
            self._content += '>'
            for i in URIlist.getItems():
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
    def addLine(self,line):
        if isinstance(line,Line):
            for i in line.getLine():
                self._content += i
        else:
            raise TypeError, "line not a Line() class Instance"
    def addScrollLine(self,line,height=None): 
        if isinstance(line,Line):
            self._content += '<Scroll'
            if height != None:
                self._content += ' Height="%s"'%(height)
            self._content += '>'
            for i in line.getLine():
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
    def addInput(self,inputItem):
        if isinstance(inputItem, inputItem):
            for i in inputItem.getInput():
                self._content += i
                
class inputItem():
    _input_list = []
    def addInput(self,prompt,URL,parameter,default,title=None,title_wrap="no"):
        content = ""
        if title != None:
            content += '<Title'
            if title_wrap != "no":
                content += ' wrao="%s"'%(title_wrap)
            content += '>%s</Title>'%(title)
        content += '<Prompt>%s</Prompt>'%(prompt)
        content += '<URL>%s</URL>'%(URL)
        content += '<Parameter>%s</Parameter>'%(parameter)
        content += '<Default>%s</Default>'%(default)
        self._input_list.append(content)
    def getInput(self):
        for i in self._input_list:
            yield i
            
class URIList():
    _items_list = []
    _base = ''
    def __init__(self,base=None):
        self._base = base
    def addItem(self,Prompt,key,base=None):
        content = '<URI key="%s">%s</URI>' % (Prompt,key)
        self._items_list.append(content)
    def getBase(self):
        if self._base != None:
            return ' base="%s"'%(self._base)
        else:
            return ''
    def getItems(self):
        for item in self._items_list:
            yield item
            
class _UrlItem():
    def __init__(self,Prompt,key):
        self._content = '<URI key="%s">%s</URI>' % (Prompt,key)
    def getContent(self):
        return self._content
    
class Line():
    _line_list = []
    def addLine(self,text,Size="normal",Align="left",Color="white"):
        self._content = '<Line'
        if Size != "normal":
            self._content += ' Size="%s"'%(Size)
        if Align != "left":
            self._content += ' Align="%s"'%(Align)
        if Color != "white":
            self._content += ' Color="%s"'%(Color)
        self._content += '>'
        self._content += '%s'%(text)
        self._content += '</Line>'
        self._line_list.append(self._content)
    def getLine(self):
        for i in self._line_list:
            yield i
            
class SoftKey():
    _softkey_list = []
    def addSoftKey(self,label,URI,index=None,icon_index=None):
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
        item = _Item(Prompt,URI,Dial,Selection)
        content = ''
        content += '<MenuItem'
        if base != None:
            content += ' base="%s"' % ( base )
        if icon != None:
            content += ' icon="%s"' % ( icon )
        content += '>%s</MenuItem>'%(item.getContent())
        self._items_list.append(content)
    def getItems(self):
        for item in self._items_list:
            yield item
            
class _Item():
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
    def getContent(self):
        return self._content
                