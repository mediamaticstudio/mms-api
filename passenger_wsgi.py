import os
import sys

PROJECT_DIR = os.path.dirname(__file__)

# Add project to path
sys.path.insert(0, PROJECT_DIR)

# Add venv site-packages to path
sys.path.insert(
    0,
    os.path.join(PROJECT_DIR, 'venv', 'lib', 'python3.9', 'site-packages')
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mmsproject.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
