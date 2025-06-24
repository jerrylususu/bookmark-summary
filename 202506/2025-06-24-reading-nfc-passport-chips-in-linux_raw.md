Title: Reading NFC Passport Chips in Linux

URL Source: https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/

Published Time: 2025-06-24T12:34:49+01:00

Markdown Content:
For boring and totally not nefarious reasons, I want to read all the data contained in my passport's NFC chip using Linux. After a long and annoying search, I settled on [roeften's pypassport](https://github.com/roeften/pypassport).

I can now read all the passport information, including biometrics.

*   [Table of Contents](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#table-of-contents)
------------------------------------------------------------------------------------------------------------

    *   [Background](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#background)        *   [Recreating the MRZ](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#recreating-the-mrz)            *   [Python code to generate an MRZ](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#python-code-to-generate-an-mrz)
    *   [Can you read a cancelled passport?](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#can-you-read-a-cancelled-passport)
    *   [Cryptography and other security](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#cryptography-and-other-security)
    *   [Can you brute-force a passport?](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#can-you-brute-force-a-passport)        *   [Is it worth brute-forcing a password?](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#is-it-worth-brute-forcing-a-password)
    *   [Installing](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#installing)
    *   [Getting structured data](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#getting-structured-data)        *   [Saving the image](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#saving-the-image)
    *   [What didn't work](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#what-didnt-work)        *   [mrtdreader](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#mrtdreader)
        *   [Jean-Francois Houzard's and Olivier Roger's pyPassport](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#jean-francois-houzards-and-olivier-rogers-pypassport)
        *   [beaujean's pyPassport](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#beaujeans-pypassport)
        *   [d-Logic](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#d-logic)
        *   [Android reader](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#android-reader)
    *   [Is it worth it?](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#is-it-worth-it)

[Background](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#background)
----------------------------------------------------------------------------------------------

The NFC chip in a passport is protected by a password. The password is printed on the inside of the physical passport. As well as needing to be physically close to the passport for NFC to work[0](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#fn:long "There are some commercially available long range readers - up to 15cm! I've no doubt some clever engineer has made a some high-powered radio device which can read things from a mile away using a…"), you also need to be able to see the password. The password is printed in the "Machine Readable Zone" (MRZ) - which is why some border guards will swipe your passport through a reader before scanning the chip; they need the password and don't want to type it in.

I had a small problem though. I'm using my old passport[1](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#fn:old "I'm not dumb enough to do this stuff on a live passport!") which [has been cancelled](https://www.gov.uk/government/publications/cancellation-of-passports/cancelling-british-passports-accessible#cancelling-epassport-version-2). Cancelling isn't just about revoking the document. It is also physically altered:

> Cut off the bottom left hand corner of the personal details page, making sure you cut the MRZ on the corner opposite the photo.

So a chunk of the MRZ is missing! Oh no! Whatever can we do!?

### [Recreating the MRZ](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#recreating-the-mrz)

The password is made up of three pieces of data:

1.   Passport Number (Letters and Numbers)
2.   Date of Birth (YYMMDD)
3.   Expiry Date (YYMMDD)

Each piece _also_ has a checksum. This calculation is defined in Appendix A to [Part 3 of Document 9303](https://www.icao.int/publications/Documents/9303_p3_cons_en.pdf).

Oh, and there's a checksum for the entire string. It's this final checksum which is cut off when the passport cover is snipped.

The final password is: `Number Number-checksum DOB DOB-checksum Expiry Expiry-checkum checksum-of-previous-digits`

#### [Python code to generate an MRZ](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#python-code-to-generate-an-mrz)

If you know the passport number, date of birth, and expiry date, you can generate your own Machine Readable Zone - this acts as the password for the NFC chip.

![Image 1](https://shkspr.mobi/blog/wp-content/plugins/tempest-highlight//svg/python.svg) Python 3
```
def calculateChecksum( value ):
    weighting = [7,3,1]
    characterWeight = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,  
        '8': 8, '9': 9, '<': 0, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 
        'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 
        'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 
        'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35
    }
    counter = 0
    result = 0
    for x in value:
        result += characterWeight[str(x)] * weighting[counter%3]
        counter += 1
    return str(result%10)

def calculateMRZ( passportNumber, DOB, expiry ):
    """
    DOB and expiry are formatted as YYMMDD
    """
    passportCheck = calculateChecksum( passportNumber )
    DOBCheck      = calculateChecksum( DOB )
    expiryCheck   = calculateChecksum( expiry )
    mrzNumber  = passportNumber + passportCheck + DOB + DOBCheck + expiry + expiryCheck
    mrzCheck = calculateChecksum( mrzNumber ).zfill(2)
    mrz =  passportNumber + passportCheck + "XXX" + DOB + DOBCheck + "X" + expiry + expiryCheck + "<<<<<<<<<<<<<<" + mrzCheck
    return mrz

print( calculateMRZ("123456789", "841213", "220229") )
```

[Can you read a cancelled passport?](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#can-you-read-a-cancelled-passport)
---------------------------------------------------------------------------------------------------------------------------------------------

I would have thought that cutting the cover of the passport would destroy the antenna inside it. But, going back to [the UK guidance](https://www.gov.uk/government/publications/cancellation-of-passports/cancelling-british-passports-accessible#cancelling-epassport-version-2):

> You must not cut the back cover on the ePassport

Ah! That's where the NFC chip is. I presume this is so that cancelled passports can still be verified for authenticity.

[Cryptography and other security](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#cryptography-and-other-security)
----------------------------------------------------------------------------------------------------------------------------------------

The security is, thankfully, all fairly standard Public Key Cryptography - [9303 part 11](https://www.icao.int/publications/Documents/9303_p11_cons_en.pdf) explains it in _excruciating_ levels of detail.

One thing I found curious - because the chip has no timer, it cannot know how often it is being read. You could bombard it with thousands of password attempts and not get locked out. Indeed, the specification says:

> the success probability of the attacker is given by the time the attacker has access to the IC, the duration of a single attempt to guess the password, and the entropy of the passport.

[Can you brute-force a passport?](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#can-you-brute-force-a-passport)
---------------------------------------------------------------------------------------------------------------------------------------

Wellllll… maybeeeee…?

Passports are generally valid for only 10 years. So that's 36,525 possible expiry dates.

Passport holders are generally under 100 years old. So that's 3,652,500 possible dates of birth.

That's already 133,407,562,500 attempts - and we haven't even got on to the 1E24 possible passport numbers!

In my experiments, sending an incorrect but valid MRZ results in the chip returning "Security status not satisfied (0x6982)" in a very short space of time. Usually less than a second.

But sending that incorrect attempt seemed to introduce a delay in the next response - by a few seconds. Sending the correct MRZ seemed to reset this and let the chip be read instantly.

So, if you knew the target's passport number and birthday, brute forcing the expiry date would take a couple of days. Not instant, but not impossible.

Most [commercial NFC chips support 100,000 writes](https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf) with no limit for the number of reads. Some also have a 24 bit read counter which increments after every read attempt. After 16 million reads, the counter doesn't increment. It _could_ be possible for a chip to self-destruct after a specific number of reads - but I've no evidence that passport chips do that.

### [Is it _worth_ brute-forcing a password?](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#is-it-worth-brute-forcing-a-password)

If you were to brute-force the MRZ, you would discover the passport-holder's date of birth. You would also get:

*   A digital copy of their photo,
*   Their full name,
*   Their sex [2](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#fn:sex "Sex is complicated. But ICAO allow for \"F for female, M for male, or X for unspecified\"."), 
*   The country which issued their passport, and
*   Their nationality.

All of that is something which you can see from looking at the passport. So there's little value in attempting to read it electronically.

[Installing](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#installing)
----------------------------------------------------------------------------------------------

As mentioned, I'm using [https://github.com/roeften/pypassport](https://github.com/roeften/pypassport)

The only library I needed to install was [pyasn1](https://pypi.org/project/pyasn1/) using `pip3 install pyasn1` - your setup may vary.

Download PyPassport. In the same directory, you can create a test Python file to see if the passport can be read. Here's what it needs to contain:

![Image 2](https://shkspr.mobi/blog/wp-content/plugins/tempest-highlight//svg/python.svg) Python 3
```
from pypassport import epassport, reader

#   Replace this MRZ with the one from your passport
MRZ = "1234567897XXX8412139X2202299<<<<<<<<<<<<<<04"

def trace(name, msg):
    if name == "EPassport":
        print(name + ": " + msg)

r = reader.ReaderManager().waitForCard()

ep = epassport.EPassport(r, MRZ)
ep.register(trace)
ep.readPassport()
```

Plug in your NFC reader, place your passport on it, run the above code. If it works, it will spit out a lot of debug information, including all the data it can find on the passport.

[Getting structured data](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#getting-structured-data)
------------------------------------------------------------------------------------------------------------------------

The structure of the passport data is a little convoluted. [The specification](https://www.icao.int/publications/Documents/9303_p10_cons_en.pdf) puts data into different "Data Groups" - each with its own ID.

By running:

![Image 3](https://shkspr.mobi/blog/wp-content/plugins/tempest-highlight//svg/python.svg) Python 3
```
ep.keys()
```

You can see which Data Groups are available. In my case, `['60', '61', '75', '77']`

*   `60` is the common area which contains some metadata. Nothing interesting there. 
*   `61` is DG1 - the full MRZ. This contains the holder's name, sex, nationality, etc. 
*   `77` is the Document Security Object - this was empty for me. 
*   `75` is DG2 to DG4 Biometric Templates - this contains the image and other metadata. 

Dumping the biometrics - `print( ep["75"] )` - gives these interesting pieces of metadata:

```
'83': '20190311201345',
'meta': {   'Expression': 'Unspecified',
            'EyeColour' : 'Unspecified',
            'FaceImageBlockLength': 19286,
            'FaceImageType': 'Basic',
            'FeatureMask': '000000',
            'FeaturePoint': {0: {'FeaturePointCode': 'C1',
                                'FeatureType': '01',
                                'HorizontalPosition': 249,
                                'Reserved': '0000',
                                'VerticalPosition': 216},
                            1: {'FeaturePointCode': 'C2',
                                'FeatureType': '01',
                                'HorizontalPosition': 141,
                                'Reserved': '0000',
                                'VerticalPosition': 214}},
            'Features': {},
            'Gender': 'Unspecified',
            'HairColour': 'Unspecified',
            'ImageColourSpace': 'RGB24',
            'ImageDataType': 'JPEG',
            'ImageDeviceType': 0,
            'ImageHeight': 481,
            'ImageQuality': 'Unspecified',
            'ImageSourceType': 'Static Scan',
            'ImageWidth': 385,
            'LengthOfRecord': 19300,
            'NumberOfFacialImages': 1,
            'NumberOfFeaturePoint': 2,
            'PoseAngle': '0600B5',
            'PoseAngleUncertainty': '000000',
            'VersionNumber': b'010'
        }
```

If I understand [the testing document](https://www.icao.int/security/mrtd/siteassets/pages/technical-reports/tr%20-%20rf%20and%20protocol%20testing%20part%204%20v2.10.pdf) - the "Feature Points" are the middle of the eyes. Interesting to see that gender (not sex!) and hair colour are also able to be recorded. The "PoseAngle" represents the [pitch, yaw, and roll](https://www.icao.int/Security/FAL/TRIP/Documents/TR%20-%20Portrait%20Quality%20v1.0.pdf) of the face.

### [Saving the image](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#saving-the-image)

Passport images are saved either with JPEG or with [JPEG2000 encoding](https://www.icao.int/Security/FAL/TRIP/Documents/TR%20-%20Portrait%20Quality%20v1.0.pdf). Given the extremely limited memory available photos are small and highly compressed. Mine was a mere 19KB.

To save the image, grab the bytes and plonk them onto disk:

![Image 4](https://shkspr.mobi/blog/wp-content/plugins/tempest-highlight//svg/python.svg) Python 3
```
photo = ep["75"]["A1"]["5F2E"]
with open( "photo.jpg", "wb" ) as f:
   f.write( photo )
```

As expected, the "FeaturePoints" co-ordinates corresponded roughly to the centre of my eyes. Nifty!

[What didn't work](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#what-didnt-work)
---------------------------------------------------------------------------------------------------------

I tried a few different tools. Listed here so you don't make the same mistakes as me!

### [mrtdreader](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#mrtdreader)

The venerable [mrtdreader](https://github.com/rubund/mrtdreader). My NFC device beeped, then mrtdreader said "No NFC device found."

I think this is because [NFC Tools haven't been updated in ages](https://github.com/nfc-tools/libnfc/issues/719).

### [Jean-Francois Houzard's and Olivier Roger's pyPassport](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#jean-francois-houzards-and-olivier-rogers-pypassport)

I looked at [pyPassport](https://code.google.com/archive/p/pypassport/) but it is only available for Python 2.

### [beaujean's pyPassport](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#beaujeans-pypassport)

This [pypassport](https://github.com/beaujeant/pypassport) only checks if a passport is resistant to specific security vulnerabilities.

### [d-Logic](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#d-logic)

[Digital Logic's ePassport software](https://www.d-logic.com/nfc-rfid-reader-sdk/software/epassport-reading/) only works with their hardware readers.

### [Android reader](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#android-reader)

[tananaev's passport-reader](https://github.com/tananaev/passport-reader) - works perfectly on Android. So I knew my passport chip was readable - but the app won't run on Linux.

[Is it worth it?](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#is-it-worth-it)
-------------------------------------------------------------------------------------------------------

Yeah, I reckon so! Realistically, you aren't going to be able to crack the MRZ to read someone's passport. But if you need to gather personal information, it's perfectly possible to do so quickly from a passport.

The MRZ is a _Machine Readable_ Zone - so it is fairly simple to OCR the text and then pass that to your NFC reader.

And even if the MRZ is gone, you can reconstruct it from the data printed on the passport.

Of course, this won't be able to detect fraudulent passports. It doesn't check against a database to see if it has been revoked[4](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#fn:interpol "Nor does it check if the holder is on some Interpol list."). I don't think it will detect any cryptographic anomalies.

But if you just want to see what's on your travel documents, it works perfectly.

* * *

1.   There are some [commercially available long range readers](https://www.shopnfc.com/en/nfc-readers-writers/300-nfc-xl-reader-long-range-hf-reader.html) - up to 15cm! I've no doubt some clever engineer has made a some high-powered radio device which can read things from a mile away using a [Pringle's tube](https://www.makeuseof.com/tag/how-to-make-a-wifi-antenna-out-of-a-pringles-can-nb/). Of note, the [ICAO guidance](https://www.icao.int/publications/Documents/9303_p11_cons_en.pdf) says:

> the unencrypted communication between a contactless IC and a reader can be eavesdropped within a distance of several metres.

[↩︎](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#fnref:long)

2.   I'm not dumb enough to do this stuff on a _live_ passport![↩︎](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#fnref:old)

3.   Sex is complicated[5](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#fn:giggle "Stop giggling at the back!"). But ICAO allow for "[F for female, M for male, or X for unspecified](https://www.icao.int/publications/Documents/9303_p4_cons_en.pdf)".[↩︎](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#fnref:sex)

4.   Nor does it check if the holder is on some Interpol list.[↩︎](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#fnref:interpol)

5.   Stop giggling at the back![↩︎](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/#fnref:giggle)
