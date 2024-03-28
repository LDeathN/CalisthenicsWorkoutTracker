from django.urls import path
from CalisthenicsWorkoutTracker.users.views import ProfileEditView, ProfileDetailsView, ProfileDeleteView, SignInUserView, SignUpUserView, logout_user

urlpatterns = [
    path('signin/', SignInUserView.as_view(), name='signin'),
    path('signup/', SignUpUserView.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='details_user'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit_user'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='delete_user'),
]
