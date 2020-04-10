# vim: fenc=utf-8 ff=unix lcs=tab\:>. list noet sw=4 ts=4 tw=0
#
# Unicode Code Point to UTF-16 Official Document Text File Converter
#
# Example
#
#   Input file data entry:
#     1F3C6 ; Basic_Emoji ; trophy # E0.6   [1] (🏆)
#
#   Output:
#     \uD83C\uDFC6 ; Basic_Emoji ; trophy # E0.6   [1] (🏆)
#
import argparse, re
from .utils import col1utf

RE_COMMENT = re.compile(r'\s*#.*$')

def _getargs():
	parser = argparse.ArgumentParser(description = '''
Convert Unicode code points in data files to UTF-16 code points for Java
regexp use. For input file format, please reference this:
https://unicode.org/Public/emoji/13.0/emoji-sequences.txt
''')
	parser.add_argument\
	(
		'filepaths'
		, metavar = 'FILEPATH'
		, nargs = '+'
		, help = 'File path'
	)
	return parser.parse_args()


def process(fname):
	'''Process file given by the filename line by line'''
	with open(fname, 'r') as f:
		l = f.readline()
		while len(l) > 0:
			pl = l.strip()
			m_comment = re.search(RE_COMMENT, pl)
			if m_comment is not None:
				pl = re.sub(RE_COMMENT, '', pl)
			if len(pl) > 0:
				print('%s' % (col1utf(l.strip()),))
			else:
				print(l, end = '')
			l = f.readline()


def main():
	args = _getargs()
	for filepath in args.filepaths:
		process(filepath)
