from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),                     # /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # /polls/1/
    path('<int:question_id>/vote/', views.vote, name='vote'),      # /polls/1/vote/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # /polls/1/results/
]
