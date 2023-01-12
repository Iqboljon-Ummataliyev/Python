from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls'))
    # path('',home,name='home'),
    # path('room/',room,name='room')
]