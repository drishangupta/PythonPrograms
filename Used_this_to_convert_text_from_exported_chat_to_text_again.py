
import re
import datetime
import time
file_path="mytexts.txt"


with open(file_path, "r") as file:
    for line in file:
        
        
        
        # Process each line here
        liner=line.strip()
        regex = r"^.{1,33}"

        test_str = liner
        match = re.search(regex, test_str)
        result= re.sub(regex,"",test_str)
        print(result)
        output_file_path = "output.txt"
        mode = "a"

        
        with open(output_file_path, mode) as file:
            file.write(result + "\n")  # Adding a newline for each iteration

    # After the first iteration, switch to write mode to overwrite existing content
            mode = "w"

    # Add a delay between iterations
            time.sleep(0.2)  # Adjust the delay time as needed

    