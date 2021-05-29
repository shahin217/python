import unittest
from Day3_Assignment import *


class TestFunction(unittest.TestCase):
    def test_formatting_time(self):   # Q1
        self.assertEqual(formatting_time('5:70:65'), '6:11:5')
        self.assertEqual(formatting_time('12:75:58'), '13:15:58')

    def test_formatting_date(self):   # Q2
        self.assertEqual(formatting_date('45/8/2018'), '14/9/2018')
        self.assertEqual(formatting_date('45/12/2020'), '14/1/2021')

    def test_is_isogram(self):   # Q3
        self.assertEqual(is_isogram('shahin'), 'no')
        self.assertEqual(is_isogram('python'), 'yes')

    def test_ip_address_to_integer(self):   # Q4
        self.assertEqual(ip_address_to_integer('25.0.11.255'), 419433471)
        self.assertEqual(ip_address_to_integer('255.255.255.255'), 4294967295)

    def test_integer_to_ip_address(self):   # Q4
        self.assertEqual(integer_to_ip_address(419433471), '25.0.11.255')
        self.assertEqual(integer_to_ip_address(42540766400282592856903984001653826561), '2001:db7:dc75:365:220a:7c84:d796:6401')

    def test_mexican_wave(self):   # Q5
        self.assertEqual(mexican_wave('shahin'), ['Shahin', 'sHahin', 'shAhin', 'shaHin', 'shahIn', 'shahiN'])
        self.assertEqual(mexican_wave('me'), ['Me', 'mE'])

    def test_maxNumber_after_one_deletion(self):   # Q6
        self.assertEqual(maxNumber_after_one_deletion(9678), 978)
        self.assertEqual(maxNumber_after_one_deletion(16704), 6704)

    def test_maxNumber_after_shuffling(self):   # Q7
        self.assertEqual(maxNumber_after_shuffling(56738), 87653)
        self.assertEqual(maxNumber_after_shuffling(123456), 654321)

    def test_frequency_of_given_word(self):   # Q8
        self.assertEqual(frequency_of_given_word('a a a r u i a', 'a'), 4)
        self.assertEqual(frequency_of_given_word('shahin learning python python is great', 'python'), 2)

    def test_convert_RGB_to_hex(self):   # Q9
        self.assertEqual(convertRGBtoHex(47, 39, 230), '#F2726E')
        self.assertEqual(convertRGBtoHex(2, 3, 4), '#020304')

    def test_accumulated_string(self):   # Q10
        self.assertEqual(accumulated_string('abcdefg'), 'A-Bb-Ccc-Dddd-Eeeee-Ffffff-Ggggggg')
        self.assertEqual(accumulated_string('abcd'), 'A-Bb-Ccc-Dddd')
