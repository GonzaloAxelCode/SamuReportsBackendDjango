
from django.urls import path

from apps.user.views import DeleteUserView, UpdatePhotoUrlView, UserAccountListView, UserDetailView,UpdateNicknameView, UpdateFirstNameView, UpdateLastNameView,  UpdateLocationView,UpdateBirthdateView,UpdatePhoneNumberView

urlpatterns = [     
    path("detailuser",UserDetailView.as_view(),name="detail_user"),
    path('deleteall', DeleteUserView.as_view(), name='delete_user'),
    path('list-users', UserAccountListView.as_view(), name='list_users'),
    path('update_photo', UpdatePhotoUrlView.as_view(), name='update_photo'),
    path('update-nickname', UpdateNicknameView.as_view(), name='update_nickname'),
    path('update-first-name', UpdateFirstNameView.as_view(), name='update_first_name'),
    path('update-last-name', UpdateLastNameView.as_view(), name='update_last_name'),
    
    path('update-location', UpdateLocationView.as_view(), name='update_location'),
    path('update-birthdate', UpdateBirthdateView.as_view(), name='update_birthdate'),
    path('update-phone-number', UpdatePhoneNumberView.as_view(), name='update_phone_number'),

]
