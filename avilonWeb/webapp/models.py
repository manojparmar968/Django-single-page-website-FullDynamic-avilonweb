from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100,null=True,blank= True)
    degnination = models.CharField(max_length=100,null=True,blank= True)
    image = models.FileField(upload_to='team_image', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Team"

class SocalMedia(models.Model):
    facebook = models.CharField(max_length=255,null=True,blank=True)
    instagram = models.CharField(max_length=255,null=True,blank=True)
    twitter = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.facebook)+" "+str(self.instagram)+" "+str(self.twitter)

    class Meta:
        verbose_name_plural = "Socail Media Pages Link"

class Gallery(models.Model):
    image = models.FileField(upload_to='gallery_image', null=True, blank=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name_plural = "Gallery"

class Client(models.Model):
    image = models.FileField(upload_to='client_image', null=True, blank=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name_plural = "Client"

class FrequentlyAskedQuestions(models.Model):
    question = models.CharField(max_length=255,null=True,blank=True)
    answer = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "FrequentlyAskedQuestions"

class ContactForm(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=255,null=True,blank=True)
    subject = models.CharField(max_length=255,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)+" "+str(self.email)

    class Meta:
        verbose_name_plural = "ContactForm"


        
class AboutUs(models.Model):
    heading = models.CharField(max_length=255,null=True,blank=True)
    sub_heading = models.CharField(max_length=255,null=True,blank=True)
    paragraph1 = models.TextField(null=True,blank=True)
    paragraph2 = models.TextField(null=True,blank=True)
    image = models.FileField(upload_to='about-us_image', null=True, blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "AboutUs"


class AboutUsPoints(models.Model):
    points = models.CharField(max_length=255,null=True,blank=True)
    aboutus = models.ForeignKey(AboutUs, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.points
