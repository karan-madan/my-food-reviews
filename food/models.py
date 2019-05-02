from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('butterchicken', kwargs={'pk': self.pk})


class Post1(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('chickencurry', kwargs={'pk': self.pk})


class Post2(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('keema', kwargs={'pk': self.pk})


class Post3(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('shahipaneer', kwargs={'pk': self.pk})


class Post4(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('kadhaipaneer', kwargs={'pk': self.pk})


class Post5(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('post-masaladosa', kwargs={'pk': self.pk})


class Post6(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('pasta', kwargs={'pk': self.pk})


class Post7(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('burger', kwargs={'pk': self.pk})


class Post8(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('pizza', kwargs={'pk': self.pk})


class Post9(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('rolls', kwargs={'pk': self.pk})


class Post10(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('naanza', kwargs={'pk': self.pk})


class Post11(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('coffee', kwargs={'pk': self.pk})


class Post12(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('lassi', kwargs={'pk': self.pk})


class Post13(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('shawarma', kwargs={'pk': self.pk})


class Post14(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('biryani', kwargs={'pk': self.pk})


class Post15(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('roastedchicken', kwargs={'pk': self.pk})


class Post16(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('tandoorichicken', kwargs={'pk': self.pk})


class Post17(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('afghanichicken', kwargs={'pk': self.pk})


class Post18(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('mushroomtikka', kwargs={'pk': self.pk})


class Post19(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
         return self.content

    def get_absolute_url(self):
        return reverse('paneertikka', kwargs={'pk': self.pk})


