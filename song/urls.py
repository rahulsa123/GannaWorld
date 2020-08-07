from django.urls import path
from . import views

app_name = "song"
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("<int:pk>/<int:year>/<int:month>/<int:day>/<slug>/",
         views.SongDetailView.as_view(), name="song_detail"),
    path("playlist/<int:pk>/<int:year>/<int:month>/<int:day>/<slug>/",
         views.PlayListDetailView.as_view(), name="playlist_detail"),
    path("create/", views.song_create, name="song_create"),
    path("like/", views.user_likes, name="song_like"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("playlist/create/", views.playlist_create_view,
         name="playlist_create"),
    path("playlist/", views.MyPlayList.as_view(), name="playlist")
]
