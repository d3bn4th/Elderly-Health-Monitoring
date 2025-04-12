import pandas as pd
from sqlalchemy import create_engine
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read the CSV file
csv_path = os.path.join(script_dir, 'fall_dataset.csv')
df = pd.read_csv(csv_path)

try:
    # Create MySQL connection
    engine = create_engine('mysql+mysqlconnector://root:@localhost/fall_detection')
    
    # Import the data
    df.to_sql('measurements', 
              engine, 
              if_exists='append',
              index=False,
              chunksize=1000)
    
    print("Data imported successfully!")
    print(f"Total records imported: {len(df)}")
    
    # Print some basic statistics
    print("\nData Summary:")
    print(f"Number of unique users: {df['user_id'].nunique()}")
    print("\nDecision categories distribution:")
    print(df['Decision'].value_counts().to_dict())

except Exception as e:
    print(f"Error: {e}")
    print("\nTroubleshooting tips:")
    print("1. Make sure MySQL is running")
    print("2. Check if the database 'fall_detection' exists")
    print("3. Verify that you have the necessary permissions")
    print("4. Ensure all required Python packages are installed (pandas, sqlalchemy, mysql-connector-python)") 