import queue
import threading
import time


class ThreadPool:
    def __init__(self, thread_number):
        self.tasks = queue.Queue()
        self.threads = []
        self.is_working = True
        for _ in range(thread_number):
            thread = threading.Thread(target=self.perform_task)
            thread.start()
            self.threads.append(thread)

    def push(self, task):
        self.tasks.put(task)

    def perform_task(self):
        while self.is_working or not self.tasks.empty():
            try:
                task = self.tasks.get_nowait()
                function = task[0]
                arguments = task[1]
                function(*arguments)
            except queue.Empty:
                time.sleep(1)
                continue

    def complete(self):
        self.is_working = False
        for thread in self.threads:
            thread.join()
