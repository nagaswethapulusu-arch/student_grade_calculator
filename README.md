# Student Grade Calculator

A beginner-friendly Python project that assigns a grade to each student based on their marks using **if, elif, and else** statements. It also detects invalid marks (below 0 or above 100).

## Objective

Practice conditional statements and apply them to a simple data analysis problem.

## Tools Used

- Python 3
- Jupyter Notebook

## Dataset

A manually created dataset of 10 students stored in two Python lists. The last two entries are included on purpose to test a failing mark and an invalid mark.

| Student | Marks |
|---------|-------|
| Asha    | 78    |
| Ravi    | 85    |
| Meena   | 62    |
| Kiran   | 90    |
| Swetha  | 71    |
| Harsh   | 89    |
| Rupesh  | 70    |
| Akhil   | 65    |
| Divya   | 45    |
| Teja    | 105   |

## Grading Logic

| Marks        | Grade   |
|--------------|---------|
| 90 - 100     | A       |
| 80 - 89      | B       |
| 70 - 79      | C       |
| 60 - 69      | D       |
| Below 60     | F       |
| < 0 or > 100 | Invalid |

## Approach

1. **Store the data** in two lists: `students` (names) and `marks` (scores).
2. **Create a function** `get_grade(mark)` that uses `if`, `elif`, and `else` to return a grade.
3. **Check for invalid marks first.** If marks are below 0 or above 100, the function returns "Invalid". This check must come first, otherwise a value like 105 would match `mark >= 90` and wrongly get an "A".
4. **Check grade ranges from highest to lowest.** Python checks conditions from top to bottom and runs the first one that is true, so each mark gets exactly one grade.
5. **Loop through the data** using `zip(students, marks)` and print each student's marks with the assigned grade in a neat table.

## How to Run

1. Install Python and Jupyter Notebook:
   ```
   pip install notebook
   ```
2. Clone or download this repository.
3. Open a terminal in the project folder and run:
   ```
   jupyter notebook
   ```
4. Open `student_grade_calculator.ipynb`.
5. Run all cells from top to bottom (`Shift + Enter`).

## Sample Output

```
Student   Marks   Grade
Asha      78      C
Ravi      85      B
Meena     62      D
Kiran     90      A
Swetha    71      C
Harsh     89      B
Rupesh    70      C
Akhil     65      D
Divya     45      F
Teja      105     Invalid
```

## Testing

The program was tested with different kinds of marks:

- Normal marks in every grade range (A, B, C, D)
- A failing mark (45 gives F)
- An invalid mark (105 gives Invalid)

## Limitations

- Grade boundaries are fixed in the code and need to be edited manually to change them.
- Marks are typed in manually instead of being read from a file.

## Possible Improvements

- Read marks from a CSV file.
- Calculate the class average and grade distribution.
- Accept user input and keep asking until valid marks are entered.

## Author

SwethaPulusu
