import os
import json
from datetime import datetime

def main():

    # Get user home path and create full filepath
    home = os.path.expanduser("~") + '/'
    fn = os.path.join(home, '.keyvault.json')

    # Initialize module variables
    updated_keyfile = {}
    dash = '-' * 100

    # Modify input() to work for Python 2 or 3
    global input
    try:
        input = raw_input
    except NameError:
        pass

    print('              __ __          _    __            ____')
    print('  ___  ____  / //_/__  __  _| |  / /___ ___  __/ / /_')
    print(' / _ \/_  / / ,< / _ \/ / / / | / / __ `/ / / / / __/')
    print('/  __/ / /_/ /| /  __/ /_/ /| |/ / /_/ / /_/ / / /_  ')
    print('\___/ /___/_/ |_\___/\__, / |___/\__,_/\__,_/_/\__/ ')
    print('                    /____/\n')

    # If the 'keyvault.json' file exists, load it
    if (os.path.exists(fn)):
        with open(fn, 'r') as f:
            # Guard against empty file
            file = f.read()
            if len(file) > 0:
                updated_keyfile = json.loads(file)

        print(dash)
        print("KEYNAME             KEY (first 16 digits)       TIMESTAMP                         COMMENT")
        print(dash)
        for k, v in updated_keyfile.items():
            print('{:<20}{:>20}{:>20}{:>40}'.format(k, v['value'][:16], v['date_created'], v['comment']))
        print('\n')

    # Begin Main control loop
    running = True
    while running:
        key = input("Enter the new API key name: ")
        val = input("Enter the new API key value: ")
        comment = input("Enter an optional comment: ")
        confirm = input("Add this key to the vault? (Y/N)")
        timestamp = datetime.now().strftime("%H:%M:%S.%f")

        # Assign k/v pairs
        newkey = {
            "value": val,
            "date_created": timestamp,
            "comment": comment
        }

        # Verify if key already exists, does user want to over write?
        if confirm == 'Y' or confirm == 'y':
            if key in updated_keyfile.keys():
                writeflag = input("Key for "+ key +" already exists. Do you want to replace it? (Y/N)")
            else:
                writeflag = 'Y'

            if writeflag == 'Y' or writeflag == 'y':
                updated_keyfile[key] = newkey
                print("Key for " + key + " has been updated.\n")
                with open(fn, 'w') as writefile:
                    writefile.write(json.dumps(updated_keyfile))
            else:
                print("New key for "+ key +" has been discarded.\n")

        else:
            print("New key for " + key + " has been discarded.\n")

        # Add another key?
        keep_running = input("Would you like to add another key to the vault? (Y/N)")
        running = True if (keep_running == 'Y' or keep_running == 'y') else False
        # End Main control loop

if __name__== "__main__":
   main()