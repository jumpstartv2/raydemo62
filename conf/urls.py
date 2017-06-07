"""URL Configuration

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

Django Macros Url:
    Pre-defined Macros Url regex variables:
        slug - [\w-]+
        year - \d{4}
        month - (0?([1-9])|10|11|12)
        day - ((0|1|2)?([1-9])|[1-3]0|31)
        id - \d+
        pk - \d+
        page - \d+
        uuid - [a-fA-F0-9]{8}-?[a-fA-F0-9]{4}-?[1345][a-fA-F0-9]{3}-?[a-fA-F0-9]{4}-?[a-fA-F0-9]{12}

    Defining your own regex variables with macrosurl:
        macrosurl.register('myhash', '[a-f0-9]{9}')
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]