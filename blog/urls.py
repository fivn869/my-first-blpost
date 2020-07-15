from django.urls import path, include
from blog.views import Register, Login, HomePage,LogoutPage,ProfileForm, Post02,PostEdit
urlpatterns = [
    path('register', Register.as_view(), name="register"),
    path('login', Login.as_view(), name="login"),
    path('home',HomePage.as_view(),name='home'),
    path('logout',LogoutPage.as_view(),name='logout'),
    path('profile',ProfileForm.as_view(),name='profile'),
    path('post/new',Post02.as_view(),name='post'),
    path('post/<int:pk>/', PostEdit.as_view(), name = 'post_edit'),
]