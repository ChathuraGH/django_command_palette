from django.db import models
# from django.contrib.gis.db import models

# Create your models here.
# my codes
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse
from django.shortcuts import redirect

	#import of tinymce
#from tinymce import HTMLField






# class Profile(models.Model):
# 	user_profile_name = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
# 	# REMOVED primary_key=True, BECOSER IT WILL NOT ALLOW CHANGE USER PROFILE NAME(USER NAME)
# 	# ABOVE FIELD USE AS UNEDITABLE,AS UNIQE USER NAME TO SHOW IN THE PROFILE


# 	website= models.URLField(max_length=150,null=True,blank=True)
# 	facebook_profile= models.URLField(max_length=150,null=True,blank=True)
# 	twitter_profile= models.URLField(max_length=150,null=True,blank=True)
# 	youtube_channal= models.URLField(max_length=150,null=True,blank=True)
# 	instagram_profile= models.URLField(max_length=150,null=True,blank=True)



# 	i_o_d_s=models.BooleanField(default=True)
# 	# inteligent profile discription state

# 	c=(
# 		('1','Male 🚹'),
# 		('2','Female 🚺'),
# 		# (None,"Don't want to mention here."),
# 		)

# 	sex=models.CharField(max_length=1,choices=c,null=True,blank=True)





# 	def __str__(self):
# 		return self.user_profile_name.username





class Post(models.Model):   #post table in the databace
	author = models.ForeignKey(User, on_delete=models.CASCADE)


	title  = models.CharField(max_length=100)
	content = models.TextField(max_length=100000)
	# content = HTMLField('Content')
	# date_posted = models.DateTimeField(default=timezone.now)
	date_posted = models.DateTimeField(auto_now_add=True)
	# feeling /happy/inspiered/welcome/good/new/other
	feeling = models.CharField(max_length=12,null=True,blank=True)
#(1) writing locating

	post_location=models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)

	# location = models.PointField()

# from=location(in the world)

#(2) post view type /privet/public/


	# to make title as post object's title
	# without this it will post object's title as postobject0,1,2
	def __str__(self):
		return self.title
		# return '"'+self.author.user_data.username+" 'S POST "+'"'+self.title+'"'
