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
    - [ ] pip install pytest-playwright 
        [Install pytest]
4) Test that you will be able to do a synchronous call using Playwright<br/>
    To run the sync.py file, just type in below command in your Visual Studio Code Terminal<br/>
        python sync.py<br/>
    OR<br/>
    Follow instructions from https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A

5) Easy means for getting locators is playwright codegen website_url

### References
https://playwright.dev/python/docs/api/class-playwright
https://www.youtube.com/watch?v=H2-5ecFwHHQ
https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A
<!-- How to select an element by id in Playwright -->
https://stackoverflow.com/questions/75151754/how-can-i-select-an-element-by-id

### Playwright Locators for Python
https://playwright.dev/python/docs/locators

<!-- References for RegEx -->
### RegEx in Python
https://stackoverflow.com/questions/9012008/pythons-re-return-true-if-string-contains-regex-pattern
https://www.w3schools.com/python/python_regex.asp
https://stackoverflow.com/questions/21405267/how-to-use-regex-in-xpath-contains-function

### For Future Exploration
<!-- Behave with Playwright -->
https://wikomtech.com/blog/create-a-behavior-driven-development-bdd-framework-with-playwright-and-python/

### Async
https://apidog.com/blog/await-in-playwright/
https://jadala-ajay16.medium.com/why-do-we-write-await-async-in-playwright-javascript-typescript-fa3c92f82841
https://blog.apify.com/python-asyncio-tutorial/
https://blog.apify.com/python-playwright/

### Page Object Model Async
https://playwright.dev/python/docs/pom