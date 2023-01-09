from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MailSendApi",
      default_version='v1',
      description='''
      This Api aimed at helping developers send mails to single or mulitple users and also receive mails without any
      additional setup. The mail/s being sent or received can also accept file/s if available by attaching single or multiple files to the 'files' field.
      
     <h1> Quick use of MailSendApi:</h1>

      <h5>To send mails to users with or without attached files:</h5>

     <p> 1: Attach their mails in a list/array in the '<strong style="color:red">to_mail</strong>' field,
    
      <p>2: Add your mail to the '<strong style="color:red">from_mail</strong>' field.

     
      <h5>To receive mails from users: </h5>

      <p>1: Attach your mail to the '<strong style="color:red">to_email</strong>' field which also accepts multiple emails
   

     <p> 2: Allow users fill their mail in the '<strong style="color:red">from_email</strong>' field. 







      ''',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nwaforglory6@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns=[
	path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	path('contactpage/', views.ContactSendingView.as_view(), name="contactpage"),
	

]