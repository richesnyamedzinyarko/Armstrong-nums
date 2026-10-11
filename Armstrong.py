def is_armstrong(number):
    """Check if a number is an Armstrong number."""
    if number < 0:
        return False
    
    str_num = str(number)
    num_digits = len(str_num)
    total_sum = sum(int(digit) ** num_digits for digit in str_num)
    
    return total_sum == number

def explain_armstrong(number):
    """Return the breakdown of the Armstrong calculation."""
    str_num = str(number)
    num_digits = len(str_num)
    breakdown = " + ".join([f"{digit}^{num_digits}" for digit in str_num])
    return f"{number} = {breakdown}"

def find_armstrong_in_range(start, end):
    """Find all Armstrong numbers within a specified range."""
    armstrong_list = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_list.append(num)
    return armstrong_list

def main():
    print("========================================")
    print("      ARMSTRONG NUMBER PROJECT          ")
    print("========================================")
    
    while True:
        print("\nChoose an option:")
        print("1. Check if a specific number is an Armstrong number")
        print("2. Find all Armstrong numbers in a range")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            try:
                num = int(input("Enter an integer to check: "))
                if is_armstrong(num):
                    print(f"\n[YES] {explain_armstrong(num)} -> It IS an Armstrong number!")
                else:
                    print(f"\n[NO] {num} is NOT an Armstrong number.")
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.")
                
        elif choice == '2':
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                
                if start > end:
                    print("\nStart value cannot be greater than end value.")
                    continue
                
                print(f"\nSearching for Armstrong numbers between {start} and {end}...")
                results = find_armstrong_in_range(start, end)
                
                if results:
                    print(f"Found {len(results)} Armstrong number(s):")
                    for num in results:
                        print(f" - {explain_armstrong(num)}")
                else:
                    print("No Armstrong numbers found in this range.")
            except ValueError:
                print("\nInvalid input. Please enter valid integers.")
                
        elif choice == '3':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()