from datetime import datetime

import pytz
from django.test import TestCase

from manager.forms import TaskForm
from manager.models import Tag


class TaskFormTest(TestCase):
    def test_valid_form(self):
        europe_kiev = pytz.timezone('Europe/Kiev')
        tags = Tag.objects.all()
        form_data = {
            'content': 'test content',
            'deadline': datetime(2033, 8, 31, 0, 0, tzinfo=europe_kiev),
            "tags": tags,
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
