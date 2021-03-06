# Packages Used By ROS Code

The following list outlines all the packages used by ROS Code - useful if building from source.

Ensure you already have Python 3.x installed on your system along with Pip as the runtime doesn't have pip installer by default.

```bat
:: Install A Package
:: Replace dir_to_runtime with the directory to the runtime site-packages folder - for example: C:\ROS-Code\runtime\win\Lib\site-packages
pip install PACKAGE_NAME --target dir_to_runtime
```

??? done "Preinstalled with Python"
    - subprocess
    - os
    - sys
    - secrets
    - warnings
    - keyword
    - importlib
    - string
    - textwrap
    - pprint
    - math
    - operator
    - statistics
    - webbrowser
    - urllib
    - random
    - datetime
    - time
    - calendar
    
??? help "Installation may be required"
    ??? summary "Pip"
        Refer to the [Pip Documentation](https://pip.pypa.io/en/stable/installing/)

!!! example "Helpful notice"
    All of the packages listed below can be install via the requirements.txt file and Pip
    
    ```bat
    :: Navigate to the ROS Code directory
    cd C:\ROS-Code
    :: Install the packages
    pip install -r requirements.txt
    ```

???+ warning "Installation required"

    ???+ example "One Line Install"
        `pip install clipboard colour`

    ??? summary "Clipboard"
        `pip install clipboard`

    ??? summary "Colour"
        `pip install colour`

???+ warning "Required when building documentation"

    ???+ example "One Line Install"
        One line install: `mkdocs mkdocs-material pymdown-extensions Pygments`
    
    ??? summary "Mkdocs"
        `pip install mkdocs`
        
    ??? summary "Mkdocs Material"
        `pip install mkdocs-material`
        
    ??? summary "Pymdown Extensions"
        `pip install pymdown-extensions`
        
    ??? summary "Pygments"
        `pip install pygments`
    
    
