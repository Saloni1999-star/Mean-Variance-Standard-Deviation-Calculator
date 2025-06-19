# Mean Variance Standard Deviation Calculator

This project provides a simple calculator for computing the mean, variance, standard deviation, maximum, minimum, and sum of a 3x3 matrix derived from a list of nine numbers. The calculations are performed using the `numpy` library for efficient numerical operations.

## Installation

To get started, clone the repository and navigate to the project directory. You can install the required dependencies using pip. 

```bash
pip install -r requirements.txt
```

## Usage

To use the Mean Variance Standard Deviation Calculator, you can import the `calculate` function from the `mean_var_std` module and pass a list of nine numbers.

### Example

```python
from mean_var_std import calculate

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = calculate(data)

print(result)
```

### Output

The output will be a dictionary containing the calculated values:

```python
{
    'mean': [[4.0, 5.0, 6.0], [2.0, 5.0, 8.0], 5.0],
    'variance': [[6.0, 6.0, 6.0], [6.0, 6.0, 6.0], 6.0],
    'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [2.449489742783178, 2.449489742783178, 2.449489742783178], 2.449489742783178],
    'max': [[7, 8, 9], [4, 5, 6], 9],
    'min': [[1, 2, 3], [1, 2, 3], 1],
    'sum': [[12, 15, 18], [6, 15, 24], 45]
}
```

## Running Tests

To ensure the functionality of the calculator, you can run the unit tests provided in the `tests` directory. Make sure you have `pytest` installed, then run:

```bash
pytest tests/test_mean_var_std.py
```

This will execute the test cases and validate the behavior of the `calculate` function.

## License

This project is licensed under the MIT License.