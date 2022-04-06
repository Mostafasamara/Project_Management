# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Project , Task
from .serializers import ProjectSerializer , TaskSerializer


## Authentication






class ProjectListApiView(APIView):

    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        project = Project.objects.filter(user = request.user.id)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'project_name': request.data.get('project_name'),
            'created_at': request.data.get('created_at'),
            'user': request.user.id
        }
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, project_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Project.objects.get(id=project_id, user = user_id)
        except Project.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, project_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        project_instance = self.get_object(project_id, request.user.id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProjectSerializer(project_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, project_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        project_instance = self.get_object(project_id, request.user.id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'project_name': request.data.get('project_name'),
            'created_at': request.data.get('created_at'),
            'user': request.user.id
        }
        serializer = ProjectSerializer(instance = project_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, project_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        project_instance = self.get_object(project_id, request.user.id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        project_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class TaskListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        task = Task.objects.filter(user = request.user.id)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'task_name': request.data.get('task_name'),
            'project' : request.data.get('project'),
            'created_at': request.data.get('created_at'),
            'start_date' : request.data.get('start_date'),
            'end_date' : request.data.get('end_date'),
            'desc' : request.data.get('desc'),
            'user': request.user.id
        }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, task_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Task.objects.get(id=task_id, user = user_id)
        except Task.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, task_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        task_instance = self.get_object(task_id, request.user.id)
        if not task_instance:
            return Response(
                {"res": "Object with task id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TaskSerializer(task_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, task_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        task_instance = self.get_object(task_id, request.user.id)
        if not task_instance:
            return Response(
                {"res": "Object with task id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
                'task_name': request.data.get('task_name'),
                'project' : request.data.get('project'),
                'created_at': request.data.get('created_at'),
                'start_date' : request.data.get('start_date'),
                'end_date' : request.data.get('end_date'),
                'desc' : request.data.get('desc'),
                'user': request.user.id
        }
        serializer = TaskSerializer(instance = task_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, task_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        task_instance = self.get_object(task_id, request.user.id)
        if not task_instance:
            return Response(
                {"res": "Object with task id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        task_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
