# Deep Learning Approach for Hate Speech Detection

This project demonstrates a deep learning-based approach for detecting hate speech in text using a Django web application. Users can input text, and the system will classify it as hate speech or not, providing a simple and effective interface for real-time predictions.

---

## Features

- **Hate Speech Detection**: Classifies whether a given text is hate speech or not using a deep learning model.
- **Django Web Interface**: Allows users to interact with the model through a user-friendly web interface.
- **Model Training**: The system uses a deep learning model trained on a dataset to predict hate speech.

---

## Requirements

To run this project, ensure the following dependencies are installed:

- **Python**: Version 3.7 or above
- **Libraries**:
  - Django
  - TensorFlow
  - Keras
  - Numpy
  - Scikit-learn

Install the required libraries by running:
```bash
pip install -r requirements.txt
```

---

## Setup and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rohanvenkatesha/Deep-Learning-Approach-for-Hate-Speech-Detection
   cd Deep-Learning-Approach-for-Hate-Speech-Detection
   ```

2. **Prepare the Dataset**:
   - Unzip the `txt_sentoken.zip` file into the `Parre` directory. This dataset will be used to train the hate speech detection model.

3. **Run the Django Server**:
   - Navigate to the `Paree_web/website/` directory:
   ```bash
   cd Paree_web/website/
   ```
   - Start the Django development server:
   ```bash
   python manage.py runserver
   ```

4. **Access the Web Interface**:
   - Open your web browser and go to `http://127.0.0.1:8000/` to use the web interface and classify text as hate speech or not.

---

## File Structure

```plaintext
Deep-Learning-Approach-for-Hate-Speech-Detection/
├── requirements.txt                # List of required dependencies
├── Paree_web/                      # Main directory for the Django web application
│   └── website/                    # Django website directory
│       ├── manage.py               # Django management file
│       ├── templates/              # HTML templates for the web app
│       ├── static/                 # Static files (CSS, JS, images)
│       ├── db.sqlite3              # Database file for Django app
│       ├── model1.h5               # Trained model file 1
│       ├── model2.h5               # Trained model file 2
│       ├── tokenizer.pickle        # Tokenizer used for text preprocessing
│       └── views.py                # Views and URL routing for the web app
├── Parre/                          # Directory for dataset and data preprocessing
│   ├── txt_sentoken.zip            # Text dataset for model training
│   ├── final_data.csv              # Final dataset for model training
│   ├── hasoc.csv                   # Additional dataset for hate speech detection
│   ├── model1.h5                   # Pre-trained model file 1
│   ├── model2.h5                   # Pre-trained model file 2
│   ├── tokenizer.pickle            # Tokenizer for text preprocessing
│   ├── parre.ipynb                 # Jupyter notebook for data analysis and preprocessing
│   ├── new_noteBook.ipynb          # Additional Jupyter notebook for model training or testing
│   ├── test.py                     # Python script for testing the model
│   └── vocab.txt                   # Vocabulary file for model training
└── README.md                       # Project documentation
```

---

## Model Information

- **Dataset**: The model is trained on the `txt_sentoken.zip` dataset, which contains text data labeled as either hate speech or non-hate speech.
- **Model**: The deep learning model uses advanced techniques like LSTM or CNN for text classification.
- **Model Files**: Pre-trained model files are located under the `Paree_web/website/` and `Parre/` directories as `model1.h5` and `model2.h5`.

---

## Future Improvements

- **Multilingual Support**: Expand the model to support multiple languages for hate speech detection.
- **Enhanced Preprocessing**: Implement more advanced text preprocessing techniques such as stemming, lemmatization, and stopword removal.
- **Real-Time Text Analysis**: Extend the system to analyze text from real-time sources such as social media or live chat.
- **Improve Model Accuracy**: Train the model on more diverse datasets to improve accuracy and robustness.

---
