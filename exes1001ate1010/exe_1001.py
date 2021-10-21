"""Read 2 variables, named A and B and make the sum of these two variables,
assigning its result to the variable X. Print X as shown below.
Print endline after the result otherwise you will get “Presentation Error”.

Input
The input file will contain 2 integer numbers.

Output
Print the letter X (uppercase) with a blank space before and after the equal
signal followed by the value of X, according to the following example.

Obs.: don't forget the endline after all."""
# A = int(input())
# B = int(input())
# X = A + B
#
# print(f'X = {X}')


def soma(a: int, b: int) -> int:
    x = a + b
    return x


# assert soma(10, 9) == 19
# assert soma(-10, 4) == -6
# assert soma(15, -7) == 8
