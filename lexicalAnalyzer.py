import re

# Regular expression to match any of the keywords
keyword_regex = r'\b(?:auto|break|alignas|alignof|and|and_eq|asm|atomic_cancel|atomic_commit|atomic_noexcept|char8_t|char16_t|char32_t|compl|concept|consteval|constexpr|constinit|const_cast|co_await|nullptr|bitand|bitor|bool|ostream|std|str|assert_eq||ifstream|char|cout|cin|try|catch|include|stoi|get|stod|case|catch|class|const|continue|default|dynamic_cast|trunc|thread_local|sycronized|delete|do|double|else|enum|module|defined|explicit|export|extern|false|float|for|friend|goto|if|inline|int|long|mutable|namespace|new|operator|private|protected|public|register|reinterpret_cast|return|short|signed|sizeof|static|static_assert|static_cast|struct|switch|template|this|throw|true|try|typedef|typeid|typename|union|unsigned|using|virtual|void|volatile|wchar_t|xor|xor_eq|not|noexcept|or|while)\b'

# Regular expressions for the operators, separators, identifiers, and integers (tokens)
operator_regex = operator_regex = r'[-+*/%=<>&|^~!]=?|<<=?|>>=?|\*\*=?|\/\/=?|==|!=|<=|>=|&&|\|\||::|\+\+|--|->|\.|->\*|\[\]|&=|\|=|\^=|<<=|>>=|~|&|\||\^|\(|\)|\[|\]|{|}|;|,|:|\?|\.|\.\*|->|new|delete|new\[\]|delete\[\]|"'

separator_regex = r'[()\[\]{};,.:]'
identifier_regex = r'[a-zA-Z_]\w*'
integer_regex = r'\b(?:0[xX][0-9a-fA-F]+|0[0-7]*|\d+)\b'

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
    input_file = 'test1.txt'  # Path to the input file (here you insert the name of the file)
    tokens = tokenize(input_file)  # Tokenize the code

    # Remove empty strings from the list of tokens
    tokens = [token for token in tokens if token]
    
    # Initialize list to store the classified tokens
    tokens_classified = [] 
    # A flag to track whether the current token is part of a string literal
    is_string = False   
    temp_str = ""
    # Append token classification to list (iterate through each token in list)
    for i in range(len(tokens)):
        # If the current token is part of a string literal and not a closing quote
        if is_string and tokens[i] != '"':
            # Append the current token to the temporary string representing the string literal
            temp_str = temp_str + " " + tokens[i]
            continue
         # If the current token is a quote   
        if tokens[i] == '"':
            if is_string:  # If it's the beginning of a string literal
                # Append the completed string literal to the classified tokens list
                tokens_classified.append([temp_str.strip(), 'string literal']) #string literal classification
            # flag to indicate whether we're inside a string literal
            is_string = not is_string
            # Append the quote token to the classified tokens list, marked as an operator
            tokens_classified.append([tokens[i], 'operator'])
        # If the current token is a separator
        elif re.match(separator_regex, tokens[i]):
            # Append the separator token to the classified tokens list, marked as a separator
            tokens_classified.append([tokens[i],'separator'])
        elif re.match(operator_regex, tokens[i]):
            # Split compound operators into individual tokens
            ops = re.findall(r'\b\w{2,}\b|.', tokens[i])
            for op in ops:
                tokens_classified.append([op, 'operator'])
        elif re.match(keyword_regex, tokens[i]):  #if current token is keyword
            tokens_classified.append([tokens[i],'keyword']) #append to token list
        elif re.match(integer_regex, tokens[i]): #if current token is a number
            tokens_classified.append([tokens[i], 'integer']) #append to token list
        elif tokens[i-1] == '"' and tokens[i+1] == '"':  #if current token is string literal
            tokens_classified.append([tokens[i],'string literal']) #append string token to list
        else:
            tokens_classified.append([tokens[i], 'identifier']) #if token is identifier append to list
    
    # Printing output as described in instructions
    for tokens, classification in tokens_classified:
        print("\"" + tokens +"\" = " + classification)


if __name__ == "__main__":
    main() 