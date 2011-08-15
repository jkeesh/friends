from viz.models import DataPoint, Friend
import facebook

def diff_data_points(old, new):
    """
    Diff using a string split on the list of friend ids
    """
    old_friends = set(old.friend_list.split(','))
    new_friends = set(new.friend_list.split(','))
    lost = old_friends - new_friends
    gained = new_friends - old_friends
    
    lost = Friend.objects.filter(id__in=lost)
    gained = Friend.objects.filter(id__in=gained)
    
    return lost, gained
    
    
def make_friend_list(data_point, friends):
    data_point.friend_list = ','.join([str(f.id) for f in friends])
    data_point.save()


def find_or_add_friend(friend_dict):
    try:
        friend = Friend.objects.get(fbid=friend_dict['id'])
    except Friend.DoesNotExist:
        friend = Friend(fbid=friend_dict['id'], name=friend_dict['name'])
        friend.save()
    return friend

def friends_lookup(user):
    up = user.get_profile()
    graph = facebook.GraphAPI(up.access_token)
    friends = graph.get_connections("me", "friends")['data']

    friend_objects = []
    for friend in friends:
        friend_objects.append(find_or_add_friend(friend))

    return friend_objects


def create_data_point(user):
    friends = friends_lookup(user)
    data_point = DataPoint(user=user)
    data_point.save()
    make_friend_list(data_point, friends)