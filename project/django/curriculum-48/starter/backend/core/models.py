from django.db import models


class Task(models.Model):
    """Starter model for Block B. Extend in later sessions (owner, category, notes)."""

    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
