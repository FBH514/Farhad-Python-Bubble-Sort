# Python Bubble Sort Algorithm
> by [François Boulay-Handfield](https://github.com/FBH514)
> 
> Github Repository: [https://github.com/FBH514/Farhad-Python-Bubble-Sort](https://github.com/FBH514/Farhad-Python-Bubble-Sort) 

## Overview
>This is a simple Python implementation of the bubble sort algorithm. 
> 
> User defines array length and largest possible random number. Program sorts the array <ins>ascendingly</ins>. 

## Constructor
>```length``` is the length of the array to be sorted.   
```largest``` is the largest possible random number in the array.

## Methods
>## \__repr__(self) -> str
>Takes no parameters and returns a formatted ```string``` with constructor parameter values.  

>## random_numbers(self) -> list  
> Takes no parameters and returns a ```list``` comprehension of size ```length``` with random numbers up to ```largest```.
 
>## sort_numbers(self, list) -> list
> Takes an ```list``` as a parameter and returns a sorted ```list``` using the bubble sort algorithm.
> > ##### How does it work?
> >An outer loop leads iteration over the array while a nested loop trails behind so that comparison is made between the leading and trailing values. When the trailing (preceding) value is higher than the leading value, the placeholder reference is assigned to the trailing value so that it may be remembered the last step of the swapping process. The (lesser) leading value is then assigned to the preceding (trailing) index. Its ensuing index assigns the placeholder reference with the higher value and swap is done. This is repeated until the array is sorted, ascendingly in this case.
 
>## print_numbers(self, list) -> None
> Takes a ```list``` as a parameter and prints the ```list```.
 
>## main(self) -> None
> Takes no parameters and runs the program in an orderly fashion.  
> 
> Control flow checks for valid input and raises exceptions based on 2 categories:  
>1. ```TypeError``` when parameters are not integers
>2. ```ValueError``` when parameters are not positive or greater than 1
>
>If input is valid, an informative message is printed to the console and the program proceeds to generate a
random array of numbers, sort the array and print the sorted array to the console. 
> 
> ```time.perf_counter()``` is called to measure the program's performance.