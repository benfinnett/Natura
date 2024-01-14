class CompilerError(Exception):
    """Custom exception for errors related to compilation.
    """
    def __init__(self, message: str):
        """Initialises a CompilerError object.

        Args:
            message (str): 
            line_number (int): _description_
            line (str): _description_
        """
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f'CompilerError: {self.message}'