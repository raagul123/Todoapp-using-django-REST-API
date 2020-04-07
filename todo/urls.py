from django.urls import path,include
from rest_framework.routers import DefaultRouter
from todo import views
from django.views.generic import TemplateView

router=DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('todo',views.UserTodoViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('login/',views.UserLoginApiView.as_view()),
]
