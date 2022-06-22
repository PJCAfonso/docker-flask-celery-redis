import os
import time
from celery import Celery

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://redis:11522'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND',
                                       'redis://redis:11522')
print(CELERY_RESULT_BACKEND, CELERY_BROKER_URL)

celery = Celery('bipas',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)


@celery.task(name='bipas.add')
def add(x: int, y: int) -> int:
    time.sleep(5)
    return x + y


@celery.task(name='bipas.block')
def block(ip: list) -> dict:
    """block a list of parameters received

    Parameters
    ----------
    ip : str or list

    Returns
    -------
    result : dict
    """

    body = {"status": "sucess", "data": [], "errors": ""}
    if not isinstance(ip, list) and not isinstance(ip, str):
        body["status"] = "bad"
        body["errors"] = f"{ip} must be a list or string!"
    else:
        body["data"] = ip
    print(body)

    return body
