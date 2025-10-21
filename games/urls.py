# games/urls.py
from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path("", views.GameListView.as_view(), name="game-list"),
    path("game/<int:pk>/", views.GameDetailView.as_view(), name="game-detail"),
    path("game/add/", views.GameCreateView.as_view(), name="game-add"),
    path("game/<int:pk>/edit/", views.GameUpdateView.as_view(), name="game-edit"),
    path("game/<int:pk>/delete/", views.GameDeleteView.as_view(), name="game-delete"),
]
