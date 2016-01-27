### Building from Source

These instructions are for local builds using the default Sphinx templates. If you want to build locally using the Rackspace 
documentation templates, use the [Deconst client](https://github.com/deconst/client).

**Prerequisites**

- Python 2.7 or later
- Mac OSx: Install [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) or [pyenv](https://github.com/yyuu/pyenv)
- Windows: Install Python, pip, and virtualenv (See [How to install Python, pip, and virtualenv with PowerShell](http://www.tylerbutler.com/2012/05/how-to-install-python-pip-and-virtualenv-on-windows-with-powershell/)).

To set up your build environment:

1. Run the following commands to Activate your virtual environment:
   ```
    bin activate env-name
   ```   

2. Run the following commands to install Sphinx and other required packages::

    ```
    pip install -r requirements.txt
    
    ```
    
To build the documentation, run the following commands:

    cd api-docs
    make clean singlehtml

To view the HTML build results in the target directory (``_build/html/``), run the following command:

    open _build/html/index.html
