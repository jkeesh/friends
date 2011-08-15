from django import template
register = template.Library()
from viz.models import DataPoint

@register.inclusion_tag('data_diff.html')
def previous_diff(data_point):
    print data_point
    prev = DataPoint.get_previous_by_created_at(data_point)
    print prev 
    return {
        'data_point': data_point,
        'prev': prev
    }
    
    