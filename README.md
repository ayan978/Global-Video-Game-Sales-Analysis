# Global Video Game Sales Analysis

This project performs an end-to-end exploratory data analysis (EDA) and predictive modeling on a global video game sales dataset. The goal is to understand historical sales trends and build a model to predict global sales based on various features like platform, genre, and publisher.

---

## Dataset

- **Source**: [Insert dataset source if public, or say “Kaggle/Provided”]
- **Description**: Contains records of over 16,000 video games with features including:
  - Name, Platform, Year of Release
  - Genre, Publisher, Critic and User Scores
  - Regional Sales (NA, EU, JP, Others)
  - Global Sales

---

## Objectives

- Clean and preprocess raw data
- Explore trends in sales across time, region, platform, and genre
- Visualize key patterns using Python libraries
- Build regression models to predict global sales
- Evaluate and compare model performance

---

## Data Cleaning

- Removed missing and duplicate entries
- Standardized column formats (e.g., year as integer)
- One-hot encoded categorical features
- Dropped irrelevant or highly missing columns

---

## Exploratory Data Analysis (EDA)

- Top publishers and platforms by global sales
- Sales trends over time
- Genre distribution and regional preferences
- Correlation heatmaps for numeric features
- Interactive and static visualizations (Seaborn, Matplotlib)

---

## Modeling

- **Models Used**:
  - Linear Regression
  - Random Forest Regressor
- **Features**:
  - Platform, Genre, Year, Publisher (encoded)
  - Critic and User Scores
- **Evaluation Metrics**:
  - R² Score, RMSE, MAE
- **Best Model**: [Insert your best-performing model here]

---

## Results & Insights

- Platform and genre significantly impact sales
- NA and EU markets are most influential in global trends
- Random Forest performed better than linear models
- Predictive accuracy was acceptable for high-level business insights

---