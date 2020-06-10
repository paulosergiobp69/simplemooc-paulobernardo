from django import forms
from django.core.mail import send_mail
from django.conf import settings

from SimpleMooc.core.mail import send_mail_template

from .models import Comment

class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Duvida', widget=forms.Textarea
    )
    
    def envia_mail(self, course)    :
        subject = '[%s] Contato' % course
        #message = 'Nome: %(name)s;E-mail: %(email)s; %(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        template_name = 'courses/contact_email.html'
        #message = message % context
        #send_mail(
        #    subject, message, settings.DEFAULT_FROM_EMAIL,
        #    [settings.CONTACT_EMAIL]
        #)

        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # so foi passado o campo de comentario no form,
        # por isso vai ser necessario colocar o commit = false e passar os campos
        # de user e o id do comentario na view: show_announcement
        fields = ['comment']
