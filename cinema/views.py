from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cinema.models import Movie
from cinema.serializer import MovieSerializer


@api_view(["GET", "POST"])
def movies_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=200)

    elif request.method == "POST":
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=200)
    elif request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        movie.delete()
        return Response({"success": True}, status=204)