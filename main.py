import string
from tika import parser

parsedFile = parser.from_file("b.docx")
print(parsedFile['content'].strip())
