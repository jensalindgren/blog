# My Training Blog

## General Information

This is a blog for training purposes. You can register accounts and post information and traning tips for others to see. You can also comment on other posts. Like them and unlike them. You can also edit and delete your own posts. You can also upload training pictures. Link to the live site can be found [here](https://letstrain.herokuapp.com/).

## Table of Contents

- [My Training Blog](#my-training-blog)
  - [General Information](#general-information)
  - [Table of Contents](#table-of-contents)
  - [Project Goals](#project-goals)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
    - [Start](#start)
  - [Structure](#structure)
  - [Database Model](#database-model)
  - [Wireframes](#wireframes)
  - [Color Scheme](#color-scheme)
  - [Features](#features)
    - [General Features](#general-features)
    - [Home Page](#home-page)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries \& Programs](#frameworks-libraries--programs)
    - [Packages](#packages)
    - [Databases](#databases)
    - [Tools Used](#tools-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Deploying to Heroku](#deploying-to-heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

## Project Goals

- Is to create a blog where people can post training tips and information. Also to create a community where people can share their training experiences and help each other out.
- Structure the site in a way that is easy to navigate and use.
- Site user can register an account and login to the site. And be able to post information and training tips for others to see.
- Site user can comment on other posts. Like them and unlike them.
- Responsive on all device sizes.

## User Goals

- As site Admin I want to manage the site and be able to delete posts and comments.
- As a site user I want to be able to register an account and login to the site.
- As a site user I want to be able to post information and training tips for others to see.
- As a site user I want to be able to comment on other posts. Like them and unlike them.

## User Stories

GitHub projects was used as my project management tool to track user stories.

### Start
I will implement more user stories as I go along. I will also add more features to the site as I go along.
![Alt text](/assets/wireframes/user_story_1.png?raw=true "User Story 1")
I was able to get the first three user story's done.
![Alt text](/assets/wireframes/user_story_2.png?raw=true "User Story 2")


## Structure

The website has been organized in a Hierarchical Tree Structure to ensure the site user navigates through the site effortlessly and intuitively.

- Home
  - The home page is the first page the user will see when they visit the site. It contains a navigation bar at the top of the page. The navigation bar contains a link to the home page, login page, register page, and logout. The home page also contains a search bar and a button to create a post. The home page also contains a list of posts. Each post contains a title, author, date, and a like button. The home page also contains a footer with links to social media. You can also edit and delete your own posts.
  
- Post Detail
  - Post Detail is a page that contains the post title, author, date, and the post content. The post detail page also contains a like button and a comment section. The comment section contains a form to add a comment and a list of comments. Each comment contains the author, date, and comment content. You can also edit and delete your own comments.

- Create Post
  - Create Post is a page that contains a form to create a post. The form contains a title field, content field, and an image field. The image field is optional. The create post page also contains a cancel button. The cancel button will take you back to the home page.

- Edit Post
  - Edit post is a page that contains a form to edit a post. The form contains a title field, content field, and an image field. The image field is optional. The edit post page also contains a cancel button. The cancel button will take you back to the home page.

- Delete Post
  - Delete post is a page that contains a form to delete a post. Gives you a options if you want delete your own post. The delete post page also contains a cancel button. The cancel button will take you back to the home page.

- Edit Comment
  - Edit comment is a page that contains a form to edit a comment. The form contains a content field. So you can update your comment.
  
- Delete Comment
  - Delete comment works as the delete post page. It contains a form to delete a comment. Gives you a options if you want delete your own comment. The delete comment page also contains a cancel button. The cancel button will take you back to the home page.

- Login
  - Login is a page that contains a form to login to the site. The form contains a username field and a password field. The login page also contains a cancel button.

## Database Model

The type of database being used for the is relational database being managed using PostgreSQL.

## Wireframes

Balsamiq has been used to showcase the appearance of the site and display structure.

## Color Scheme

The color scheme has been chosen to be a dark theme with a light theme for the text. This is to make the site more appealing to the eye and to make the text more readable.

## Features

### General Features

- The website has been designed from a mobile first perspective.
- Site is responsive and will adapt to different screen sizes.
- Navigation bar is fixed to the top of the page.
- Search bar is available on all pages.
- Footer is available on all pages. And contains links to social media.

### Home Page

## Technologies Used

### Languages

- HTML5
- CSS3
- Python
- JavaScript

### Frameworks, Libraries & Programs

- Django
  - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- Django Templates
  - Django templates are used to render the data from the backend to the frontend.
- Font Awesome
  - Font Awesome is a font and icon toolkit based on CSS and LESS.
- Bootstrap
  - Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.
- jQuery
  - jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax.

### Packages

- Gunicorn
  - Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.

- SummerNote
  - SummerNote is a JavaScript library that allows you to create a WYSIWYG editor.

- Cloudinary
  - Cloudinary is a cloud-based image and video management service.

### Databases

- ElephantSQL
  - ElephantSQL is a PostgreSQL database as a service. It is a cloud-based database that is managed by the vendor.

- Heroku
  - Heroku Postgres database was used in production, as a service based on PostgreSQL provided by Heroku.

### Tools Used

- Git
  - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

- GitHub
  - GitHub is used to store the project code after being pushed from Git.
  
- Gitpod
  - GitPod was used for writing code, committing, and then pushing to GitHub.

- Balsamiq
  - Balsamiq was used to create the wireframes during the design process.
  
- Am I Responsive
  - Am I Responsive was used to preview the website across a variety of popular devices.

- Chrome DevTools
  - Chrome DevTools was used to test the website across a variety of popular devices.

- W3C Markup Validation Service
  - W3C Markup Validation Service was used to validate the HTML code.

- W3C CSS Validation Service
  - W3C CSS Validation Service was used to validate the CSS code.

- JSHint
  - Used to validate the JavaScript code.

## Testing

Testing information can be found in a separate file [here](TESTING.md).


## Deployment

### Deploying to Heroku

The project was deployed to Heroku using the following steps:

1. Create a requirements.txt file using the terminal command `pip3 freeze --local > requirements.txt`
2. Create a Procfile for connecting to Heroku with web gunicorn my_training_blog.wsgi

3. Push the requirements.txt and Procfile to GitHub.

4. Create a env.py and added os.environ.get("SECRET_KEY") and os.environ.get("CLOUDINARY_URL") and os.environ.get("DATABASE_URL")

4. Create a new app on Heroku, give it a name, and set the region to Europe.

5. Go to settings and click on "Reveal Config Vars".
   - Set the following config vars:
   - CLOUDINARY_URL and copy url from cloudinary
   - DATABASE_URL and copy the url from Elphantsql that was created from a new instance
   - SECRET_KEY added the secret key from env.py
   - Added PORT and set it to 8000
   - Added DISABLE_COLLECTSTATIC and set it to 1 just for the app to deploy. I removed it when the app was done.

6. In settings.py, set the following:
   - ALLOWED_HOSTS = ['my-training-blog.herokuapp.com', 'localhost']
   - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
   - STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
   - STATICFIELS_DIRS = [os.path.join(BASE_DIR, 'static')]
   - STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   - MEDIA_URL = '/media/'
   - DEFUALT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
   - Added in templates directory to the TEMPLATES DIRS
   - In the INSTALLED_APPS added cloudinary and cloudinary_storage
   - Added in the screect key from env.py SECRET_KEY = os.environ.get('SECRET_KEY')
   - Added import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

1. Go to the Deploy tab and select GitHub as the deployment method. Click on Deploy branch. Wait to the build is complete. And open the app with the Open App button. Link to the live site can be found [here](https://my-training-blog.herokuapp.com/).


## Credits

### Content
- Website content was written by the developer.

### Media

- The photos used in this site were obtained from [Unsplash](https://unsplash.com/).

### Code
- Stack Overflow was used to help with the code. and W3Schools. were consulted for code examples. And regular basis for inspiration.. To better understand the code and how to implement it.

### Acknowledgements

- My mentor Marcel for continuous helpful feedback.

- My fiancee for her support and encouragement.

Back to [top](#table-of-contents)