from django.urls import path
from .views import LostlistView, LostDetailView

app_name = 'lostitem'

urlpatterns = [
    path('', LostlistView.as_view()),
    path('<int:lostid>/', LostDetailView.as_view())
]