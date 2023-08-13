class EmailService: # type: ignore
    def send_email(self,message,receiver):
        print(f"sending email: {message} to {receiver}")
class SmsService: # type: ignore
    def send_sms(self,message,receiver):
        print(f"Sending SMS: {message} to {receiver}")
class NotificationService:
    def __init(self):
        self.email_service = EmailService()
        self.sms_serivce = SmsService()
    def send_notification(self,message,recevier,method):
        if method == 'email':
            self.email_service.send_email(message,recevier)
        elif method =="sms":
            self.sms_serivce.send_sms(message,recevier)
"""
Direcrty depends on concrete class 
** This violates the DIP High-level modules should not depend on low-level modules both should depend on absraction 
    *** Harder to change
    *** less flexible
    
""" 

from abc import ABC,abstractclassmethod

class IMessageService(ABC):
    @abstractclassmethod
    def send(self,message,recevier):
        pass
class EmailService(IMessageService):
    def send(self,message,recevier):
        print(f"Sending email: {message} to {recevier}")
class SmsService(IMessageService):
    def send(self,message,recevier):
        print(f"Sending SMS: {message} to {recevier}")
    
class NotitficationService:
    def __init__(self,message_service: IMessageService):
        self.message_service = message_service
    def send_notification(self,message,recevier):
        self.message_service.send(message,recevier)
        
