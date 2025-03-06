#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webbrowser
import threading

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quick_start_01.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    def open_browser():
        webbrowser.open_new('http://127.0.0.1:8000')

    if 'runserver' in sys.argv:
        threading.Timer(1.25, open_browser).start()

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
