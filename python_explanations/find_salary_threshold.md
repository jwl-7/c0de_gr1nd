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
* BLANK

## Code Dissection
1. BLANK