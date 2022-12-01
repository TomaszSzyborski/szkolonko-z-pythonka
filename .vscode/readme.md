To install all dependencies use the following command:

For Linux or MacOs:
```
code --list-extensions | xargs -L 1 echo code --install-extension
```

for Windows:
```
code --list-extensions | % { "code --install-extension $_" }
```

To save list of extensions use the following command:
```
code --list-extensions > extensions.list
```