
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('list/', emp_list),
    path('employee/', emp),
]