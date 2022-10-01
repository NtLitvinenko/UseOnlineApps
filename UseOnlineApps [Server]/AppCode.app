# Here your app code
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# If you need install module(s) use install
# example: install("module name")
# Pre installed modules: tkinter, sys, os, etc standart python libaries

