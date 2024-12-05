from django.db import models
from user.models import User


status_choice = (("Completed", "Completed"),
                 ("Pending", "Pending"),
                 ("Cancelled", "Cancelled"))


class Status(models.Model):
    status_name = models.CharField(choices=status_choice, max_length=100)

    class Meta:
        db_table = 'status'

    def __str__(self):
        return self.status_name

# Create your models here.

status_choice = (("Completed", "Completed"),
                 ("Pending", "Pending"),
                 ("Cancelled", "Cancelled"))
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    estimated_time = models.IntegerField()
    start_date = models.DateField()
    completion_date = models.DateField()
    status = models.CharField(choices=status_choice, max_length=100,  null=True, blank=False)
    
    
    class Meta:
        db_table = 'project'
    
    def __str__(self):
        return self.title                    
        
   

class ProjectTeam(models.Model):

    Project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey( User, on_delete=models.CASCADE, null=True, blank=False)
    
    
    
    class Meta:
        db_table = 'project_team'


status_choice = (("Completed", "Completed"),
                 ("Pending", "Pending"),
                 ("Cancelled", "Cancelled"))
class ProjectModule(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    moduleName = models.CharField(max_length=100)
    description = models.TextField()
    estimeted_hours = models.IntegerField()
    status = models.CharField(choices=status_choice,max_length=100)
    startDate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'project_module'

    def __str__(self):
        return self.moduleName
