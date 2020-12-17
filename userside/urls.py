from django.urls import path
from userside import views
app_name = 'userside'


urlpatterns = [
	path('',views.index,name='home'),
	path('dashboard/',views.dashboard,name='dashboard')
]