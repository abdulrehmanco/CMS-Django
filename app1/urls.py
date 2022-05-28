from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('',views.signin, name='sigin'),
    path('dash',views.dashboard, name='dashboard'),
    path('signin',views.signin, name='signin'),
    path('med',views.medicine, name='med'),
    path('suppl',views.suppliers, name='suppl'),
    path('empl',views.employee, name='empl'),
    path('recipt',views.recipt, name='recipt'),
    path('mad_delete/<event_id>',views.mad_delete, name='mad_delete'),
    path('com_delete/<event_id>',views.com_delete, name='com_delete'),
    path('signup',views.signup, name='signup'),
    path('logout',views.handlelogout, name='logout'),
]
