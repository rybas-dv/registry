# Nexus 3 raw files transfer

Some solution for transfer file from source Nexus 3 repository to another. 

## Usage

You need Python 3.8 to run this script. You also need to install the requirements listed in `requirements.txt`.

Launch the script with:

    python3.8 main.py [-h]

For example:
    
    python3.8 main.py <source> <destination> <repository name> <source user>  <source password> <destination user> <destination password>
    python3.8 main.py https://nexus.test.com https://nexus2.test.com terraform-state admin1 password admin2 password

You have to supply argument:

* `-h` shows a help page.
