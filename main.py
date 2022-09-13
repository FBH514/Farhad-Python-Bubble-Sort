import random
import time

class BubbleSort:

    def __init__(self, length: int, largest: int):
        """
        BubbleSort class constructor
        length: desired array length
        high: highest possible random number
        """
        self.length = length
        self.largest = largest

    def __repr__(self) -> str:
        """Returns a formatted string with constructor parameter values"""
        return f"Sorted array of {self.length} random numbers, between 1 and {self.largest}"

    def random_numbers(self) -> list:
        """List comprehension to generate random numbers"""
        return [random.randint(1, self.largest) for _ in range(self.length)]

    @staticmethod
    def sort_numbers(arr: list) -> list:
        """
        Sorts the array using the bubble sort algorithm

        An outer loop leads iteration over the array while a nested loop trails behind
        so that comparison is made between the leading and trailing values. When the trailing (preceding) value is
        higher than the leading value, the placeholder reference is assigned to the trailing value so that
        it may be remembered the last step of the swapping process. The (lesser) leading value is then
        assigned to the preceding (trailing) index. Its ensuing index assigns the placeholder reference
        with the higher value and swap is done. This is repeated until the array is sorted, ascendingly in this case
        """
        for outer in range(len(arr)):           # outer loop takes the lead
            for inner in range(outer):          # inner loop trails against the outer loop
                if arr[inner] > arr[outer]:     # is the trailing value larger than the leading value?
                    placeholder = arr[outer]    # if true save the smallest value for later
                    arr[outer] = arr[inner]     # swap the smaller leading value at trailing position
                    arr[inner] = placeholder    # swap the larger trailing value at leading position
        return arr

    @staticmethod
    def print_numbers(arr: list) -> None:
        """Prints the sorted array"""
        print(arr)

    def main(self) -> None:
        """
        Main function to run the program.
        Control flow checks for valid input and raises exceptions based on 2 categories:
        1. TypeError when parameters are not integers
        2. ValueError when parameters are not positive or greater than 1

        If input is valid, an informative message is printed to the console and the program proceeds to generate a
        random array of numbers, sort the array and print the sorted array to the console.

        A timer is used to measure the program's performance.
        """
        print()
        if type(self.length) or type(self.largest) != int:
            if type(self.length) and type(self.largest) != int:
                raise TypeError("Length and largest parameters must be integers")
            elif type(self.length) != int:
                raise TypeError("Length parameter must be an integer")
            elif type(self.largest) != int:
                raise TypeError("Largest parameter must be an integer")
        if not self.length > 1 or not self.largest > 1:
            if self.length <= 1:
                raise ValueError("Length parameter must be greater than 1")
            else:
                raise ValueError("Largest parameter must be greater than 1")
        print(self.__repr__())
        print()
        self.print_numbers(self.sort_numbers(self.random_numbers()))
        print(f"Time Elapsed –> {time.perf_counter()}s")


if __name__ == "__main__":
    bubble_sort = BubbleSort(20, 100)
    bubble_sort.main()
