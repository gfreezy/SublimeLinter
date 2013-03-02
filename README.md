SublimeLinter
=============

This is a migration of SublimeLinter to Sublime Text 3. Currently, Python lint is implemented with `flake8`.It is only tested on Mac Mountain Lion.

Installing
----------
Package Control is not avaliable on Sublime Text 3 currently. So you have to install SublimeLinter manually.

**Without Git:** Download the latest source from [GitHub](https://github.com/gfreezy/SublimeLinter) and copy the SublimeLinter folder to your Sublime Text "Packages" directory.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/gfreezy/SublimeLinter.git


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 3/Packages/

* Linux:

        ~/.config/sublime-text-3/Packages/

* Windows:

        %APPDATA%/Sublime Text 3/Packages/

Python
-------
You need `flake8` installed to lint Python. And make sure `flake8` is in the PATH variable.

    pip install flake8
