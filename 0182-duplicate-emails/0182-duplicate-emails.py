import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    count=person.groupby('email').size().reset_index(name='count1')
    duplicates=count[count['count1']>1]
    return duplicates[['email']].rename(columns={'email':'Email'})
    