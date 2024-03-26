from __future__ import absolute_import

from celery import Celery

app = Celery("myCeleryProj", include=["myCeleryProj.tasks"])

app.config_from_object("myCeleryProj.settings")


if __name__ == "__main__":
    app.start()
