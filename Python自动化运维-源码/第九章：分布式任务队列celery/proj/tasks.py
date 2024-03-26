from __future__ import absolute_import

from proj.celery import app
import time

@app.task
def add(x, y):
    time.sleep(3)
    print(f"x+y={x+y}")
    return x + y
