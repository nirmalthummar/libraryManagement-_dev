
from django.urls import path
from app_admin.views import app_admin_view
from app_book.views import app_book_view

urlpatterns = [
   path("appadmin", app_admin_view),
   
]