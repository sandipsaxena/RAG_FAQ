# RAG_FAQ  

  
# FAQ Chatbot for a Company Manual Project using RAQ and Python

## Prerequisites

Ensure you have the following installed on your system before proceeding:

- **Python 3.8 or higher**
- **pip (Python package manager)**
- **Visual Studio Code (VS Code)**
- **Virtual Environment (optional but recommended)**

## Downloading the Project

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd <project-folder>
   ```
   *OR*

2. **Download the ZIP file:**
   - Go to the repository link.
   - Click on **Code** and select **Download ZIP**.
   - Extract the ZIP file and navigate to the project folder.

## Setting Up the Environment

It is recommended to create a virtual environment to manage dependencies.

### On Windows:
```sh
python -m venv venv
venv\Scripts\activate
```

### On macOS/Linux:
```sh
python -m venv venv
source venv/Scripts/activate
```

## Installing Dependencies

After activating the virtual environment, install the required Python packages:
```sh
pip install -r requirements.txt
```

## Running the Chatbot

### Using VS Code (Recommended)
1. Open the project folder in VS Code.
2. Ensure the `launch.json` file is correctly set up.
3. Press `F5` to launch the application, which will start `app.py`.

### Using the Command Line
Execute the following command to start the chatbot:
```sh
python app.py
```

## Configuration

- Create a `.env` file in the project and add:
  ```sh
  OPENAI_API_KEY=your_key
  ```

## Troubleshooting

- If you encounter missing dependencies, ensure you are using the correct Python version and try reinstalling:
  ```sh
  pip install -r requirements.txt --upgrade
  ```
- Check error logs in `logs/` for debugging issues.

## Document
For now, I have added some Keynotes And Characteristics[of Homeopathic Medicine] With Comparisons of some of the Leading Remedies of the Materia Medica by Henry Clay Allen, M. D.  

## Example:  

your question: uses of Ruta Graveolens  

answer:
{"answer":"Ruta Graveolens, also known as Rue or Herb of Grace, is a plant with various medicinal uses. Some common uses of Ruta Graveolens include:\n\n1. Relief from arthritis and joint pain: Ruta Graveolens is believed to have anti-inflammatory properties that can help reduce arthritis pain and inflammation in joints.\n\n2. Treatment of skin conditions: The herb is used topically to treat skin conditions like acne, eczema, and psoriasis due to its antibacterial and anti-inflammatory properties.\n\n3. Menstrual pain relief: Ruta Graveolens is often used to alleviate menstrual cramps and other symptoms associated with menstruation.\n\n4. Digestive aid: The herb can be used to improve digestion and treat digestive issues like constipation and bloating.\n\n5. Insect repellent: Ruta Graveolens is known to repel insects and can be used as a natural insect repellent in gardens or as a natural bug spray.\n\nThese are just a few of the many traditional and alternative medicinal uses of Ruta Graveolens. It is important to consult with a healthcare professional before using this herb for medicinal purposes."}
