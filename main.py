import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
    from django.core.management import execute_from_command_line

    args = ['name', 'runserver', '127.0.0.1:8000']
    execute_from_command_line(args)
