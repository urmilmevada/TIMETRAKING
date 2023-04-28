#Project Models
from django.db import models
from user.models import User



# Status Class Don't consider this class as it is not used anywhere
status_choice = (("Completed","Completed"),
                 ("Pending","Pending"),
                 ("Cancelled","Cancelled"))
class Status(models.Model):
    status_name = models.CharField(choices=status_choice,max_length=100)

    class Meta:
        db_table='status'
   
    def __str__(self):
        return self.status_name


# Project Class
status_choice = (("Completed","Completed"),
                 ("Pending","Pending"),
                 ("Cancelled","Cancelled"))
class Timetracker(models.Model):
    project_title = models.CharField(max_length=100,null=True)
    project_decription = models.TextField(null=True)
    project_technology = models.CharField(max_length=100,null=True)
    project_estimated_hours = models.IntegerField(null=True)
    project_start_date = models.DateField(null=True)
    project_completion_date = models.DateField(null=True)
    project_file = models.FileField(upload_to='project_files/',null=True,blank=True)
    status = models.CharField(choices=status_choice,max_length=100,null=True)

    class Meta:
        db_table='timetracker'
   
    def __str__ (self):
        return self.project_title


# Project Module Class
status_choice = (("Completed","Completed"),
                 ("Pending","Pending"),
                 ("Cancelled","Cancelled"))
class Project_Module(models.Model):
    project = models.ForeignKey(Timetracker,on_delete=models.CASCADE,null=True)
    module_name = models.CharField(max_length=100,null=True)
    module_description = models.TextField(null=True)
    module_estimated_hours = models.IntegerField(null=True)
    module_start_date = models.DateField(null=True)
    module_completion_date = models.DateField(null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(choices=status_choice,max_length=100,null=True)

    class Meta:
        db_table='project_module'

    def __str__(self):
        return self.module_name
   

# Project Task Class
status_choice = (("Completed","Completed"),
                 ("Pending","Pending"),
                 ("Cancelled","Cancelled"))
priorityChoice=(
   ('High','High Priority'),
   ('Less','Less Priority')
)
class Project_Task(models.Model):
   module = models.ForeignKey(Project_Module,on_delete=models.CASCADE,null=True)
   project = models.ForeignKey(Timetracker,on_delete=models.CASCADE,null=True)
   task_title = models.CharField(max_length=100,null=True)
   task_description = models.TextField(null=True)
   priority = models.CharField(choices=priorityChoice,max_length=30,null=True)
   user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
   task_estimated_hours = models.IntegerField(null=True)
   task_util_minutes = models.IntegerField(null=True)
   status = models.CharField(choices=status_choice,max_length=100,null=True)

   class Meta:
       db_table='project_task'

   def __str__(self):
       return self.task_title
   

# Badge Class

badgeChoice=(
   ('IN','InProgress'),
   ('QF','QuickFinisher'),
   ('LL','LazyLoader'),
   ('SU','SilentUser')
)
class Badge(models.Model):
   badge = models.CharField(choices=badgeChoice,max_length=25,null=True)
   class Meta:
       db_table='badge'

   def __str__(self):
       return self.badge
   

# Project Team Class
status_choice = (("Completed","Completed"),
                 ("Pending","Pending"),
                 ("Cancelled","Cancelled"))
badgeChoice=(
   ('IN','InProgress'),
   ('QF','QuickFinisher'),
   ('LL','LazyLoader'),
   ('SU','SilentUser')
)
class Project_Team(models.Model):
    team_name = models.CharField(max_length=100,null=True)
    project = models.ForeignKey(Timetracker,on_delete=models.CASCADE,null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status = models.CharField(choices=status_choice,max_length=100,null=True)
    badge = models.CharField(choices=badgeChoice,max_length=25,null=True)

    class Meta:
        db_table = 'project_team'

    def __str__(self):
        return self.team_name
   

# User Task Class
status_choice = (("Completed","Completed"),
                 ("Pending","Pending"),
                 ("Cancelled","Cancelled"))
class User_Task(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   task = models.ForeignKey(Project_Task,on_delete=models.CASCADE,null=True)
   status = models.CharField(choices=status_choice,max_length=100,null=True)
   user_totalutil_minutes = models.IntegerField(null=True)

   class Meta:
       db_table='user_task'

   def __str__(self):
       return self.user_id


# Task Badge Class
   
class Task_Badge(models.Model):
    badge = models.ForeignKey(Badge,on_delete=models.CASCADE,null=True)
    task = models.ForeignKey(Project_Task,on_delete=models.CASCADE,null=True)
    
    class Meta:
       db_table='task_badge'
    
    def __str__(self):
       return self.badge