from django.db import models

# CourseManager(models.Manager):
#     pass

class CourseManager(models.Manager):
    def validator(self,data):
        errors = {}
        if len(data["name"]) < 5:
            errors["name"] = "name should be min 5 characters"
        if len(data["desc"]) < 15:
            errors["description"] = "description should be min 15 characters"
        return errors


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
