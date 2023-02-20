from django.urls import path
from .views import SignUpView,SignOutView, profile
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup' ),
    path('profile/', profile,name='profile'),
    path('signout/', SignOutView.as_view(), name='logout'),
]