from django.urls import path
from basics import views
urlpatterns = [
    path('sum/',views.sum),
]