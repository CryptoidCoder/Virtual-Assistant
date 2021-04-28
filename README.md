# Virtual-Assistant

## This Is Where All The Code Is Kept For My Virtual-Assistant Project

<br> 

### If you Want To Download This Code Then see The Commands Below:

#### [Computer_Only](https://github.com/CryptoidCoder/Virtual-Assistant/tree/Computer-Only)
- This is the part that runs solely on a computer
- To Get The Code:
- - `git clone --branch Computer_Only https://CryptoidCoder/Virtual-Assistant.git`

#### [Modular(Discord)](https://github.com/CryptoidCoder/Virtual-Assistant/tree/Modular(Discord))
- This is the part that uses discord.py to compuincate between devices
- To Get The Code:
- - `git clone --branch Modular(Discord) https://CryptoidCoder/Virtual-Assistant.git`

#### [Modular(I2C)](https://github.com/CryptoidCoder/Virtual-Assistant/tree/Modular(I2C))
- This is the part that uses microcontrollers and I2C to communicate
- To Get The Code:
- - `git clone --branch Modular(I2C) https://CryptoidCoder/Virtual-Assistant.git`

#### [Modular(Webhooks)](https://github.com/CryptoidCoder/Virtual-Assistant/tree/Modular(Webhooks))
- This is the part that uses webhooks to connect to a losant workflow
- To Get The Code:
- - `git clone --branch Modular(Webhooks) https://CryptoidCoder/Virtual-Assistant.git`


### Running:
- Generally there is a `requirements.txt` file, so run the following command to get all the modules:
- - `pip install -r requirements.txt`
- you will often have to create `.env` files with api keys etc in them
- There should alwasy be a README.md file that will explain anything else though.


### More About The Project:

- ### Virtual Assistant

There will be one device (a raspberry pi probably) running a host script and that will send information to other Pi's, so they can do other things.

This will mean that all you have to do is edit a couple of lines and you are ready to go.
