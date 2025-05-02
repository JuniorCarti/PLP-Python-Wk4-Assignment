def file_processor():
    """
    This program reads a file, modifies its content by adding line numbers,
    and writes the modified version to a new file with error handling.
    """
    
    # Get filename from user with validation
    while True:
        input_filename = input("Enter the name of the file to read: ").strip()
        if input_filename:  # Check if input is not empty
            break
        print("Error: Filename cannot be empty. Please try again.")
    
    output_filename = "modified_" + input_filename
    
    try:
        # Read the original file
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()
            
            # Check if file is empty
            if not lines:
                raise ValueError("The file is empty")
                
            # Process content (add line numbers)
            modified_lines = []
            for i, line in enumerate(lines, 1):
                modified_lines.append(f"{i}: {line}")
            
            # Write to new file
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.writelines(modified_lines)
                
            print(f"Success! Modified file saved as '{output_filename}'")
            print(f"Processed {len(lines)} lines")
            
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'")
    except UnicodeDecodeError:
        print("Error: Could not decode the file (possibly a binary file)")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__} - {e}")
    finally:
        print("File processing complete.")

# Run the program
if __name__ == "__main__":
    file_processor()