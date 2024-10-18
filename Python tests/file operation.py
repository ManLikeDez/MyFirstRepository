import win32com.client

def open_word_document(file_path):
    """Opens a local Word document using win32com.client.

    Args:
        file_path (str): The path to the Word document.
    """

    try:
        word_app = win32com.client.Dispatch("Word.Application")
        word_app.Visible = True
        doc = word_app.Documents.Open(file_path)
    except Exception as e:
        print(f"Error opening Word document: {e}")

if __name__ == "__main__":
    file_path = r"C:\Users\dere_\Downloads\Senior Service Desk Analyst-2022.docx"  # Replace with the actual file path
    open_word_document(file_path)

# To open text file
def open_local_text_file(file_path):
  """Opens a local text file and returns its contents.

  Args:
    file_path: The path to the file to open.

  Returns:
    The contents of the file as a string.
  """

  try:
    with open(file_path, 'r') as f:
      contents = f.read()
      return contents
  except FileNotFoundError:
    print(f"File not found: {file_path}")
    return None

file_path = "C:\\Users\\dere_\\Documents\\testing.txt"  # Replace with your actual file path
contents = open_local_text_file(file_path)

if contents:
  print(contents)

vowel_count = 0
for line in contents:
   if "i" in line:
    vowel_count += 1

print(f"The vowel count is {vowel_count}.")

