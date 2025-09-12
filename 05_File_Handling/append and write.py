rite to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

Example
Open the file "demofile.txt" and append content to the file:

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())
Overwrite Existing Content
To overwrite the existing content to the file, use the w parameter:

Example
Open the file "demofile.txt" and overwrite the content:

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())
Note: the "w" method will overwrite the entire file.

Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists

Example
Create a new file called "myfile.txt":

f = open("myfile.txt", "x")
Result: a new empty file is created.

with open("demofile.txt") as f:
            written_content = f.read()
            print(f"Content written:\n{written_content}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 4. Appending to a file
    print("4. APPENDING TO A FILE:")
    append_file_path = os.path.join(current_dir, "output.txt")
    try:
        with open(append_file_path, 'a') as f:
            f.write("Appending a new line to the existing file.\n")
            f.write("Another appended line.\n")
        print(f"Successfully appended to {append_file_path}")
        
        # Read back the appended content
        with open(append_file_path, 'r') as f:
            appended_content = f.read()
            print(f"Content after appending:\n{appended_content}")
    
    except Exception as e:
        print(f"An error occurred while appending: {e}")
    
    print("\n=== End of Demonstration ===")