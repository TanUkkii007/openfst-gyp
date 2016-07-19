# openfst-gyp
gyp definition for openfst (http://www.openfst.org)

Currently target to openfst 1.5.3.

# How to start

Download openfst and unzip it as `openfst-1.5.3` to current directory.

To create a project file of, for example XCode,

```
gyp openfst.gyp --depth=. -f xcode --generator-output=./build.xcodefiles/
```
