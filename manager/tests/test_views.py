from datetime import datetime

import pytz
from django.test import TestCase
from django.urls import reverse

from manager.models import Task, Tag

TASK_URL = reverse("manager:task-list")
TAG_URL = reverse("manager:tag-list")


class PublicTaskTests(TestCase):
    def test_retrieve_tasks(self):
        europe_kiev = pytz.timezone('Europe/Kiev')
        Task.objects.create(
            content="Test task",
            deadline=datetime(2024, 3, 5, 14, 30, tzinfo=europe_kiev)
        )
        
        response = self.client.get(TASK_URL)
        
        tasks = Task.objects.all()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        
        self.assertTemplateUsed(response, "manager/task_list.html")


class PublicTagTests(TestCase):
    def test_retrieve_tags(self):
        Tag.objects.create(
            name="Test tag",
        )
        
        response = self.client.get(TAG_URL)
        
        tags = Tag.objects.all()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["tag_list"]),
            list(tags)
        )
        
        self.assertTemplateUsed(response, "manager/tag_list.html")


class TaskUpdateCompletionViewTestCase(TestCase):
    def setUp(self):
        europe_kiev = pytz.timezone('Europe/Kiev')
        self.task = Task.objects.create(
            content="Test Task",
            deadline=datetime(2024, 3, 5, 14, 30, tzinfo=europe_kiev),
            is_completed=False
        )
        self.url = reverse("manager:update-completion", kwargs={'pk': self.task.pk})
    
    def test_toggle_task_completion(self):
        # Initial check if task is not completed
        self.assertFalse(self.task.is_completed)
        
        # Testing if task is marked as completed if it wasn't
        response = self.client.post(self.url)
        
        self.assertEqual(response.status_code, 302)
        
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)
        
        # Check for "Undo" button to make task not completed
        response = self.client.post(self.url)
        
        self.assertEqual(response.status_code, 302)
        
        self.task.refresh_from_db()
        self.assertFalse(self.task.is_completed)
