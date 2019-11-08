from test_framework import generic_test


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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
