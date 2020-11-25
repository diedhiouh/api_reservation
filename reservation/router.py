from .viewset import userviewsets 
from rest_framework.routers import DefaultRouter 
  
router = DefaultRouter()
router.register('user', userviewsets, basename ='user_api')