import unittest
from Day1_Assignment import *


class TestFunction(unittest.TestCase):
    def test_greater(self):   # Q1 testing
        self.assertAlmostEqual(greater(67, -84, 12), 67)
        self.assertAlmostEqual(greater(-67, -84, -12), -12)
        self.assertAlmostEqual(greater(67, 84, 12), 84)
        self.assertAlmostEqual(greater(0, -84, -12), 0)

    def test_armstrong(self):   # Q2 testing
        self.assertEqual(armstrong(153), 'yes')
        self.assertEqual(armstrong(134), 'no')

    def test_result(self):   # Q3 testing
        self.assertEqual(result(153), ('reverse is', 351, 'sum is', 9))
        self.assertEqual(result(674), ('reverse is', 476, 'sum is', 17))

    def test_hcf(self):   # Q4 testing
        self.assertAlmostEqual(hcf(3, 5), 1)
        self.assertAlmostEqual(hcf(5, 15), 5)

    def test_lcm(self):   # Q5 testing
        self.assertAlmostEqual(lcm(3, 5), 15)
        self.assertAlmostEqual(lcm(15, 30), 30)

    def test_leap_year(self):   # Q6 testing
        self.assertEqual(leap(2016), 'yes')
        self.assertEqual(leap(2013), 'no')

    def test_type_of_triangle(self):   # Q7 testing
        self.assertEqual(typeOfTriangle(2, 4, 5), 'Scalene triangle')
        self.assertEqual(typeOfTriangle(3, 5, 3), 'isosceles triangle')
        self.assertEqual(typeOfTriangle(5, 5, 5), 'equilateral triangle')
        self.assertEqual(typeOfTriangle(5, 4, 3), 'right angle triangle')

    def test_quadrant(self):   # Q9 testing
        self.assertEqual(findQuadrant(2, 3), 'first quadrant')
        self.assertEqual(findQuadrant(-2, 3), 'second quadrant')
        self.assertEqual(findQuadrant(-2, -3), 'third quadrant')
        self.assertEqual(findQuadrant(2, -3), 'fourth quadrant')
        self.assertEqual(findQuadrant(2, 0), 'on line')
        self.assertEqual(findQuadrant(0, 3), 'on line')
        self.assertEqual(findQuadrant(0, 0), 'center')

    def test_addition(self):   # Q10 testing addition
        self.assertAlmostEqual(addition(-4, 6), 2)
        self.assertAlmostEqual(addition(-4, -6), -10)
        self.assertAlmostEqual(addition(4, -6), -2)
        self.assertAlmostEqual(addition(4, 6), 10)

    def test_subtraction(self):   # Q10 testing subtraction
        self.assertAlmostEqual(subtraction(3, 6), -3)
        self.assertAlmostEqual(subtraction(13, 6), 7)
        self.assertAlmostEqual(subtraction(-3, -6), 3)
        self.assertAlmostEqual(subtraction(3, -6), 9)

    def test_multiplication(self):   # Q10 testing multiplication
        self.assertAlmostEqual(multiplication(4, 6), 24)
        self.assertAlmostEqual(multiplication(-4, -6), 24)
        self.assertAlmostEqual(multiplication(4, -6), -24)
        self.assertAlmostEqual(multiplication(-4, 0), 0)

    def test_division(self):   # Q10 testing division
        self.assertAlmostEqual(division(7, 5), 1.4)
        self.assertAlmostEqual(division(6, 3), 2)
        self.assertAlmostEqual(division(-7, 5), -1.4)
        self.assertAlmostEqual(division(7, -5), -1.4)

    def test_modulus(self):   # Q10 testing modulus
        self.assertAlmostEqual(modulus(7, 5), 2)
        self.assertAlmostEqual(modulus(-7, -5), -2)
        self.assertAlmostEqual(modulus(-7, 5), 3)
        self.assertAlmostEqual(modulus(7, -5), -3)

    def test_floor_division(self):   # Q10 testing floor division
        self.assertAlmostEqual(floorDivision(34, 6), 5)
        self.assertAlmostEqual(floorDivision(7, 5), 1)
        self.assertAlmostEqual(floorDivision(-34, 6), -6)
        self.assertAlmostEqual(floorDivision(34, -6), -6)

    def test_power(self):   # Q10 testing power
        self.assertAlmostEqual(power(5, 3), 125)
        self.assertAlmostEqual(power(2, 5), 32)
        self.assertAlmostEqual(power(-2, 3), -8)
        self.assertAlmostEqual(power(2, -5), 0.03125)

    def test_fibonacci(self):   # Q11 testing fibonacci
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])

    def test_tribonacci(self):   # Q11 testing tribonacci
        self.assertEqual(tribonacci(5), [0, 0, 1, 1, 2])

    def test_factorial(self):   # Q12 testing factorial
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(0), 1)

    def test_sum_of_factors(self):   # Q13 testing sum of factors
        self.assertEqual(sumOfFactors(5), 1)
        self.assertEqual(sumOfFactors(55), 17)
        self.assertEqual(sumOfFactors(905), 187)

    def test_character_check(self):   # Q14 testing character check
        self.assertEqual(vowelCheck('y'), 'consonant')
        self.assertEqual(vowelCheck('O'), 'vowel')

    def test_digital_sum(self):   # Q15 testing digital sum
        self.assertEqual(digitalRoot(2345), 5)

    def test_prime(self):   # Q16 prime no
        self.assertEqual(prime(4, 89), [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89])

    def test_sum_of_triangular_no(self):   # Q17 sum of triangular no
        self.assertEqual(sumOfTriangularNo(14), 560)

    def test_max_number(self):   # Q18 maximum number after deleting one digit
        self.assertEqual(maxNumber(8769), 879)

    def test_no_of_matches(self):   # Q20 no of matches of teams with each other
        self.assertEqual(noOfMatch(10), 45)

    def test_super_prime(self):   # Q19 super prime
        self.assertEqual(superPrimes(241), [3, 5, 11, 17, 31, 41, 59, 67, 83, 109, 127, 157, 179, 191, 211, 241])


if 'name' == '__main__':
    unittest.main()
