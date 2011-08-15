from django import template
register = template.Library()
from viz.models import DataPoint

from viz.data import diff_data_points

@register.inclusion_tag('data_diff.html')
def previous_diff(data_point):
    prev = DataPoint.get_previous_by_created_at(data_point, user=data_point.user)
    lost, gained = diff_data_points(prev, data_point)
    
    
    return {
        'data_point': data_point,
        'prev': prev,
        'lost': lost,
        'gained': gained
    }
    
    