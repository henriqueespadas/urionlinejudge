"""The formula to calculate the area of a circumference is defined as A = π . R2.
Considering to this problem that π = 3.14159:
Calculate the area using the formula given in the problem description.
Input
The input contains a value of floating point (double precision), that is the variable R.
Output
Present the message "A=" followed by the value of the variable, as in the example bellow,
with four places after the decimal point. Use all double precision variables. Like all the problems,
don't forget to print the end of line after the result, otherwise you will receive "Presentation Error"."""

# radio = float(input())
# pi = 3.14159
# area = pi * (radio ** 2)
# print(f"A={area:.4f}")


def area(radio: float) -> float:
    pi = 3.14159
    total = pi * (radio ** 2)
    return round(total, 4)


# assert area(2.00) == 12.5664
# assert area(100.64) == 31819.3103
# assert area(150.00) == 70685.7750
