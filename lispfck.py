import ox
import click
import pprint

lexer = ox.make_lexer([
    ('OPEN_PARENTHESIS', r'\('),
    ('CLOSE_PARENTHESIS', r'\)'),
    ('PLAIN_TEXT', r'[-a-zA-Z]+'),
    ('NUMBER', r'[0-9]+'),
    ('IGNORE_COMMENT', r';[^\n]*'),
    ('IGNORE_NEWLINE', r'\s+'),
])

tokens = [
    'PLAIN_TEXT',
    'NUMBER',
    'OPEN_PARENTHESIS',
    'CLOSE_PARENTHESIS'
]

atom = lambda x: x
term = lambda x: (x,)
comp = lambda x, y: (x,) + y
pare = lambda x, y: '()'
expr = lambda x, y, z: y


parser = ox.make_parser([
    ('expr : OPEN_PARENTHESIS term CLOSE_PARENTHESIS', expr),
    ('expr : OPEN_PARENTHESIS CLOSE_PARENTHESIS', pare),
    ('term : atom term', comp),
    ('term : atom', term),
    ('atom : expr', atom),
    ('atom : PLAIN_TEXT', atom),
    ('atom : NUMBER', atom),
], tokens)

@click.command()
@click.argument('file', type=click.File('r'))

def printTree(file):
    tokens = lexer(file.read())
    pprint.pprint(parser(tokens))

printTree()