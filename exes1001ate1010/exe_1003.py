"""Read two integer values.
After this, calculate the product between them and store the result in a variable named PROD.
Print the result like the example below. Do not forget to print the end of line after the result,
otherwise you will receive “Presentation Error”.
Input
The input file contains 2 integer numbers.
Output
Print the message "PROD" and PROD according to the following example,
with a blank space before and after the equal signal."""

# A = int(input())
# B = int(input())
# PROD = A * B
# print(f'PROD = {PROD}')


def product(a: int, b: int) -> int:
    total = a * b
    return total



# assert product(3, 9) == 27
# assert product(-30, 10) == -300
# assert product(0, 9) == 0
