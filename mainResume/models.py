from django.db import models
from datetime import date

# Create your models here.
class skill(models.Model):
    id = models.AutoField(primary_key=True)
    skill_name = models.CharField("Skill Name", max_length=50)
    description = models.TextField()

    # Define the choices for level of the skill
    LEARNING = "L"
    PRACTICING = "P"
    EXPERT = "E"
    MASTER = "M"

    experience_choices = [
        (LEARNING, "Learning"),
        (PRACTICING, "Practicing"),
        (EXPERT, "Expert"),
        (MASTER, "Master"),

    ]
    experience_level = models.CharField(choices=experience_choices, default=MASTER, max_length=50)
    
    # Define the choices for skill type
    TECHNICAL = "Tech"
    PRODUCT = "Prod"
    SALES = "Sales"
    MARKETING = "Market"
    MANAGERIAL = "Managerial"

    type_choices = [
        (TECHNICAL, "Technical"),
        (PRODUCT, "Product"),
        (SALES, "Sales"),
        (MARKETING, "Marketing"),
        (MANAGERIAL, "Managerial"),

    ]
    skill_type = models.CharField(choices=type_choices, default=TECHNICAL, max_length=50)

    def __str__(self):
        return str(self.skill_name)

class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField("Employer Name", max_length=50)
    position_name = models.CharField("Position Name", max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, default=date.today)
    achievements = models.TextField()
    related_skills = models.ForeignKey(skill, on_delete=models.DO_NOTHING)
    company_url = models.CharField("Employer URL", max_length=50, blank=True)
    def __str__(self):
        return str(self.company_name + ' ' + self.position_name)



    