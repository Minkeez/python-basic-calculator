import unittest
from calculator import calculate, parse_number

class TestCalculator(unittest.TestCase):
  
  def test_parse_number_float(self):
    self.assertEqual(parse_number("3.14"), 3.14)
    self.assertEqual(parse_number("-2.5"), -2.5)

  def test_parse_number_complex(self):
    self.assertEqual(parse_number("1+2j"), complex(1, 2))
    self.assertEqual(parse_number("-3-4j"), complex(-3, -4))

  def test_parse_number_invalid(self):
    self.assertIsNone(parse_number("abc"))
    self.assertIsNone(parse_number("2+2")) # It may interpreted as a complex misrepresentation

  def test_calculate_add(self):
    self.assertEqual(calculate(2, 3, '+'), 5)
    self.assertEqual(calculate(1+2j, 2+3j, '+'), 3+5j)

  def test_calculate_sub(self):
    self.assertEqual(calculate(5, 2, '-'), 3)
    self.assertEqual(calculate(5+2j, 1+1j, '-'), 4+1j)

  def test_calculate_mul(self):
    self.assertEqual(calculate(2, 3, '*'), 6)
    self.assertEqual(calculate(1+2j, 2+3j, '*'), (1+2j)*(2+3j))

  def test_calculate_div(self):
    self.assertEqual(calculate(6, 2, '/'), 3)
    self.assertIsNone(calculate(5, 0, '/')) # divided by 0 => None
    self.assertEqual(calculate(1+2j, 1+1j, '/'), (1+2j)/(1+1j))
  
  def test_calculate_invalid_operation(self):
    self.assertIsNone(calculate(2, 3, '^'))
    self.assertIsNone(calculate(2, 3, ''))

if __name__ == "__main__":
  unittest.main()