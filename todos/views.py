import json
from django.shortcuts import render
from django.views.generic import View
from .models import Todo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

def todo_instance_to_dictionary(todo):
  """
  장고 단일 모델 인스턴스, 혹은 쿼리셋을 파이썬 딕셔너리로 변환하는 헬퍼 함수
  """
  result = {}
  result["id"] = todo.id
  result["text"] = todo.text
  result["done"] = todo.done
  
  return result

class TodoListView(View):
  def get(self, request):
    try:
      todo_list = []
      todo_queryset = Todo.objects.all()
      for todo_instance in todo_queryset:
        todo_list.append(todo_instance_to_dictionary(todo_instance))
      data = { "todos": todo_list }
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to get todos"}, status=404)


class TodoCreateView(View):
  ### CBV에서 csrf를 우회하기 위한 방법
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super(TodoCreateView, self).dispatch(request, *args, **kwargs)

  def post(self, request):
    try:
      params = json.loads(request.body)
    except:
      return JsonResponse({"msg": "Invalid parameters"}, status=403)

    try:
      todo_instance = Todo.objects.create(text=params["text"])
      todo_dict = todo_instance_to_dictionary(todo_instance)
      data = { "todo": todo_dict }
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to create todos"}, status=404)


class TodoView(View):
    ### CBV에서 csrf를 우회하기 위한 방법
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super(TodoView, self).dispatch(request, *args, **kwargs)

  def get(self, request, id):
    try:
      todo_instance = Todo.objects.get(id=id)
      todo_dict = todo_instance_to_dictionary(todo_instance)
      data = { "todo": todo_dict }
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to edit todo"}, status=404)

  def put(self, request, id):
    try:
      params = json.loads(request.body)
    except:
      return JsonResponse({"msg": "Invalid parameters"}, status=403)

    try:
      todo_instance = Todo.objects.get(id=id)
      todo_instance.text = params["text"]
      todo_instance.save()
      todo_dict = todo_instance_to_dictionary(todo_instance)
      data = { "todo": todo_dict }
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to edit todo"}, status=404)
  
  def delete(self, request, id):
    try:
      todo_instance = Todo.objects.get(id=id)
      todo_dict = todo_instance_to_dictionary(todo_instance)
      todo_instance.delete()
      data = { "todo": todo_dict }
      return JsonResponse(data,status=200)
    except:
      return JsonResponse({"msg": "Failed to delete todo"}, status=404)