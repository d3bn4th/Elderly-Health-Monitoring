import mysql.connector
import csv
import os
import sys
from mysql.connector import Error

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': '',  # Replace with your MySQL password
    'database': 'elderly_health_monitoring'
}

# Path to the Data directory
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Data')

def test_connection(config):
    """Test the database connection with given configuration"""
    try:
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password']
        )
        if connection.is_connected():
            print("Successfully connected to MySQL server")
            connection.close()
            return True
    except Error as e:
        print(f"Error connecting to MySQL server: {e}")
        print("\nPlease check your MySQL credentials and ensure the server is running.")
        print("You may need to:")
        print("1. Start your MySQL server")
        print("2. Update the DB_CONFIG in this script with correct credentials")
        print("3. Ensure you have necessary permissions")
        return False
    return False

def create_database():
    """Create the database if it doesn't exist"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
            print(f"Database {DB_CONFIG['database']} created successfully")
            return True
            
    except Error as e:
        print(f"Error creating database: {e}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def create_tables():
    """Create all tables using the SQL schema"""
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Read and execute SQL schema
            schema_path = os.path.join(DATA_DIR, 'schema.sql')  # Changed from create_tables.sql to schema.sql
            if not os.path.exists(schema_path):
                print(f"Error: Schema file not found at {schema_path}")
                return False
                
            with open(schema_path, 'r') as file:
                sql_commands = file.read()
                
            # Split commands and execute each one
            for command in sql_commands.split(';'):
                if command.strip():
                    cursor.execute(command)
                    
            connection.commit()
            print("Tables created successfully")
            return True
            
    except Error as e:
        print(f"Error creating tables: {e}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def load_data_from_csv():
    """Load data from all CSV files into their respective tables"""
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # List of tables and their corresponding CSV files
            tables = {
                'users': 'users.csv',
                'mental_health': 'mental_health.csv',
                'lifestyle': 'lifestyle.csv',
                'sleep_disorders': 'sleep_disorders.csv',
                'falls_fractures': 'falls_fractures.csv',
                'mobility': 'mobility.csv',
                'vision_audition': 'vision_audition.csv',
                'weight_bmi': 'weight_bmi.csv',
                'sleep_duration_quality': 'sleep_duration_quality.csv',
                'sleep_activity': 'sleep_activity.csv',
                'vitals_backup': 'vitals_backup.csv',
                'heart_rate': 'heart_rate.csv'
            }
            
            for table, csv_file in tables.items():
                csv_path = os.path.join(DATA_DIR, csv_file)
                if not os.path.exists(csv_path):
                    print(f"Warning: CSV file not found at {csv_path}")
                    continue
                    
                try:
                    # Read CSV file
                    with open(csv_path, 'r') as file:
                        csv_reader = csv.reader(file)
                        headers = next(csv_reader)  # Skip header row
                        
                        # Create the INSERT query
                        placeholders = ', '.join(['%s'] * len(headers))
                        query = f"INSERT INTO {table} ({', '.join(headers)}) VALUES ({placeholders})"
                        
                        # Insert data
                        for row in csv_reader:
                            cursor.execute(query, row)
                        
                        connection.commit()
                        print(f"Data loaded into {table} successfully")
                except Error as e:
                    print(f"Error loading data into {table}: {e}")
                    connection.rollback()
            
            return True
            
    except Error as e:
        print(f"Error connecting to database: {e}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def main():
    print("Starting database setup...")
    
    # Test connection first
    if not test_connection(DB_CONFIG):
        sys.exit(1)
    
    # Create database
    if not create_database():
        sys.exit(1)
    
    # Create tables
    if not create_tables():
        sys.exit(1)
    
    # Load data from CSV files
    if not load_data_from_csv():
        sys.exit(1)
    
    print("Database setup completed successfully!")

if __name__ == "__main__":
    main() 