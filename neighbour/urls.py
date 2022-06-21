from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns=[
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("profile/update/", views.update_profile, name="update_profile"),
    path("posts/", views.posts, name="posts"),
    path("post/save/", views.create_post, name="save_post"),
    path("contacts/", views.contacts, name="contacts"),
    path("contact/create/", views.create_contact, name="create_contact"),
    path("business/", views.business, name="business"),
    path("business/create/", views.create_business, name="create_business"), 
    path("alerts/", views.alerts, name="alerts"),
    path("search/", views.search, name="search"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)