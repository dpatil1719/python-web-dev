# Learning Journal — Exercise 2.8 (Deploying a Django Application)

## 1. What was the purpose of this Exercise?

The purpose of this exercise was to prepare a Django web application for production deployment and host it on a public web server. It also focused on improving the user interface using static files like CSS and JavaScript, configuring security settings, and ensuring the application works correctly in a live environment.

---

## 2. What did you learn about static files in Django?

I learned that static files include CSS, JavaScript, and images that are not generated dynamically. Django requires a static folder and specific settings such as STATIC_URL, STATICFILES_DIRS, and STATIC_ROOT to properly serve these files.

I also learned how to link CSS and JavaScript files in templates using:

{% load static %}

This allows Django to locate static resources correctly.

---

## 3. What steps are required to deploy a Django application?

To deploy a Django application, I learned that the following steps are required:

• Upload the project to GitHub  
• Configure production settings (DEBUG=False, SECRET_KEY security, ALLOWED_HOSTS)  
• Install production packages like Gunicorn and WhiteNoise  
• Configure static file handling  
• Create a Procfile to tell the server how to run the app  
• Freeze dependencies using requirements.txt  
• Deploy the application to a hosting platform such as Heroku  
• Run migrations and create a superuser  
• Add data through the admin panel  

---

## 4. What challenges did you face during deployment?

Some challenges I faced included:

• Heroku rejecting older Python versions  
• Static folder missing errors  
• Database configuration errors due to missing PostgreSQL addon  
• Migration errors because tables were not created yet  

I resolved these by:

• Updating Python version  
• Creating a static folder  
• Adding Heroku PostgreSQL database  
• Running migrations correctly  

---

## 5. What did you learn about production security settings?

I learned that production environments require additional security settings such as:

• DEBUG must be set to False  
• SECRET_KEY must not be exposed  
• HTTPS security settings should be enabled  
• Cookies should be marked secure  

These settings prevent sensitive information from being exposed.

---

## 6. How did testing help in this project?

Testing helped verify that:

• Login protection worked correctly  
• Search functionality returned correct results  
• Charts rendered properly  
• Forms validated correctly  

Running automated tests ensured the application was stable before deployment.

---

## 7. What is the most important thing you learned?

The most important lesson I learned is how to take a web application from development to production. This includes configuring environment settings, handling databases, managing dependencies, and making the application accessible online.

---

## 8. How confident do you feel after this exercise?

I feel confident that I can now:

• Deploy Django applications  
• Configure production settings  
• Troubleshoot deployment issues  
• Prepare applications for real-world use  

This exercise gave me real-world experience in full-stack deployment.
