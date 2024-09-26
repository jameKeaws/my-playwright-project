## my-playwright-project
Playwright basic configuration and setup with Python Language

# PREREQUISITES / SETUP
### PREREQUISITES (Windows Setup)
1) Download and Install Python
    https://www.python.org/downloads/
        Check on most of the Optional Features during Python install (e.g. Documentation, pip, td/tk and IDLE, Python test suite, py launcher.  Additional options might be available by the time you are reading this)
        You will also need to set Python in your system environment variables > Path
        OR 
        You could have Python added to environment variables during the Python installation (Advanced Options > Add Python to environment variables)
2) Install IDE (e.g. Visual Studio Code, Pycharm)
    Visual Studio Code > https://code.visualstudio.com/
3) Check that you have updated version of pip.  Install playwright.
    pip install --upgrade pip [Upgrade for pip]
    pip install playwright [Install all the different dependencies and package we need for Playwright]
    playwright install [Install the browsers (e.g. Chromium, Firefox, Webkit) and libraries to record videos automatically.  We don't have to worry about the browser drivers not being in the correct path or place]
4) Test that you will be able to do a synchronous call using Playwright
    You could do python sync.py to test if the existing code works for you
    OR
    Follow instructions from https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A

# REFERENCES
https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A

https://playwright.dev/python/docs/api/class-playwright
