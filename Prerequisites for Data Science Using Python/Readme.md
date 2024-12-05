
## **Introduction**
***
- Welcome to this session on **Prerequisites for Data Science**.
- In this session, I’ll walk you through the foundational skills and tools you need to get started.
  
### **What is Data Science?**
***
**Data Science** is an interdisciplinary field that focuses on extracting knowledge and actionable insights from structured (***This data is organized in a fixed format, such as a table, and is easy to search and analyze***) and unstructured data (***This data is not organized in a predefined format and can be in many different forms, such as audio and video files, emails, and text messages***). It combines principles from:
1. **Mathematics and Statistics**: To analyze data patterns and relationships.
2. **Computer Science and Programming**: To process, manage, and manipulate large datasets.
3. **Domain Expertise**: To apply data-driven solutions effectively in specific industries.
   
### **Real-World Applications of Data Science**
***
1. **Healthcare**: Predicting diseases, personalizing treatments, and improving patient outcomes.
2. **Finance**: Fraud detection, credit scoring, and stock market analysis.
3. **Retail**: Customer segmentation, sales forecasting, and inventory management.
4. **Transportation**: Route optimization, predictive maintenance, and autonomous vehicles.
5. **Entertainment**: Content recommendations on platforms like Netflix or Spotify.

### **Why is Python Good for Data Science?**
***
Python is a high-level, general-purpose programming language known for its simplicity and versatility. Python has become the most popular language for data science, and here's why:
#### 1. **Ease of Use and Readability**
- Python’s simple syntax makes it easy to learn and use, even for beginners.
- Its natural language-like structure enables data scientists to focus on solving problems rather than understanding code.
#### 2. **Rich Ecosystem of Libraries and Frameworks**
Python has a vast collection of libraries tailored for data science:
- **Data Manipulation**: `pandas`, `numpy`
- **Data Visualization**: `matplotlib`, `seaborn`, `plotly`
- **Machine Learning**: `scikit-learn`, `TensorFlow`, `PyTorch`
- **Big Data Processing**: `Dask`, `PySpark`
#### 3. **Integration with Other Tools**
- Python integrates seamlessly with other languages and tools like SQL, R, and big data platforms like Hadoop and Spark.
- It works well with various data formats (CSV, Excel, JSON, databases, etc.).
#### 4. **Open-Source and Community Support**
- Python is free to use and open-source, with a massive global community.
- Abundant resources, forums, and tutorials make problem-solving easier.
#### 5. **Support for Automation**
- Python scripts can automate repetitive tasks, like data cleaning, saving time for more complex analyses.
#### 7. **Extensive Data Science Frameworks**
- Python frameworks streamline data science workflows:
    - **Jupyter Notebooks**: Interactive coding environment for data exploration and visualization.
    - **Google Colab**: Cloud-based Python environment.

>[!note]
>https://learnxinyminutes.com/docs/python/ 
## **1. Downloading Python**
***
- Visit [python.org](https://python.org) and download the latest version of Python.
- During installation, **check the box to add Python to PATH**—this is essential for running Python from the command line.
- Choose an **IDE** to code in:
  - **Jupyter Notebook**: Interactive and great for data science.
  - **VS Code** or **PyCharm**: Ideal for larger projects.

## **2. Basics of Python Coding**
***
- Python is simple and versatile. Here’s what you need to know:
  - **Variables and Data Types**: `x = 10`, `name = "Alice"`.
  - **Control Flow**: 
    ```python
    if x > 5:
        print("x is greater than 5")
    for i in range(3):
        print(i)
    ```
  - Practice basic operations to build confidence.

## **3. Using Comments in Python**
***
- Comments help make your code readable:
  - Single-line: `# This is a comment`
  - Multi-line: 
    ```python
    """
    This is a
    multi-line comment
    """
    ```
- Always document what your code does for better collaboration and understanding.
  
## **4. Executing Commands**
***
- Run Python scripts using:
  - Command line: `python script.py`
  - IDE: Use the **Run** button or an integrated terminal.
## **5. Importing Packages/Libraries**
***
A package is a collection of different modules. Modules are nothing but files with python code
- Python's power lies in its libraries:
    - Install with `pip`: `pip install pandas`
    - Import with:  `import pandas as pd import numpy as np`
- Commonly used libraries for Data science are `pandas`, `numpy`, and `matplotlib`

## 6. How to get Data in python
***
### **6.1. Install pandas**: 
Before using pandas, you need to install it if it’s not already installed:
```python
pip install pandas
```
### **6.2. Import pandas**
After installing pandas, you need to import it in your Python script:
```python
import pandas as pd
```
## 7. Loading Data into Python Using pandas
***
#### a. **Loading Data from a CSV File**
One of the most common formats is CSV (Comma Separated Values). To load a CSV file into a pandas Data Frame(a two-dimensional, labeled data structure, similar to a table or a spreadsheet, where data is organized in rows and columns.):

```python
import pandas as pd  
# Load data from a CSV file 
data = pd.read_csv('path_to_file.csv')  
# Display the first 5 rows of the DataFrame 
print(data.head())
```

- **`pd.read_csv()`**: Reads a CSV file and returns a DataFrame.
- **`head()`**: Displays the first 5 rows of the DataFrame.
  
#### b. **Loading Data from an Excel File**

If you have data in an Excel file (`.xlsx`), use **`read_excel()`**:
```python
import pandas as pd 
# Load data from an Excel file 
data = pd.read_excel('path_to_file.xlsx', sheet_name='Sheet1') 
# Display the first 5 rows 
print(data.head())
```

#### Example

```python
import pandas as pd 
# Create a dictionary with data 
data = { 
"Name": ["Alice", "Bob", "Charlie"],
"Age": [25, 30, 35],
"City": ["New York", "Los Angeles", "Chicago"]
 } 
# Create a DataFrame from the dictionary 
df = pd.DataFrame(data) 
# Display the DataFrame 
print(df)
```
## 8. Saving Output in Python
***
In Python, you often need to save your output for later use, whether it's to a file, a database, or some other medium. Saving output is crucial for data persistence and further analysis. Below are some common ways to save output in Python:
### 8.1. **Saving to a CSV File**
CSV (Comma-Separated Values) is one of the most common formats for saving data. You can easily write data to a CSV file using the `pandas` library.
```python
import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

# Saving DataFrame to a CSV file
df.to_csv('output.csv', index=False)
```
>[!note]
**`to_csv()`**: This function writes the DataFrame to a CSV file. The `index=False` argument prevents pandas from writing the index (row labels) to the file.

### 8.2. **Saving to an Excel File**
For more structured data storage, Excel files are widely used in business and finance.
```python
df.to_excel('output.xlsx', index=False)
```
>[!note]
 **`to_excel()`**: This saves the DataFrame to an Excel file. You can also specify the sheet name using the `sheet_name` argument.


## 9.Accessing Data in pandas DataFrame
***
A pandas DataFrame is a table-like structure where data is stored in rows and columns. You can access columns, rows, or individual cells using various methods:
#### 9.1 Accessing Columns:

```python
import pandas as pd 
# Sample DataFrame 
df = pd.DataFrame({
 "Name": ["Alice", "Bob", "Charlie"],
 "Age": [25, 30, 35],
 "City": ["New York", "Los Angeles", "Chicago"]
 })  
 # Accessing a single column 
 print(df['Name'])
```

Use the column name inside square brackets to get the entire column.
#### 9.2 Accessing Rows:

```python
#Accessing a specific row using the `iloc` indexer (by position) 
print(df.iloc[1])  # Accesses the second row
```

 **`iloc[]`**: Allows you to access rows by their numerical index.
#### 9.3 Accessing Specific Cells:

```python
# Accessing a specific cell using `iloc` for rows and columns 
print(df.iloc[1, 2])  # Accesses the cell in row 2, column 3
```

Use `iloc[]` with both row and column indices.

