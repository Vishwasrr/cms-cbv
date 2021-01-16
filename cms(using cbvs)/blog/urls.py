from django.urls import path
from blog.views import Home, Detail, Update, Delete, Create, Index
# , Create, )

app_name = 'blog'
urlpatterns = [
    path('create/', Create.as_view(), name='create'),
    path('blog/', Index.as_view(), name='all'),
    path('', Home.as_view(), name='home'),
    path('<int:pk>', Detail.as_view(), name='detail'),
    path('<int:pk>/edit/', Update.as_view(), name='edit'),
    path('<int:pk>/delete/', Delete.as_view(), name='delete')
]
