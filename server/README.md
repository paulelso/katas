# Exploring HTTPS With Python

Real Python article https://realpython.com/python-https/

Required dependencies:

$ pip install flask uwsgi requests

Issue installing uwsgi. ERROR: Could not build wheels for uwsgi, which is required to install pyproject.toml-based projects

Cause: If you updated macOS from an earlier version with an "over the top" installation, your earlier development environment may remain intact. You will need to install the new version of Xcode Command Line Tools to avoid headaches. First, check what you have. Check if you previously installed the full Xcode package:

$ xcode-select -p

If you see: /Library/Developer/CommandLineTools
The Xcode Command Line Tools may be installed or an empty directory may be present.

How to test:

% ls /Library/Developer/CommandLineTools/usr/bin/git

You should see:

/Library/Developer/CommandLineTools/usr/bin/git

You should see:
/Library/Developer/CommandLineTools/usr/bin/git

If you see "ls: /Library/Developer/CommandLineTools/usr/bin/git: "No such file or directory" reinstall Xcode:

% sudo rm -rf /Library/Developer/CommandLineTools
% xcode-select --install

 % ls /Library/Developer/CommandLineTools/usr/bin/git
/Library/Developer/CommandLineTools/usr/bin/git

pip install uwsgi