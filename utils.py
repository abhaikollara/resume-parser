import tika
tika.initVM()
from tika import parser


def read_text(path):
    return parser.from_file(path)['content']
