import PyPDF2
import functools
import logging


def filter_lines_with_words(pdf_path, words):
    lines_with_words = []

    # Open the PDF file
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        # Iterate through each page
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            if text:
                # Split the text into lines
                lines = text.split("\n")
                for line in lines:
                    # Check if any of the words are in the line
                    if any(word in line for word in words):
                        lines_with_words.append(line)
    return lines_with_words


# Example usage:
pdf_path = "example.pdf"
words_to_search = ["data", "science", "machine", "learning"]
result_lines = filter_lines_with_words(pdf_path, words_to_search)

for line in result_lines:
    print(line)


# Adding another function


def log_function(level=logging.INFO):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.log(
                level,
                f"Calling function {func.__name__} with args: {args}, kwargs: {kwargs}",
            )
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_function(level=logging.DEBUG)
def add(a, b):
    return a + b


@log_function(level=logging.WARNING)
def subtract(a, b):
    return a - b


print(add(3, 5))
print(subtract(10, 3))
