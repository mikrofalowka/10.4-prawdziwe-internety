'''kod odpowiedzialny za komunikacje z API'''
import requests
from flask import Flask
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MmE0OWVhMDk0ZmVmOGFmOTQ0NzQzZjhiMjEzMWI5OCIsIm5iZiI6MTcyNTEwOTI2NC44OTQxODksInN1YiI6IjY2ZDJmYzcwNWE4YTllNWUyZGMwZDNkOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.WVX9fLWnV8LffEHEXD0RqlX-KZRMWkO8xrpRj_R98Ig"
app = Flask(__name__)

def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, rozmiar='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f'{base_url}{rozmiar}/{poster_api_path}'

def get_movies_list(list_type='popular'):
    endpoint = f'https://api.themoviedb.org/3/movie/{list_type}'
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(endpoint, headers=headers) 
    response.raise_for_status()
    return response.json()

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data['results'][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"][:how_many]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()