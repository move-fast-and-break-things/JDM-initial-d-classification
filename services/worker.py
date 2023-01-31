import asyncio
from multiprocessing import Process, Manager, Queue, Lock
from pydantic import BaseModel, Field
from typing import Callable, List, Dict, Any
from uuid import UUID, uuid4


class TaskModel(BaseModel):
    task: Callable
    args: List
    kwargs: Dict
    id: UUID = Field(default_factory=uuid4)


class TaskOutput(BaseModel):
    data: Any = None
    id: UUID = None


class Worker(Process):
    def __init__(self, input_queue, output_list):
        Process.__init__(self)
        self.input_queue = input_queue
        self.output_list = output_list
        self.daemon = True

        self.lock_process = Lock()

    def run(self):
        while True:
            item: TaskModel = self.input_queue.get()

            if item is not None:
                result = None
                result = item.task(*item.args, **item.kwargs)

                output = TaskOutput(data=result, id=item.id)
                self.lock_process.acquire()
                self.output_list[item.id] = output
                self.lock_process.release()


class TaskQueue:
    def __init__(self):
        self.manager = Manager()
        self.output_list = self.manager.dict()
        self.input_queue = Queue()

        self.lock_process = Lock()

        self.worker = Worker(self.input_queue, self.output_list)
        self.worker.start()

    async def task_delay(self, task: Callable, args: List = [], kwargs: Dict = {}):
        task_obj = TaskModel(task=task, args=args, kwargs=kwargs)
        task_id = task_obj.id
        self.input_queue.put(task_obj)
        task_result = None

        while True:
            await asyncio.sleep(5)
            self.lock_process.acquire()

            if task_id in self.output_list.keys():
                task_output: TaskOutput = self.output_list.pop(task_id)
                task_result = task_output.data
            self.lock_process.release()
            if task_result:
                return task_result
