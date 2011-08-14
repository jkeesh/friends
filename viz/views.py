# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
import facebook
from viz.models import UserProfile, Friend, DataPoint
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def create_data_point(user):
    pass

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
    

def friends(request):
    """
    Display the users friends.
    """
    user = request.user
    friends = friends_lookup(user)
    # up = user.get_profile()
    # graph = facebook.GraphAPI(up.access_token)
    # friends = graph.get_connections("me", "friends")['data']
    return render_to_response("friends.html", {
            "friends": friends,
            "user": user
        },
        context_instance=RequestContext(request)
    )


def index(request):
    cookie = facebook.get_user_from_cookie(request.COOKIES, 
                    settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
                    
    message = 'Ok.'
    user = None
    if cookie:
        print 'hi'
        print cookie
        try:
            up = UserProfile.objects.get(id=cookie['uid'])
            user = up.user
        except UserProfile.DoesNotExist:            
            graph = facebook.GraphAPI(cookie["access_token"])
            profile = graph.get_object("me")
            print profile
            
            try:
                user = User.objects.get(username=profile['username'])
            except User.DoesNotExist:                            
                user = User.objects.create_user(profile['username'], 
                            email='test@example.com',
                            password=profile['username'])
                user.first_name = profile['first_name']
                user.last_name = profile['last_name']
                user.save()
            
            up = UserProfile(user=user, id=cookie['uid'], access_token=cookie['access_token'])
            up.save()
        
        user = authenticate(username=user.username, password=user.username)
        if user is not None:
            login(request, user)
        else:
            print "user was none"
    else:
        message = "Error with the user"
    
    
    return render_to_response("index.html", {
            "facebook_app_id": settings.FACEBOOK_APP_ID,
            "message": message,
            "current_user": user
        },
        context_instance=RequestContext(request)
    )