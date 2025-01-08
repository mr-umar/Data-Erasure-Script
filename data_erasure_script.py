import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep


# List of data brokers emails
dataBrokersEmails = [
    "data-privacy@acxiom.com",
    "consumer.datadeletion@experian.com",
    "customerservice.eportsupport@equifax.com",
    "privacy@corelogic.com",
    "customersupport@dnb.com",  # Dun & Bradstreet https://support.google.com/adspolicy/answer/13650402
    "datenschutz@schober.de",
    "dpo@bisnode.com",
    "dpo@criteo.com",
    "privacy@zeotap.com",
    "privacy@axiomlaw.com",
    "privacy@intelius.com",
    "privacy@spokeo.com",
    "privacy@datanyze.com",
    "privacy@zoominfo.com"
]



# App-specific password
print("ℹ️ If you have two-factor authentication enabled, please generate an app-specific password at https://myaccount.google.com/apppasswords.\n")

# Function to validate user input
def validateEmailAndPassword():
    while True:
        userEmail = input("> Enter your Gmail address: ")
        userPassword = input("> Enter your Gmail password (or app-specific password): ")
        try:
            # Attempt to connect to Gmail SMTP to validate credentials
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(userEmail, userPassword)
                print("✔️ Gmail credentials verified successfully.")
                return userEmail, userPassword
        except Exception as e:
            print(f"❌ Failed to verify credentials: {e}. Please try again.\n")

# Request user information
userEmail, userPassword = validateEmailAndPassword()
firstName = input("> Enter your first name: ")
lastName = input("> Enter your last name: ")

# Confirm user details before proceeding
print("\nPlease confirm your details:\n")
print(f"- Gmail Address: {userEmail}")
print(f"- First Name: {firstName}")
print(f"- Last Name: {lastName}\n")
confirmation = input("> Do you want to proceed with these details? (Y/N): ").strip().lower()
if confirmation != "yes" or confirmation != "y":
    print("❌ Process canceled by the user.")
    exit()

print("\n\n📧 Sending emails to data brokers...")

# SMTP server configuration
smtpServer = "smtp.gmail.com"
smtpPort = 587


# Email
subject = "Request for Erasure of Personal Data Under the GDPR"
body = f"""
Dear Data Protection Officer,

I am writing to exercise my right under Article 17 of the General Data Protection Regulation (GDPR) to request the immediate erasure of all personal data concerning me that you hold. This includes, but is not limited to, any data collected, processed, or shared with third parties.

As per GDPR requirements, please ensure the following:

1. Erase all personal data: Permanently delete all personal data related to me from your records and databases.

2. Inform third parties: Notify any third parties with whom you have shared my personal data of this erasure request and ensure they also delete the data in question.

3. Confirmation of action: Provide written confirmation that the above actions have been completed within one month of receipt of this request, as stipulated by GDPR.

I am including my email address as an initial identifier for you to verify and process this request: {userEmail}.

If you require any further information to confirm my identity or to process this request, please contact me promptly.

Failure to comply with this request will compel me to lodge a formal complaint with the relevant supervisory authority and seek legal remedies available under GDPR.

Thank you for your prompt attention to this matter.

Sincerely,

{firstName} {lastName}
{userEmail}
"""

# Send email function
def sendEmail(recipientEmail):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = userEmail
        msg["To"] = recipientEmail
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server
        with smtplib.SMTP(smtpServer, smtpPort) as server:
            server.starttls()  # Start a secure connection
            server.login(userEmail, userPassword)
            server.sendmail(userEmail, recipientEmail, msg.as_string())

        print(f"✔️ Email successfully sent to {recipientEmail}")
    except Exception as e:
        print(f"❌ Failed to send email to {recipientEmail}: {e}")

# Send emails to all data brokers
for brokerEmail in dataBrokersEmails:
    sendEmail(brokerEmail)
    sleep(3)

