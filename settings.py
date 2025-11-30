import os
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql',
 'NAME': os.getenv('DB_NAME', 'myapp'),
 'USER': os.getenv('DB_USER', 'postgres'),
 'PASSWORD': os.getenv('DB_PASSWORD', ''),
 'HOST': os.getenv('DB_HOST', 'localhost'),
 'PORT': os.getenv('DB_PORT', '5432'),
 }
}
# Для демонстрации балансировки - выводим hostname pod'а
import socket
def get_hostname():
  return socket.gethostname()
