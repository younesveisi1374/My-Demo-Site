from django.urls import path
from website.views import index_view, profile_view, contact_view

urlpatterns = [
    path("", index_view, name='index_view'),
    path("profile", profile_view, name='profile'),
    path("contact", contact_view, name='contact'),
]