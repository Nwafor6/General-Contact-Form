from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ContactSerializer
from rest_framework import generics
from django.core.mail import send_mail, EmailMultiAlternatives,EmailMessage
from django.template import Template, Context
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ContactSendingView(generics.CreateAPIView):
	serializer_class=ContactSerializer

	def post(self, request, *args, **kwargs):

		name=request.POST["name"]
		subject=request.POST["subject"]
		from_email=request.POST["from_email"]
		to_email=request.POST.getlist("to_email")
		body=request.POST["body"]
		files=request.FILES.getlist("files")

		total_sent_mail=0

		for email in to_email:

			message=EmailMessage(

			subject,
			body,
			from_email,
			[email]

			)
			total_sent_mail +=1
			# attach file if any exist
			if files:
				for file in files:
					# message.attach_file(file)
					message.attach(file.name,file.read(), file.content_type )
			message.send()

			# attach the file to the email message


		return Response({"response": 'Message sent !!', "total_sent_mail": total_sent_mail,})


