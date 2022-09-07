import random
import time

class Farhad:

    def __init__(self, length, high):
        self.length = length
        self.high = high

    def __repr__(self):
        return f"{self.length} numbers, between 1 and {self.high}"

    def random_numbers(self):
        arr = [random.randint(1, self.high) for _ in range(self.length)]
        return arr

    @staticmethod
    def sort_numbers(arr):
        length = len(arr)
        for outer in range(length):
            for inner in range(outer):
                if arr[inner] > arr[outer]:
                    placeholder = arr[outer]
                    arr[outer] = arr[inner]
                    arr[inner] = placeholder
        return arr

    def print_numbers(self):
        print(self.sort_numbers(self.random_numbers()))

    def main(self):
        print(self.__repr__())
        self.print_numbers()
        print(f"Time Elapsed –> {time.perf_counter()}s")


if __name__ == "__main__":
    farhad = Farhad(20, 100)
    farhad.main()


