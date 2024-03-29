import re
import keyword

# get all keywords
allKeywords = keyword.kwlist
def tokenize(): 
    #regex to match any of the keywords
    keyword_regex = r'\b(?:' + '|'.join(allKeywords) + r')\b'

    #regex for the operators, separatos, identiers, and integers (tokenize)
    operator_regex = r'[\+\-\*/%=<>&|^~]=?|<<=?|>>=?|\*\*=?|\/\/=?|==|!=|<=|>=|in|not in|is|is not|and|or|not'
    separator_regex = r'[()\{\};]'
    identifier_regex = r'[a-zA-Z_]\w*'
    integer_regex = r'\b\d+(\.\d+)?\b'

    # Combine regular expressions 
    tokens = '|'.join([keyword_regex, operator_regex, separator_regex, identifier_regex, integer_regex])
    
    allTokens = []  # List to store tokens