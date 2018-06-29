from kombu.common import Broadcast


class CeleryConf:
    # List of modules to import when celery starts.
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_IMPORTS = ('main.tasks')
    CELERY_QUEUES = (Broadcast('q1'),)
    CELERY_ROUTES = {
        'tasks.sampletask': {'queue': 'q1'}
    }