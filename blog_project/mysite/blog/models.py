from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE) # just made every user as super user which u wouldn't want 
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    published_date = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True) # publish date zaoori nahi mention karna , maybe we wanna save it as a draft 

    def publish(self):
        self.published_date = timezone.now() # at time of actually publishing pulish date aegi 
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk}) #ye pk is the key since each post will have its own sequential key 
        #after you have published the post where should u go . This is an inbuilt method
    

    def __str__(str):
        return self.title # apna title dikhaega post jab call kiya jaega ( basically its title will be listed )


class Comment(models.Model):
    post = models.ForeignKey("blog.Post", related_name = 'comments', on_delete=models.CASCADE) # connecting this post with post 
    author = models.CharField(max_length=30)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False ,default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def get_absolute_url(self):
        return reverse("post_list")
    

    def __str__(self):
        return self.text
