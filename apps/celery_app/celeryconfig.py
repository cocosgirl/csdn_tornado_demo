CELERY_RESULT_BACKEND = 'redis://root:teset@test.com:6379/10'  # 指定 Backend
CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'

CELERY_IMPORTS = (
    "apps.demo.service.asynchronous.AsynchronousService",
)
