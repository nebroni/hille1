from django.core.management import execute_from_command_line
from django.http import  HttpResponseRedirect
from django.urls import path
from django.shortcuts import render
from password import password as p

ROOT_URLCONF=__name__,
DEBUG=True,
SECRET_KEY='secret',
TEMPLATES=[
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': ['C:\\Users\\User\\PycharmProjects\\hillel1\\html'],
	}
]




dict1 = {}

def handler(request):
	url = request.POST.get('req','')
	massage = 'Invalid URL . Allowed schemes: http,ftp,https'
	short_url = p()
	if url.startswith(('http://','https://','ftp://')):
		dict1[short_url] = url
		massage = short_url
	return render(request, 'zen.html', {'message': massage, 'check': len(massage)})

def redirect(request,key):
	return HttpResponseRedirect(dict1[key])

urlpatterns = [
	path('', handler, name='index'),
	path('<key>', redirect)
]

if __name__ == "__main__":
	execute_from_command_line()
