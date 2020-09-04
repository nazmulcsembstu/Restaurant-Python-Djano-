from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(resquest):
	return render(resquest, 'KhawaDawa/Index.html')

def About(resquest):
	return render(resquest, 'KhawaDawa/About.html')

def Menu(resquest):
	return render(resquest, 'KhawaDawa/Menu.html')

def BanFacility(resquest):
	return render(resquest, 'KhawaDawa/BanFacility.html')

def RecVendors(resquest):
	return render(resquest, 'KhawaDawa/RecVendors.html')

def Gallery(resquest):
	return render(resquest, 'KhawaDawa/Gallery.html')

def Catering(resquest):
	return render(resquest, 'KhawaDawa/Catering.html')

def Events(resquest):
	return render(resquest, 'KhawaDawa/Events.html')

def Contact(resquest):
	return render(resquest, 'KhawaDawa/Contact.html')

def BanBook(resquest):
	return render(resquest, 'KhawaDawa/BanBook.html')
