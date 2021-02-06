from django.shortcuts import render

def helloworld(request):
    name = "Magyo"
    context = {'name': name}
    return render(request, "helloworld/helloworld.html", context)
