workers = 1
keepalive = 180
timeout = 180

#bind = 'localhost:8000'
bind = '0.0.0.0:8002'

worker_class = 'uvicorn.workers.UvicornWorker'
