"""
API de Bloco de Notas usando Django REST Framework
Instalar: pip install django djangorestframework

Configuração necessária:
1. django-admin startproject notas_projeto
2. cd notas_projeto
3. python manage.py startapp notas
4. Adicionar este código em notas/views.py, notas/serializers.py, notas/models.py
5. Configurar urls.py

Este arquivo mostra a estrutura completa simplificada
"""

# models.py
from django.db import models

class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo


# serializers.py
from rest_framework import serializers

class NotaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(max_length=200)
    conteudo = serializers.CharField()
    data_criacao = serializers.DateTimeField(read_only=True)


# views.py (usando ViewSet)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

# Banco em memória para exemplo
notas_db = []
contador_id = 1

class NotaViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(notas_db)
    
    def create(self, request):
        global contador_id
        nota = {
            "id": contador_id,
            "titulo": request.data.get("titulo"),
            "conteudo": request.data.get("conteudo"),
            "data_criacao": datetime.now().isoformat()
        }
        notas_db.append(nota)
        contador_id += 1
        return Response(nota, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        for nota in notas_db:
            if nota["id"] == int(pk):
                return Response(nota)
        return Response({"erro": "Nota não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        for i, nota in enumerate(notas_db):
            if nota["id"] == int(pk):
                notas_db[i].update({
                    "titulo": request.data.get("titulo", nota["titulo"]),
                    "conteudo": request.data.get("conteudo", nota["conteudo"])
                })
                return Response(notas_db[i])
        return Response({"erro": "Nota não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        for i, nota in enumerate(notas_db):
            if nota["id"] == int(pk):
                notas_db.pop(i)
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"erro": "Nota não encontrada"}, status=status.HTTP_404_NOT_FOUND)


# urls.py
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet

router = DefaultRouter()
router.register(r'notas', NotaViewSet, basename='nota')

urlpatterns = [
    path('', include(router.urls)),
]
"""
