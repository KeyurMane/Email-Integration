from django.urls import path
from .views import sendmailview

urlpatterns = [
    path('v1/',sendmailview)
]