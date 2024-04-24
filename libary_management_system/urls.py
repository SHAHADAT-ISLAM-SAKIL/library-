from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('user_account_authentication/',include('user_account.urls')),
    path('post/',include('post.urls')),
    path('transaction/',include('transcation.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)