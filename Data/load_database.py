import mysql.connector
import csv
import os
from mysql.connector import Error

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': '',  # Replace with your MySQL password
    'database': 'elderly_health_monitoring'
}

def create_database():
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
            
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_tables():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Read and execute SQL schema
            with open('create_tables.sql', 'r') as file:
                sql_commands = file.read()
                
            # Split commands and execute each one
            for command in sql_commands.split(';'):
                if command.strip():
                    cursor.execute(command)
                    
            connection.commit()
            print("Tables created successfully")
            
    except Error as e:
        print(f"Error creating tables: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def load_data_from_csv():
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
                # Read CSV file
                with open(csv_file, 'r') as file:
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
        print(f"Error loading data: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():
    print("Starting database setup...")
    
    # Create database
    create_database()
    
    # Create tables
    create_tables()
    
    # Load data from CSV files
    load_data_from_csv()
    
    print("Database setup completed successfully!")

if __name__ == "__main__":
    main() 