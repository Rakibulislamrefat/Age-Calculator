from datetime import datetime

def calculate_age():
    print("\n=== Age Calculator ===\n")
    
    try:
        # Get birth date from user
        birth_date = input("Enter your birth date (DD/MM/YYYY): ")
        
        # Convert string to datetime object
        birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
        
        # Get current date
        current_date = datetime.now()
        
        # Calculate age
        age = current_date.year - birth_date.year
        
        # Check if birthday hasn't occurred this year
        if current_date.month < birth_date.month or \
           (current_date.month == birth_date.month and current_date.day < birth_date.day):
            age -= 1
        
        # Calculate months and days
        if current_date.day >= birth_date.day:
            days = current_date.day - birth_date.day
        else:
            days = (current_date.day - birth_date.day) + 30
            
        if current_date.month >= birth_date.month:
            months = current_date.month - birth_date.month
        else:
            months = (current_date.month - birth_date.month) + 12
            
        # Print results
        print("\nYour age is:")
        print(f"{age} years, {months} months, and {days} days")
        
    except ValueError:
        print("\nError: Please enter the date in the correct format (DD/MM/YYYY)")

if __name__ == "__main__":
    while True:
        calculate_age()
        
        # Ask if user wants to calculate another age
        again = input("\nWould you like to calculate another age? (yes/no): ").lower()
        if again != 'yes':
            print("\nThank you for using the Age Calculator!")
            break
