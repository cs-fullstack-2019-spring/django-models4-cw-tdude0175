from django.urls import path
from . import views


urlpatterns = \
    [
        path('',views.index,name = 'index'),
        path('children/' , views.childList , name = 'childList'),
        path('moms/' , views.momList,name = 'momList'),
        path('newchild/',views.newChildren, name = 'newChildren'),
        path('deletemom/',views.deleteMom , name = 'deleteMom')
    ]