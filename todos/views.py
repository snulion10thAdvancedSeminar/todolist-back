import json
from django.views.generic import View
from .models import Todo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def todo_instance_to_dictionary(todo):
  """
  장고 단일 모델 인스턴스, 혹은 쿼리셋을 파이썬 딕셔너리로 변환하는 헬퍼 함수
  """
  result = {}
  result["id"] = todo.id
  result["text"] = todo.text
  result["done"] = todo.done
  return result

class ViewWithoutCSRFAuthentication(View):
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super(ViewWithoutCSRFAuthentication, self).dispatch(request, *args, **kwargs)

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

class TodoCreateView(ViewWithoutCSRFAuthentication):
  def post(self, request):
    try:
      body = json.loads(request.body) #body에서 받아온 것을 역직렬화!
    except:
      return JsonResponse({"msg": "Invalid parameters"}, status=400)

    try:
      todo_instance = Todo.objects.create(text=body["text"])
    except:
      return JsonResponse({"msg": "Failed to create todos"}, status=400)

    todo_dict = todo_instance_to_dictionary(todo_instance)
    data = { "todo": todo_dict }
    return JsonResponse(data, status=200)

class TodoCheckView(ViewWithoutCSRFAuthentication):
  def patch(self, request, id):
    try:
      todo_instance = Todo.objects.get(id=id)
      todo_instance.check_todo()
      todo_dict = todo_instance_to_dictionary(todo_instance)
      data = { "todo": todo_dict }
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to create todos"}, status=400)

class TodoView(ViewWithoutCSRFAuthentication):
  def get(self, request, id):
    try:
      todo_instance = Todo.objects.get(id=id)
      todo_dict = todo_instance_to_dictionary(todo_instance)
      data = { "todo": todo_dict }
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to edit todo"}, status=404)

  def patch(self, request, id):
    try:
      body = json.loads(request.body)
    except:
      return JsonResponse({"msg": "Invalid parameters"}, status=400)

    try:
      todo_instance = Todo.objects.get(id=id)
      todo_instance.text = body["text"]
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
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to delete todo"}, status=404)
