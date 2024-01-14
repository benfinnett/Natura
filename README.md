# Natura
Natura is a new programming language that leverages the contextual awareness of a large language model (LLM) to provide a more intuitive coding experience. Using an AI-based compiler, Natura allows users to write code in a style closer to natural language or pseudocode. 

The potential of Natura to decrease the barrier of entry into programming thus making it more accessible to a broader audience makes it highly relevant and novel. This aligns with the demand for technology that is not only powerful but also user-friendly and intuitive. Having an AI-based compiler that understands various synonymous coding expressions allows users a more flexible and efficient programming experience. This project not only reflects the technical complexity and innovative spirit encouraged in modern AI development, but also represents a significant step towards the future of programming languages.

Whilst the language may not be practical for most projects, it has potential usecases in education, as the compiler is far more lenient with syntactical errors, whilst still communicating the logic behind programming and code.

# Requirements
To use the compiler, the following must be installed:
- [openai](https://pypi.org/project/openai/): Python package to access the OpenAI API.
- [gcc](https://gcc.gnu.org/install/): C code compiler.

You can also perform:
`pip install -r requirements.txt`
to install the Python dependancies through pip.

You must also create an `api_key.txt` file in the `assets` directory containing nothing but your OpenAI [API key](https://platform.openai.com/api-keys).

# Building from VS Code
If you want to build your Natura code directly from VS Code, you can do so by following these steps:
1. Navigate to your project's `.vscode` directory.
2. Create a new file "tasks.json" and paste the below JSON into it.
3. Replace the placeholder directory path with the path to your installation of the Natura compiler.
4. Now, with your Natura file open and focused, you can navigate to `Terminal > Run Build Task` or hit <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> (by default) to build your Natura code to an executable file. The `.exe` file will end up in the `out` directory.

```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Build .nat file",
            "type": "shell",
            "command": "C:/Python311/python.exe", // Ensure this is the correct Python version
            "args": [
                "natura_compiler.py",
                "${file}"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": [],
            "options": {
                "cwd": "PATH/TO/src" // Replace this line with your path to the /src directory
            }
        }
    ]
}
```
