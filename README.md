# Elderly Health Monitoring Database Setup

This directory contains scripts and data files to set up the Elderly Health Monitoring database.

## Prerequisites

1. MySQL Server installed and running
2. Python 3.x installed
3. pip (Python package installer)

## Setup Instructions

1. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure database connection:
   - Open `load_database.py`
   - Update the DB_CONFIG dictionary with your MySQL credentials:
     ```python
     DB_CONFIG = {
         'host': 'localhost',
         'user': 'your_username',
         'password': 'your_password',
         'database': 'elderly_health_monitoring'
     }
     ```

3. Run the database setup script:
   ```bash
   python load_database.py
   ```

The script will:
- Create the database if it doesn't exist
- Create all necessary tables
- Load data from CSV files into the tables

## Data Files

The following CSV files will be loaded into the database:
- users.csv
- mental_health.csv
- lifestyle.csv
- sleep_disorders.csv
- falls_fractures.csv
- mobility.csv
- vision_audition.csv
- weight_bmi.csv
- sleep_duration_quality.csv
- sleep_activity.csv
- vitals_backup.csv
- heart_rate.csv

## Schema

The database schema is defined in `create_tables.sql` and includes tables for:
- User information
- Mental health metrics
- Lifestyle factors
- Sleep patterns and disorders
- Physical mobility
- Vision and hearing assessments
- Vital signs and measurements
- Activity tracking 