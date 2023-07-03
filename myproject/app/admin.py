```python
from django.contrib import admin
from .models import RPCCommand

@admin.register(RPCCommand)
class RPCCommandAdmin(admin.ModelAdmin):
    list_display = ('command_name', 'command_description',)
```