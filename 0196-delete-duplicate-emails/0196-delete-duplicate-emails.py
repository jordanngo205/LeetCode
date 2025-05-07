import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort by 'id' so smallest id comes first for each email
    person.sort_values(by='id', inplace=True)

    # Drop duplicates, keeping the first occurrence (i.e. the smallest id)
    person.drop_duplicates(subset='email', keep='first', inplace=True)

    # Optional: reset index (not required unless formatting matters)
    person.reset_index(drop=True, inplace=True)
