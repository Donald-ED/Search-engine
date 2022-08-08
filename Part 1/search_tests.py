from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch

# List of all available article titles for this search engine
# The benefit of using this is faster code - article_titles() will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
ARTICLE_TITLES = article_titles()

def test_example_unit_tests():
    # Storing into a variable so don't need to copy and paste long list every time
    # If you want to store search results into a variable like this, make sure you pass a copy of it when
    # calling a function, otherwise the original list (ie the one stored in your variable) is going to be
    # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
    dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']

    # Example tests, these do not count as your tests

    # Basic search, function #1
    assert search('dog') == dog_search_results

    # Advanced search option 1, function #2
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']
    assert title_length(25, dog_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(3, dog_search_results.copy()) == ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid']

    # Advanced search option 3, function #4
    assert random_article(3, dog_search_results.copy()) == 'Black dog (ghost)'

    # Advanced search option 4, function #5
    assert favorite_article('Guide dog', dog_search_results.copy()) == True

    # Advanced search option 5, function #6
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']
    assert multiple_keywords('volleyball', dog_search_results.copy()) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 1
    advanced_response = 25

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'Edogawa, Tokyo\', \'Kevin Cadogan\', \'Endogenous cannabinoid\', \'Black dog (ghost)\', \'2007 Bulldogs RLFC season\', \'Mexican dog-faced bat\', \'Dalmatian (dog)\', \'Guide dog\', \'Georgia Bulldogs football\', \'Endoglin\', \'Sun dog\', \'The Mandogs\', \'Landseer (dog)\']\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
def test_unit_tests():
  bat_search_results = ['Mexican dog-faced bat']
  
  music_search_results = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
  
  computer_search_results = ['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'List of computer role-playing games', 'Mode (computer interface)']

  #Test cases for search function
  assert search('bat') == bat_search_results
  
  assert search('music') == music_search_results
  
  assert search('computer') == computer_search_results
  #Text cases for title_length
  assert title_length(10, bat_search_results.copy()) == []
  
  expected0 = ['French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Aco (musician)', 'Richard Wright (musician)', '1936 in music', '1962 in country music', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'David Levi (musician)', 'George Crum (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
  assert title_length(25, music_search_results.copy()) == expected0
  
  assert title_length(-7, computer_search_results.copy()) == []
  
  #Test cases for article_count
  assert article_count(10, bat_search_results.copy()) == []
  
  assert article_count(10, music_search_results.copy()) == ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)']

  assert article_count(-4, computer_search_results.copy()) == ['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer', 'Scores (computer virus)']

  #Text cases for random_article
  assert random_article(0, bat_search_results.copy()) == "Mexican dog-faced bat"
  
  assert random_article(6, music_search_results.copy()) == 'Rock music'

  assert random_article(-6, computer_search_results.copy()) == 'Personal computer'

  #Test cases for favorite_article
  assert favorite_article('dog', bat_search_results.copy()) == False
  
  assert favorite_article("Noise (music)", music_search_results.copy()) == True

  assert favorite_article("computer", computer_search_results.copy()) == False

  #Test cases for mutiple_keywords
  expected = ['Mexican dog-faced bat', '1922 in music', '1986 in music', '1936 in music', '1962 in country music', '1996 in music', 'English folk music (1500–1899)']
  assert multiple_keywords("1", bat_search_results.copy()) == expected
  
  assert multiple_keywords("",music_search_results.copy())== music_search_results

  expected0 = ['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'List of computer role-playing games', 'Mode (computer interface)', 'C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)', 'Semaphore (programming)']
  assert multiple_keywords("programming", computer_search_results.copy()) == expected0 


@patch('builtins.input')
def test_integration_test(input_mock):
  keyword = '0'
  advanced_option = 3
  advanced_response = 6

  output = get_print(input_mock, [keyword, advanced_option, advanced_response])

  expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: 2007 in music\n'

  assert output == expected
# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To actually make all your tests run, call all of your test functions here.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    test_example_unit_tests()
    test_example_integration_test()
    test_unit_tests()
    test_integration_test()
