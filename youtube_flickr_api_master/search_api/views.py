from django.shortcuts import render
from django.conf import settings
from random import randint
import requests

# Create your views here.


def index(request):
    video_link = ''
    img_link = ''

    if request.method == 'POST':

        try:
            # search for Youtube video
            if request.POST['submit'] == 'youtube':
                search_url = 'http://127.0.0.1:8000/api/v1/youtube/'
                search_str = request.POST.get('search')
                params = {
                    'query': search_str,
                }

                youtube_req = requests.get(search_url, params=params)
                video_id = youtube_req.json()['results'][0]['id']['videoId']
                video_link = str('https://www.youtube.com/embed/' + video_id)

            if request.POST['submit'] == 'flickr':
                # search for Flickr image
                search_url = 'http://127.0.0.1:8000/api/v1/flickr/'
                search_str = request.POST.get('search')
                params = {
                    'query': search_str,
                }

                flickr_req = requests.get(search_url, params=params)
                img = flickr_req.json()['results'][0]
                img_link = 'https://farm' + str(img['farm']) + '.staticflickr.com/' + str(
                    img['server']) + '/' + str(img['id']) + '_' + str(img['secret']) + '.jpg'

        except:
            return render(request, 'search_api/errors.html')

    context = {
        'video_link': video_link,
        'img_link': img_link,
    }

    return render(request, 'search_api/index.html', context)
