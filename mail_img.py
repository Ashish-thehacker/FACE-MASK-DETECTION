import smtplib
import imghdr
from email.message import EmailMessage
# class mail_alert:
def mail_alert(time, name):
    Sender_Email = 'gauravgutagg10000@gmail.com'
    Reciever_Email_1 = 'gs2016064@sgsitsindore.in'
    # Reciever_Email_2 = 'gauravguptagg10000@gmail.com'
    # recipients = ['gs2016064@sgsitsindore.in', 'gauravguptagg10000@gmail.com']
    Password = 'vbfbqopnyzbhxnnz'
    alert_message = name + " has broken Rules and Regulation at " + time
    newMessage = EmailMessage()                         
    newMessage['Subject'] = "msg alert" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email_1 
    # newMessage['To'] = ", ".join(recipients)
    # newMessage['To'] = Reciever_Email_2                  
    newMessage.set_content(alert_message) 

    # with open("images/harsh123.jpg", 'rb') as f:
    #     image_data = f.read()
    #     image_type = imghdr.what(f.name)
    #     image_name = f.name

    # newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
    print("mail sent successfully")

mail_alert("26/08/22","harsh")