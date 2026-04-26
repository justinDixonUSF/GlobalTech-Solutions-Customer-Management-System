# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message printed at the start of the program
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# The key is the service name (string)
# The value is the hourly rate (number)
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cloud Consulting": 220,
    "Cybersecurity": 250,
    "Technical Support": 90
}

# TODO 2: Create customer dictionaries
# Each dictionary represents a single customer
# All customers use the same keys for consistency
customer1 = {
    "company_name": "AlphaTech Inc",
    "contact_person": "John Smith",
    "email": "john@alphatech.com",
    "phone": "813-555-1010"
}

customer2 = {
    "company_name": "Beta Industries",
    "contact_person": "Sarah Johnson",
    "email": "sarah@betaind.com",
    "phone": "813-555-2020"
}

customer3 = {
    "company_name": "Gamma Logistics",
    "contact_person": "Michael Brown",
    "email": "michael@gammalogistics.com",
    "phone": "813-555-3030"
}

customer4 = {
    "company_name": "Delta Finance",
    "contact_person": "Emily Davis",
    "email": "emily@deltafinance.com",
    "phone": "813-555-4040"
}

# TODO 3: Create a master customers dictionary
# Keys = customer IDs
# Values = the customer dictionaries created above
# This creates a nested dictionary structure
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
# Loop through the dictionary using .items()
# .items() gives both the key (customer ID) and value (customer info)
print("\nAll Customers:")
print("-" * 60)

for cid, info in customers.items():
    print(f"Customer ID: {cid}")

    # Loop through each customer's fields
    for key, value in info.items():
        print(f"  {key}: {value}")

    print()

# TODO 5: Look up specific customers
# Demonstrates direct dictionary access and .get()

# Direct access to get full dictionary for customer C002
c002_info = customers["C002"]

# Access a nested value (contact person for C003)
c003_contact = customers["C003"]["contact_person"]

# Use .get() to safely attempt retrieving a customer that may not exist
# If not found, return the default message
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
print("C002 Info:", c002_info)
print("C003 Contact Person:", c003_contact)
print("C999 Lookup:", c999_info)

# TODO 6: Update customer information
# Modify existing dictionary values and add new ones

# Update C001 phone number
customers["C001"]["phone"] = "813-555-9999"

# Add a new field "industry" to customer C002
customers["C002"]["industry"] = "Manufacturing"

print("\n\nUpdating Customer Information:")
print("-" * 60)
print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries
# Each project contains project details
# The projects dictionary maps customer IDs to lists of projects
project1 = {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000}
project2 = {"name": "Security Audit", "service": "Cybersecurity", "hours": 60, "budget": 15000}
project3 = {"name": "Data Dashboard", "service": "Data Analysis", "hours": 80, "budget": 14000}
project4 = {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 100, "budget": 22000}
project5 = {"name": "IT Support Setup", "service": "Technical Support", "hours": 50, "budget": 5000}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4],
    "C004": [project5]
}

print("\n\nProject Information:")
print("-" * 60)

# Loop through each customer and their projects
for cid, plist in projects.items():
    print(f"{cid}:")
    for p in plist:
        print(" ", p)

# TODO 8: Calculate project costs
# Cost = service hourly rate * hours worked
# Rates are looked up from the services dictionary
print("\n\nProject Cost Calculations:")
print("-" * 60)

for cid, plist in projects.items():
    for p in plist:
        rate = services[p["service"]]   # lookup rate
        cost = rate * p["hours"]        # calculate cost
        print(f"{p['name']} ({cid}) - Cost: ${cost}")

# TODO 9: Customer statistics using dictionary methods
print("\n\nCustomer Statistics:")
print("-" * 60)

# Display all customer IDs
print("Customer IDs:", customers.keys())

# Extract company names from customer values
print("Customer Companies:")
for c in customers.values():
    print(c["company_name"])

# Count number of customers
print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
# Count how many projects use each service
service_counts = {}

for plist in projects.values():
    for p in plist:
        service = p["service"]

        # Use .get() to avoid errors if service not yet counted
        service_counts[service] = service_counts.get(service, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
print(service_counts)

# TODO 11: Financial aggregations
# Collect hours and budgets, then apply aggregation functions
all_hours = []
all_budgets = []

for plist in projects.values():
    for p in plist:
        all_hours.append(p["hours"])
        all_budgets.append(p["budget"])

total_hours = sum(all_hours)
total_budget = sum(all_budgets)
avg_budget = total_budget / len(all_budgets)
max_budget = max(all_budgets)
min_budget = min(all_budgets)

print("\n\nFinancial Summary:")
print("-" * 60)
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Max Budget:", max_budget)
print("Min Budget:", min_budget)

# TODO 12: Customer summary report
# Shows stats per customer
print("\n\nCustomer Summary Report:")
print("-" * 60)

for cid, cust in customers.items():
    plist = projects.get(cid, [])

    num_projects = len(plist)
    hours = sum(p["hours"] for p in plist)
    budget = sum(p["budget"] for p in plist)

    print(f"{cust['company_name']} ({cid})")
    print(" Projects:", num_projects)
    print(" Total Hours:", hours)
    print(" Total Budget:", budget)
    print()

# TODO 13: Dictionary comprehension for adjusted rates
# Increase all service rates by 10%
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
print(adjusted_rates)

# TODO 14: Filter customers with projects
active_customers = {
    cid: customers[cid]
    for cid in customers
    if cid in projects and len(projects[cid]) > 0
}

print("\n\nActive Customers (with projects):")
print("-" * 60)
print(active_customers)

# TODO 15: Create dictionary mapping customer IDs to total budgets
customer_budgets = {
    cid: sum(p["budget"] for p in plist)
    for cid, plist in projects.items()
}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# TODO 16: Categorize services by price tier
service_tiers = {
    service: ("Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic")
    for service, rate in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# TODO 17: Customer validation function
# Checks if all required fields exist
def validate_customer(customer_dict):

    required = ["company_name", "contact_person", "email", "phone"]

    for field in required:
        if field not in customer_dict:
            return False

    return True

print("\n\nCustomer Validation:")
print("-" * 60)

for cid, cust in customers.items():
    print(cid, "Valid:", validate_customer(cust))

# TODO 18: Add project status and count them
statuses = ["active", "completed", "pending"]
i = 0

for plist in projects.values():
    for p in plist:
        p["status"] = statuses[i % len(statuses)]
        i += 1

status_counts = {}

for plist in projects.values():
    for p in plist:
        status = p["status"]
        status_counts[status] = status_counts.get(status, 0) + 1

print("\n\nProject Status Summary:")
print("-" * 60)
print(status_counts)

# TODO 19: Budget analysis function
# Returns total, average, and project count per customer
def analyze_customer_budgets(projects_dict):

    result = {}

    for cid, plist in projects_dict.items():

        total = sum(p["budget"] for p in plist)
        count = len(plist)
        avg = total / count if count > 0 else 0

        result[cid] = {
            "total": total,
            "average": avg,
            "count": count
        }

    return result

print("\n\nDetailed Budget Analysis:")
print("-" * 60)

budget_analysis = analyze_customer_budgets(projects)
print(budget_analysis)

# TODO 20: Service recommendation system
# Suggest services the customer hasn't used yet
def recommend_services(customer_id, customers, projects, services):

    used_services = set()

    # Find services already used by the customer
    for p in projects.get(customer_id, []):
        used_services.add(p["service"])

    recommendations = []

    # Recommend services not yet used
    for service in services:
        if service not in used_services:
            recommendations.append(service)

    return recommendations

print("\n\nService Recommendations:")
print("-" * 60)

for cid in customers:
    rec = recommend_services(cid, customers, projects, services)
    print(f"{cid} recommended services:", rec)