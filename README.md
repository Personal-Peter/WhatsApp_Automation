# WhatsApp Automation

- We are using python library known as [pywhatkit](https://pypi.org/project/pywhatkit/) to automate whatsApp messages.
- To Schedule we are using [Scheduler](https://pypi.org/project/scheduler/).
- Check out the links for furthure understanding.

## Installation packages

1. package

```cmd
pip install pywhatkit
```

2. package

```cmd
pip install scheduler
```

## WhatsApp

```Python
import pywhatkit as whatsapp

phone_number = input('Enter your phone Number\n')
whatsapp.sendwhatmsg(phone_number,"Hay.",13,47,15,True,2) 
```

- In the above program we are importing a [pywhatkit](https://pypi.org/project/pywhatkit/). Which is a python library for sending messages.

- In the function takes the data like `( Phone_number,"Message in quotes",time in hours( 24 hours format), Time in minutes, Time delay after how long the message should be sent, Boolean which takes true or false (Which is used to close the tab where whatsappweb is opened), Time delay in closing the tab)`

## Scheduler

- As the name suggest scheduler is used to schedule a program to run at specfic time ( Daily, Once, Twice, montly ..etc.)
- The only problem we have is that we can't keep our laptop running 24/7 as server. For this we need to use a external server. Which will work 24/7 & execute the code when time comes.

## Work in progress [replit](https://replit.com/)
