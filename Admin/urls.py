from django.urls import path
from Admin import views
urlpatterns = [
    path('district/',views.District),
]