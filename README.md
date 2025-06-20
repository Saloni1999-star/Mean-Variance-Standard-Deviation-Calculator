# 📊 Mean, Variance & Standard Deviation Calculator

A simple Python project that calculates basic statistical measures — **mean**, **variance**, and **standard deviation** — from a dataset.
About This Project

This version is customized by **Saloni Dhiman** as part of hands-on learning in Python and data analysis. Originally forked and enhanced with clear explanations, structure, and formatting.

---

## 🚀 Features
- Calculates mean, variance, and standard deviation
- Easy-to-read Python functions
- Beginner-friendly and customizable

---

## 📁 Project Files
- `main.py`: Main script to execute the program
- `mean_var_std.py`: Logic and functions
- `README.md`: Project overview and credits

---
### This project is part of freecodecamp data analysis with python

Create a function named `calculate()` in `mean_var_std.py` that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix. 

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix. 

The returned dictionary should follow this format:
```py
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

If a list containing less than 9 elements is passed into the function, it should raise a `ValueError` exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

For example, `calculate([0,1,2,3,4,5,6,7,8])` should return:
```py
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]}
}
```
### Running
Run the main.py it will calucalute the mean, variance, standard deviation. You can also changes the values according to your needs.

## 🧠 Skills Used
- Python
- Mathematical logic
- Code structuring

---

## 👩‍💻 Author
**Saloni Dhiman**
