from django.urls import path
from .views import index, ComposerListView, ComposerDetailView

urlpatterns = [
    path('', ComposerListView.as_view()),
    path('<int:id>', ComposerDetailView.as_view()),
    path('view/', index),
 ]
