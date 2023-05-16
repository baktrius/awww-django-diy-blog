# Django DIY Blog (Adopted to be awww task)

## Credits
Task is modified version of MSD assessment. Details below.

## Task overview
1. This task builds up on previous one so if you haven't done it, and you get lost, maybe check it out (awww1 branch)
2. Clone this repository from github to your local drive.
3. Checkout awww2 branch
4. Follow setup instructions from Quick Start section (below)
5. During previous iteration i messed up code performing commenting. I cheated and used CreateView for both showing post details and adding comments. Thats why endpoint `/blog/blog/<blogId>` shows post description (when GET http method is used) and add comment (when POST http method is used). That's not very nice, but what can you do not? I changed POST part of endpoint `/blog/blog/<blogId>` so that on success instead of redirect it returns json. Inspect returned json format (how to do this? - tip don't try to be very smart).
6. Fill in `blog/static/scripts/comment.js` so that
   a) appropriate request is send using ajax
   b) page is updated after request succeeds (without reloading)
   c) use date returned from django, possibly don't modify other code (then `comment.js`)

If you get stuck anywhere along the road you are welcome to ask me questions.


Basic blog site written in Django (part of MDN Django module assessment)
----
This web application creates an very basic blog site using Django. The site allows blog authors to create text-only blogs using the Admin site, and any logged in user to add comments via a form. Any user can list all bloggers, all blogs, and detail for bloggers and blogs (including comments for each blog).

The models for this site are as shown below:

![Django Blog Models](./blog/static/images/diy_django_mini_blog_models.png)


For more information see the associated [MDN assessment page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog).


## Quick Start

To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
   We recommend using a Python virtual environment.
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python3` to start Python):
   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.
