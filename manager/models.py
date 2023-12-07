from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)
    
    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(null=True, default=False)
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)
    
    def __str__(self) -> str:
        return self.content
    
    class Meta:
        ordering = ["is_completed", "-created"]
