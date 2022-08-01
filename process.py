from random import randint


class Process:
    id_counter = 5000

    def __init__(self, name, priority, bound_type):
        if type(priority) is not int:
            raise ValueError("Priority must be a integer between 1 and 4.")
        elif not 1 <= priority <= 4:
            raise ValueError("Priority must be a integer between 1 and 4.")
        elif bound_type != "io" and bound_type != "cpu":
            raise ValueError("Process Bound Type must be equal to 'io' or 'cpu'.")

        self.id = Process.id_counter
        Process.id_counter += 1

        self.name = name
        self.priority = priority
        self.bound_type = bound_type

        self.total_cpu_time = randint(1, 10)

    def __str__(self):
        return f'(id:{self.id}, nome:{self.name}, prioridade: {self.priority}, bound_type: {self.bound_type}, tempo de cpu total: {self.total_cpu_time})'
