"""Read two integer values. After this, calculate the product between them and store the result in a variable named
PROD.
Print the result like the example below. Do not forget to print the end of line after the result, otherwise you will
 receive “Presentation Error”.
Input
The input file contains 2 integer numbers.
Output
Print the message "PROD" and PROD according to the following example, with a blank space before and after the equal
signal."""


def simple_product(num1: int, num2: int) -> int:
    num1 = int(input())
    num2 = int(input())
    total = num1 * num2
    return total


# num1 = int(input())
# num2 = int(input())
# total = (num1 * num2)
# print(f'PROD = {total}')
