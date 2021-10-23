from django.urls import path
from .views import index, ComposerListView, ComposerDetailView

urlpatterns = [
    path('', index),
    path('api/', ComposerListView.as_view()),
    path('api/<int:id>', ComposerDetailView.as_view()),
 ]
