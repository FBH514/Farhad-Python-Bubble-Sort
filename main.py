import random
import time

class Farhad:

    def __init__(self, length, high):
        """
        length: desired array length
        high: highest possible random number
        """
        self.length = length
        self.high = high

    def __repr__(self):
        return f"Sorted array of {self.length} random numbers, between 1 and {self.high}"

    def random_numbers(self):
        """List comprehension to generate random numbers"""
        arr = [random.randint(1, self.high) for _ in range(self.length)]
        return arr

    @staticmethod
    def sort_numbers(arr):
        """Sorts the array using the bubble sort algorithm"""
        length = len(arr)
        for outer in range(length):             # outer loop takes the lead
            for inner in range(outer):          # inner loop trails against the outer loop
                if arr[inner] > arr[outer]:     # is the trailing value larger than the leading value?
                    placeholder = arr[outer]    # if true save the smallest value for later
                    arr[outer] = arr[inner]     # swap the smaller leading value at trailing position
                    arr[inner] = placeholder    # swap the larger trailing value at leading position
        return arr

    def print_numbers(self):
        """Prints the sorted array"""
        print(self.sort_numbers(self.random_numbers()))

    def main(self):
        """Main function"""
        print(self.__repr__())
        self.print_numbers()
        print(f"Time Elapsed –> {time.perf_counter()}s")


if __name__ == "__main__":
    farhad = Farhad(20, 100)
    farhad.main()


