from django.db import models

# Create your models here.

class AboutContent(models.Model):
    image = models.ImageField(upload_to='about_images/')
    title = models.CharField(max_length=1000)
    description = models.TextField()
    Available_subject = models.CharField(max_length=1000)
    numOfSubject = models.IntegerField()
    Courses_Available = models.CharField(max_length=1000)
    numOfCourses = models.IntegerField()
    skilled_instructors = models.CharField(max_length=1000)
    numOfInstructors = models.IntegerField()
    Happy_Students = models.CharField(max_length=1000)
    numOfStudents = models.IntegerField()
    
    def __str__(self):
        return "About Content"
    
class FeatureContent(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    Skilled_Instructors = models.CharField(max_length=400)
    SkilledDescription = models.TextField()
    International_Certificate = models.CharField(max_length=600)
    InternationalDescription = models.TextField()
    Online_Classes = models.CharField(max_length=600)
    OnlineDescription = models.TextField()
    image = models.ImageField(upload_to='feature_images/')
    
    def __str__(self):
        return "Feature Content"
    
    
class Instructors(models.Model):
    image = models.ImageField(upload_to='instructors')
    name = models.CharField(max_length=300)
    course = models.CharField(max_length=700)
    x = models.CharField(max_length=500)
    facebook = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    youtube = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    

class ReleaseCoure(models.Model):
    image = models.ImageField(upload_to='course/')
    name = models.CharField(max_length=500)
    instructor = models.ForeignKey('Instructors', on_delete=models.CASCADE)
    description = models.TextField()
    description2 = models.TextField()
    rating = models.FloatField()
    lectures = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=200)
    language = models.CharField(max_length=250)
    course_price = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Participant(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  course = models.ForeignKey(ReleaseCoure, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
    


class Testimonial(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    
    def __str__(self):
        return "Testimonial Content"
    

class testimonialSlider(models.Model):
    image = models.ImageField(upload_to='about_images/')
    name = models.CharField(max_length=1000)
    msg = models.TextField()
    course = models.ForeignKey(ReleaseCoure, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class OurLocation(models.Model):
    location = models.TextField()
    phone = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    
    def __str__(self):
        return "Our Location"
    
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=1000)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

