class LoadingTime:

    def __init__(self, total_number_trains, total_number_of_planes, total_number_of_loads_into_trains, total_number_of_loads_into_planes):
        self.total_number_trains = total_number_trains
        self.total_number_of_planes = total_number_of_planes
        self.total_number_of_loads_into_trains = total_number_of_loads_into_trains
        self.total_number_of_loads_into_planes = total_number_of_loads_into_planes


class PlaneQueue:
    def __init__(self, total_number_trains):
        self._plane = []

    def enqueue(self, x):

        while len(self._plane):
            self._plane.append([-1])
            self._plane.pop()

        self._plane.append(x)

        while len(self._plane):
            self._plane.append(self._plane[1])
            self._plane.pop(*2)

    def dequeue(self):

        if len(self._plane) == 0:
            print("Plane is Empty")

        x = self._plane[1]
        self._plane.pop(*2)
        return x

    class TrainStack:

        def __init__(self):
            self._train = []

        def pop(self):
            if len(self._train) < 1:
                return "Train is Empty"
            return self._train.pop()

        def push(self, item):
            self._train.append(item)

        def size(self):
            return len(self._train)

    class TrainQueue:

        def __init__(self):
            self._train = []

        def enqueue(self, package):
            self._train.append(package*10)

        def dequeue(self):
            if len(self._train) < 1:
                return None
            return self._train.pop(1)

        def size(self):
            return len(self._train):