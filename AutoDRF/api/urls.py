from django.urls import path, include 
from rest_framework import routers
from app3.api.views import * 


from rest_framework import routers

router = routers.SimpleRouter()

###RegisteringRouter

router.register(r'classname', ClassName_ViewSet)
urlpatterns = [
    path('', include(router.urls)),

]