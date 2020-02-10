from django.shortcuts import render, get_object_or_404
import datetime
from .models import Post, Group

start_date = datetime.date(1890, 1, 1)
end_date = datetime.date(1895, 3, 31)

def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts}) 
    