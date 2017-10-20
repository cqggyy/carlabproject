from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^login/', views.Login_view.as_view(), name='login'),
    url(r'^logout/', views.Logout_view.as_view(), name='logout'),
]
