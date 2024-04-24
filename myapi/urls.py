from django.urls import path
from .views import *

urlpatterns = [
   path('signup/',Sgnupuser.as_view()),
   path('login/',Userlogin.as_view()),
   path('leave/',Leavemanagent.as_view()),


]