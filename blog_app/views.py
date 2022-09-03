from blog_app.models import Post
from django.views import generic


class PostList(generic.ListView):
    queryset = Post.objects.filter().order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'




    # {% block sidebar %} {% include 'sidebar.html' %} {% endblock sidebar %}
# Create your views here.
