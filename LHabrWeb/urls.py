from django.contrib import admin
from django.urls import path, include
from LHabrApp.views import good_morning, index_blog, index, create_post, \
    LLoginView, LLogoutView, profile, PostAPIView
from django.conf import settings
from django.conf.urls.static import static
from LHabrApp.views import RegUserView, RegisterDoneView


urlpatterns = [

    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('good_morning/', good_morning, name='g_morming'),
    path('blog/', index_blog, name='blog_pg'),
    path('create/', create_post, name='create_post'),
    path('accounts/login/', LLoginView.as_view(), name='login'),
    path('accounts/logout', LLogoutView.as_view(), name='logout'),
    path('accounts/profile', profile, name='profile'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegUserView.as_view(), name='register'),
    path('api/v1/postlist', PostAPIView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # urlpatterns = [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


