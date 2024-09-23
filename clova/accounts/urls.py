from django.urls import path
from .views import LoginView, SignupView

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view())
]