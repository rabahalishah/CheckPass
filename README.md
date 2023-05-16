
# About the Project


## CheckPass
Checkpass is an app script whcih will help you in finding the most secure password for your valuable accounts. CheckPass is capable of safely checking your password whether it has pawned or not. If yes, then how many times it has pawned.

Feel free to check your passwords because the password which user will enter will not be send directly to the API. The password firts would be encoded into SHA-256 code whihc is impossible to decode. In this way user will be safely able to select their passwords for their accounts.
## Checking Password result 1
You can see this password which I had passed as an argument was pawned too many times. So this app is advising me not to select this password for my use as it has pawned too many times.

![App Screenshot](https://github.com/rabahalishah/CheckPass/assets/117630286/af873f06-56bc-4293-95e6-256b8e01edf2)

## Checking Password result 2
In this case, I passed a random difficult password. It has check it safely and allowed to set this gibberish as my password as it has not pawned ever.

![App Screenshot](https://github.com/rabahalishah/CheckPass/assets/117630286/6f5c4532-2655-4692-a098-e99f6fb41fb2)



## Built With

<img src="https://user-images.githubusercontent.com/36489953/78834570-0f5b2e80-79ef-11ea-8260-11a33e15fc1c.png" width="150" height="150" />



# Getting Started
Following are some easy steps you have to follow to run this project in your machine
## Prerequisites
* Install [Python](https://www.python.org/downloads/)
  

## Installation

1. Fork this Repo
2. Clone this repo

```bash
  git clone https://github.com/github_username/repo_name.git
```
3. Create Virtual environment either using pip or conda respectively
```bash
  python -m venv myvenv
  conda create -n my-env
```
4. Activate your virtual environment 
```bash
  . Activate
  conda activate my-env
```
5. Now go to project directory and run the following command
```bash
  pip install requests
  pip install urllib3==1.26.6 
```
## How to Run
Following is syntax to give the aruguments to this app. For security purposes we have design this app to take input aruguments in the form of text/doc file. So you password couldn't even store in your machine.
```bash
  python checkpass.py "path/filename"
```



## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch
```bash
  git checkout -b feature/AmazingFeature
```
3. Commit your Changes 
```bash
  git commit -m 'Add some AmazingFeature'
```
4. Push to the Branch 
```bash
  git push origin feature/AmazingFeature
```
5. Open a Pull Request


## Contact
Rabah Ali Shah - Software Developer
- https://www.linkedin.com/in/rabah-ali-shah-774706202 
- muhammadrabah.ali46@gmail.com
