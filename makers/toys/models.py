from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=50)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Division(models.Model):
    name = models.CharField(max_length=50)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Toy(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    status_id = models.ForeignKey(Status, on_delete=models.PROTECT)
    division1_id = models.ForeignKey(Division, on_delete=models.PROTECT)
    unique = models.TextField()
    target = models.TextField()
    discover = models.TextField()
    documents = models.NullBooleanField()
    just_an_idea = models.NullBooleanField()
    product_specs = models.NullBooleanField()
    product_sample = models.NullBooleanField()
    product_no_branding = models.NullBooleanField()
    product_need_marketing = models.NullBooleanField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Toy Submission #{}'.format(self.id)
