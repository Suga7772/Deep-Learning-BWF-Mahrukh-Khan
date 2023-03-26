from collections import OrderedDict

glossary = OrderedDict()

glossary['set'] = 'collection of non iterable elements'
glossary['input()'] = 'takes user input from terminal of any data type'
glossary['if'] = 'condition checking , initial block'
glossary['elif'] = 'else if block , for calculating if the "if" clause is false'
glossary['for'] = 'loop iterator that iterates each element of a set, collection'
glossary['=='] = 'conditional equality checker from both values that are on either side'
glossary['print()'] = 'output command , will print everything encapsulated inside circle brackets in form of a string'
glossary['list'] = 'mutable data structure'
glossary['not in '] = 'condition checker, similar to != operation'
glossary['split()'] = 'seperates data of a string from empty spaces '

for title, definition in glossary.items():
    print(title.title() + " : " + definition)