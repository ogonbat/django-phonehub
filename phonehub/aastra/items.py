'''
Created on 05/03/2012

@author: ogonbat
'''
class ConfigurationItem():
    _configuration_list = []
    
    def addItem(self,paramenter,value,setType="remote"):
        content = ""
        content += '<ConfigurationItem'
        if setType != "remote":
            content += ' setType="%s"'%(setType)
        content += '<Parameter>%s</Parameter>'%(paramenter)
        content += '<Value>%s</Value>'%(value)
        content += '</ConfigurationItem>'
        self._configuration_list.append(content)    
    def getItem(self):
        for i in self._configuration_list:
            yield i
        del self._configuration_list[:]
            
class ExecuteItem():
    _execute_list = []
    
    def addItem(self,URI=None,interruptCall=None):
        content = ""
        content += '<ExecuteItem'
        if URI != None:
            content += ' URI="%s"'%(URI)
        if interruptCall != None:
            content += ' interruptCall="%s"'%(interruptCall)
        content += ' />'
        self._execute_list.append(content)
        
    def getItem(self):
        for i in self._execute_list:
            yield i
        del self._execute_list[:]

class MessageItem():
    
    _message_list = []
    
    def addItem(self,text,index,typeAlert=None,Timeout="45",URI=None):
        content = ""
        content += '<Message'
        content += ' Index="%s"'%(index)
        if typeAlert != None:
            content += ' Type="%s"'%(typeAlert)
        if Timeout != "45":
            content += ' Timeout="%s"'%(Timeout)
        if URI != None:
            content += ' URI="%s"'%(URI)
        content += '>%s</Message>'%(text)
        self._message_list.append(content)
    
    def getItem(self):
        for i in self._message_list:
            yield i
        del self._message_list[:]
        
class inputItem():
    _input_list = []
    
    def addItem(self,prompt=None,parameter=None,default=None,selection=None,typeMode="string",is_password="no",editable="yes",softkey=None):
        content = ""
        content += '<InputField'
        if typeMode != "string":
            content += ' type="%s"'%(typeMode)
        else:
            if is_password != "no":
                content += ' password="yes"'
        if editable != "yes":
            content += ' editable="no"'
        content += '>'
        if prompt != None:
            content += '<Prompt>%s</Prompt>'%(prompt)
        if parameter != None:
            content += '<Parameter>%s</Parameter>'%(parameter)
        if default != None:
            content += '<Default>%s</Default>'%(default)
        if selection != None:
            content += '<Selection>%s</Selection>'%(selection)
        if softkey != None:
            if isinstance(softkey,SoftKeyItem):
                for i in softkey.getItem():
                    content += i
            else:
                raise TypeError, "SoftKey Item not a SoftKey() class Instance"
        content += '</InputField> '
        self._input_list.append(content) 
    
    def getItem(self):
        for i in self._input_list:
            yield i
        del self._input_list[:]

class SoftKeyItem():
    _softkey_list = []
    
    def addItem(self,label,URI,index,icon_index=None):
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
        
    def getItem(self):
        for i in self._softkey_list:
            yield i
        del self._softkey_list[:]

class MenuItem():
    
    _items_list = []
    
    def addItem(self,Prompt,URI,base=None,icon=None,Dial=None,Selection=None):
        item = _MenuItem(Prompt,URI,Dial,Selection)
        content = ''
        content += '<MenuItem'
        if base != None:
            content += ' base="%s"' % ( base )
        if icon != None:
            content += ' icon="%s"' % ( icon )
        content += '>%s</MenuItem>'%(item.getContent())
        self._items_list.append(content)
        
    def getItem(self):
        for item in self._items_list:
            yield item
        del self._items_list[:]

class _MenuItem():
    
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

class IconItem():
    
    _icons_list = []
    
    def addItem(self,iconName,index=None):
        self._content = '<Icon'
        if index != None:
            self._content += ' index="%s"'%(index)
        self._content += '>%s</Icon>'%(iconName)
        self._icons_list.append(self._content)
        
    def getItem(self):
        for i in self._icons_list:
            yield i
        del self._icons_list[:]

class URIItem():
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
        
    def getItem(self):
        for item in self._items_list:
            yield item
        del self._items_list[:]
            
class _UrlItem():
    
    def __init__(self,Prompt,key):
        self._content = '<URI key="%s">%s</URI>' % (Prompt,key)
        
    def getContent(self):
        return self._content
    
class LineItem():
    
    _line_list = []
    
    def addItem(self,text,Size="normal",Align="left",Color="white"):
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
        
    def getItem(self):
        for i in self._line_list:
            yield i
        del self._line_list[:]