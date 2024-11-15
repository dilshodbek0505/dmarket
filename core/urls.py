from typing import Any
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.conf.urls.i18n import i18n_patterns

from captcha import fields

from .schema import swagger_urlpatterns

class LoginForm(AuthenticationForm):
    captcha = fields.ReCaptchaField()

    def clean(self):
        captcha = self.cleaned_data.get("captcha")
        if not captcha:
            return
        return super().clean()


admin.site.login_form = LoginForm
admin.site.login_template = "login.html"

urlpatterns = [
    path("", lambda _request: redirect('swagger/')),
    path("admin/rosetta/", include("rosetta.urls")),
    path("admin/", admin.site.urls),
    path("api/v1/notifications/", include("apps.notification.urls", namespace="notifications")),
] 

urlpatterns += i18n_patterns(
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
    prefix_default_language=False
)

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
