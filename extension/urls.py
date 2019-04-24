from django.urls import path

from . import views
app_name='extension'
urlpatterns = [
    
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>', views.DetailView.as_view(), name='detail'),
	path('<int:question_id>/submit', views.answer, name='answer')	
	
]