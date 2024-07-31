from django.urls import path
from . import views

urlpatterns =[ path('login/',views.Userlogin,name="login"),
               path('logout/',views.Userlogout,name="logout"),
               path('signup/',views.Signup,name="SignUp") ]