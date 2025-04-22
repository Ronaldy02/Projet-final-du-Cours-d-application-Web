from django.contrib import admin
from django.urls import path,include
from .views import livre_create,signup,liste_livres,Livre_delete,Livre_detail,Livre_update
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('livre/creer/',livre_create,name='creer_livre'),
    path('',liste_livres,name='liste_livres'),
    path('livre/<int:pk>/detail/',Livre_detail,name='livre_detail'),
    path('livre/<int:pk>/modifier/',Livre_update,name='modifier_livre'),
    path('livre/<int:pk>/supprimer/',Livre_delete,name='supprimer_livre'),
    path('accounts/signup/',signup,name='signup')
]