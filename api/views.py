from rest_framework import generics, permissions
from todo import serializers
from todo.models import Todo

class TodoCompletedList(generics.ListAPIView):
    serializer_class = serializers.TodoSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        Todo.objects.filter(user=user, datecomplete__isnull=False)
