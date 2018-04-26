# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

PRODUCTS=[
	{'id':'1','price':'19.99'},
	{'id':'2','price':'29.99'},
	{'id':'3','price':'4.99'},
	{'id':'4','price':'49.99'}
]
def index(request):
	request.session.modified = True
	return render(request,'amadon_app/amadon.html')

def buy(request):

	for product in PRODUCTS:
		if request.POST['product_id']==product['id']:
			total=int(request.POST['quantity'])*float(product['price'])
			
	request.session['total']=total
	request.session.modified = True

	# if request.method=='POST':
	# 	total_quantity+=request.POST['quantity']
	# 	print total_quantity


	
	
	return redirect('/checkout')
def checkout(request):

	return render(request,'amadon_app/checkout.html')


