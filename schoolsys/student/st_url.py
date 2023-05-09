from django.urls import path
from.views import*
urlpatterns = [
    path('reg',addstudent.as_view(),name='addstd')

]
