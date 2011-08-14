# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
import facebook
from viz.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def index(request):
    cookie = facebook.get_user_from_cookie(request.COOKIES, 
                    settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
                    
    message = 'Ok.'
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
            
            up = UserProfile(user=user, id=cookie['uid'])
            up.save()
        
        user = authenticate(username=user.username, password=user.username)
        print 'authenticating..'
        if user is not None:
            print "After auth"
            print user
            login(request, user)
        else:
            print "user was none"
        print up
        print user
            
            #print "No profile for this user"
            #user = User(first_name=fb_user['first_name'], last_name=fb_user['last_name'], email=fb_user['email'])
            #social_user.username = str(uuid.uuid4())[:30]
            #social_user.save()
            
            ## Make a User and UserProfile

            
            # # Store a local instance of the user data so we don't need
            # # a round-trip to Facebook on every request
            # user = User.get_by_key_name(cookie["uid"])
            # if not user:
            #     graph = facebook.GraphAPI(cookie["access_token"])
            #     profile = graph.get_object("me")
            #     user = User(key_name=str(profile["id"]),
            #                 id=str(profile["id"]),
            #                 name=profile["name"],
            #                 profile_url=profile["link"],
            #                 access_token=cookie["access_token"])
            #     user.put()
            # elif user.access_token != cookie["access_token"]:
            #     user.access_token = cookie["access_token"]
            #     user.put()
            # self._current_user = user
    else:
        message = "Error with the user"
    
    
    return render_to_response("index.html", {
            "facebook_app_id": settings.FACEBOOK_APP_ID,
            "message": message,
            "current_user": user
        },
        context_instance=RequestContext(request)
    )