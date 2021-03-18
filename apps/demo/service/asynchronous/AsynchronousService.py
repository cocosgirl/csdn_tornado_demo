
from apps.celery_app import app
from apps.demo.service.detail.ComplexService import ComplexService


@app.task
def async_split_complex(**kwargs):
    complexservice = ComplexService()
    complexservice.split_complex(**kwargs)


@app.task
def async_merge_complex(**kwargs):
    complexservice = ComplexService()
    complexservice.merge_complex(**kwargs)
