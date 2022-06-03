from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('registration/', views.Registration.as_view(), name="registration"),
    path('detail_info/', views.DetailInfo.as_view(), name="detail"),
    path('notebooks/', views.Nothebooks.as_view(), name='note_main'),
    path('detail_comment/', views.DetailCommentsApi.as_view()),
    path('notebook_api/', views.NothebookApi.as_view()),
    path('notebook_api/<int:pk>', views.NothebookApiDeleteOrupdate.as_view()),
    path('videocards/', views.Videocard.as_view(), name="videocards"),
    path('displays/', views.Monitors.as_view(), name="displays"),
    path('memory/', views.Memory.as_view(), name="memory"),
    path('accounts/', include('allauth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
