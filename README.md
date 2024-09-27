## my-playwright-project
Playwright basic configuration and setup with Python Language

## PREREQUISITES / SETUP
### Windows Setup
1) Download and Install Python <br/>
    https://www.python.org/downloads/
        Check on most of the Optional Features during Python install (e.g. Documentation, pip, td/tk and IDLE, Python test suite, py launcher.  Additional options might be available by the time you are reading this)<br/>
        You will also need to set Python in your system environment variables > Path<br/>
        OR <br/>
        You could have Python added to environment variables during the Python installation (Advanced Options > Add Python to environment variables)
2) Install IDE (e.g. Visual Studio Code, Pycharm)
    Visual Studio Code > https://code.visualstudio.com/
3) Check that you have updated version of pip.  Install playwright.<br/>
    Below are the initial set of commands you need to run in Visual Studio Code terminal for the project.  You could refer to this Youtube video : https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A<br/>
    - [ ] pip install --upgrade pip
        [Upgrade for pip]<br/>
    - [ ] pip install playwright
        [Install all the different dependencies and package we need for Playwright]<br/>
    - [ ] playwright install
        [Install the browsers (e.g. Chromium, Firefox, Webkit) and libraries to record videos automatically.  We don't have to worry about the browser drivers not being in the correct path or place]<br/>
4) Test that you will be able to do a synchronous call using Playwright<br/>
    To run the sync.py file, just type in below command in your Visual Studio Code Terminal<br/>
        python sync.py<br/>
    OR<br/>
    Follow instructions from https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A

### References
https://playwright.dev/python/docs/api/class-playwright
https://www.youtube.com/watch?v=H2-5ecFwHHQ
https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A
<!-- How to select an element by id in Playwright -->
https://stackoverflow.com/questions/75151754/how-can-i-select-an-element-by-id

### Additional Reference
https://playwright.dev/docs/locators
