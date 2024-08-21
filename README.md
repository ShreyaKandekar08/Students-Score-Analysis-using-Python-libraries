# Students-Score-Analysis-using-Python-libraries

This project analyzes the relationship between various socio-demographic factors and student scores in mathematics, reading, and writing. The analysis aims to uncover patterns and insights based on gender, parental education level, marital status, and ethnic group.

## Project Overview

The dataset used in this project contains information on students' scores across three subjects: Mathematics, Reading, and Writing, along with their gender, parental education level, marital status, and ethnic group.

## Key Steps in the Analysis:

1. Data Loading and Cleaning:
   - The dataset is loaded, and any unnecessary columns are dropped.
   - The data is inspected for null values and basic statistical information.

2. Gender Distribution Analysis:
   - A count plot is used to visualize the distribution of genders within the dataset.
   - Insight: The number of females in the dataset is higher than the number of males.

3. Impact of Parental Education on Scores:
   - The average scores in Mathematics, Reading, and Writing are calculated based on the parents' education levels.
   - A heatmap is used to visualize the relationship between parental education and student scores.
   - Insight: Parental education has a positive impact on student scores.

4. Impact of Parental Marital Status on Scores:
   - The average scores are also calculated based on the parents' marital status.
   - A heatmap is used to explore this relationship.
   - Insight: The marital status of parents has a negligible or no impact on student scores.

5. Outlier Detection:
   - Box plots are used to detect extreme values in student scores.

6. Ethnic Group Distribution:
   - The distribution of students across different ethnic groups is visualized using a pie chart.

### Visualizations:

- **Count Plot:** Gender distribution.
- **Heatmaps:** Relationships between parental education/marital status and student scores.
- **Box Plots:** Outlier detection for scores.
- **Pie Chart:** Distribution of ethnic groups.

### Conclusion:

The analysis reveals that parental education plays a significant role in students' academic performance, while parental marital status appears to have little impact. Additionally, the dataset showcases a diverse representation of students across different ethnic groups.

## How to Run the Code

1. Clone the repository to your local machine.
2. Ensure you have Python installed along with the necessary libraries (`numpy`, `pandas`, `matplotlib`, and `seaborn`).
3. Run the Python script to generate the visualizations and analysis.

## Dependencies

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

