from . import views
from django.urls import path, include
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'buss', views.BusView, 'bus')
router.register(r'userr', views.UserView, 'user')
router.register(r'bookk', views.BookView, 'book')

urlpatterns = [
    path('', views.home, name="home"),
    path('findbus', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),
    path('api/', include(router.urls)),

]
