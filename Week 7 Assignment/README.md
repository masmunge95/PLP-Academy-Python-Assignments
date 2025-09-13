# 📊 Student Scores Analysis & Prediction

This project explores and predicts student math performance using Python’s data-science stack.  
It cleans and analyzes a dataset of student demographics and scores, visualizes key trends,  
and builds a **Random Forest classifier** to predict Math Score categories (Low / Medium / High).

---

## ✨ Features

- **Data Cleaning & Preparation**  
  - Handles missing values and encodes categorical variables  
  - Creates derived metrics such as `AvgReadWriteScore`

- **Exploratory Data Analysis (EDA)**  
  - Summary statistics of math, reading, and writing scores  
  - Correlation analysis between reading/writing averages and math performance  
  - Multi-sheet Excel export of all visualization data

- **Machine Learning Model**  
  - Random Forest Classifier with tunable number of trees (`n_estimators`)  
  - Stratified train/test split for balanced evaluation  
  - Confusion matrix and classification report

- **Logging & Versioning**  
  - Each model run (accuracy, confusion-matrix counts, hyper-parameters)  
    is appended to **Prediction_Model_history.xlsx** for easy history tracking.
  - Visualization data saved to a fresh **Visualization_Data.xlsx** file on each run.
  - Cleaned master dataset stored in **Cleaned_student_records_expanded_version.xlsx**.

---

## 🗂 Repository Structure

```
.
├── Students_Scores.ipynb                     # Main analysis & prediction notebook
├── Expanded_data_with_more_features.csv       # Original source dataset
├── Cleaned_student_records_expanded_version.xlsx  # Cleaned and prepared dataset
├── Visualization_Data.xlsx                    # Auto-generated charts data (4 sheets)
├── Prediction_Model_history.xlsx              # Log of model runs and metrics
└── README.md                                  # Project overview (this file)
```

---

## 🛠 Requirements

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

Python 3.8+ is recommended.

---

## 🚀 How to Run

1. **Open the Notebook**  
   Launch Jupyter and open `Students_Scores.ipynb`.

2. **Run All Cells**  
   Execute each cell sequentially.  
   - Data cleaning and EDA will produce inline visualizations.
   - The Random Forest model will output a classification report and confusion matrix.

3. **Outputs**  
   - `Visualization_Data.xlsx` is regenerated with new chart sheets:
     * `LineChart_Data`
     * `BarChart_Data`
     * `Histogram_Data`
     * `ScatterPlot_Data`
   - Model runs (accuracy, confusion-matrix counts) are appended to `Prediction_Model_history.xlsx`.
   - A fully cleaned dataset is saved as `Cleaned_student_records_expanded_version.xlsx`.

---

## ⚡ Performance Notes

- Writing to a brand-new workbook (`Visualization_Data.xlsx`) keeps runtime low (~11 s).  
- Appending multiple sheets to a large existing workbook can be significantly slower.

---

## 📌 Next Steps

- Experiment with other models (e.g., Gradient Boosting, XGBoost).
- Add cross-validation or grid search for hyperparameter tuning.
- Explore fairness metrics to check for bias across demographic groups.

---

## 🧑‍🤝‍🧑 Acknowledgements

This project was created for educational purposes to demonstrate a full  
data-science workflow—from raw scores to predictive modeling.
