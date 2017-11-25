import ox
import click
import pprint

lexer = ox.make_lexer([
    ('OPEN_P', r'\('),
    ('CLOSE_P', r'\)'),
    ('TEXT', r'[-a-zA-Z]+'),
    ('NUMBER', r'[0-9]+'),
    ('ignore_COMMENT', r';[^\n]*'),
    ('ignore_NEWLINE', r'\s+'),
])

tokens = [
    'TEXT',
    'NUMBER',
    'OPEN_P',
    'CLOSE_P'
]

