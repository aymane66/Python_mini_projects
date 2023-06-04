"""
when Amal was born, her father opened a bank account for her.
On each anniversary, her father transfers 500 MAD to her account
in addition to an amount equal to triple her age.

For example, when she is 4 years old, she would receive:
        500 MAD + (4 * 3) MAD = 512 MAD.
        and her bank balance would be 2030 MAD
"""

age = input("Age: ")

try:
    age = int(age)
    s = 0
    for i in range(1, age + 1):
        s += 500 + (i * 3)
    print(f"Balance: {s} MAD")

except ValueError:
    print("Invalid input! ")