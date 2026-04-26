# GlobalTech Solutions Customer Management System

## Overview

This project builds a customer management system using Python
dictionaries. It stores customer data, tracks projects, calculates
costs, and generates business insights through aggregation and analysis.

The script demonstrates how to work with nested dictionaries, perform
lookups, and analyze structured data.

## Technologies Used

-   Python

## Features

### Service Management

-   Defines service categories with hourly rates
-   Supports dynamic rate adjustments using dictionary comprehension

### Customer Data Handling

-   Stores customer information using dictionaries
-   Organizes customers into a master dictionary with unique IDs
-   Supports lookup, update, and validation of customer records

### Project Tracking

-   Assigns multiple projects to each customer
-   Stores project details such as service type, hours, and budget
-   Displays project information for each customer

### Cost Calculations

-   Calculates project costs using service rates and hours worked
-   Aggregates total hours and budgets across all projects

### Data Analysis

-   Counts service usage across projects
-   Computes financial metrics:
    -   Total hours
    -   Total budget
    -   Average budget
    -   Maximum and minimum budget

### Customer Insights

-   Generates per-customer summaries including:
    -   Number of projects
    -   Total hours worked
    -   Total budget

### Advanced Features

-   Identifies active customers with ongoing projects
-   Maps customer IDs to total budgets
-   Categorizes services into pricing tiers (Basic, Standard, Premium)
-   Adds project status and tracks status distribution

### Functions

-   validate_customer: checks if required fields exist
-   analyze_customer_budgets: returns total, average, and count of
    projects per customer
-   recommend_services: suggests unused services for each customer

## How to Run

1.  Ensure Python is installed

2.  Run the script: python your_script_name.py

3.  Review the printed outputs in the console

## Output

The script prints: - Customer details - Lookup results - Updated
records - Project listings - Cost calculations - Service usage
statistics - Financial summaries - Customer reports - Service
recommendations

## Key Insights

-   Some services are used more frequently than others
-   Budget distribution varies across customers
-   High-value services fall into the premium tier
-   Recommendations help expand service usage across customers

## Notes

-   All data is stored in dictionaries, no external files required
-   Designed for learning dictionary operations and aggregation
-   Script runs from start to finish without user input

## Author

Justin Dixon
