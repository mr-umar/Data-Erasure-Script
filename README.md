# Data Erasure Script 📧

## Overview 🌍
This Python script helps users exercise their **GDPR rights** by sending personalized emails to data brokers requesting the erasure of personal data. It automates the process of contacting multiple data brokers via Gmail's SMTP server.

## Features ✨
- **User Input**: Requests your Gmail address, app-specific password, first name, and last name.
- **Credential Validation**: Verifies Gmail credentials before proceeding.
- **GDPR Compliance**: Drafts a formal GDPR-compliant email to request data deletion.
- **Multiple Recipients**: Sends emails to a predefined list of major data brokers.
- **Secure Communication**: Uses TLS encryption for secure connections with Gmail's SMTP server.

## Prerequisites ⚙️
1. **Python**: Ensure Python is installed on your system.
2. **App-Specific Password**:
   - If two-factor authentication (2FA) is enabled for your Gmail account, generate an app-specific password.
   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords) and follow the instructions.

## Setup 🛠️
1. **Install Required Libraries**:
   No external libraries are required as the script uses Python's built-in `smtplib` and `email` modules.

2. **Download the Script**:
   Save the script as `data_erasure_script.py`.

3. **Prepare Your Gmail Account**:
   - Ensure your account has access to less secure apps enabled, or use an app-specific password.

## How to Use 🚀
1. **Run the Script**:
   Execute the script in your terminal or IDE:
   ```bash
   python data_erasure_script.py
   ```

2. **Provide Information**:
   - Enter your Gmail address.
   - Enter your Gmail password or app-specific password.
   - Enter your first name and last name.

3. **Confirmation**:
   - Review the details you entered.
   - Confirm to proceed with sending the emails.

4. **Email Dispatch**:
   - The script sends GDPR-compliant emails to all data brokers in the predefined list.
   - You will see confirmation messages for each email sent.

## List of Data Brokers 📋
- Acxiom: `data-privacy@acxiom.com`
- Experian: `consumer.datadeletion@experian.com`
- Equifax: `customerservice.eportsupport@equifax.com`
- CoreLogic: `privacy@corelogic.com`
- Dun & Bradstreet: `customersupport@dnb.com` 
- Schober: `datenschutz@schober.de`
- Bisnode: `dpo@bisnode.com`
- Criteo: `dpo@criteo.com`
- Zeotap: `privacy@zeotap.com`
- Axiom: `privacy@axiomlaw.com`
- Intelius: `privacy@intelius.com`
- Spokeo: `privacy@spokeo.com`
- Datanyze: `privacy@datanyze.com`
- ZoomInfo: `privacy@zoominfo.com`

## Email Template ✉️
Below is the template used by the script:

---
```text
Subject: Request for Erasure of Personal Data Under GDPR

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
```
---

## Notes 📝
- **Email Rate Limits**: Gmail may limit the number of emails sent in a short period. The script includes a delay to mitigate this.

## Disclaimer ⚠️
This script is provided for informational purposes and should be used responsibly. Ensure you have the legal right to request data deletion from the listed brokers.
