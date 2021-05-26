from django.urls import include,path
from rest_framework import routers
from cowrywise import views

# router = routers.DefaultRouter()
# router.register(r'timestamp',views.timestamp_list,'timestamp')


urlpatterns = [
    path('timestamp/', views.timestamp_list)
]