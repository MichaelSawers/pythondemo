print('Welcome to Sawers Law\'s first computer automated program.\
 Please answer the following questions, and you will be provided with a subject line and body text to paste into your Outlook email to easily send to clients.')

print('Please enter the client\'s full name, with a space in between: ')
clientsName = input()

print('Please enter the reponsible lawyer\s full name: ')
lawyersName = input()

print('Please enter the date of the meeting in the format (month DD YYYY): ')
meetingDate = input()

print('Please enter the time of the meeting in the format (00:00 PM or AM): ')
timeOfMeeting = input()

if lawyersName == "Bob Sawers":
    rate = "$393.75"
    lawyersEmail = "rs@smlaw.ca"
elif lawyersName == "Paula Kay":
    rate = "$393.75"
    lawyersEmail = "plk@smlaw.ca"
elif lawyersName == "Stewart LaPrarie":
    rate = "$262.50"
    lawyersEmail = "sl@smlaw.ca"
elif lawyersName == "Lee Carter":
    rate = "$262.50"
    lawyersEmail = "lc@smlaw.ca"
elif lawyersName == "Maria Faheem":
    rate = "$262.50"
    lawyersEmail = "mf@smlaw.ca"

import pyperclip
subject = 'Phone Consultation at ' + timeOfMeeting + ' on ' + meetingDate + ' with ' + lawyersName
pyperclip.copy(subject)
print('the subject line has now been copied to the clipboard. Please go to your Outlook email and paste it in now.')
while True:
    if input('Are you ready to move forward? Please type y or n: ') != 'n':
        break

#text copying below
body = f"""Dear {clientsName},
 
I am writing to confirm your telephone consultation appointment with {lawyersName} on {meetingDate} at {timeOfMeeting}. As discussed, the consultation fee is {rate} which includes GST. 
 
Please find attached an Acknowledgement of Preliminary Advice Form and a Credit Card Authorization Form, both to be filled out and returned for processing prior to your appointment. Alternatively, you can e-transfer your payment to: 
 
Email: reception1@smlaw.ca
 
Password: Consult123
 
If you do not have access to a printer or scanner and are unable to fill out the attached forms, please provide the information required for a payment by credit card, with express instructions (by email) authorizing us to process the payment for this consultation. For the preliminary advice form, please provide us with express instructions (by email) that you confirm and acknowledge the contents of the form.  
 
Can you please also provide a street mailing address for our records.
 
I look forward to receiving a copy of all documentation relating to your employment for your lawyer to review prior to your consultation. You can provide all the required documents by email to {lawyersEmail} with a CC to reception1@smlaw.ca.
 
{lawyersName} will contact you at {timeOfMeeting} on {meetingDate}.
 
Should you have any questions before your appointment, please do not hesitate to contact our office.
 
Regards,
Zoe Lloyd"""

pyperclip.copy(body)
print('the body has now been copied to the clipboard. Please go to your Outlook email and paste it in now.')




    




