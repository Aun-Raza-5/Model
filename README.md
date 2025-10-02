# Autism Spectrum Disorder (ASD) Predictor

This repository contains a Python-based desktop application that screens for Autism Spectrum Disorder (ASD) in children using a machine learning model. The tool provides an interactive questionnaire and instantly predicts ASD likelihood based on user responses.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [File Structure](#file-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Model Details](#model-details)
- [Questionnaire](#questionnaire)
- [Prediction Output](#prediction-output)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

This ASD Predictor is a graphical user interface (GUI) written in Python using Tkinter. It guides caregivers through a series of questions about a child’s behavior and background, then uses a trained machine learning model to estimate the probability that the child is on the autism spectrum.

---

## Features

- **Interactive Questionnaire:** 18+ child-focused questions covering behavioral, social, and developmental indicators.
- **Intuitive GUI:** Clean, scrollable form with clear instructions and accent colors.
- **Immediate Prediction:** Shows ASD/Non-ASD result and confidence score based on responses.
- **Visual Feedback:** Probability bar chart for prediction confidence.
- **Supports Pre-trained Model:** Uses saved scikit-learn model and encoders for rapid inference.
- **Modular Design:** Easily adapt questions, encoders, or model.

---

## File Structure

- `app.py`: Main application code (Tkinter GUI, prediction logic).
- `best_model.pkl`: Pre-trained machine learning model (pickle file).
- `encoders.pkl`: Fitted encoders for categorical variables.
- `feature_names.pkl`: List of model feature names.

---

## Getting Started

### Prerequisites

- Python 3.7+
- `pip` for Python package management

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Aun-Raza-5/Model.git
    cd Model
    ```
2. Install dependencies:
    ```bash
    pip install pandas matplotlib scikit-learn
    ```

3. Ensure the following files are in the project root:
    - `app.py`
    - `best_model.pkl`
    - `encoders.pkl`
    - `feature_names.pkl`

---

## Usage

Run the application:
```bash
python app.py
```

- The GUI will launch, presenting questions about the child.
- Enter/select responses for each question.
- Click **Predict**.
- A popup window will show the prediction result (ASD/Non-ASD) and probability chart.

---

## Model Details

- **Model File:** `best_model.pkl` (scikit-learn model)
- **Encoders:** Saved label encoders for categorical input fields (`encoders.pkl`)
- **Features Used:** See `feature_names.pkl`

This model was trained on data relevant to ASD screening and expects features in the same format as provided by the GUI.

---

## Questionnaire

Key sample questions:
- Does your child have trouble understanding body language or facial expressions?
- Is your child overly sensitive to sounds, lights, or textures?
- Does your child struggle to start conversations or social interactions?
- What is your relation to the child?
- What is your child's ethnicity and country of residence?
- Has your child been previously diagnosed with autism?

Questions marked with a ⭐ are ranked as important for prediction.

---

## Prediction Output

- **Result:** "🧠 ASD" or "✅ Non-ASD"
- **Probability:** Likelihood score between 0 and 1.
- **Chart:** Bar graph indicating prediction confidence.

---

## Dependencies

- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/)
- [tkinter](https://docs.python.org/3/library/tkinter.html) (standard Python library)

Install with:
```bash
pip install pandas matplotlib scikit-learn
```

---

## Troubleshooting

- **Missing .pkl files:** Ensure all required pickle files are present in the directory.
- **Incorrect input format:** Age must be a number; other fields have dropdowns for valid entries.
- **Prediction error:** If you encounter "Prediction failed," check that your inputs are complete and files are present.

---

## Contributing

Contributions are welcome! Please fork the repository, make changes, and open a pull request with a detailed description.

---

## License

Distributed under the MIT License. See `LICENSE` for details.

---

## Acknowledgements

- Original ASD screening datasets and research
- Python and open-source ML libraries
- All contributors to this project

---

## Contact

For questions or support, please open an issue or contact [Aun-Raza-5](https://github.com/Aun-Raza-5).
