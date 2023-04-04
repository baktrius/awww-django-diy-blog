# Django DIY Blog (Adopted to be awww task)

## Credits
Task is modified version of MSD assessment. Details below.

## Task overview
1. Read original task overview at [MDN assessment page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog)
2. Clone this repository from github to your local drive.
3. Checkout awww1 branch
4. Follow setup instructions from Quick Start section (below)
5. Tests shouldn't pass, but you should be able to visit index page and bloggers list
6. Create models Blog and BlogComment according to task description
7. Check that tests from test_model.py are satisfied
8. Add created models to admin (check that you are successful)
9. Create View displaying list of blogs using generic.ListView (appropriate template should be created)
10. Make appropriate changes to urls.py and check that your list is displaying correctly
11. Create merged view for both displaying article and its comments and adding new comments (user authentication isn't required). You can find previous templates in template directory

If you get stuck anywhere along the road I suggest checking this commit changes as they explicitly highlight what I have deleted from fully working example to create this task. And of course you are welcome to ask me questions.


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
