from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Updated to handle hashed passwords

    def __str__(self):
        return self.username

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    portfolio = models.URLField()

    def __str__(self):
        return self.email


class Experience(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    username = models.OneToOneField(Login, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    about_me = models.TextField()
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    projects = models.TextField()  # Use comma-separated values for simplicity
    skills = models.TextField()   # Use comma-separated values for simplicity
    education = models.TextField()  # Use comma-separated values for simplicity
    experiences = models.ManyToManyField(Experience)
    interests = models.TextField()  # Use comma-separated values for simplicity
    achievements = models.TextField()  # Use comma-separated values for simplicity
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Job(models.Model):
        company_name = models.CharField(max_length=255)
        company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
        job_role = models.CharField(max_length=255,null=True, blank=True)
        skills_required = models.TextField(null=True, blank=True)
        job_description = models.TextField(null=True, blank=True)
        last_date_for_submission = models.DateField(null=True, blank=True)
        application_link = models.URLField(null=True, blank=True)

        def __str__(self):
            return f"{self.job_role} at {self.company_name}"

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_image = models.ImageField(upload_to='events/')
    event_description = models.TextField()
    event_date = models.DateField()

    def __str__(self):
        return self.event_name
        

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('ProfitAndLoss', 'Profit and Loss'),
        ('Percentage', 'Percentage'),
        ('PermutationAndCombination', 'Permutation and Combination'),
        ('TableChart', 'Table Chart'),
        ('PieChart', 'Pie Chart'),
        ('BarGraph', 'Bar Graph'),
        ('CPlusPlus', 'C++'),
        ('Java', 'Java'),
        ('Python', 'Python'),
    ]

    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)

    def __str__(self):
        return f"{self.category} - {self.question_text[:50]}"

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    questions = models.ManyToManyField(Question)
    duration_in_minutes = models.IntegerField()

    def __str__(self):
        return self.title

class UserSubmission(models.Model):
    id = models.AutoField(primary_key=True)  
    username = models.ForeignKey(Login, on_delete=models.CASCADE, to_field='username')
    category = models.CharField(max_length=100 ,null=True)  # Store category name instead of ID
    score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('username', 'category')

    def __str__(self):
        return f"{self.username} - {self.category} - {self.score}"





