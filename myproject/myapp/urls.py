from django.urls import path
from . import views
from .views import SendWhatsAppMessagesView,mark_absent_view
urlpatterns = [
    path('', views.home_view, name='home'),
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('teacher/', views.teacher_view, name='teacher'),
    path('students/', views.student_list_view, name='student_list'),
    path('student/', views.student_view, name='student'),
    path('student/<int:pk>/', views.student_display_view, name='student_display'),
    path('student/<int:pk>/edit/', views.student_edit_view, name='student_edit'),
    path('student/<int:pk>/delete/', views.student_delete_view, name='student_delete'),
    path('search/', views.search_view, name='search'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('send_messages/', SendWhatsAppMessagesView.as_view(), name='send_messages'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('mark_absent/', mark_absent_view, name='mark_absent'),        # Add this line
    # path('send_messages_view/', send_messages_view, name='send_messages_view'),  # Add this line
]
