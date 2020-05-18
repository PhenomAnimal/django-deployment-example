from django import template

# Method 1

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of arg from the string
    """

    return value.replace(arg,'')


# Method 2
# register = template.Library()
#
# def cut(value,arg):
#     """
#     This cuts out all values of arg from the string
#     """
#
#     return value.replace(arg,'')
#
# 'cut' is what we want to call the filter, while cut is the function itself that runs when we call the filter
# register.filter('cut', cut)
