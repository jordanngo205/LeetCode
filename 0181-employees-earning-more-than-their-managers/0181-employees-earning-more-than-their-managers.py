import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged=employee.merge(employee,how='inner',left_on='managerId',right_on='id', suffixes=('','_mgr'))
    result = merged[merged['salary']>merged['salary_mgr']]
    return result[['name']].rename(columns={'name':'Employee'})