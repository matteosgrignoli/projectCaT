from rest_framework.response import Response
from rest_framework.views import APIView
import random
import requests
from django.conf import settings


class YouTubeVideoView(APIView):
    def get(self, request):
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        search = request.query_params.get('query')
        search_params = {
            'part': 'snippet',
            'q': search,
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 9,
            'type': 'video',
            'videoDuration': 'short',
        }

        videos = requests.get(search_url, params=search_params)
        results = videos.json()['items']

        return Response({"results": results})


class FlickrImgView(APIView):
    def get(self, request):
        random_imgs = []

        # connection to Flickr API setup
        search_url = 'https://www.flickr.com/services/rest/'
        search = request.query_params.get('query')
        search_params = {
            'method': 'flickr.photos.search',
            'api_key': settings.FLICKR_DATA_API_KEY,
            'tags': search,
            'format': 'json',
            'nojsoncallback': 1,
            'media': 'photos',
            'per_page': 500,
            'page': 1,
        }

        # request
        pics = requests.get(search_url, params=search_params)

        # 3 indexes based on the total  umber of images returned
        results = pics.json()['photos']
        if results['total'] >= 500:
            max_range = 500
        else:
            max_range = results['total']
        random_indexes = random.sample(range(0, max_range-1), 3)

        # list of 3 images based on the random selection above
        for i in random_indexes:
            random_imgs.append(pics.json()['photos']['photo'][i])

        return Response({'results': random_imgs})
