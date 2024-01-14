import os
import sys
from modules.errors import CompilerError
from modules.tokeniser import Tokeniser
from modules.cbuilder import generate_c, build_executabe
    
def get_text_from_file(path: str) -> str:
    """Reads data from textual file path. Joins all lines into a single string.

    Args:
        path (str): File path to textual file. Can be relative or absolute.

    Returns:
        str: File data as a single string.
    """
    abs_path = os.path.abspath(path)

    with open(abs_path, 'r') as file:
        data = ''.join(file.readlines())
    
    return data

def read_natura_file(path: str) -> list[str]:
    """Reads data from .nat file path.

    Args:
        path (str): File path to .nat file. Can be relative or absolute.

    Returns:
        list[str]: File data as a list with each line of code being a list element.
    """
    abs_path = os.path.abspath(path)
    
    extension = abs_path.split('.')[-1]
    if extension != 'nat':
        raise ValueError('File extension must be .nat')

    with open(abs_path, 'r') as file:
        data = file.readlines()
    
    return data

def main(file_path: str) -> None:
    PERSIST_CONSOLE = True

    print('Starting Natura Compiler...')
    # Read in language grammar, tokens, and the LLM instructions
    natura_grammar = get_text_from_file('./assets/language/formal_grammar.ebnf')
    language_tokens = get_text_from_file('./assets/language/tokens.json')
    tokeniser_instructions = f'Backus-Naur Form:\n{natura_grammar}\n\n' + \
                             f'Tokens:\n{language_tokens}\n\n' + \
                             get_text_from_file('./assets/tokeniser_instructions.txt')

    # Read in OpenAI API key and create tokeniser object
    api_key = get_text_from_file('./assets/api_key.txt')
    parser = Tokeniser(tokeniser_instructions, api_key)

    print('Starting lexical analysis...')
    nat_file = read_natura_file(file_path)
    token_stream = parser.tokenise_file(nat_file)

    # Handle invalid tokens
    invalid_token_indices = parser.validate_token_types(token_stream)
    if invalid_token_indices:
        for i in invalid_token_indices:
            print(f'Invalid token found at index {i}: {token_stream[i]}')
        exit(1)
    print('Lexical analysis complete.')
    
    print('Building C code...')
    c_code = generate_c(token_stream, api_key, PERSIST_CONSOLE)
    build_executabe(c_code, file_path)
    print('Executable built.')

if __name__ == '__main__':
    # Get .nat file name from command line arguments
    if len(sys.argv) > 1:
        nat_file_path = sys.argv[1]
        extension = os.path.splitext(nat_file_path)[1]

        if extension != '.nat':
            raise CompilerError('File extension must be .nat')
    else:
        raise CompilerError('No .nat file path provided.')
    
    # Run program
    main(nat_file_path)