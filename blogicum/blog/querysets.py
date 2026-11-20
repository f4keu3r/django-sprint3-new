from django.db import models
from django.utils import timezone


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            is_published=True,
            pub_date__lte=timezone.now()
        )

    def with_published_category(self):
        return self.filter(
            category__is_published=True
        )

    def available(self):
        return self.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        )

    def with_relations(self):
        return self.select_related('author', 'category')
