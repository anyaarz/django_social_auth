from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
import json
import urllib.request 
import requests
# Create your views here.
def login(request):
    return render(request, 'login.html')
@login_required
def home(request):
    social_user = request.user.social_auth.filter(
                                                    provider='vk-oauth2',
                                                ).first()    
    goodies = []
    if social_user:
        print(social_user)
        url = u'https://api.vk.com/method/friends.get?user_id={0}' \
              u'&order=random&count=6&offset=5&fields=photo_200' \
              u'&access_token={1}&v=5.101'.format(
                  social_user.uid,
                  social_user.extra_data['access_token'],
              )
    response = requests.get(url)
    friends = json.loads(response.text)
    #friends = json.loads(urlopen(response).read()).get('data')
    print(friends['response']['items'])
    for friend in friends['response']['items']:
        goodies.append(friend)
    print(goodies)
    #response = requests.get(query)
    #print(response.json()["response"])
    #return render_to_response('friendslist.html', {'goodies': goodies})
    return render( request, 'home.html', context={'goodies':goodies})


    

