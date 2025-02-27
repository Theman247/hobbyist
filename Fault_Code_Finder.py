import pandas as pd

# Load Excel file
data = pd.read_excel("Fault_Code.xlsx")
# Prompt user for SPN version
vsn = int(input("Enter SPN version (2 or 4): "))
spn = int(input("Enter SPN code (integer): "))
fmi = int(input("Enter FMI code (integer): "))
if vsn == 2:

# Find the corresponding integer in column L based on SPN in column K
    matching_rows = data[data["V2"] == spn]

    if not matching_rows.empty:
        reference_value = matching_rows["V4"].values[0]
    
    # Use reference value to find the same integer in column A
        filtered_rows = data[data["ADM3_FC_SPN"] == reference_value]

        if not filtered_rows.empty:
        
        # Use FMI code to find the same integer in column B
            final_rows = filtered_rows[filtered_rows["ADM3_FC_FMI"] == fmi]
        
         # Output values from targeted cells within a column
            print("Location:", final_rows["Location"].values)
            print("Description:", final_rows["Description"].values)
            print("Remedial_Actions:", final_rows["Remedial_Actions"].values)
            print("Pin:", final_rows["Pin"].values)
            if not final_rows.empty:
            # Output the data from the colu1mn with the same name as the values from row A and B
                output_column = str(reference_value)  # Convert to string to match column names
   
            else:
                print("No matching row found for given FMI code.")
        else:
            print("No matching values found in SPN V4") 

    else:
	    print("No matching rows found for the given SPN code.")
elif vsn == 4:
    matching_rows = data[data["V4"] == spn]
    if not matching_rows.empty:
        reference_value = matching_rows["V4"].values[0]
    
    # Use reference value to find the same integer in column A
        filtered_rows = data[data["ADM3_FC_SPN"] == reference_value]

        if not filtered_rows.empty:
        
        # Use FMI code to find the same integer in column B
            final_rows = filtered_rows[filtered_rows["ADM3_FC_FMI"] == fmi]
        
         # Output values from targeted cells within a column
            print("Location:", final_rows["Location"].values)
            print("Description:", final_rows["Description"].values)
            print("Remedial_Actions:", final_rows["Remedial_Actions"].values)
            print("Pin:", final_rows["Pin"].values)
            if not final_rows.empty:
            # Output the data from the colu1mn with the same name as the values from row A and B
                output_column = str(reference_value)  # Convert to string to match column names
   
            else:
                print("No matching row found for given FMI code.")
        else:
            print("No matching values found in SPN V4")

    else:
	    print("No matching rows found for the given SPN code.")
