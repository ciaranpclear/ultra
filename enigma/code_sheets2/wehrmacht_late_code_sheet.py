"""


WEHRMACHT ENIGMA (LATE)

 Date | UKW | Walzenlage | Ringstellung | Grundstellung |      Steckerverbindungen      |   Kenngruppen   |
------|-----|------------|--------------|---------------|-------------------------------|-----------------|
      |     |            |              |               |                               |                 |
  31. |  C  | I  II  V   | 10  14  02   |  12  19  17   | BF SD AY HG OU QC WI RL XP ZK | YQV VUC XXO GVF |
------|-----|------------|--------------|---------------|-------------------------------|-----------------|


WEHRMACHT LATE ENCRYPTION/DECRYPTION PROCEDURES

1940 -> 31 October 1944

ENCRYPTION PROCEDURE

01. From the code sheet select a date.

02. Setup the machine according to that days settings.

03. Select two random characters and one of the three character kengruppen to create A
    five character message identifier.

    USNJD

04. Create a random three character initial rotor setting.

    FXJ

05. Set the machines rotor settings to the initial rotor setting FXJ.

06. Create a random three character message key.

    USF

07. With the machine set to the initial rotor settings encrypt the message
    key twice.

    ANEINY

08. Set the machines rotor settings to the message key USF.

09. Encrypt the message.

10. Create the message header.

    1230 = 3tle = 1tl = 200 = FXJ ANEINY

    USNJD BAIST QOCFS IWYDV CPIHK AYSS WBAUC
    OATFN QOAML ZIAYS BQYDJ IQTEV CHSF ZOPQW
    ABCUW SOKJD AYWVC SKNGS QGSUB XIKS QBUDI

    * 1230 is the time the message was sent. 24 hour GMT.
    * 3tle is the number of parts to the message.
    * 1tl is the first part of the message.
    * 200 is the number of characters in the message including the five character
      message identifier.
    * ANEINY is the twice encrypted message key.

11. Send the message. The header is sent in plain text.

DECRYPTION PROCEDURE

01. From the code sheet select a date.

02. Setup the machine according to that days settings.

03. Set the machines rotor settings to the initial rotor setting in the message header.

04. Decrypt the six character message key to get USF.

    USFUSF

05. Set the machines rotor settings to the message key.

06. Excluding the first five characters of the message which is the two random characters
    and three character kengruppen decrypt the rest of the message. The kengruppen can be
    used to confirm the key sheets daily settings that where used to send the message.




From 31 October 1944

ENCRYPTION PROCEDURE

01. From the code sheet select a date.

02. Setup the machine according to that days settings.

03. Select two random characters and one of the three character kengruppen to create A
    five character message identifier.

    USNJD

04. Create a random three character initial rotor setting.

    FXJ

05. Set the machines rotor settings to the initial rotor setting FXJ.

06. Create a random three character message key.

    USF

07. With the machine set to the initial rotor settings encrypt the message
    key.

    ANE

08. Set the machines rotor settings to the message key USF.

09. Encrypt the message.

10. Create the message header.

    1230 = 3tle = 1tl = 200 = FXJ ANEINY

    USNJD BAIST QOCFS IWYDV CPIHK AYSS WBAUC
    OATFN QOAML ZIAYS BQYDJ IQTEV CHSF ZOPQW
    ABCUW SOKJD AYWVC SKNGS QGSUB XIKS QBUDI

    * 1230 is the time the message was sent. 24 hour GMT.
    * 3tle is the number of parts to the message.
    * 1tl is the first part of the message.
    * 200 is the number of characters in the message including the five character
      message identifier.
    * ANE is the encrypted message key.

11. Send the message. The header is sent in plain text.

DECRYPTION PROCEDURE

01. From the code sheet select a date.

02. Setup the machine according to that days settings.

03. Set the machines rotor settings to the initial rotor setting in the message header.

04. Decrypt the message key to get USF.

    USF

05. Set the machines rotor settings to the message key.

06. Excluding the first five characters of the message which is the two random characters
    and three character kengruppen decrypt the rest of the message. The kengruppen can be
    used to confirm the key sheets daily settings that where used to send the message.
"""
