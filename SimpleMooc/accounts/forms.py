from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User 
#--> mudou depois de criar o nosso usuario
from django.contrib.auth import get_user_model

from SimpleMooc.core.mail import send_mail_template
from SimpleMooc.core.utils import generate_hash_key

from .models import PasswordReset

User = get_user_model()

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email

        raise forms.ValidationError('Nenhum usuário encontrado com este E-mail')

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'accounts/password_reset_mail.html'
        subject = 'Criar nova senha no simple MOOC'
        context = {
            'reset': reset,
        }
        send_mail_template(subject, template_name, context, [user.email])



#class RegisterForm(UserCreationForm):
class RegisterForm(forms.ModelForm):
#    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A Confirmação não está correta')
        return password2


    def save(self, commit=True):
        user =  super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User 
        fields = ['username', 'email']


class EditAccountForm(forms.ModelForm):
    # removido na aula 47
    """
    def clean_email(self):
        email = self.cleaned_data['email']
        # este é um processo de alterar usuario, entao o dados esta editado
        # esta queryset faz: pega o email da tela e busca na tabela todos que possuam o 
        # email exceto o atual, pois assim se houver outro email alem do dele mesmo vai ser 
        # verdadeiro e nao vai deixar colocar
        queryset =  User.objects.filter(email=email).exclude(pk=self.instance.pk)

        if queryset.exists():
            raise forms.ValidationError('Já existe usuário com este E-mail')

        return email
    """
    class Meta:
        model = User
    # removido na aula 47
    #    fields = ['username', 'email', 'first_name', 'last_name']
        fields = ['username', 'email', 'name']
    