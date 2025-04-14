-- Create database tables for Elderly Health Monitoring System

-- Users table
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    age INT,
    gender VARCHAR(10)
);

-- Mental Health table
CREATE TABLE mental_health (
    mental_health_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    exhaustion_score INT,
    depression_total_score FLOAT,
    anxiety_perception VARCHAR(50),
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Lifestyle table
CREATE TABLE lifestyle (
    lifestyle_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    smoking VARCHAR(50),
    alcohol_units FLOAT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Sleep Disorders table
CREATE TABLE sleep_disorders (
    disorder_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    sleep_disorder VARCHAR(50),
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Falls and Fractures table
CREATE TABLE falls_fractures (
    fall_fracture_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    falls_one_year INT,
    fractures_three_years INT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Mobility table
CREATE TABLE mobility (
    mobility_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    balance_single_score VARCHAR(50),
    gait_speed_4m FLOAT,
    grip_strength_abnormal VARCHAR(10),
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Vision and Audition table
CREATE TABLE vision_audition (
    health_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    vision_score VARCHAR(50),
    audition_score VARCHAR(50),
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Weight and BMI table
CREATE TABLE weight_bmi (
    vital_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    weight_kg FLOAT,
    height_cm FLOAT,
    bmi FLOAT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Sleep Duration and Quality table
CREATE TABLE sleep_duration_quality (
    sleep_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    sleep_duration_hours FLOAT,
    sleep_quality INT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Sleep Activity table
CREATE TABLE sleep_activity (
    sleep_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    physical_activity_minutes INT,
    stress_level INT,
    daily_steps INT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Vitals Backup table
CREATE TABLE vitals_backup (
    vital_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    systolic_bp INT,
    diastolic_bp INT,
    heart_rate INT,
    weight_kg FLOAT,
    height_cm FLOAT,
    bmi FLOAT,
    health_risk TINYINT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Heart Rate table
CREATE TABLE heart_rate (
    vital_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    heart_rate INT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Blood Pressure table
CREATE TABLE blood_pressure (
    bp_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    systolic_bp INT,
    diastolic_bp INT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Sleep Data Backup table
CREATE TABLE sleep_data_backup (
    sleep_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    sleep_duration_hours FLOAT,
    sleep_quality INT,
    physical_activity_minutes INT,
    stress_level INT,
    blood_pressure VARCHAR(20),
    heart_rate INT,
    daily_steps INT,
    sleep_disorder VARCHAR(50),
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Health History Backup table
CREATE TABLE health_history_backup (
    history_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    hospitalizations_1yr INT,
    hospitalizations_3yr INT,
    vision_score VARCHAR(50),
    audition_score VARCHAR(50),
    falls_one_year INT,
    fractures_three_years INT,
    timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
); 