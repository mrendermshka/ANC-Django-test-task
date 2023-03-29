from django.urls import path, include
from .views import *
urlpatterns = [
    path("", index),
    path("generate", generate),
    path("get_worker", worker_AJAX_RESPONSE),
    path("every_worker", workers)
]
