from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'main'

urlpatterns = [
    # Patterns to show the quiz
    path('',            views.HomeView.as_view(),   name='main'),
    path('start/',       views.StartView.as_view(),  name='start_quiz'),
    path('<int:pk>/', views.QuizView.as_view(),   name='show_quiz'),
    # Question level add/edit/update patterns.
    path('create/', views.QCreateView.as_view(), name='create_question'),
    path('list/', views.QListView.as_view(), name='list_question'),
    path('show/<int:pk>/',   views.QDetailView.as_view(), name='show_question'),
    path('change/<int:pk>/', views.QUpdateView.as_view(), name='update_question'),
]
