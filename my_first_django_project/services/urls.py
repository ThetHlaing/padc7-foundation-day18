from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="Service Index"),
    path('detail/<str:name>/<int:id>',views.detail,name="Service Detail")
]