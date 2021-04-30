from django.shortcuts import render, HttpResponse

# Create your views here.
def survey(request):
     print('survey view method:', request.method)
     return render (request, 'survey.html')
def add_user(request):
     if request.method == "POST":
          context = {
          'fname': request.POST['fname'],
          'lname': request.POST['lname'],
          'loc': request.POST['loc'],
          'type': request.POST['type'],
          'campus':request.POST['campus'],
          }
          return render (request, 'showing.html', context)
          # print (request.POST['fname'] , request.POST['lname'])
     return HttpResponse(request)