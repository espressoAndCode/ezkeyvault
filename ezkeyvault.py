import os
import json
from datetime import datetime

def main():
    # Get user home path and create full filepath
    home = os.path.expanduser("~") + '/'
    fn = os.path.join(home, '.keyvault.json')

    updated_keyfile = {}
    dash = '-' * 100

    print('              __ __          _    __            ____')
    print('  ___  ____  / //_/__  __  _| |  / /___ ___  __/ / /_')
    print(' / _ \/_  / / ,< / _ \/ / / / | / / __ `/ / / / / __/')
    print('/  __/ / /_/ /| /  __/ /_/ /| |/ / /_/ / /_/ / / /_  ')
    print('\___/ /___/_/ |_\___/\__, / |___/\__,_/\__,_/_/\__/ ')
    print('                    /____/')

    # If the 'apivault.txt' file exists, load it
    if (os.path.exists(fn)):
        with open(fn, 'r') as f:
            # Guard against empty file
            file = f.read()
            if len(file) > 0:
                updated_keyfile = json.loads(file)

        print(dash)
        print("KEYNAME             KEY (first 16 digits)       TIMESTAMP                         DOCS")
        print(dash)
        for k, v in updated_keyfile.items():
            print('{:<20}{:>20}{:>20}{:>40}'.format(k, v['value'][:16], v['date_created'], v['docs_site']))
        print('\n\n')

    running = True
    while running:
        key = input("Enter the new API key name: ")
        val = input("Enter the new API key value: ")
        site = input("Enter a URL for documentation (optional)")
        confirm = input("Add this key to the vault? (Y/N)")
        timestamp = datetime.now().strftime("%H:%M:%S.%f")

        newkey = {
            "id": "",
            "value": val,
            "date_created": timestamp
        }
        if not site == None:
            newkey["docs_site"] = site

        if confirm == 'Y' or confirm == 'y':
            if key in updated_keyfile.keys():
                writeflag = input("Key for "+ key +" already exists. Do you want to replace it? (Y/N)")
            else:
                writeflag = 'Y'

            if writeflag == 'Y' or writeflag == 'y':
                updated_keyfile[key] = newkey
                print("Key for " + key + " has been updated.")
                print('Updated keyfile: ', updated_keyfile)
                with open(fn, 'w') as writefile:
                    writefile.write(json.dumps(updated_keyfile))
            else:
                print("New key for "+ key +" has been discarded.")

        else:
            print("New key for " + key + " has been discarded.")

        keep_running = input("Would you like to add another key to the vault? (Y/N)")
        running = True if (keep_running == 'Y' or keep_running == 'y') else False

if __name__== "__main__":
   main()