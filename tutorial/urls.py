from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'implementations', views.ImplementationViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'curriculums', views.CurriculumViewSet)
router.register(r'degreePrograms', views.DegreeprogramViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'units', views.UnitViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'userImplementations', views.UserImplementationViewSet)
router.register(r'usersDegreeprograms', views.UsersDegreeprogramViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
