import random
import time
import ThreadPool


class Sample:
    def __init__(self, minimum, maximum, size):
        self.minimum = minimum
        self.maximum = maximum
        self.size = size
        self.elements = [random.randint(self.minimum, self.maximum) for _ in range(self.size)]

    def calculate_sum(self, power, initial, element_number, auxiliary):
        try:
            sum = 0
            for index in range(initial, initial + element_number):
                sum += self.elements[index] ** power
        except IndexError:
            pass
        auxiliary.append(sum)

    def calculate_mean(self, thread_number, element_number):
        initial = 0
        start_time = time.time()
        thread_pool = ThreadPool.ThreadPool(thread_number)
        auxiliary = []
        while initial < self.size:
            thread_pool.push((self.calculate_sum, [1, initial, element_number, auxiliary]))
            initial += element_number
        thread_pool.complete()
        end_time = time.time()
        return sum(auxiliary) / self.size, end_time - start_time

    def calculate_variance(self, thread_number, element_number):
        initial = 0
        start_time = time.time()
        thread_pool = ThreadPool.ThreadPool(thread_number)
        auxiliary = []
        while initial < self.size:
            thread_pool.push((self.calculate_sum, [2, initial, element_number, auxiliary]))
            initial += element_number
        thread_pool.complete()
        end_time = time.time()
        return sum(auxiliary) / self.size - self.calculate_mean(thread_number, element_number)[0] ** 2, end_time - \
               start_time
