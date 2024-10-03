import tmdb_client
from unittest.mock import Mock
#get_single_movie, get_movie_images, get_single_movie_cast.

def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):

   mock_movie_id = 123
   mock_movie_response = {'title': 'Mock', 'id': mock_movie_id}

   requests_mock = Mock()
   requests_mock.return_value.json.return_value = mock_movie_response
   monkeypatch.setattr('tmdb_client.requests.get', requests_mock)

   movie = tmdb_client.get_single_movie(mock_movie_id)
   assert movie == mock_movie_response

def test_get_single_movie_cast(monkeypatch):
   mock_movie_id = 123
   mock_how_many = 10
   mock_single_movie_cast = {'cast': [{'name1': 'Name_1'},{'name2':'Name_2'}]}

   requests_mock = Mock()

   response = requests_mock.return_value

   response.json.return_value = mock_single_movie_cast

   monkeypatch.setattr('tmdb_client.requests.get', requests_mock)
   cast = tmdb_client.get_single_movie_cast(mock_movie_id,mock_how_many)

   assert cast == mock_single_movie_cast['cast']

def test_get_movie_images(monkeypatch):
   mock_movie_id = 123
   mock_movie_images = {'backdrops'}

   requests_mock = Mock()
   
   response = requests_mock.return_value
   response.json.return_value = mock_movie_images
   
   monkeypatch.setattr('tmdb_client.requests.get', requests_mock)
   image = tmdb_client.get_movie_images(mock_movie_id)

   assert image == mock_movie_images

