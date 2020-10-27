from django.urls import path

from pets import views

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("cat/random", views.CatView.as_view(), name="cats"),
    path("dog/random", views.DogView.as_view(), name="dogs"),
]
