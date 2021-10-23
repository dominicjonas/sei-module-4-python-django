# from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, response

from rest_framework import views, response, status, exceptions

from .models import Composer
from .serializers import ComposerSerializer

# Create your views here.
def index(request):
    print(request)
    # grabbing what we need from the database
    list = Composer.objects.all()
    # creating a context object
    context = {'composers': list}
    # rendering based on a template
    return render(request, 'composers/index.html', context)


class ComposerListView(views.APIView):
    def get(self, request):
        composers = Composer.objects.all()
        serialized_composers = ComposerSerializer(composers, many=True)
        return response.Response(serialized_composers.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        # create an Album instance from the request data
        composer_to_add = ComposerSerializer(data=request.data)
        # save the Album to database
        if composer_to_add.is_valid():
            composer_to_add.save()
            return response.Response(composer_to_add.data, status=status.HTTP_201_CREATED)

        return response.Response(
            composer_to_add.errors, status=status.HTTP_400_BAD_REQUEST
        )

class ComposerDetailView(views.APIView):
    def get_composer_by_id(self, id):
        try:
            return Composer.objects.get(id=id)
        except Composer.DoesNotExist:
            raise exceptions.NotFound(detail="Composer does not exist")

    def get(self, request, id):
        composer = self.get_composer_by_id(id)
        serialized_composer = ComposerSerializer(composer)
        return response.Response(serialized_composer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        composer = self.get_composer_by_id(id)
        composer.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        composer = self.get_composer_by_id(id)
        updated_composer = ComposerSerializer(composer, data=request.data)
        if updated_composer.is_valid():
            updated_composer.save()
            return response.Response(
                updated_composer.data, status=status.HTTP_202_ACCEPTED
            )
        return response.Response(
            updated_composer.errors, status=status.HTTP_400_BAD_REQUEST
        ) 








# API handlers

def composers(request):
    if request.method == 'GET':
        return create(request)
    if request.method == 'POST':
        return create(request)

def composers(request):
    if request.method == 'GET':
        return read_one(request)
    if request.method == 'PATCH':
        return update(request)
    if request.method == 'DELETE':
        return delete(request)


# CRUD

def create(request):
    # something something
    return HttpResponse('CREATE')

def read(request):
    #  can we get albums back as json
    return HttpResponse('READ')

def read_one(request):
    #  can we get albums back as json
    return HttpResponse('READ ONE')

def update(request):
    return HttpResponse('UPDATE')

def delete(request):
    #  can we delete an album
    return HttpResponse('DELETE')