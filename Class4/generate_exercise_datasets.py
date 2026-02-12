"""
Generate all datasets for Class 4 Exercises
Creates 9 CSV files with realistic synthetic data
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Create data directory if it doesn't exist
import os
os.makedirs('data', exist_ok=True)

print("Generating datasets for Class 4 exercises...")
print("="*60)

# ============================================================================
# DATASET 1: Student Scores (Easy - Exercise 1)
# ============================================================================
print("\n1. Generating student_scores.csv...")

n_students = 200
student_scores = pd.DataFrame({
    'student_id': range(1, n_students + 1),
    'exam_score': np.random.normal(75, 12, n_students).clip(40, 100).round(1)
})

student_scores.to_csv('data/student_scores.csv', index=False)
print(f"   ✓ Created: {len(student_scores)} students, mean={student_scores['exam_score'].mean():.1f}")

# ============================================================================
# DATASET 2: Employee Salaries (Easy - Exercise 2)
# ============================================================================
print("\n2. Generating employee_salaries.csv...")

departments = ['Engineering', 'Sales', 'Marketing', 'HR']
n_employees = 500

# Different salary distributions by department
dept_salaries = {
    'Engineering': (90000, 20000),  # mean, std
    'Sales': (75000, 18000),
    'Marketing': (70000, 15000),
    'HR': (65000, 12000)
}

emp_data = []
emp_id = 1

for dept in departments:
    n_dept = n_employees // len(departments)
    mean_sal, std_sal = dept_salaries[dept]
    
    salaries = np.random.normal(mean_sal, std_sal, n_dept).clip(40000, 200000)
    years_exp = np.random.exponential(5, n_dept).clip(0, 30)
    
    for i in range(n_dept):
        emp_data.append({
            'employee_id': emp_id,
            'department': dept,
            'salary': round(salaries[i], 2),
            'years_experience': round(years_exp[i], 1)
        })
        emp_id += 1

employee_salaries = pd.DataFrame(emp_data)
employee_salaries.to_csv('data/employee_salaries.csv', index=False)
print(f"   ✓ Created: {len(employee_salaries)} employees across {len(departments)} departments")

# ============================================================================
# DATASET 3: House Simple (Easy - Exercise 3)
# ============================================================================
print("\n3. Generating house_simple.csv...")

n_houses = 300
sqft = np.random.normal(2000, 600, n_houses).clip(800, 5000)
# Price correlates with sqft with some noise
price = 150000 + (sqft * 150) + np.random.normal(0, 40000, n_houses)
price = price.clip(100000, 1500000)

house_simple = pd.DataFrame({
    'house_id': range(1, n_houses + 1),
    'sqft': sqft.round(0).astype(int),
    'price': price.round(0).astype(int)
})

house_simple.to_csv('data/house_simple.csv', index=False)
correlation = house_simple['sqft'].corr(house_simple['price'])
print(f"   ✓ Created: {len(house_simple)} houses, correlation={correlation:.3f}")

# ============================================================================
# DATASET 4: Customer Transactions (Medium - Exercise 4)
# ============================================================================
print("\n4. Generating customer_transactions.csv...")

n_transactions = 10000
# Create right-skewed distribution
amounts = np.random.lognormal(3.5, 1.2, n_transactions)

categories = ['Electronics', 'Clothing', 'Home', 'Books']
customer_types = ['New', 'Regular', 'Premium']

transactions = pd.DataFrame({
    'transaction_id': range(1, n_transactions + 1),
    'amount': amounts.round(2),
    'date': [datetime(2023, 1, 1) + timedelta(days=int(x)) 
             for x in np.random.uniform(0, 365, n_transactions)],
    'category': np.random.choice(categories, n_transactions),
    'customer_type': np.random.choice(customer_types, n_transactions, 
                                     p=[0.3, 0.5, 0.2])
})

transactions.to_csv('data/customer_transactions.csv', index=False)
print(f"   ✓ Created: {len(transactions)} transactions, skewness={transactions['amount'].skew():.2f}")

# ============================================================================
# DATASET 5: Real Estate (Medium - Exercise 5)
# ============================================================================
print("\n5. Generating real_estate.csv...")

n_properties = 1000

# Create correlated features
sqft = np.random.normal(2200, 700, n_properties).clip(800, 6000)
bedrooms = (sqft / 500 + np.random.normal(0, 0.5, n_properties)).clip(1, 7).round(0)
bathrooms = (bedrooms * 0.75 + np.random.normal(0, 0.3, n_properties)).clip(1, 5).round(1)
age = np.random.exponential(15, n_properties).clip(0, 100).round(0)
lot_size = np.random.gamma(3, 0.15, n_properties).clip(0.05, 2).round(2)
garage_spaces = np.random.choice([0, 1, 2, 3], n_properties, p=[0.1, 0.3, 0.5, 0.1])
distance_to_city = np.random.gamma(2, 3, n_properties).clip(0.5, 50).round(1)
crime_rate = np.random.beta(2, 5, n_properties) * 100
school_rating = np.random.normal(6.5, 1.5, n_properties).clip(1, 10).round(1)
condition_score = np.random.normal(7, 1.5, n_properties).clip(1, 10).round(1)
renovation_year = np.where(
    np.random.random(n_properties) < 0.3,
    np.random.randint(1990, 2024, n_properties),
    0
)

# Price based on multiple factors
price = (
    100000 + 
    sqft * 120 + 
    bedrooms * 15000 + 
    bathrooms * 10000 - 
    age * 1000 + 
    lot_size * 50000 +
    garage_spaces * 8000 -
    distance_to_city * 2000 -
    crime_rate * 500 +
    school_rating * 5000 +
    condition_score * 8000 +
    np.random.normal(0, 30000, n_properties)
)
price = price.clip(80000, 1000000)

real_estate = pd.DataFrame({
    'price': price.round(0).astype(int),
    'sqft': sqft.round(0).astype(int),
    'bedrooms': bedrooms.astype(int),
    'bathrooms': bathrooms,
    'age': age.astype(int),
    'lot_size': lot_size,
    'garage_spaces': garage_spaces,
    'distance_to_city': distance_to_city,
    'crime_rate': crime_rate.round(2),
    'school_rating': school_rating,
    'condition_score': condition_score,
    'renovation_year': renovation_year.astype(int)
})

real_estate.to_csv('data/real_estate.csv', index=False)
print(f"   ✓ Created: {len(real_estate)} properties with 12 features")

# ============================================================================
# DATASET 6: Daily Sales (Medium - Exercise 6)
# ============================================================================
print("\n6. Generating daily_sales.csv...")

days = 730  # 2 years
start_date = datetime(2022, 1, 1)

dates = [start_date + timedelta(days=i) for i in range(days)]
day_names = [d.strftime('%A') for d in dates]

# Base sales with trend, seasonality, and day-of-week effects
trend = np.linspace(50000, 60000, days)
seasonal = 5000 * np.sin(np.linspace(0, 4*np.pi, days))  # 2-year cycle

day_effects = {
    'Monday': 0.95,
    'Tuesday': 0.98,
    'Wednesday': 1.0,
    'Thursday': 1.02,
    'Friday': 1.15,
    'Saturday': 1.25,
    'Sunday': 0.85
}

daily_sales = trend + seasonal + np.random.normal(0, 3000, days)

# Apply day-of-week effects
for i, day in enumerate(day_names):
    daily_sales[i] *= day_effects[day]

# Add holiday effects
holidays = np.random.choice(range(days), 15, replace=False)
is_holiday = np.zeros(days, dtype=bool)
is_holiday[holidays] = True
daily_sales[holidays] *= 1.3

daily_sales = daily_sales.clip(20000, 100000).round(2)

sales_df = pd.DataFrame({
    'date': dates,
    'daily_sales': daily_sales,
    'day_of_week': day_names,
    'is_holiday': is_holiday
})

sales_df.to_csv('data/daily_sales.csv', index=False)
print(f"   ✓ Created: {len(sales_df)} days with seasonal patterns and {is_holiday.sum()} holidays")

# ============================================================================
# DATASET 7: Customer Survey (Hard - Exercise 7)
# ============================================================================
print("\n7. Generating customer_survey.csv...")

n_respondents = 5000

# Demographics
age = np.random.normal(45, 15, n_respondents).clip(18, 90).round(0)
income = np.random.lognormal(11, 0.6, n_respondents).clip(20000, 300000).round(0)
education = np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 
                             n_respondents, p=[0.3, 0.4, 0.25, 0.05])

survey_data = {
    'respondent_id': range(1, n_respondents + 1),
    'age': age,
    'income': income,
    'education': education
}

# Add 20 survey questions (1-5 scale)
for q in range(1, 21):
    responses = np.random.choice([1, 2, 3, 4, 5], n_respondents, 
                                 p=[0.05, 0.15, 0.4, 0.3, 0.1])
    survey_data[f'q{q}'] = responses

survey_df = pd.DataFrame(survey_data)

# Introduce structured missingness (MAR pattern)
# Higher income people less likely to report income
income_missing_prob = 1 / (1 + np.exp((income - 100000) / 30000))
income_missing = np.random.random(n_respondents) < income_missing_prob
survey_df.loc[income_missing, 'income'] = np.nan

# Older people skip some questions
for q in [15, 16, 17, 18]:
    age_missing_prob = (age - 18) / 100
    age_missing = np.random.random(n_respondents) < age_missing_prob
    survey_df.loc[age_missing, f'q{q}'] = np.nan

# Random missingness for other questions (MCAR)
for q in [5, 10]:
    random_missing = np.random.random(n_respondents) < 0.05
    survey_df.loc[random_missing, f'q{q}'] = np.nan

survey_df.to_csv('data/customer_survey.csv', index=False)
missing_pct = survey_df.isnull().sum().sum() / (survey_df.shape[0] * survey_df.shape[1]) * 100
print(f"   ✓ Created: {len(survey_df)} respondents, {missing_pct:.1f}% missing data (structured)")

# ============================================================================
# DATASET 8: E-commerce Full (Hard - Exercise 8)
# ============================================================================
print("\n8. Generating ecommerce_full.csv...")

n_trans = 50000

segments = ['New', 'Regular', 'Premium']
categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
regions = ['North', 'South', 'East', 'West']

# Segment characteristics
segment_probs = [0.25, 0.55, 0.2]
segment_avg_values = {'New': 50, 'Regular': 100, 'Premium': 250}

trans_data = []
for i in range(1, n_trans + 1):
    segment = np.random.choice(segments, p=segment_probs)
    category = np.random.choice(categories)
    region = np.random.choice(regions)
    
    # Order value depends on segment and category
    base_value = segment_avg_values[segment]
    if category == 'Electronics':
        base_value *= 2.5
    elif category == 'Home':
        base_value *= 1.5
    
    order_value = np.random.gamma(2, base_value/2)
    quantity = np.random.poisson(2) + 1
    customer_age = np.random.normal(40, 12, 1)[0]
    
    trans_data.append({
        'transaction_id': i,
        'customer_segment': segment,
        'product_category': category,
        'region': region,
        'order_value': round(order_value, 2),
        'quantity': quantity,
        'date': datetime(2023, 1, 1) + timedelta(days=int(np.random.uniform(0, 365))),
        'customer_age': int(customer_age),
        'is_repeat_customer': np.random.choice([True, False], p=[0.7, 0.3])
    })

ecommerce_df = pd.DataFrame(trans_data)
ecommerce_df.to_csv('data/ecommerce_full.csv', index=False)
print(f"   ✓ Created: {len(ecommerce_df)} transactions with segment and regional data")

# ============================================================================
# DATASET 9: Credit Risk (Hard - Exercise 9)
# ============================================================================
print("\n9. Generating credit_risk.csv...")

n_applicants = 8000

# Generate features
age = np.random.normal(40, 12, n_applicants).clip(18, 75).round(0)
income = np.random.lognormal(10.5, 0.7, n_applicants).clip(15000, 250000).round(0)
employment_length = np.random.exponential(6, n_applicants).clip(0, 40).round(1)
debt = income * np.random.beta(2, 5, n_applicants)
credit_score = np.random.normal(680, 80, n_applicants).clip(300, 850).round(0)
loan_amount = np.random.lognormal(9.5, 0.8, n_applicants).clip(1000, 100000).round(0)
interest_rate = (20 - (credit_score - 300) / 550 * 15) + np.random.normal(0, 2, n_applicants)
interest_rate = interest_rate.clip(3, 25).round(2)
term = np.random.choice([36, 60], n_applicants, p=[0.6, 0.4])
purpose = np.random.choice(['debt_consolidation', 'credit_card', 'home', 'car', 'other'], 
                          n_applicants, p=[0.3, 0.2, 0.15, 0.2, 0.15])
grade = pd.cut(credit_score, bins=[0, 600, 650, 700, 750, 850], 
               labels=['D', 'C', 'B', 'A', 'AA']).astype(str)
delinquencies = np.random.poisson(0.5, n_applicants)
inquiries = np.random.poisson(1, n_applicants)
open_accounts = np.random.poisson(5, n_applicants) + 2

# Calculate default probability based on risk factors
default_prob = 1 / (1 + np.exp(
    -(-5 + 
      (debt/income) * 3 + 
      (850 - credit_score) / 100 + 
      delinquencies * 0.3 + 
      inquiries * 0.2 - 
      employment_length * 0.05 + 
      np.random.normal(0, 1, n_applicants))
))

default = (np.random.random(n_applicants) < default_prob).astype(int)

# Introduce some missing values
income_missing = np.random.random(n_applicants) < 0.08
employment_missing = np.random.random(n_applicants) < 0.05
delinq_missing = np.random.random(n_applicants) < 0.03

credit_risk = pd.DataFrame({
    'applicant_id': range(1, n_applicants + 1),
    'age': age.astype(int),
    'income': income,
    'employment_length': employment_length,
    'debt': debt.round(2),
    'credit_score': credit_score.astype(int),
    'loan_amount': loan_amount.astype(int),
    'interest_rate': interest_rate,
    'term': term,
    'purpose': purpose,
    'grade': grade,
    'delinquencies': delinquencies,
    'inquiries': inquiries,
    'open_accounts': open_accounts,
    'default': default
})

# Apply missing values
credit_risk.loc[income_missing, 'income'] = np.nan
credit_risk.loc[employment_missing, 'employment_length'] = np.nan
credit_risk.loc[delinq_missing, 'delinquencies'] = np.nan

credit_risk.to_csv('data/credit_risk.csv', index=False)
default_rate = default.mean() * 100
print(f"   ✓ Created: {len(credit_risk)} applicants, {default_rate:.1f}% default rate")

print("\n" + "="*60)
print("✅ All datasets generated successfully!")
print("\nDataset Summary:")
print("-" * 60)
print(f"1. student_scores.csv        : {len(student_scores):,} rows")
print(f"2. employee_salaries.csv     : {len(employee_salaries):,} rows")
print(f"3. house_simple.csv          : {len(house_simple):,} rows")
print(f"4. customer_transactions.csv : {len(transactions):,} rows")
print(f"5. real_estate.csv           : {len(real_estate):,} rows")
print(f"6. daily_sales.csv           : {len(sales_df):,} rows")
print(f"7. customer_survey.csv       : {len(survey_df):,} rows")
print(f"8. ecommerce_full.csv        : {len(ecommerce_df):,} rows")
print(f"9. credit_risk.csv           : {len(credit_risk):,} rows")
print("-" * 60)
print(f"Total data points: {sum([len(df) for df in [student_scores, employee_salaries, house_simple, transactions, real_estate, sales_df, survey_df, ecommerce_df, credit_risk]]):,}")
print("\n💾 All files saved to 'data/' directory")
