from django.db import models
from django.utils import timezone


class PostQuerySet(models.QuerySet):

    def available(self):
        """Посты, доступные для показа читателю."""
        return self.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        )

    def with_relations(self):
        return self.select_related('author', 'category')
