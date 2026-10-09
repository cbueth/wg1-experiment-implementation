import unittest

from utils.question_id import build_question_identifier


class TestBuildQuestionIdentifier(unittest.TestCase):

    def test_integer_inputs(self):
        self.assertEqual(build_question_identifier(1, 1, 1, 1), '1111')
        self.assertEqual(build_question_identifier(10, 1, 2, 1), '10121')
        self.assertEqual(build_question_identifier(13, 1, 3, 2), '13132')

    def test_float_inputs_do_not_leak_decimal_points(self):
        # the id columns can be read back as floats if the source table has a
        # stray non-empty bottom row
        result = build_question_identifier(1.0, 1.0, 1.0, 1.0)
        self.assertEqual(result, '1111')
        self.assertNotIn('.', result)

    def test_string_condition_and_question_numbers(self):
        # condition_no and question_no are extracted as single characters
        self.assertEqual(build_question_identifier(8, 1, '2', '1'), '8121')

    def test_float_and_int_mixed_inputs(self):
        self.assertEqual(build_question_identifier(10.0, 1, 2.0, '1'), '10121')

    def test_matches_item_id_suffix_without_leading_zero(self):
        # item ids are zero padded to a fixed width; the identifier drops the
        # extra leading zero for single digit stimulus ids
        item_id = 'MPRC_PopSci_MultiplEYE_xx_01111'
        suffix = item_id.split('_')[-1]
        self.assertEqual(build_question_identifier(1, 1, 1, 1), suffix[1:])


if __name__ == '__main__':
    unittest.main()
