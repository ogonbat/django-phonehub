'''
Created on 07/03/2012

@author: cingusoft
'''
from django.utils.functional import wraps
from django.http import HttpResponseRedirect

def is_aastra(view):
    @wraps(view)
    def inner(request,*args,**kwargs):
        user_agent = request.META['HTTP_USER_AGENT']
        partial_agent = user_agent.split(' ')
        if "Aastra" in partial_agent[0]:
            pass
        else:
            return HttpResponseRedirect('settings.LOGIN_URL')
        return view(request,*args,**kwargs)
    return inner
