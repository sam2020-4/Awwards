"""reviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url,include
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'', include('awwards.urls')),
# ]
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
# from django.contrib.auth import views as auth_views
from registration.backends.simple.views import RegistrationView
from awwards.forms import RegisterForm
from awwards import views
from awwards.views import MerchList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('awwards.urls')),
    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=RegisterForm
        ),
        name='registration_register',
    ),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^logout/$', views.logout, {"next_page": 'logout'}), 
    # url('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^tinymce/', include('tinymce.urls')),
    url('awwards-api/',views.MerchList.as_view(), name='awwards_api'),    
]
