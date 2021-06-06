from django.shortcuts import render

# Create your views here.


def loadsum(request):
    return render(request, 'sum.html')


def loadanswer(request):
    a = int(request.POST['val1'])
    b = int(request.POST['val2'])
    c = a+b
    print(c)
    return render(request, 'answer.html', {'answer': c})
