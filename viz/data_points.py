from viz.models import DataPoint

def diff_data_points(old, new):
    """
    Diff using a string split on the list of friend ids
    """
    old_friends = set(old.friend_list.split(','))
    new_friends = set(new.friend_list.split(','))
    
    lost = old_friends - new_friends
    gained = new_friends - old_friends
    
    return lost, gained


def create_data_point(user):
    friends = friends_lookup(user)
    data_point = DataPoint()
    data_point.save()
    ## Expand a list into arguments with *list
    ## http://stackoverflow.com/questions/4959499/how-to-add-multiple-objects-to-manytomany-relationship-at-once-in-django
    data_point.friends.add(*friends)