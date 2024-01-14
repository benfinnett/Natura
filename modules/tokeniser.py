import json
from tqdm import tqdm
import openai
from modules.errors import CompilerError

class Tokeniser:
    """A compiler tokeniser that uses the OpenAI API to tokenise code.
    """
    def __init__(self, instructions: str, api_key: str):
        openai.api_key = api_key
        self.model = 'gpt-3.5-turbo-1106'
        self.temperature = 0.0
        self.instructions = instructions

        with open('./assets/language/tokens.json') as file:
            self.token_list = json.load(file)

    def parse_json(self, json_string: str) -> list[dict[str, str]]:
        """Parses a JSON string (the output from OpenAI's ChatGPT model) into a list of dictionaries
        representing the token stream.

        Args:
            json_string (str): The JSON formatted string to parse.

        Raises:
            json.decoder.JSONDecodeError: If the JSON string is invalid.

        Returns:
            list[dict[str, str]]: The parsed JSON string as a list of dictionaries.
        """
        try:
            data = json.loads(json_string)
            return data
        except json.decoder.JSONDecodeError:
            raise CompilerError(json_string)
    
    def tokenise_line(self, line: str, line_number: int) -> list[dict[str, str]] | None:
        """Tokenises a single line of code using the OpenAI API.

        Args:
            line (str): The line of code to tokenise.
            line_number (int): The line number of the line of code.

        Raises:
            ValueError: If the OpenAI API provides an unexpected output.

        Returns:
            list[dict[str, str]] | None: The tokenised line as a list of dictionaries or None for newlines.
        """
        if line == '\n':
            return None
        
        response = openai.chat.completions.create(
            model=self.model,
            messages=[{'role': 'user', 'content': self.instructions + '\n' + line}],
            temperature=self.temperature
        )
        
        response_content = response.choices[0].message.content
        print(response_content)

        if not response_content:
            raise CompilerError(f'Unable to tokenise line {line_number}: No response from API')
        elif response_content.startswith('ERROR'):
            raise CompilerError(f'Unable to tokenise line {line_number}: {response_content.split("ERROR: ")[-1]}') 
        
        json_data = self.parse_json(response_content)
        return json_data if isinstance(json_data, list) else [json_data]
    
    def tokenise_file(self, code_lines: list[str]) -> list[dict[str, str]]:
        """Tokenises a file of code using the OpenAI API.

        Args:
            code_lines (list[str]): The lines of code to tokenise.

        Returns:
            list[dict[str, str]]: The tokenised file as a list of dictionaries representing the token stream.
        """
        tokens: list[dict[str, str]] = []
        for i in tqdm(range(len(code_lines)), desc='Tokenising file: ', ncols=100):
            tokenised_line = self.tokenise_line(code_lines[i], line_number=i + 1)
            if tokenised_line:
                tokens += tokenised_line
                tokens.append({'token_type': 'endline'})
        return tokens

    def validate_token_types(self, token_list: list[dict[str, str]]) -> list[int]:
        """Validates the token types in a token stream.

        Args:
            token_list (list[dict[str, str]]): The token stream to validate.

        Returns:
            list[int]: A list of indices of invalid tokens.
        """
        token_names = list(self.token_list['keywords'].values()) + self.token_list['nonTerminals']
        invalid_token_indices = []
        for i, token in enumerate(token_list):
            if token['token_type'] not in token_names:
                invalid_token_indices.append(i)
        return invalid_token_indices