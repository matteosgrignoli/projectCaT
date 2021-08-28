# projectCaT
API server (for Youtube and Flickr search)

1 - create virtual environment

2 - clone repo

3 - run 'pip install requirements.txt'

4 - cd into 'youtube_flickr_api_master'

5 - start server -> 'python manage.py runserver'

6 - API endpoints:
    youtube: http://localhost:8000/api/v1/youtube/
    params:
        'search': <string> search terms

    flickr: http://localhost:8000/api/v1/flickr/
    params:
        'search': <string> search terms

7 - Website: http://localhost:8000/