from django.urls import path
from . import views

app_name = 'livepolls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),#/livepolls/5/
    path('<int:question_id>/vote/', views.vote, name='vote'),#/livepolls/5/vote/
    path('<int:question_id>/results/', views.results, name='results'),#/livepolls/5/result/    
]