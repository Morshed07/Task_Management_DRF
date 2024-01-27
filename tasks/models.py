from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_complete = models.BooleanField(default=False)
    img = models.ImageField(upload_to='img',blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])
    
class TaskImages(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="task_images",blank=True,null=True, default='')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Task Images'

