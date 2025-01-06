# Data Erasure Script

## Overview
This Python script is designed to help users exercise their **GDPR rights** by sending personalized emails to data brokers requesting the erasure of personal data. It automates the process of contacting multiple data brokers by leveraging Gmail's SMTP server.

## Features
- **User Input**: Requests your Gmail address, app-specific password, first name, and last name.
- **Compliance with GDPR**: Drafts a formal GDPR-compliant email to request the deletion of personal data.
- **Multiple Recipients**: Sends emails to a predefined list of major data brokers.
- **Secure Connection**: Uses TLS encryption for secure communication with Gmail's SMTP server.

## Prerequisites
1. **Python**: Ensure you have Python installed on your system.
2. **App-Specific Password**: If two-factor authentication (2FA) is enabled for your Gmail account, generate an app-specific password:
   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords).
   - Follow the instructions to generate a password for this script.

## Setup
1. **Install Required Libraries**:
   No external libraries are required as the script uses Python's built-in `smtplib` and `email` modules.

2. **Download the Script**:
   Save the script as `data_erasure_script.py`.

3. **Prepare Your Gmail Account**:
   - Ensure your account has access to less secure apps enabled, or use an app-specific password.

## How to Use
1. **Run the Script**:
   Execute the script in your terminal or IDE:
   ```bash
   python data_erasure_script.py
   ```

2. **Provide Information**:
   - Enter your Gmail address.
   - Enter your Gmail password or app-specific password.
   - Enter your first name and last name.

3. **Email Dispatch**:
   - The script sends GDPR-compliant emails to all data brokers in the predefined list.
   - You will see confirmation messages for each email sent.

## List of Data Brokers
- Acxiom: `data-privacy@acxiom.com`
- Experian: `consumer.datadeletion@experian.com`
- Equifax: `uk.dataprotection@equifax.com`
- CoreLogic: `privacy@corelogic.com`
- Dun & Bradstreet: `data-privacy@dnb.com`
- Schober: `datenschutz@schober.de`
- Bisnode: `privacy@bisnode.com`
- Criteo: `dpo@criteo.com`
- Zeotap: `privacy@zeotap.com`
- Axiom: `privacy@axiomlaw.com`
- Intelius: `privacy@intelius.com`
- Spokeo: `privacy@spokeo.com`
- Whitepages: `privacy@whitepages.com`
- Datanyze: `privacy@datanyze.com`
- ZoomInfo: `privacy@zoominfo.com`

## Email Template
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

## Notes
- **Email Rate Limits**: Gmail may limit the number of emails sent in a short period. The script includes a delay to mitigate this.
- **Error Handling**: The script provides feedback for any errors encountered while sending emails.

## Disclaimer
This script is provided for informational purposes and should be used responsibly. Ensure you have the legal right to request data deletion from the listed brokers.
