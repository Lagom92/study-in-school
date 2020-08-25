"""infoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from infoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('aiclass/', views.aiclass, name='aiclass'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('add/<int:id>/', views.add, name='add'),
    path('student/<int:student_id>/', views.student, name='student'),
    path('edit/<int:student_id>/', views.edit, name='edit'),
    path('delete/<int:class_id>/<int:student_id>/', views.delete, name='delete'),

    # accounts
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
