# Compute a Salary Threshold
Given a list of salaries and a target payroll, compute the salary cap.

## Examples
```
 Input: target = 70
        salaries = [20, 30, 40, 90, 100]
Output: 14.0

 Input: target = 210
        salaries = [20, 30, 40, 90, 100]
Output: 60.0
```

## Solution
```python
def find_salary_cap(target_payroll, current_salaries):
    n = len(current_salaries)
    current_salaries.sort()
    unadjusted = 0.0
    for i, curr in enumerate(current_salaries):
        people = n - i
        adjusted = curr * people
        if unadjusted + adjusted >= target_payroll:
            return (target_payroll - unadjusted) / people
        unadjusted += curr
    return -1
```

## Explanation
Let _T_ = target payroll, _n_ = number of elements, and _k_ = which element:
* The cap _c_ = (_T_ - _A_[_i_]) / (_n_ - _k_)

Let's look at an example:
* _T_ = 120
* _A_ = [20, 30, 40, 90, 100]
1. Calculate payrolls for the caps:
    * Let _x_ = unadjusted
    1. 20 &times; 5 = 100; _x_ = 20
    2. 30 &times; 4 = 120 + 20 = 140; _x_ = 50
    3. 40 &times; 3 = 120 + 50 = 170; _x_ = 90
    4. 90 &times; 2 = 180 + 90 = 270; _x_ = 180
    5. 100 &times; 1 = 100 + 180 = 280
    6. _A_ = [100, 140, 170, 270, 280]
2. _T_ = 120 lies between 100 and 140, which means _c_ lies between 20 and 30
3. Solve for the cap _c_
    1. 20 + 4*c* = 120
    2. 4*c* = 100
    3. _c_ = 25
4. Thus, the salary threshold _c_ = 25.0

## Code Dissection
1. BLANK