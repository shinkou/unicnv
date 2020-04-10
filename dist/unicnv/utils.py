# vim: fenc=utf-8 ff=unix lcs=tab\:>. list noet sw=4 ts=4 tw=0
import math, re

RE_COL1 = re.compile(r'^[^;]+')
RE_HEX = re.compile(r'(\b[0-9A-Fa-f]+\b)')

def ux(i):
	'''Convert hex to valid UTF-16 character expression \\uXXXX'''
	i = int(i, 16)
	if 0xffff < i:
		i = int.from_bytes(chr(i).encode('utf-16be'), 'big')
	nob = 1 if 2 > i else math.ceil(math.log(i, 0xffff))
	s = ''
	for cnt in range(0, nob):
		s += '\\u%04X' % ((i >> (16 * (nob - cnt - 1))) & 0xffff,)
	return s


def col1utf(s):
	'''Convert Unicode code points in the 1st column to UTF-16'''
	s = RE_COL1.sub(
		lambda m_col1: RE_HEX.sub(
			lambda m_hex: ux(m_hex.group(0))
			, m_col1.group(0)
		)
		, s
	)
	return s
