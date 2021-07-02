from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('manage_store/', views.manage_store, name='manage_store'),
    path('add_store/', views.add_store, name='add_store'),
    path('delete_store/<int:id>/',views.delete_store, name='deletestore'),
    path('<int:id>/', views.edit_store, name='editstore'),
    path('edit_store/update/<int:id>/', views.update, name='updatedata'),
    path('manage_medicine/', views.manage_medicine, name='manage_medicine'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('delete_medicine/<int:id>/', views.delete_medicine, name='deletemedicine'),
    path('edit_medicine/<int:id>/', views.edit_medicine, name='editmedicine'),
    path('edit_medicine/upmedicine/<int:id>/', views.upmedicine, name='updatemedicine'),
    path('logout/', views.logout, name='logout'),
]