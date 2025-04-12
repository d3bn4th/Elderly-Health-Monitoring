# Fall Detection Database Setup

This repository contains a fall detection dataset and instructions for setting it up as a MySQL database.

## Prerequisites

1. **MySQL Server**
   ```bash
   # For macOS (using Homebrew)
   brew install mysql
   brew services start mysql

   # For Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install mysql-server
   sudo systemctl start mysql
   ```

2. **Python Dependencies**
   ```bash
   pip install pandas sqlalchemy mysql-connector-python
   ```

## Database Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create Database and Table
Run the following SQL commands:

```sql
-- Create database
CREATE DATABASE IF NOT EXISTS fall_detection;

-- Use the database
USE fall_detection;

-- Create measurements table
CREATE TABLE measurements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    Distance DECIMAL(10,4),
    Pressure DECIMAL(10,4),
    HRV DECIMAL(10,4),
    `Sugar level` DECIMAL(10,4),
    SpO2 DECIMAL(10,4),
    Accelerometer BOOLEAN,
    Decision TINYINT,
    created_at TIMESTAMP,
    INDEX idx_user_id (user_id),
    INDEX idx_decision (Decision)
);
```

### 3. Import Data
Run the Python script to import the data:
```bash
python import_fall_detection.py
```

### Alternative: Restore from Backup
If you have received a database backup file (`fall_detection_backup.sql`), you can restore it using these steps:

1. Create the database:
```sql
CREATE DATABASE IF NOT EXISTS fall_detection;
USE fall_detection;
```

2. Import the backup:
```bash
# Option 1: Using mysql client
mysql -u [username] -p fall_detection < fall_detection_backup.sql

# Option 2: Using source command within mysql
mysql -u [username] -p
mysql> USE fall_detection;
mysql> source fall_detection_backup.sql;
```

Replace `[username]` with your MySQL username. When prompted, enter your MySQL password.

If the backup file is compressed (`.sql.gz`), first decompress it:
```bash
gunzip fall_detection_backup.sql.gz
```

## Data Description

The dataset contains the following columns:
- `user_id`: Unique identifier for each user
- `Distance`: Distance measurement in meters
- `Pressure`: Pressure measurement
- `HRV`: Heart Rate Variability
- `Sugar level`: Blood sugar level
- `SpO2`: Blood oxygen saturation level
- `Accelerometer`: Boolean value indicating accelerometer status
- `Decision`: Fall detection decision (0: No fall, 1: Potential fall, 2: Confirmed fall)
- `created_at`: Timestamp of the measurement

## Verification

To verify the data import, connect to MySQL and run:
```sql
USE fall_detection;
SELECT COUNT(*) FROM measurements;  -- Should return total number of records
SELECT Decision, COUNT(*) FROM measurements GROUP BY Decision;  -- Distribution of decisions
```

## Troubleshooting

1. **MySQL Connection Issues**
   - Verify MySQL is running:
     ```bash
     # For macOS
     brew services list
     
     # For Ubuntu/Debian
     sudo systemctl status mysql
     ```
   - Check MySQL user permissions:
     ```sql
     GRANT ALL PRIVILEGES ON fall_detection.* TO 'your_username'@'localhost';
     FLUSH PRIVILEGES;
     ```

2. **Data Import Issues**
   - Ensure all required Python packages are installed
   - Check file paths in the import script
   - Verify CSV file encoding and format

3. **Common Errors**
   - "Access denied": Check MySQL user permissions
   - "Table already exists": Drop existing table or use different name
   - "Column not found": Verify CSV column names match table structure

## Database Schema

```sql
DESCRIBE measurements;
```

Expected output:
```
+---------------+---------------+------+-----+---------+----------------+
| Field         | Type          | Null | Key | Default | Extra          |
+---------------+---------------+------+-----+---------+----------------+
| id            | int           | NO   | PRI | NULL    | auto_increment |
| user_id       | int           | NO   | MUL | NULL    |                |
| Distance      | decimal(10,4) | YES  |     | NULL    |                |
| Pressure      | decimal(10,4) | YES  |     | NULL    |                |
| HRV           | decimal(10,4) | YES  |     | NULL    |                |
| Sugar level   | decimal(10,4) | YES  |     | NULL    |                |
| SpO2          | decimal(10,4) | YES  |     | NULL    |                |
| Accelerometer | tinyint(1)    | YES  |     | NULL    |                |
| Decision      | tinyint       | YES  | MUL | NULL    |                |
| created_at    | timestamp     | YES  |     | NULL    |                |
+---------------+---------------+------+-----+---------+----------------+
```
