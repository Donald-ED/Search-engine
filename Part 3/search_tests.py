from search import title_to_info, keyword_to_titles, search, article_info, article_length, title_timestamp, favorite_author, multiple_keywords, display_result
from search_tests_helper import print_basic, print_advanced, print_advanced_option, get_print
from wiki import article_metadata, title_to_info_map, keyword_to_titles_map
from unittest.mock import patch
from copy import deepcopy

# List of all available article titles for this search engine
# The benefit of using this is faster code - these functions will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()
TITLE_TO_INFO = title_to_info_map()
KEYWORD_TO_TITLES = keyword_to_titles_map()

# Storing into a variable so don't need to copy and paste long list every time
DOG = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']

TRAVEL = ['Time travel']

MUSIC = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']

PROGRAMMING = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']

SOCCER = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']

PHOTO = ['Digital photography']

SCHOOL = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']

PLACE = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

DANCE = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']

def test_example_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'an article title': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'another article title': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_example_keyword_to_titles_tests():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'some': ['an article title'], 'words': ['an article title', 'another article title'], 'that': ['an article title'], 'make': ['an article title', 'another article title'], 'up': ['an article title'], 'sentence': ['an article title'], 'more': ['another article title'], 'could': ['another article title'], 'sentences': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #3
    assert search('dog') == DOG

    # Advanced search option 1, function #4
    expected = {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}
    assert article_info(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat', 'Guide dog']
    assert article_length(8000, deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Black dog (ghost)': 1220471117, 'Mexican dog-faced bat': 1255316429, 'Dalmatian (dog)': 1207793294, 'Guide dog': 1165601603, 'Sun dog': 1208969289}
    assert title_timestamp(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Andrea', deepcopy(DOG), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(DOG)) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat', 'Guide dog']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
def test_title_to_info_tests():
    assert title_to_info(METADATA) == TITLE_TO_INFO
    # Create fake metadata to test
    fake_metadata = [['A sentence', 'andrea', 1234567890, 103, ['A', 'sentence', 'is', 'a', 'group', 'of', 'words']],
                     ['A phrase', 'helloworld', 987123456, 8029, ['A', 'phrase', 'is', 'an', 'incomplete', 'sentence']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'A sentence': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'A phrase': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_keywords_to_titles_tests():
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES
    # Create fake metadata to test
    fake_metadata = [['A sentence', 'andrea', 1234567890, 103, ['A', 'sentence', 'is', 'a', 'group', 'of', 'words']],
                     ['A phrase', 'helloworld', 987123456, 8029, ['A', 'phrase', 'is', 'an', 'incomplete', 'sentence']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'A': ['A sentence', 'A phrase'], 'sentence': ['A sentence', 'A phrase'], 'is': ['A sentence', 'A phrase'], 'a': ['A sentence'], 'group': ['A sentence'], 'of': ['A sentence'], 'words': ['A sentence'], 'phrase': ['A phrase'], 'an': ['A phrase'], 'incomplete': ['A phrase']}


    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_unit_tests():
  #Test for search function
  assert search("programming") == PROGRAMMING
  assert search("DanCe") == DANCE
  assert search("SCHOOL") == SCHOOL

  #Test for article_info function
  expected = {'C Sharp (programming language)': {'author': 'Eaglizard', 'timestamp': 1232492672, 'length': 52364}, 'Python (programming language)': {'author': 'Lulu of the Lotus-Eaters', 'timestamp': 1137530195, 'length': 41571}, 'Lua (programming language)': {'author': 'Makkuro', 'timestamp': 1113957128, 'length': 0}, 'Covariance and contravariance (computer science)': {'author': 'Wakapop', 'timestamp': 1167547364, 'length': 7453}, 'Personal computer': {'author': 'Darklock', 'timestamp': 1220391790, 'length': 45663}, 'Ruby (programming language)': {'author': 'Hervegirod', 'timestamp': 1193928035, 'length': 30284}}

  assert article_info(deepcopy(PROGRAMMING), TITLE_TO_INFO) == expected

  expected = {'List of Canadian musicians': {'author': 'Bearcat', 'timestamp': 1181623340, 'length': 21023}, '2009 in music': {'author': 'SE KinG', 'timestamp': 1235133583, 'length': 69451}, 'Old-time music': {'author': 'Badagnani', 'timestamp': 1124771619, 'length': 12755}, '1936 in music': {'author': 'JohnRogers', 'timestamp': 1243745950, 'length': 23417}, 'Indian classical music': {'author': 'Davydog', 'timestamp': 1222543238, 'length': 9503}} 

  assert article_info(deepcopy(DANCE), TITLE_TO_INFO) == expected

  expected = {'Edogawa, Tokyo': {'author': 'Ciphers', 'timestamp': 1222607041, 'length': 4526}, 'Fisk University': {'author': 'NerdyScienceDude', 'timestamp': 1263393671, 'length': 16246}, 'Annie (musical)': {'author': 'Piano non troppo', 'timestamp': 1223619626, 'length': 27558}, 'Alex Turner (musician)': {'author': 'CambridgeBayWeather', 'timestamp': 1187010135, 'length': 9718}}

  assert article_info(deepcopy(SCHOOL), TITLE_TO_INFO) == expected

  #Test for article_length function
  assert article_length(5000, deepcopy(PROGRAMMING), TITLE_TO_INFO) == ['Lua (programming language)']

  assert article_length(10000, deepcopy(DANCE), TITLE_TO_INFO) == ['Indian classical music']

  assert article_length(-1000, deepcopy(SCHOOL), TITLE_TO_INFO) == []

  #Test for title_timestamp function
  expected = {'C Sharp (programming language)': 1232492672, 'Python (programming language)': 1137530195, 'Lua (programming language)': 1113957128, 'Covariance and contravariance (computer science)': 1167547364, 'Personal computer': 1220391790, 'Ruby (programming language)': 1193928035}
  assert title_timestamp(deepcopy(PROGRAMMING), TITLE_TO_INFO) == expected

  assert title_timestamp(deepcopy(DANCE), TITLE_TO_INFO) == {'List of Canadian musicians': 1181623340, '2009 in music': 1235133583, 'Old-time music': 1124771619, '1936 in music': 1243745950, 'Indian classical music': 1222543238}

  assert title_timestamp(deepcopy(SCHOOL), TITLE_TO_INFO) == {'Edogawa, Tokyo': 1222607041, 'Fisk University': 1263393671, 'Annie (musical)': 1223619626, 'Alex Turner (musician)': 1187010135}

  #Test for favourite_author Function
  assert favorite_author('lulu of the lotus-eaters', deepcopy(PROGRAMMING), TITLE_TO_INFO) == True

  assert favorite_author('Gary', deepcopy(DANCE), TITLE_TO_INFO) == False

  assert favorite_author('nerdy science dude', deepcopy(SCHOOL), TITLE_TO_INFO) == True

  #Test for multiple_keywords Function
  expected = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)', 'Ken Kennedy (computer scientist)', 'Human computer', 'List of dystopian music, TV programs, and games', 'Single-board computer', 'Personal computer', 'Digital photography', 'Mode (computer interface)']
  assert multiple_keywords('computer', deepcopy(PROGRAMMING)) == expected

  assert multiple_keywords('photoGraphy', deepcopy(SCHOOL)) == ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)', 'Digital photography', 'Wildlife photography']
  assert multiple_keywords('Sports', deepcopy(DANCE)) == DANCE

@patch('builtins.input')
def test_integration_test(input_mock):
    keyword = 'and'
    advanced_option = 2
    advanced_response = 7000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['French pop music', 'Edogawa, Tokyo', 'Ken Kennedy (computer scientist)', '1986 in music', 'Kevin Cadogan', 'Lights (musician)', 'Human computer', 'Aube (musician)', 'List of overtone musicians', 'USC Trojans volleyball', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Mexican dog-faced bat', 'Embryo drawing', 'Joe Becker (musician)', 'Will Johnson (soccer)', 'Fiskerton, Lincolnshire', 'B (programming language)', 'Steven Cohen (soccer)', 'Tom Hooper (musician)', 'Endoglin', 'Lua (programming language)', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'The Mandogs', 'Scores (computer virus)', 'George Crum (musician)', 'Wildlife photography', 'Traditional Thai musical instruments', 'Landseer (dog)', 'Les Cousins (music club)', 'Paul Carr (musician)', 'Spawning (computer gaming)', 'Sean Delaney (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', 'Mode (computer interface)']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To make all tests run, call all test functions inside the if statement.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    # As you're done with each function, uncomment the example test functions
    # and make sure they pass
    test_example_title_to_info_tests()
    test_example_keyword_to_titles_tests()
    test_example_unit_tests()
    test_example_integration_test()
