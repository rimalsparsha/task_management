from django.urls import path

from authentication.views import CustomTokenObtainPairView, UserCreateView

urlpatterns = [
    # register
    path('register/', UserCreateView.as_view(), name='user-register'),

    # login and obtain token
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]
