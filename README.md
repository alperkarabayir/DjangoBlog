# ALPER'S OFFICE APP ASSIGNMENT SOLUTION
Dear Developer, my name is Alper and because of my current job's overtime and end of year reporting watch on weekend, I developed that project in limited time, it took around 6-7 hours, but did my best. This explains a brief explanation about my application and how to run it. Enjoy!

## APPLICATION STACK DESCRIPTION
I use `Django` because it has all things I need to build in this scope also as you wanted. In this case I use database of django default sqlite3 db.
I found big part of frontend css and bootstrap files from internet and created my htmls, i didnt want to waste my limited time for frontend actually. Focused more on backend part.
I use Django's in-build `unittest` module to test the routes of my application functions.

I used `Postman` to test my links.

I also use `pylint` to tidy up my code and integrate it into `VSCode` but after i removed my code to PyCharm, i uninstalled it from project for faster development. 
PyCharm gives you help to write Clean code already, and i know it is important for team performance as it makes my code understandable and easier to maintain.

I used `gunicorn` but there was a problem about ports. Didn't find the solution. Changed it to default one.

I use Python's `virtual environment` a.k.a. `venv` to build my dependencies. I choose Docker as a container to isolate packages in Linux development environment as an alternative for `venv`.

I follow [this](https://www.python.org/dev/peps/pep-0008/) for coding styles as i learned.

I also use `Git local`.

## FILE STRUCTURE
```
OfficeCodeApp/         					# the application directory
│
├── .gitignore                  		
├── .dockerignore
├── venv                        		# isolated package for this project. [Important] run this first before executing any runnables if you don't want to use Docker
├── blog/                     		 	# blog application directory
│   ├── __init__.py             		# just to mark for package directory│  
│   ├── migrations            			# migration files for sqlite3 db - models│   
│   ├── static             				# css files of my frontend│   
│   ├── templates.py             		# template files of my frontend   
│   ├── admin.py             			# registration models to my admin page│   
│   ├── apps.py             			# default python file│    
│   ├── forms.py             			# registration form file   
│   ├── models.py             			# models of my project created in this file│  
│   ├── serializers.py             		# I added a webservice to reach all post from app and its serializer in it   
│   ├── signals.py             			# I found on internet actually, user - profile connection receiver  
│   ├── test.py             			# test file of my application calls│    
│   ├── urls.py             			# url patterns file│   
│   └── views.py          				# views file for pages and services
├── OfficeCodeApp/                     	# this is the project main directory!
│   ├── __init__.py             		# just to mark for package directory
│   ├── asgi.py             			# default asgi.py file   
│   ├── settings.py             		# project settings file   
│   ├── urls.py             			# main url patterns file│   
│   └── wsgi.py               			# default wsgi.py file 
├── README.md                   
├── manage.py                     		# main driver of application
├── db.sqlite3                     		# database of application
├── Dockerfile                  		# my custom Docker image to build and run in Docker
└── requirements.txt            		# additional Python-friendly packages for this application

```

RUNNING APP:
You can use run it with docker => "docker run -it -p 8000:8000 officeappcode"
Or you can run it without docker => "python manage.py runserver"
you have to activate venv before
you can open app.`http://127.0.0.1:8000/`
`http://127.0.0.1:8000/`

***IMPORTANT*** 
In test sqlite3 db file i added 2 users ```admin:123``` and ```Alper:test12345``` You can login with this users or create a user with clicking Register link.
After you logged in, you will go to redirect to homepage, which you can see all posts order by date. On the top navigator:
```
Register: You can create a new user by filling form.

Login: You can login with a user.

Home: Homepage => You can click user's name and you will see user's all posts. In addition you can click to Topic of a post and you will see all posts belong to that Topic. If post belongs to logged user, it will activate a delete button - "just for creator of post"

Search: Search page => after you clicked that link, you can search anything you want, it is searching users, topics and posts on the same time. 

New Post: You can create a new post by adding Title, Content and choosing Topic from combobox. I added 2 topics by shell to db. "Technology and Science". After you post you will see your post created.

Profile: Every user can see his profile info and posts. 

Logout: For out.

Beside that I created a webservice for getting all datas => You can go to link and see datas into browser as JSON formatted style http://127.0.0.1:8000/getallposts/ or use Postman "GET" method with link.

http://127.0.0.1:8000/admin/ django default admin panel. You can see models.

```
***IMPORTANT***


With my Best Regards, I hope we can talk and work together in future as part of bigger projects. 