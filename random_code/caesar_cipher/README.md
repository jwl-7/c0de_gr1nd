# Caesar Cipher
Write a program that encrypts plaintext -> ciphertext using the caesar cipher.\
Add a function that decrypts the ciphertext -> plaintext using frequency analysis.\
Add a function that decrypts the ciphertext -> plaintext using brute force.

## Examples
```
Pick a mode [1-3]: 1
Enter plaintext: hello world
Enter shift key [1-26]: 5

Encipherment
-------------------------------------------
[5] MJQQT BTWQI
```

```
Pick a mode [1-3]: 2
Enter ciphertext: MJQQT BTWQI

Frequency Analysis
-------------------------------------------
Q : 3
T : 2
M : 1
J : 1

Top Possible Shift Keys: [12, 11, 8, 5]

Top Possible Translations
-------------------------------------------
[12] AXEEH PHKEW
[11] BYFFI QILFX
[8] EBIIL TLOIA
[5] HELLO WORLD
```

```
Pick a mode [1-3]: 3
Enter ciphertext: MJQQT BTWQI

Brute Force
-------------------------------------------
[1] LIPPS ASVPH
[2] KHOOR ZRUOG
[3] JGNNQ YQTNF
[4] IFMMP XPSME
[5] HELLO WORLD
[6] GDKKN VNQKC
[7] FCJJM UMPJB
[8] EBIIL TLOIA
[9] DAHHK SKNHZ
[10] CZGGJ RJMGY
[11] BYFFI QILFX
[12] AXEEH PHKEW
[13] ZWDDG OGJDV
[14] YVCCF NFICU
[15] XUBBE MEHBT
[16] WTAAD LDGAS
[17] VSZZC KCFZR
[18] URYYB JBEYQ
[19] TQXXA IADXP
[20] SPWWZ HZCWO
[21] ROVVY GYBVN
[22] QNUUX FXAUM
[23] PMTTW EWZTL
[24] OLSSV DVYSK
[25] NKRRU CUXRJ
[26] MJQQT BTWQI
```