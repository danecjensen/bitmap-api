```python
from django.urls import path
from . import views

urlpatterns = [
    path('rpc/', views.RPCView.as_view(), name='rpc'),
]
```