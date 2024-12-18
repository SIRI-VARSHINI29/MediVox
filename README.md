# MediVox: Conversational Healthcare Bot

## Introduction

MediVox is a user-friendly and accessible healthcare bot designed to revolutionize how individuals interact with health-related information and support. By harnessing advanced technologies such as **Natural Language Processing (NLP)**, **Artificial Intelligence (AI)**, and **Speech Recognition**, MediVox enables meaningful and human-like conversations about health. Its goal is to make healthcare information more accessible, personalized, and empathetic.

## Key Features

MediVox facilitates a wide range of healthcare-related tasks, including:

1. **Providing Healthcare Information**:  
   - Users can inquire about symptoms, conditions, treatments, medications, and general health advice.  
   - MediVox delivers accurate, relevant, and timely information in response.

2. **Symptom Assessment**:  
   - Users can describe their symptoms using natural language or speech.  
   - MediVox assesses symptom severity and provides guidance on the next steps.

3. **Personalized Health Recommendations**:  
   - By collecting user data and preferences, MediVox offers tailored recommendations for maintaining health, managing conditions, and seeking medical care.

4. **Telemedicine Appointment Facilitation**:  
   - MediVox helps users schedule appointments with healthcare providers, locate nearby clinics or hospitals, and access information about available healthcare services.

5. **Emotional Support and Guidance**:  
   - In addition to delivering information, MediVox offers empathy, encouragement, and advice for managing chronic conditions, mental health issues, or lifestyle changes.

## Technologies Used

The MediVox project leverages:

- **Speech Recognition**: Converts spoken commands into text using the `SpeechRecognition` library.
- **Text-to-Speech**: Provides audio responses via the `pyttsx3` library.
- **Natural Language Processing**:
  - **NLTK** for tokenization, lemmatization, and stop word removal.
  - **Scikit-learn** for TF-IDF vectorization and similarity calculations.
- **Artificial Intelligence**: Adaptive learning from user interactions to improve response accuracy.
- **JSON**: Stores and manages intents, patterns, and responses.

## Prerequisites

To set up and run MediVox, ensure the following:

1. Python 3.7+ installed.
2. Install required libraries:
   ```bash
   pip install SpeechRecognition pyttsx3 nltk scikit-learn
   ```
3. Download necessary NLTK data:
   ```python
   nltk.download('punkt')
   nltk.download('wordnet')
   nltk.download('stopwords')
   ```

## How to Run

1. Clone the repository or download the project files.
2. Ensure the `intents.json` file is configured with healthcare-related queries and responses.
3. Connect a microphone to your system.
4. Run the `main.py` file:
   ```bash
   python main.py
   ```
    Run the `ui.py` file:
   ```bash
   python ui.py
   ```
5. Speak your queries, such as:
   - "What are the symptoms of a cold?"
   - "How do I treat a fever?"

## Future Enhancements

- Expand intents to cover more health conditions and queries.
- Add multilingual support for broader accessibility.
- Integrate dynamic data sources for real-time updates (e.g., health alerts).
- Include visual analytics for health monitoring.


