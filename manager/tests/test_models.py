from datetime import datetime

from django.test import TestCase

from manager.models import Task, Tag


class ModelsTests(TestCase):
    def test_task_str(self):
        task = Task.objects.create(
            content="test content",
            deadline=datetime(2024, 3, 5, 14, 30)
        )
        self.assertEqual(
            str(task),
            f"{task.content}"
        )
    
    def test_tag_str(self):
        tag = Tag.objects.create(name="test")
        self.assertEqual(str(tag), f"{tag.name}")
