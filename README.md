##### By FeverCode 
### Pitch-Create

## Table of Content

+ [Description](#description)
+ [Requirements](#requirements)
+ [Installation](#installation)
+ [Running Project](#running-project)
+ [Running Tests](#running-tests)
+ [Behaviour Driven Development(BDD)](#behaviour-driven-development-bdd)
+ [Technologies Used](#technologies-used)
+ [Licence](#licence)
+ [Authors Info](#authors-info)


## Description
<p>In life, you only have 60 seconds to impress someone. 1 minute can make or break you. How do we make sure that you use your 1 minute to actually say something meaningful? This is an application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them..</p>

Live link to the project
[Pitch-Create](https://pitch-create.herokuapp.com/)

## Requirements
* A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```
-Python version 3.8
-Flask
-Pip
-virtualenv
-A text  Editor
```

## Installation
* Open Terminal {Ctrl+Alt+T} on ubuntu
* git clone `https://github.com/FeverCode/pitch-create`
* cd News-Source
* code . or atom . based on prefered text editor

## Running Project
* On terminal where you have opened the cloned project
    * `python3.8 -m venv --without-pip virtual` - To create virtual enviroment
    * `source virtual/bin/activate` - To activate the virtual enviroment
    * `pip install -r requirements.txt` - To install requirements
    * `$ chmod a+x start.sh` - to make the projet executable
    * `$ ./start.sh` - to run the project

## Running Tests
* To run test for the project
    * `$ python3.8 manager.py test`

## Behaviour Driven Development (BDD)
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments template with your comment and other comments|
 
## Technologies Used
* python3.8
* Flask


## Licence

MIT License

Copyright (c) [2022] [FeverCode]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Authors Info

LinkedIn - [https://www.linkedin.com/in/gedion-onsongo-112543210/)

Reddit - [https://www.reddit.com/user/stainscode]
   


