from django.urls import path
from basics import views
urlpatterns = [
    path('sum/',views.sum),
    path('calculator/',views.Calculate),
    path('LS/',views.large),
]