# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
import facebook

def login(request):
    print request
    
    cookie = facebook.get_user_from_cookie(request.COOKIES, 
                    settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
                    
    message = 'Ok.'
    if cookie:
        pass
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
            "message": message
        },
        context_instance=RequestContext(request)
    )