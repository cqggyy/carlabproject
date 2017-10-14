from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^login/', views.user_login, name='login'),
]
