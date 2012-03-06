from django.http import HttpResponse

class AastraXmlResponse(HttpResponse):
    def __init__(self, content='',encoding='UTF-8',charset="ISO-8859-1"):
        #convert the object into a text script
        encoding_header = '<?xml version"1.0" encoding="%s"?>' % (encoding)
        content = encoding_header + content
        super(AastraXmlResponse,self).__init__(content)
        self['Content-Length'] = len(content)
        self['Content-Type'] = "%s; charset=%s" % ("text/xml",charset)