from Sample import Sample
#from matplotlib import pyplot


class Experiment:
    def __init__(self, minimum, maximum, size, maximum_thread_number, element_number):
        self.sample = Sample(minimum, maximum, size)
        self.maximum_thread_number = maximum_thread_number
        self.element_number = element_number

    def start_mean_experiment(self):
        durations = []
        for thread_number in range(1, self.maximum_thread_number + 1):
            mean, duration = self.sample.calculate_mean(thread_number, self.element_number)
            durations.append(duration)
        return durations

    def start_variance_experiment(self):
        durations = []
        for thread_number in range(1, self.maximum_thread_number + 1):
            variance, duration = self.sample.calculate_mean(thread_number, self.element_number)
            durations.append(duration)
        return durations
