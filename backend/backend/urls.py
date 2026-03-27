from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
import os

def serve_frontend(request):
    """Serve the frontend index.html when visiting http://127.0.0.1:8000/"""
    frontend_path = os.path.join(settings.BASE_DIR, '..', '..', 'frontend', 'index.html')
    frontend_path = os.path.normpath(frontend_path)
    try:
        with open(frontend_path, 'r', encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='text/html')
    except FileNotFoundError:
        return HttpResponse(
            "<h2 style='font-family:sans-serif;padding:40px'>"
            "✅ MediCore Backend is running!<br><br>"
            "<small style='color:#666'>Open <code>frontend/index.html</code> in your browser, "
            "or visit <a href='/api/records/'>/api/records/</a></small></h2>"
        )

urlpatterns = [
    path('', serve_frontend, name='frontend'),
    path('admin/', admin.site.urls),
    path('api/records/', include('records.urls')),
    path('api/billing/', include('billing.urls')),
]
