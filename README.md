# Gender Detection Using Machine Learning

## Overview

Gender Detection Using Machine Learning is a Flask-based web application that predicts whether a given name is Male or Female. The application uses Natural Language Processing (NLP) techniques and a Machine Learning model trained on a dataset of names and their corresponding genders.

The user enters a name through a web interface, and the trained model predicts the gender instantly.

---

## Features

* Predict gender from a given name
* User-friendly web interface
* Machine Learning-based prediction
* Flask backend integration
* Real-time prediction results
* Responsive and modern UI
* Beginner-friendly project structure

---

## Technologies Used

### Frontend

* HTML5
* CSS3

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* CountVectorizer
* Multinomial Naive Bayes

### Other Libraries

* Pandas
* Joblib

---

## Project Structure

GENDER_DETECTIO...
│
|
├── output
│
|   └── Screenshot 2026-06-07 235...
│
├── static
│   └── style.css
│
├── templates
│   └── index.html
│
├── app.py
├── create_dataset.py
├── gender_dataset.csv
├── gender_model.pkl
├── model.py
├── README.md
├── Screenshot 2026-06-07 2350...
└── vectorizer.pkl

---

## Dataset

The dataset contains names and their corresponding genders.

Example:

| Name     | Gender |
| -------- | ------ |
| James    | Male   |
| John     | Male   |
| Mary     | Female |
| Jennifer | Female |

---

## Machine Learning Workflow

1. Load the dataset.
2. Convert names into lowercase format.
3. Extract text features using CountVectorizer.
4. Split data into training and testing sets.
5. Train the Multinomial Naive Bayes model.
6. Evaluate model accuracy.
7. Save the trained model using Joblib.
8. Integrate the model with Flask.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Gender_Detection.git
cd Gender_Detection
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Model Training

```bash
python model.py
```

This will generate:

* gender_model.pkl
* vectorizer.pkl

---

## Run Flask Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Example Prediction

Name:Sameera
Predicted Gender:Female

Name:Sadhik
Predicted Gender:Male

![alt text](<Screenshot 2026-06-07 235027.png>)

## Future Enhancements

* Larger dataset for higher accuracy
* Deep Learning implementation
* Gender probability score
* REST API integration
* Database connectivity
* Deployment on Render or Railway
* Mobile-friendly design

---

## Learning Outcomes

Through this project, you will learn:

* Machine Learning fundamentals
* Text preprocessing
* Feature extraction using NLP
* Model training and evaluation
* Flask web development
* Model deployment basics

---

## Author

SAMEERA.SHAIK

---

## License

This project is developed for educational and learning purposes.
