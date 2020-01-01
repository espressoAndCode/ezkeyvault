# ezKeyVault

A very simple and easy to use key management system. *ezKeyVault* was created to give beginning developers an easy way to use API keys without writing them directly into their code, subsequently forgetting about them, and pushing them to their public Github repos.

## Getting Started

This project has two parts
  - ezKeyVault - a CLI based key manager where the user can add and view their API keys. This is for local use only on a developer's machine, and is installed only once.
  ezKeyVault creates a simple key/value store that writes a hidden text file in the user's home directory. ezKeyVault does not encrypt any content, it's sole purpose is to facilitate separation of the keys from the working code. Once a key is added to the ezKeyVault, it can be accessed from any project on the user's machine via the *ezKey* `pip` module.

  - ezKey - a `pip` module that the user can add to their projects to facilitate easy access to their API keys during development. You can learn more about using ezKey [here.](https://pypi.org/project/ezkey/)

### Prerequisites

You will need Python 2 or 3 on your system to use this software. ezKeyVault and ezKey were built on OSX and should work on any *.nix machine.

### Installing ezKeyVault

Navigate to your home directory and clone this repo.

```
$ cd ~
$ git clone https://github.com/espressoAndCode/ezkeyvault.git
```

Add the following line of code to your `.bash_profile` or `.bashrc` file.

```
alias ezkeyvault="python ${HOME}/ezkeyvault/ezkeyvault.py"
```

Now you can run the ezKeyVault from any path in your system by simply typing `ezkeyvault`. You will be given a series of options as shown here:

```
$ ezkeyvault
              __ __          _    __            ____
  ___  ____  / //_/__  __  _| |  / /___ ___  __/ / /_
 / _ \/_  / / ,< / _ \/ / / / | / / __ `/ / / / / __/
/  __/ / /_/ /| /  __/ /_/ /| |/ / /_/ / /_/ / / /_
\___/ /___/_/ |_\___/\__, / |___/\__,_/\__,_/_/\__/
                    /____/

Enter the new API key name: GoogleMaps
Enter the new API key value: dfhglafdhlgfljnfljkahughukdfnfdna
Enter an optional comment: This is my first key.
Add this key to the vault? (Y/N)y
Key for GoogleMaps has been updated.

Would you like to add another key to the vault? (Y/N)n
```
- **Enter the new API key name:** - You can enter any valid string here. This is the value that will later be passed into ezkey.getkey(value) to retrieve the API key in your project code.
- **Enter the new API key value:** - This is the actual API key, the value entered above is gibberish. You should cut and paste your real API key here. This is saved as a string, so *do not add additional quotes!*
- **Enter an optional comment:** - Like the prompt says.
- **Add this key to the vault?** - You can bail out here if there are any errors.

Finally, you will see an acknowledgement that the key has been added / updated.
**NOTE** - If you enter an existing keyname, you will be asked to verify that you want to overwrite the existing key. If you agree by entering Y, your old key will be discarded and replaced with the new one. If you want to create multiple key versions for the same service, you must name them differently.

tl;dr: every key must have a unique name.

Once you have entered keys, ezKeyVault will display them when the application runs:

```
$ ezkeyvault
              __ __          _    __            ____
  ___  ____  / //_/__  __  _| |  / /___ ___  __/ / /_
 / _ \/_  / / ,< / _ \/ / / / | / / __ `/ / / / / __/
/  __/ / /_/ /| /  __/ /_/ /| |/ / /_/ / /_/ / / /_
\___/ /___/_/ |_\___/\__, / |___/\__,_/\__,_/_/\__/
                    /____/

----------------------------------------------------------------------------------------------------
KEYNAME             KEY (first 16 digits)       TIMESTAMP                         COMMENT
----------------------------------------------------------------------------------------------------
GoogleMaps              dfhglafdhlgfljnf     15:09:20.899481                   This is my first key.
Facebook                ds6dg54hgf354dfg     15:22:54.348236                            Another key.
Twitterv01              a;foivjsdfbgjsfl     15:23:16.804868


Enter the new API key name:
```
Notice that only the first 16 characters of the key are shown. The entire key will be returned to your code when accessed with *ezkey*.


## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details

