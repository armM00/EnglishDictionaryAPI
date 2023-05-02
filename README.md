![alt text](https://i.pinimg.com/originals/d1/0f/de/d10fde83b975cd247c2817b5d8c970e1.jpg)


# Dictionary API

This is a simple Flask-based API that retrieves word definitions from a CSV file and returns them in JSON format. 

## Getting Started

### Prerequisites
- Python 3.11.3
- Flask
- csv (included in Python standard library)

### Installation

1. Clone the repository:

   - `git clone https://github.com/armM00/EnglishDictionaryAPI.git`
   - `pip install Flask`

2. Run the server:

   - `python main.py`

## Usage

### Endpoints

`/api/v1/<word>`

Returns the definition of the specified word. If the word is not found in the CSV file, a 404 error is returned.

### Example Request

- GET `/api/v1/hello HTTP/1.1`

- Host: localhost:5001

### Example Response

- HTTP/1.1 200 OK

- Content-Type: application/json

`{
"definition": "Used as a greeting or to begin a conversation.",
"word": "Hello"
}`

## CSV Format

The CSV file should have two columns: `word` and `definition`. Each row represents a single word.
