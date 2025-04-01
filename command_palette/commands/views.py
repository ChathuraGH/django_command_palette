from django.shortcuts import render

# Create your views here.





import hashlib
# from django.db import models.User
from django.contrib.auth.models import User,Group
from faker import Faker
import random


from .models import *


def generate_objects(model, count, theme):
    """
    Generates a specified number of Django model instances with data influenced by the given theme.
    
    Args:
        model (django.db.models.Model): The Django model class for which objects will be created.
        count (int): The number of objects to generate.
        theme (str): A theme string to influence the data generation (used for seeding).
    """
    fake = Faker()
    
    # Generate a consistent seed from the theme string
    seed = int(hashlib.sha256(theme.encode()).hexdigest(), 16) % (2**32)
    fake.seed_instance(seed)
    random.seed(seed)
    
    for _ in range(count):
        data = {}
        for field in model._meta.get_fields():


            # if field.is_relation:
                # print("Hello aaWorld::"+field.name+field.name)
                # data[field.name] = User.objects.get(id=1)
                # print('::remote_field::--',models.RemoteField)

                # continue  # Skip relational fields
            if field.primary_key:
                continue  # Skip primary key
            
            field_type = type(field)


            if field_type == models.ForeignKey:
                print("Hello aaWorld__1::"+field.name+":__:"+str(field_type)+":__:"+str(field.is_relation))
                


                # data[field.name] = User.objects.get(id=1)

                data[field.name] = random.choice(list(User.objects.all()))



                # data[field.name] = fake.text()
                print("Hello aaWorld__2::"+str(data[field.name]))




            # Handle different field types with appropriate Faker methods
            elif field_type == models.CharField:
                max_length = field.max_length
                if max_length > 50:
                    value = fake.text(max_length)[:max_length]
                else:
                    value = fake.word()[:max_length]
                data[field.name] = value
            elif field_type == models.TextField:
                data[field.name] = fake.text()
            elif field_type == models.IntegerField:
                data[field.name] = fake.random_int()
            elif field_type == models.BooleanField:
                data[field.name] = fake.boolean()
            elif field_type == models.DateField:
                data[field.name] = fake.date_object()
            elif field_type == models.DateTimeField:
                data[field.name] = fake.date_time()
            elif field_type == models.EmailField:
                data[field.name] = fake.email()
            elif field_type == models.FloatField:
                data[field.name] = fake.pyfloat()
            elif field_type == models.DecimalField:
                data[field.name] = 10
            # elif field_type == models.remote_field:

                



        
            else:
            	# print('Welcome to Online IDE!! Happy Coding :)')

                # Default to a string if the field type is not explicitly handled
                data[field.name] = fake.word()

        
        # Create and save the model instance
        instance = model(**data)
        instance.save()



def generate_user_objects(count):

	for i in range(0,count):
	    fake = Faker()
	    name = fake.name()
	    first_name = name.split(' ')[0]
	    last_name = ' '.join(name.split(' ')[-1:])
	    username = first_name[0].lower() + last_name.lower().replace(' ', '')
	    user = User.objects.create_user(username, password=username)
	    user.first_name = first_name
	    user.last_name = last_name
	    user.is_superuser = False
	    user.is_staff = False
	    user.email = username + "@" + last_name.lower() + ".com"
	    user.save()



def cm(request):

    fake = Faker()


    generate_objects(Post,10,fake.word())

    # generate_objects(Post,10,'food')

    generate_user_objects(5)

    return render(request, 'cm.html')

