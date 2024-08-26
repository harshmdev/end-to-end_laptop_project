# Laptop Price Prediction

A machine learning project that predicts laptop prices based on various specifications such as RAM, processor, storage, display size, and other features.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Features](#features)
- [Model and Methodology](#model-and-methodology)
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Project Description

This project uses machine learning to predict the prices of laptops based on their specifications. By analyzing various features like RAM, processor type, storage capacity, display size, and more, the model aims to provide accurate price predictions.

- Price: The retail price of the laptop, typically in the local currency (e.g., USD, INR). This is the target variable the model aims to predict.

- Brand: The manufacturer or brand name of the laptop (e.g., Dell, HP, Lenovo). This feature helps capture brand-related price variations.

- Utility: The primary intended use of the laptop, such as gaming, business, or general use. This categorization helps in understanding the laptop’s market segment.

- Weight: The weight of the laptop, usually in kilograms (kg). It influences portability and often correlates with other features like battery capacity and display size.

- Warranty: The warranty period provided by the manufacturer, usually in years. A longer warranty can be a sign of higher quality or confidence in the product.

- Display Size: The size of the laptop's screen, measured diagonally in inches. Larger displays often correlate with higher prices due to increased material costs and enhanced user experience.

- PPI (Pixels Per Inch): The pixel density of the display, which affects the sharpness and clarity of the screen. Higher PPI usually means a better display quality.

- Touch Screen: A binary indicator (1 or 0) showing whether the laptop has a touch-enabled screen. Touch screens are often more expensive due to additional technology and manufacturing costs.

- RAM: The amount of Random Access Memory (RAM) in gigabytes (GB). More RAM allows for better multitasking and performance, especially in memory-intensive applications.

- SSD: The storage capacity of the Solid-State Drive (SSD) in gigabytes (GB). SSDs are faster and more expensive than traditional hard drives, significantly affecting the laptop's price.

- Graphic: The type or model of the graphics processing unit (GPU) in the laptop. High-end GPUs are crucial for gaming, video editing, and other graphics-intensive tasks, often raising the laptop's price.

- Core: The number of processor cores in the laptop's CPU. More cores allow for better parallel processing and improved performance, particularly in demanding applications.

- HDMI: A binary indicator (1 or 0) showing whether the laptop has an HDMI port, which is used for video output to external displays. The presence of an HDMI port can add to the laptop's versatility.

- Backlit Keyboard: A binary indicator (1 or 0) indicating whether the laptop has a backlit keyboard. This feature is often associated with higher-end laptops and improves usability in low-light conditions.

- Battery Capacity: The battery capacity, usually measured in watt-hours (Wh). Higher battery capacity typically offers longer battery life, which is a crucial selling point for portable devices.

- Processor: The specific model of the laptop's central processing unit (CPU). The processor type is a significant determinant of overall performance and pricing.



## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/harshmdev/end-to-end_laptop_project.git
   cd end-to-end_laptop_project
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the main.py**
   ```cmd
   python run main.py
   ```
4. **Run streamlit app**
   ```cmd
   streamlit run app.py
   ```

   - If you have implemented a web interface for predictions:
     ```bash
     streamlit run app.py
     ```

## Features

- Predict laptop prices based on various specifications.
- Clean and preprocess raw data for modeling.
- Train and evaluate machine learning models.
- Web interface for easy predictions.
- Analytics Module for analysis on the data.

## Model and Methodology
- **Data Gathering**: It will scrape the website and export the data in csv format.
- **Data Ingestion**: Pick the gathered data and make it little ready for further processing.
- **Data Preprocessing**: Cleaned the data , prepare the data for further cleaning.
- **Data Cleaning**: Completely clean the data , make columns in correct format .
- **Missing Value Imputation**: Fill all the missing values and also Extracted relevant features like RAM, storage, processor, etc., from the dataset
- **Feature Selection**: Select necessary features for model building.
- **Modeling Selection and Evaluation**: Used models such as Linear Regression, Random Forest, and SVR for prediction.Evaluated models using metrics like R2-squared, find std, mean absolute error.
- **Recommender System** : A system to predict laptop prices based on the user inputs.



## License

This project is licensed under the Apache License - see the `LICENSE` file for details.

## Authors

- **Harsh Mohan** - *Initial work* - [Your Profile](https://github.com/your-username)

## Acknowledgments

- Thanks to the open-source libraries used in this project.
- Special thanks to the data sources.
- Inspiration for the project from various online tutorials and articles.
