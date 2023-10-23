import subprocess
import datetime

# Run the WMIC command to get a list of installed programs
command = 'wmic product get name,version,InstallDate,Vendor,URLInfoAbout'
result = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)

# Parsing the output and storing the data in a list
installed_programs = result.stdout.split('\n')[1:]
installed_programs = [program.strip() for program in installed_programs if program.strip()]

# Writing the data to a text file
with open('installed_programs.txt', 'w') as file:
    file.write("List of Installed Programs:\n")
    for program in installed_programs:
        file.write(program + '\n')
()

current_year = datetime.datetime.now().year

print(f"\u00A9 {current_year}, Olajide Olanrewaju, Olajide.m.olanrewaju@gmail.com, www.olanre.netlify.app .")
print("List of installed programs has been saved to installed_programs.txt")
