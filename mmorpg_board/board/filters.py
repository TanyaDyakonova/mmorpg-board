import django_filters
from .models import Reply

class ReplyFilter(django_filters.FilterSet):
    class Meta:
        model = Reply
        fields = ['post']