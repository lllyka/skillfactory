from django import template

register = template.Library()

@register.filter(name='Censor')

def Censor(censor_text,cens_world):
    if cens_world in censor_text:
        print('***')
    else:
        return censor_text