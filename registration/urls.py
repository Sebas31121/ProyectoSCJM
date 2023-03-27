from django.urls import path
from .views import SignUpView, SignOutView, profile, editProfileView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup' ),
    path('profile/', profile , name='profile'),
    path('signout/', SignOutView.as_view(), name='logout'),
    path('<pk>/update/', editProfileView, name='update_profile'),

]