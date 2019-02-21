from django.shortcuts import render
from django.http import HttpResponse
from .models import Child , Mom , State , Citizen
# Create your views here.

def index(request):
    return HttpResponse("test")

# each Mom is link to [Child] via (child) special comparison word and that is how this works
def childList(request):
    childlist = Child.objects.all()
    namePrint = ''
    for eachChild in childlist:
        namePrint += f"child: {eachChild} <br>"
        for eachMom in Mom.objects.filter(child__firstName=eachChild.firstName):
            namePrint += f" mom: {eachMom} <br>"
    return HttpResponse(namePrint)


# each Child is linked to [Mom] via {mother} foreignkey so that is what you use to compare
def momList(request):
    momList = Mom.objects.all()
    namePrint = ''
    for eachMom in momList:
        namePrint += f'{eachMom} <br>'
        for eachChild in Child.objects.filter(mother__firstName = eachMom.firstName):
            namePrint += f'child: {eachChild} <br>'
    return HttpResponse(namePrint)

# goes through each mom and gives them a child
def newChildren(request):
    momList = Mom.objects.all()
    for eachMom in momList:
        newChild = Child(firstName = "Revolver", lastName = "ocelet", mother = eachMom)
        newChild.save()
    return HttpResponse("baby Boom")

# delete is used to remove mom in first index
def deleteMom(request):
    momList= Mom.objects.all()
    momList[0].delete()
    return HttpResponse("big mana terminated")


