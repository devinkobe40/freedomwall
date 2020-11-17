from django.urls import reverse_lazy, path
from . import views
from django.views.generic import TemplateView

from . import views
app_name = 'discussion'

urlpatterns = [
    path('', views.ThreadListView.as_view(), name='all'),
    path('thread/<int:pk>', views.ThreadDetailView.as_view(), name='detail'),
    path('thread/create_thread', views.ThreadCreateView.as_view(success_url = reverse_lazy('discussion:all')), name='create_thread'),

    #Image View
    path('thread_img/<int:pk>', views.stream_file, name='picture'),

    #Comments
    path('thread/<int:pk>/post_comment', views.CommentCreateView.as_view(), name='comment')
]
