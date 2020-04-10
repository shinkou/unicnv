# vim: fenc=utf-8 ff=unix lcs=tab\:>. list noet sw=4 ts=4 tw=0
import unittest

from unicnv.utils import ux

class UnicnvTestCase(unittest.TestCase):
	def test_ux(self):
		ucs = {
			'231A': r'\u231A'
			, '1F319': r'\uD83C\uDF19'
		}
		for original, converted in ucs.items():
			self.assertEqual(ux(original), converted)

if '__main__' == __name__:
	unittest.main()
