from django.urls import path
from . import views, api_views

app_name = 'search_api'


urlpatterns = [
    path('v1/youtube/', api_views.YouTubeVideoView.as_view(), name='youtube_api'),
    path('v1/flickr/', api_views.FlickrImgView.as_view(), name='flikr_api')
]
