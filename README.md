# Virtual_Assistant - Modular(Webhooks)

### One main PC as the brains (Gru)
#### The alexa skill endpoint will go to a pythonanywhere server which will reformat the json and send it here.
#### Then sending webhooks off to the other devices.



## Prerequests:
- `pip install -r requirements.txt`

## How To Format `.env` file:
- Create a file called `.env`
- In it should be the following:

- In between the ' ' you need to add your own token
```

# .env

Master = 'MasterName'

losant_url = "https://triggers.losant.com/webhooks/blahblahblah"

#Other
wolframappid = 'ABCDEF-1GHIJKLM2N'

#email
Your_Username = 'someone@something.com'
Codingemail = 'someoneelse@something.com'
Normalemail = 'someone@something.com'
Your_Password = 'abcdefghijklmnop'




```

### To Do Thing1:
- `python file1.py --arg1:thing --arg2:thing1/thing2`
- You need to have `--arg1:` or `--arg2:` before an argument
- The first argument is to *do this thing*
- If you use `thing1` for your second argument - it will do `thing1`
- If you use `thing2` for your second argument - it will do `thing2`


## Future:
[Read this TODO File to see what I plan to do in the future](TODO)

