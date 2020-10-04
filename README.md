# Software With Will

### Resources Used (Citations/URLS)
##### Initial Setup
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-20-04</br>
https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04</br>
##### Production Services (Nginx, Gunicorn, CertBot, AWS)
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04</br>
https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04#step-1-%E2%80%94-installing-certbot</br>
https://www.digitalocean.com/community/tutorials/how-to-set-up-object-storage-with-django</br>
##### File Permissions
https://linuxize.com/post/linux-chown-command/#:~:text=The%20chown%20command%20allows%20you,the%20group%20members%2C%20and%20others</br>
https://www.guru99.com/file-permissions.html</br>
https://stackoverflow.com/questions/16808813/nginx-serve-static-file-and-got-403-forbidden</br>
```
sudo usermod -a -G your_user www-data
sudo chown -R :www-data /path/to/your/static/folder
```
##### Django Project
https://docs.djangoproject.com/en/3.1/howto/windows/#:~:text=Django%20can%20be%20installed%20easily%20using%20pip%20within%20your%20virtual%20environment.&text=This%20will%20download%20and%20install,version%20in%20the%20command%20prompt</br>
