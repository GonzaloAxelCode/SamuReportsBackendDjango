
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


from django.conf.urls.static import static
from django.contrib.sites.models import Site


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("apps.user.urls")),
    path("api/", include("apps.uploadcsv.urls")),
    path("api/reports/", include("apps.reports.urls"))
]


# urlpatterns += [re_path(r'^.*',
#                        TemplateView.as_view(template_name='index.html'))]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
