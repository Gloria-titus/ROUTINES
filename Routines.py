import pandas as pd
import os

# Data for the daily routine schedule
schedule_data = [
    ["6:30 AM - 6:50 AM", "Wake up & Morning Prayer", "Spiritual reflection, gratitude journaling."],
    ["6:50 AM - 7:10 AM", "Bible Study", "Focus on selected scripture and personal insights."],
    ["7:10 AM - 7:30 AM", "Quick Shower & Skincare", "Refresh and prepare for the day (cleanse, tone, moisturize, sunscreen)."],
    ["7:30 AM - 8:30 AM", "Breakfast & Relaxation", "High-protein meal and light relaxation (e.g., motivational podcast)."],
    ["8:30 AM - 10:00 AM", "Career Study Block (1)", "AWS or Python: Review, learn new concepts, and practice hands-on."],
    ["10:00 AM - 10:45 AM", "Chloe Ting Workout", "Follow Chloe Ting’s daily challenge workout."],
    ["10:45 AM - 11:00 AM", "Cool Down & Snack", "Light stretches and rehydrate with water or a smoothie."],
    ["11:00 AM - 1:30 PM", "Projects & Hands-On Practice", "AWS labs, Python mini-projects (e.g., automating a task)."],
    ["1:30 PM - 2:00 PM", "Lunch", "Balanced meal with protein, veggies, and carbs."],
    ["2:00 PM - 3:00 PM", "Career Study Block (2)", "CCNA basics: Concepts review, tutorial, and hands-on simulations."],
    ["3:00 PM - 4:30 PM", "Personal Projects", "Portfolio projects (e.g., Python automation or DevOps tasks)."],
    ["4:30 PM - 5:00 PM", "Break", "Walk or relax with calming activities."],
    ["5:00 PM - 6:00 PM", "Networking/Research", "LinkedIn updates, join communities, and explore industry trends."],
    ["6:00 PM - 7:00 PM", "Dinner", "Nutritious meal and connection with loved ones."],
    ["7:00 PM - 8:00 PM", "Study Block (Final Review)", "Revise AWS, Python, or CCNA concepts from earlier in the day."],
    ["8:00 PM - 9:00 PM", "Scheduled Activities", "Bible Study (Wed), Bitcoin Class (Tue/Thu), or spiritual journaling/creative hobbies."],
    ["9:00 PM - 10:00 PM", "Leisure", "Hobbies, light reading, or creative work (e.g., crochet)."],
    ["10:00 PM - 10:30 PM", "Skincare & Wind Down", "Night cream or treatments, prepare for restful sleep."],
    ["10:30 PM - 6:30 AM", "Sleep", "Aim for 6-8 hours of quality rest."]
]

# Creating DataFrame for schedule
df_schedule = pd.DataFrame(schedule_data, columns=["Time", "Activity", "Details"])

# Data for the study modules
study_modules_data = {
    "AWS Solutions Architect": [
        ["Intro to Cloud Concepts", "Basics of AWS, core services overview.", "Week 1"],
        ["EC2 & Compute Services", "Launch instances, scaling, and pricing.", "Week 2"],
        ["Networking & VPC", "Secure networks, subnets, NAT, gateways.", "Week 3"],
        ["Storage Solutions", "S3, EBS, EFS, lifecycle policies.", "Week 4"],
        ["Databases", "RDS, DynamoDB, Aurora; selection criteria.", "Week 5"],
        ["Identity & Security", "IAM, roles, policies, and access management.", "Week 6"],
        ["Monitoring & Optimization", "CloudWatch, Trusted Advisor, cost strategies.", "Week 7"],
        ["Practice Labs & Exam Prep", "Hands-on scenarios, mock exams, review.", "Week 8"]
    ],
    "Python Basics": [
        ["Syntax, Variables, Types", "Fundamentals of Python programming.", "Weeks 1-2"],
        ["Control Flow", "Loops, conditionals, efficient code writing.", "Week 3"],
        ["Functions & Modules", "Write reusable and modular code.", "Week 4"],
        ["File Handling & Data Struct", "Work with files, lists, and dictionaries.", "Week 5"],
        ["Object-Oriented Programming", "Classes, inheritance, encapsulation.", "Week 6"],
        ["Debugging & Practice", "Debugging techniques and small projects.", "Week 7"]
    ],
    "CCNA Basics": [
        ["Networking Fundamentals", "IP addressing, subnetting basics.", "Week 1"],
        ["Routing & Switching", "Configuring routers and switches.", "Week 2"],
        ["Security Fundamentals", "Firewalls, VPNs, and securing networks.", "Week 3"],
        ["Wireless Networking", "Configuring and managing wireless networks.", "Week 4"],
        ["Practice Labs & Review", "Packet Tracer simulations and exam prep.", "Week 5"]
    ]
}

# Converting study modules to DataFrames
df_aws = pd.DataFrame(study_modules_data["AWS Solutions Architect"], columns=["Topic", "Details", "Timeline"])
df_python = pd.DataFrame(study_modules_data["Python Basics"], columns=["Topic", "Details", "Timeline"])
df_ccna = pd.DataFrame(study_modules_data["CCNA Basics"], columns=["Topic", "Details", "Timeline"])

# Data for financial goals
financial_goals_data = [
    ["Buy a Phone", "Save Ksh. 3,000/month", "5 months", "15,000"],
    ["Move Out", "Save Ksh. 10,000/month", "4 months", "40,000"],
    ["Pay off Debt", "Allocate Ksh. 5,700/month", "5 months", "28,500"],
    ["Savings/Investment", "Start saving Ksh. 7,000/month", "After Month 5", "TBD"]
]

# Creating DataFrame for financial goals
df_financial_goals = pd.DataFrame(financial_goals_data, columns=["Priority", "Action Plan", "Timeline", "Progress (Ksh)"])

# Define the directory and file path
directory = r'C:\Users\Administrator\Desktop\random-commits\csv_files'  # Corrected path without spaces
schedule_file = r'C:\Users\Administrator\Desktop\random-commits\csv_files\schedules.csv'  # Corrected path

# Check if the directory exists, create it if it doesn't
if not os.path.exists(directory):
    os.makedirs(directory)

# Now save the DataFrame
df_schedule.to_csv(schedule_file, index=False)

# Define the file paths for other exports
study_file_aws = r'C:\Users\Administrator\Desktop\random-commits\csv_files\aws_study_modules.csv'
study_file_python = r'C:\Users\Administrator\Desktop\random-commits\csv_files\python_study_modules.csv'
study_file_ccna = r'C:\Users\Administrator\Desktop\random-commits\csv_files\ccna_study_modules.csv'
financial_file = r'C:\Users\Administrator\Desktop\random-commits\csv_files\financial_goals.csv'

# Export all DataFrames to CSV
df_schedule.to_csv(schedule_file, index=False)
df_aws.to_csv(study_file_aws, index=False)
df_python.to_csv(study_file_python, index=False)
df_ccna.to_csv(study_file_ccna, index=False)
df_financial_goals.to_csv(financial_file, index=False)

# Return the paths of the files
(schedule_file, study_file_aws, study_file_python, study_file_ccna, financial_file)
