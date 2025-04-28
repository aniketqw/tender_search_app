# Indian Tender Search Application

## Overview
The Indian Tender Search Application is a web-based tool designed to help users find and filter tenders from various sources in India. The application allows users to search for tenders based on specific keywords, view detailed information about each tender, and manage keywords dynamically.

## Features
- Search for tenders across multiple sources.
- Filter tenders based on recency and relevance.
- Add and refine keywords for more accurate searches.
- User-friendly interface built with Gradio.

## Technologies Used
- Python
- Gradio
- Langchain
- BeautifulSoup
- Requests
- Pandas

## Installation

### Prerequisites
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository
```bash
git clone https://github.com/yourusername/tender-search-app.git
cd tender-search-app
```

### Install Dependencies
You can install the required dependencies using pip:
```bash
pip install requests beautifulsoup4 pandas gradio langchain tavily-python
```

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Open your web browser and navigate to the URL provided in the terminal (usually `http://localhost:7860`).
3. Enter your search query in the input box and click on "Search Tenders".
4. You can also add keywords to refine your search.

## Adding Keywords
To add a keyword:
1. Enter the category (e.g., "construction") in the category input box.
2. Enter the keyword you want to add in the keyword input box.
3. Click on "Add Keyword".

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This application utilizes various APIs and data sources for tender information.
- Special thanks to the developers of the libraries used in this project.

## Contact
For any inquiries, please contact [aniketsaxena627@gmail.com].
