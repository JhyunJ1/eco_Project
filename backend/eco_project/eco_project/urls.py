from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mission/', include("Mission.urls")),
    path('user/', include("User.urls")),
    path('mileage/', include("mileage.urls")),
]