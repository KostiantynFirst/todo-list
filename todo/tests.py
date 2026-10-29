from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from todo.models import Task, Tag


class TaskToggleViewTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="Test task")

    def test_post_marks_task_as_done(self):
        url = reverse("todo:task-toggle", kwargs={"pk": self.task.pk})
        response = self.client.post(url)

        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)
        self.assertRedirects(response, reverse("todo:index"))

    def test_post_marks_done_task_as_not_done(self):
        task = Task.objects.create(content="Done task", is_done=True)
        url = reverse("todo:task-toggle", kwargs={"pk": task.pk})
        response = self.client.post(url)
        task.refresh_from_db()
        self.assertFalse(task.is_done)
        self.assertRedirects(response, reverse("todo:index"))

    def test_get_is_not_allowed(self):
        url = reverse("todo:task-toggle", kwargs={"pk": self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)
        self.task.refresh_from_db()
        self.assertFalse(self.task.is_done)


class TaskModelTests(TestCase):

    def test_ordering_not_done_first_then_newest(self):
        now = timezone.now()
        old_done = Task.objects.create(content="old done", is_done=True)
        old_todo = Task.objects.create(content="old todo")
        new_todo = Task.objects.create(content="new todo")
        Task.objects.filter(pk=old_done.pk).update(
            created_at=now - timedelta(days=2)
        )
        Task.objects.filter(pk=old_todo.pk).update(
            created_at=now - timedelta(days=1)
        )

        tasks = list(Task.objects.all())

        self.assertEqual(tasks, [new_todo, old_todo, old_done])


class PagesTests(TestCase):

    def test_index_page_shows_task(self):
        Task.objects.create(content="Buy milk")

        response = self.client.get(reverse("todo:index"))

        self.assertContains(response, "Buy milk")

    def test_tag_list_page_shows_tag(self):
        Tag.objects.create(name="study")

        response = self.client.get(reverse("todo:tag-list"))

        self.assertContains(response, "study")
