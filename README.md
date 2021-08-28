# projectCaT
API server (for Youtube and Flickr search)

1 - create virtual environment -> 'python -m venv djangoAPI'

2 - activate virtual environment -> 'djangoAPI/Scripts/activate'

3 - clone repo

4 - cd into projectCaT

5 - run 'pip install -r requirements.txt'

6 - cd into 'youtube_flickr_api_master'

7 - start server -> 'python manage.py runserver'

8 - API endpoints:
    youtube: http://localhost:8000/api/v1/youtube/
    
        params:
            'query': <string> search terms:
                'http://localhost:8000/api/v1/youtube/?query=<string>'

    
    flickr: http://localhost:8000/api/v1/flickr/

        params:
            'query': <string> search terms:
                'http://localhost:8000/api/v1/flickr/?query=<string>'
                

9 - Website: http://localhost:8000/