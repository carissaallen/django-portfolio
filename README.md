# Portfolio + Blog Built With Django

The goal of this project is to build my own portfolio, as well as a fully functional blog.

Through the creation of this project, I learned how to:
  * Add apps to my Django project
  * Work with databases including SQLite and Postgres
  * Access the admin panel
  * Create super users 
  * Create virtual environments 
  * Make a responsive website with Bootstrap 4
  * Work with static and media files 

# Deployments

`ssh djangodeploy@carissa.io`

Activate the virtual environment.<br>
`source myvenv/bin/activate`

After making changes, create and run new migrations.<br>
`python manage.py makemigrations`
`python manage.py migrate`

Restart Gunicorn, then restart Nginx.<br>
`systemctl restart gunicorn && systemctl restart nginx`

# Reference
Click [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04) to reference how to set up Django with Postgres, Nginx, and Gunicorn on Ubuntu 16.04.
