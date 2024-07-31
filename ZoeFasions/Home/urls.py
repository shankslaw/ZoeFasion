from django.urls import path
from . import views

urlpatterns = [ path('',views.home,name="Home"),
                path('view-items/',views.list,name="List"),
                path('add-products/',views.creation,name="Create"),
                path('deletion/<int:pk>',views.delete,name="Delete"),
                path('editing/<int:pk>',views.edit,name="Edit")
               ]