from madlib_cli.madlib import read_template,parse,prompt,merge,write_file

"""
input : file path
output : the content f the file 

"""
def test_reading_file():
    actual=read_template('assest/madlib.txt')
    expected="Make Me A Video Game!\n\nI the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!\n\nWhat are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."
    assert actual==expected

"""
input :  function that takes in a template string 
output: returns a string with language parts removed and a separate list of those language parts.
"""
def test_parse():
    actual=parse()
    expected=(['Adjective', 'Adjective', 'A First Name', 'Past Tense Verb', 'A First Name', 'Adjective', 'Adjective', 'Plural Noun', 'Large Animal', 'Small Animal', "A Girl's Name", 'Adjective', 'Plural Noun', 'Adjective', 'Plural Noun', 'Number 1-50', "First Name's", 'Number', 'Plural Noun', 'Number', 'Plural Noun'], "Make Me A Video Game!\n\nI the {} and {} {} have {}{}'s {} sister and plan to steal her {} {}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find.")
    assert actual==expected

"""
input:bare” template and a list of user entered language parts
output: returns a string with the language parts inserted into the template.

"""
def  test_merge():
    actual=merge()
    expected=write_file()
    assert actual==expected
    