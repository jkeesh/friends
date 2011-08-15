# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
import facebook
from viz.models import UserProfile, Friend, DataPoint
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect


def data(request):
    """
    Handle the diff data view
    """
    dp = DataPoint.objects.all().order_by('-created_at')
    print dp
    
    return render_to_response("data.html", {
            "user": request.user,
            "dp": dp
        },
        context_instance=RequestContext(request)
    )

def friends(request):
    """
    Display the users friends.
    """
    latest = DataPoint.objects.all().order_by('-created_at')[0]
    return redirect('/data_point/%d' % latest.id)
    
def data_point_display(request, id):
    ## Display friends for a single data point
    user = request.user
    dp = DataPoint.objects.get(pk=id)
    friends = dp.friends.all()
    return render_to_response("friends.html", {
            "friends": friends,
            "user": user,
            "dp": dp
        },
        context_instance=RequestContext(request)
    )


def index(request):
    cookie = facebook.get_user_from_cookie(request.COOKIES, 
                    settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
                    
    message = 'Ok.'
    user = None
    data_points = None
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
        
        data_points = DataPoint.objects.all().order_by('-created_at')
    else:
        message = "Error with the user"
    
    
    return render_to_response("index.html", {
            "facebook_app_id": settings.FACEBOOK_APP_ID,
            "message": message,
            "current_user": user,
            'data_points': data_points
        },
        context_instance=RequestContext(request)
    )