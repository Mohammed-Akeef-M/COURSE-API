
from django.contrib import admin
from django.urls import path
from subject.views import courseview, Coursedetailview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/course', courseview),
    path('api/course/<int:pk>', Coursedetailview),
]
