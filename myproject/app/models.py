```python
from django.db import models

class RPCCommand(models.Model):
    command_name = models.CharField(max_length=200)
    command_description = models.TextField()

    def __str__(self):
        return self.command_name
```