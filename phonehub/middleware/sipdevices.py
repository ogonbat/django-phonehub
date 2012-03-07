'''
Created on 07/03/2012

@author: ogonbat
'''
import re
class SipDevicesMiddleware(object):
    regu_aastra = re.compile(r"Aastra6730i|Aastra6731i|Aastra6735i|Aastra6737i|Aastra6751i|Aastra51i|Aastra6753i|Aastra53i|Aastra6755i|Aastra55i|Aastra6757i|Aastra57i|Aastra6739i|Aastra6757iCT|Aastra57iCT|Aastra6757ict|Aastra57ict")
    def process_request(self,request):
        request.device = {}
        if request.META.has_key('HTTP_USER_AGENT'):
            user_agent = request.META['HTTP_USER_AGENT']
            b = self.regu_aastra.search(user_agent)
            if b:
                basic_info = user_agent.split(' ')
                request.device['model'] = basic_info[0]
                #get mac addr and firmware version
                basic_mac_info = basic_info[1].split(':')
                request.device['mac'] = basic_mac_info[1]
                
                basic_firmware_info = basic_info[2].split(':')
                request.device['firmware'] = basic_firmware_info[1]
                if request.META.has_key('HTTP_X_AASTRA_EXPMOD1'):
                    request.device['mod1'] = request.META['HTTP_X_AASTRA_EXPMOD1']
                if request.META.has_key('HTTP_X_AASTRA_EXPMOD2'):
                    request.device['mod2'] = request.META['HTTP_X_AASTRA_EXPMOD2']
                if request.META.has_key('HTTP_X_AASTRA_EXPMOD3'):
                    request.device['mod3'] = request.META['HTTP_X_AASTRA_EXPMOD3']
        return