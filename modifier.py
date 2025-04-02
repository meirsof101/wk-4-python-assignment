def read_file(filename):
    """Try to read a file and return its contents."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def write_file(filename, content):
    """Try to write content to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"Error: You don't have permission to write to '{filename}'.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while writing: {e}")
        return False

def process_content(content, choice):
    """Process the content based on user's choice."""
    if choice == '1':  # Uppercase
        return content.upper()
    elif choice == '2':  # Lowercase
        return content.lower()
    elif choice == '3':  # Add line numbers
        lines = content.split('\n')
        return '\n'.join(f"{i+1}: {line}" for i, line in enumerate(lines))
    else:
        return None

def main():
    while True:
        input_filename = input("Enter the input filename (or 'exit' to quit): ")
        if input_filename.lower() == 'exit':
            print("Exiting program.")
            break
            
        content = read_file(input_filename)
        if content is None:
            continue
            
        print("\nFile read successfully!")
        print("-" * 40)
        print("Content preview:")
        preview_lines = content.split('\n')[:3]
        for line in preview_lines:
            if len(line) > 60:
                print(line[:60] + "...")
            else:
                print(line)
        if len(preview_lines) < len(content.split('\n')):
            print("...")
        print("-" * 40)
        
        while True:
            print("\nHow would you like to modify the file?")
            print("1. Convert to UPPERCASE")
            print("2. Convert to lowercase")
            print("3. Add line numbers")
            choice = input("Enter your choice (1-3): ")
            
            processed_content = process_content(content, choice)
            if processed_content is None:
                print("Invalid choice. Please select 1, 2, or 3.")
                continue
            break
            
        while True:
            output_filename = input("Enter the output filename: ")
            if not output_filename:
                print("Filename cannot be empty.")
                continue
                
            if os.path.exists(output_filename):
                overwrite = input(f"'{output_filename}' already exists. Overwrite? (y/n): ")
                if overwrite.lower() != 'y':
                    continue
                    
            if write_file(output_filename, processed_content):
                print(f"\nSuccess! Modified content written to '{output_filename}'")
                break

if __name__ == "__main__":
    print("File Read & Write Program with Error Handling")
    print("=" * 50)
    main()