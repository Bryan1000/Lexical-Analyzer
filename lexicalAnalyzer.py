import re
import keyword

# Get all keywords
allKeywords = keyword.kwlist

# Regular expression to match any of the keywords
keyword_regex = r'\b(?:' + '|'.join(allKeywords) + r')\b'

# Regular expressions for the operators, separators, identifiers, and integers (tokens)
operator_regex = r'[+\-*/%<>=!&|^~]=?|<<=?|>>=?|\*\*=?|\/\/=?|==|!=|<=|>=|in|not in|is|is not|and|or|not'
separator_regex = r'[()\{\};]'
identifier_regex = r'[a-zA-Z_]\w*'
integer_regex = r'\b\d+\b'

# Combine regular expressions 
tokens = '|'.join([keyword_regex, operator_regex, separator_regex, identifier_regex, integer_regex])

def tokenize(input_file): 

    allTokens = []  # List to store tokens

    with open(input_file, 'r') as file: # Open the file and read it
        for line in file: # Iterate through each line of the file
           
            # Remove any comments and whitespace
            line = re.sub(r'//.*|/\*.*?\*/', '', line).strip()
    
            
            # Tokenize the line using the combined tokens
            line_tokens = re.findall(tokens, line)

            # Extend tokens list with line tokens
            allTokens.extend(line_tokens)

    return allTokens

def main():
    input_file = 'test1.txt'  # Path to the input file
    tokens = tokenize(input_file)  # Tokenize the code

    # Remove empty strings from the list of tokens
    tokens = [token for token in tokens if token]
    
    tokens_classified = {}
    # Append token classification to list
    for token in tokens:
        if token in operator_regex:
            tokens_classified[token] = 'operator'
        elif token in separator_regex:
            tokens_classified[token] = 'seperator'
        elif token in keyword_regex:
            tokens_classified[token] = 'keyword'
        elif token in integer_regex:
            tokens_classified[token] = 'integer'
        else:
            tokens_classified[token] = 'identifier'
    
    # Print tokens 
    # print(tokens)

    # Print tokens with classification
    # print(tokens_classified)

    # Printing output as described in instructions
    for i in tokens_classified:
        print('"' + i + '" = ' + tokens_classified[token])

if __name__ == "__main__":
    main() 