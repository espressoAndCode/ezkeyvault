# ezKeyVault

A very simple and easy to use key management system. *ezKeyVault* was created to give beginning developers an easy way to use API keys without writing them directly into their code, subsequently forgetting about them, and pushing them to their public Github repos.

## Getting Started

This project has two parts
  - ezKeyVault - a CLI based key manager where the user can add and view their API keys. This is for local use only on a developer's machine, and is installed only once.
  ezKeyVault creates a simple key/value store that writes a hidden text file in the user's home directory. ezKeyVault does not encrypt any content, it's sole purpose is to facilitate separation of the keys from the working code. Once a key is added to the ezKeyVault, it can be accessed from any project on the user's machine via the *ezKey* `pip` module.

  - ezKey - a `pip` module that the user can add to their projects to facilitate easy access to their API keys during development.

### Prerequisites

You will need Python 2 or 3 on your system to use this software. ezKeyVault and ezKey were built on OSX and should work on any *.nix machine.

### Installing ezKeyVault

Navigate to your home directory and clone this repo.

```
$ cd ~
$ git clone https://github.com/espressoAndCode/ezkeyvault.git
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details

