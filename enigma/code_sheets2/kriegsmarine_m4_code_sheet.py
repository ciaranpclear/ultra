"""


KRIEGSMARINE M4 ENIGMA

MACHINE SETUP PROCEDURE

INNER SETTINGS STANDARD M4 ENIGMA

Monats-tag |     Innere Einstellung           |
-----------|----------------------------------|
           |                                  |
    29.    | B Beta     VII     IV      V     |
           |   A        G       N       O     |
-----------|----------------------------------|
    27.    | B Beta     II      I       VIII  |
           |   A        T       Y       F     |
-----------|----------------------------------|

Monats-tag |                 Steckerverbindungen                 | Grundstellung |
-----------|-----------------------------------------------------|---------------|
    30.    | 18/16 17/4 21/6 3/16 19/14 22/7 8/1 12/25 5/9 10/15 |  H  F  K  D   |
-----------|-----------------------------------------------------|---------------|
    29.    |                                                     |               |



INNER SETTINGS USING UKW-D (DORA)

Monats-tag |       Innere Einstellung       |
-----------|--------------------------------|
           |                                |
    29.    | Beta    VII     IV       V     |
           | A       G       N        O     |
-----------|--------------------------------|

Monats-tag | Dora  |      Steckerverbindungen      | Grundstellung |
-----------|-------|-------------------------------|---------------|
    30.    | AB CD | AB CD EF GH IJ KL MN OP QR ST |  H  F  K  D   |
-----------|       |-------------------------------|---------------|
    29.    | EF GH | AB CD EF GH IJ KL MN OP QR ST |  I  G  R  V   |
-----------|       |-------------------------------|---------------|
    28.    | IJ KL | AB CD EF GH IJ KL MN OP QR ST |  D  U  N  W   |
-----------|       |-------------------------------|---------------|
    27.    | MN OP | AB CD EF GH IJ KL MN OP QR ST |  C  I  K  S   |
-----------|       |-------------------------------|---------------|
    26.    | QR ST | AB CD EF GH IJ KL MN OP QR ST |  X  Y  M  R   |
-----------|       |-------------------------------|---------------|
    25.    | UV WX | AB CD EF GH IJ KL MN OP QR ST |  V  H  T  X   |
-----------|       |-------------------------------|---------------|


KRIEGSMARINE M4 ENCRYPTION/DECRYPTION PROCEDURES

ENCRYPTION PROCEDURE

01. From the code sheets inner settings select a date and message indicator.

02. Use the selected inner settings to set the reflector type and rotor types.
    Ensure that the ring setting of the fourth rotor is set to 'A'. Set the remaining
    ring setting from left to right.

03. In outer settings find the same date and message indicator. Use the outer settings
    to set the plugboard settings and rotor settings.

04. Create a random trigram. VRM.

05. Type the above trigram into the machine and record the output. KKZ.

06. Set the conventional rotor settings to the output trigram of the enigma machine. Do
    not change the rotor setting of the fourth rotor.

07. Write down the message indicator and add a random letter in front of it. (L)MPV.

08. Write down the random trigram that was created in step 04 and add a random letter to
    the end of it. VRM(Q).

09. Write these two quadgrams on top of each other.
    LMPV
    VRMQ

10. Write down the letter pairs as follows.
    LV=    MR=    PM=    VQ=

11. Use the bigram tables to encrypt each letter pair.
    LV=AX  MR=CJ  PM=AC  VQ=ZL

12. Combine the encrypted letters as follows.
    AXCJ  ACZL

13. Create the message header.
    BRU     2130    27      001     24

    * BRU is a random trigram.
    * 2130 is the time the message was sent. 24 hour GMT.
    * 31 is the date.
    * 001 is the message tracking number.
    * 24 is the number of four letter blocks in the message.

14. The encrypted message is padded at the beginning and end by the two quadgrams.

    AXCJ ACZL .... .... .... .... .... .... .... .... .... AXCJ ACZL

15. Send the header and mesage. Only the part of the message repressented by .... is encrypted.


DECRYPTION PROCEDURE

01. Extract the two four letter blocks from the beginning and end of the message.
    AXCJ ACZL

02. Regroup the letters as follows.
    AXCJ -> AX CJ AC ZL
    ACZL

03. Prepare to decrypt letter pairs using the bigram tables.
    AX=    CJ=    AC=    ZL=

04. Decrypt the letter pairs using the bigram tables.
    AX=LV  CJ=MR  AC=PM  ZL=VQ

05. Write down the decrypted letter pairs.
    LV  MR  PM  VQ

06. Write out the letter pairs as follows to create a quadgram.
    LV  MR  PM  VQ
    ||  ||  ||  ||
    L|  M|  P|  V|
     V   R   M   Q

07. Write down the top quadgram and drop the first letter.
    MPV

08. Write down the bottom quadgram.
    VRMQ

09. Use the trigram MPV to look up the key in the inner settings.

10. Use the selected inner settings to set the reflector type and rotor types.
    Ensure that the ring setting of the fourth rotor is set to 'A'. Set the remaining
    ring setting from left to right.

11. In outer settings find the same date and message indicator. Use the outer settings
    to set the plugboard settings and rotor settings.

12. Type the quadgram VRMQ into the enigma machine and record its output KKZW.

13. Set the conventional rotor settings to KKZ.

14. Decrypt the cipher text that is between the two quadgrams from step 01.
"""
