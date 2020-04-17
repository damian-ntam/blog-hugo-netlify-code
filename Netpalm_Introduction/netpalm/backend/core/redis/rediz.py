from redis import Redis
import redis
from rq import Queue, Connection, Worker
from rq.job import Job
import json
from multiprocessing import Process
from rq.registry import StartedJobRegistry, FinishedJobRegistry, FailedJobRegistry

from backend.core.routes import routes
from backend.core.redis.rediz_workers import nodeworker
from backend.core.redis.rediz_workers import nodeworkerconstructor
from backend.core.confload.confload import config

class rediz:

    def __init__(self):

        #globals
        self.server = config().redis_server
        self.port = config().redis_port
        self.ttl = config().redis_task_ttl
        self.timeout = config().redis_task_timeout
        self.routes = routes.routes
        self.core_q = config().redis_core_q
        self.base_connection = Redis(self.server, self.port)
        self.base_q = Queue(self.core_q, connection=self.base_connection)
        self.queuedb = {}

    def getqueue(self, host):
        result = self.queuedb.get(host, False)
        return result

    def create_queue_worker(self, qname):
        try:
            self.base_q.enqueue_call(func=nodeworkerconstructor, args=(qname,), ttl=self.ttl)
            self.queuedb[qname] = {}
            self.queuedb[qname]["queue"] = Queue(qname, connection=self.base_connection)
            return self.queuedb[qname]["queue"]
        except Exception as e:
            return e

    def check_and_create_q_w(self, hst):
        try:
            qexists = self.getqueue(hst)
            if not qexists:
                self.create_queue_worker(hst)
        except Exception as e:
            return e

    def sendtask(self, q, exe, **kwargs):
        try:
            task = self.queuedb[q]["queue"].enqueue_call(func=self.routes[exe], description=q, ttl=self.ttl, kwargs=kwargs["kwargs"], timeout=self.timeout)
            resultdata = {
                    'status': 'success',
                    'data': {
                        'task_id': task.get_id(),
                        'created_on': task.created_at,
                        'task_queue': q,
                        'task_status': task.get_status(),
                        'task_result': task.result
                    }
            }
            return resultdata
        except Exception as e:
            return e
            
    def fetchtask(self, task_id):
        try:
            task = Job.fetch(task_id, connection=self.base_connection)
            if task:
                response_object = {
                    'status': 'success',
                    'data': {
                        'task_id': task.get_id(),
                        'created_on': task.created_at,
                        'task_queue': task.description,
                        'task_status': task.get_status(),
                        'task_result': task.result,
                    }
                }
            return response_object
        except Exception as e:
            return e

    def getjoblist(self, q):
        try:
            # if single host lookup
            if q:
                qexists = self.queuedb.get(q, False)
                if qexists:
                    t = self.queuedb[q]["queue"].get_job_ids()
                    if t:
                        response_object = {
                            'status': 'success',
                            'data': {
                                'task_id': t
                            }
                        }
                        return response_object
                    else:
                        return False
                else:
                    return False
            #multi host lookup
            elif not q:
                for i in self.queuedb:
                    task = self.queuedb[i]["queue"].get_job_ids()
                response_object = {
                    'status': 'success',
                    'data': {
                        'task_id': task
                    }
                }
                return response_object
        except Exception as e:
            return e

    def getjobliststatus(self, q):
        try:
            if q:
                task = self.queuedb[q]["queue"].get_job_ids()
                response_object = {
                    'status': 'success',
                    'data': {
                        'task_id': []
                    }
                }
                #get startedjobs
                startedjobs = self.getstartedjobs(self.queuedb[q]["queue"])
                for job in startedjobs:
                    task.append(job)

                #get finishedjobs
                finishedjobs = self.getfinishedjobs(self.queuedb[q]["queue"])
                for job in finishedjobs:
                    task.append(job)

                #get failedjobs
                failedjobs = self.getfailedjobs(self.queuedb[q]["queue"])
                for job in failedjobs:
                    task.append(job)

                if task:
                    for job in task:
                        try:
                            jobstatus = Job.fetch(job, connection=self.base_connection)
                            jobdata = {
                            'task_id': jobstatus.get_id(),
                            'created_on': jobstatus.created_at,
                            'task_status': jobstatus.get_status(),
                            'task_queue': jobstatus.description,
                            'task_result': jobstatus.result,
                            }
                            response_object["data"]["task_id"].append(jobdata)
                        except Exception as e:
                            return e
                            pass
                return response_object
        except Exception as e:
            return e

    def getstartedjobs(self, q):
        try:
            registry = StartedJobRegistry(q, connection=self.base_connection)
            response_object = registry.get_job_ids()
            return response_object
        except Exception as e:
            return e

    def getfinishedjobs(self, q):
        try:
            registry = FinishedJobRegistry(q, connection=self.base_connection)
            response_object = registry.get_job_ids()
            return response_object
        except Exception as e:
            return e

    def getfailedjobs(self, q):
        try:
            registry = FailedJobRegistry(q, connection=self.base_connection)
            response_object = registry.get_job_ids()
            return response_object
        except Exception as e:
            return e