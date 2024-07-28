import PyPDF2


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
