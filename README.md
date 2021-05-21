A python selenium application to monitor, notify and checkout  
NOTE: currently, only Best Buy is supported. Other websites and applications may come depending on time, and utility

# Requirements
## Software
1. Selenium
2. twilio (for text notifications of availability)
3. Chrome webdriver path added to environment. (Unfortunately this excludes ARM processors as there is no chrome browser currently)

## Best Buy
Currently, the process requires an account with a credit card and shipping information already added.

## Personal Information
The project requires that the Best Buy account email, password, and default credit card ccv be provided in the `topSecretInfo.py` file. Also there, are the phone number, and sid and token fields for twilio