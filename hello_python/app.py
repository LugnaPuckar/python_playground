from flask import Flask
import os

app = Flask(__name__)

# vars
folder_name = 'content'
md_filename = 'home.md'


# Read the home.md in ./content/
def read_text_content():
    file_path = os.path.join(os.path.dirname(__file__), f'{folder_name}', f'{md_filename}')
    with open(file_path, 'r') as file:
        return file.read()
    
# Load the text and display it.
@app.route("/")
def home():
    home_text = read_text_content()
    return f"{home_text}"

# run
if __name__ == "__main__":
    app.run(debug=True)