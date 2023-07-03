```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .serializers import CommandSerializer
from .models import Command
import json

@csrf_exempt
@require_POST
def rpc_api(request):
    data = json.loads(request.body)
    serializer = CommandSerializer(data=data)
    if serializer.is_valid():
        command = Command.objects.get(name=serializer.validated_data['name'])
        result = command.execute(serializer.validated_data['params'])
        return JsonResponse({'result': result})
    else:
        return JsonResponse(serializer.errors, status=400)
```