Title: How iOS Restricts Features by Region: A Look at MobileGestalt and Eligibility

URL Source: https://type.cyhsu.xyz/2024/09/ios-feature-regional-lockout/

Published Time: 2024-09-26T00:00:00+00:00

Markdown Content:
As agreed by many reviewers, the iPhone 16 series launched this year in a curiously “hollow” state: the heavily touted Apple Intelligence won’t be enabled until iOS 18.1 in October, and even then, it won’t be available to users in mainland China and the European Union. Indeed, this is just the latest example of iPhone features being fragmented by region. Against the increasingly complex landscape of global regulation, the differences in feature sets across regional variants of the iPhone have become so pronounced that they almost seem like different phones.

To opine on the practice I have no interest. Apple is a for-profit that is capable of and responsible for its own decisions of whether and how to comply. On the other hand, users can vote with their wallets. What’s more intriguing to me, though, is how Apple manages this growing set of regional feature restrictions. Below are some brief and preliminary notes of my research based on available information for the perusal of readers with similar interests in the topic. Due to my limited knowledge of iOS development and forensics, errors and omissions may be inevitable, and corrections are welcome.

In short, two components in the current version of iOS, MobileGestalt and Eligibility, are mainly responsible for implementing regional feature restrictions:

*   **MobileGestalt** is a system library located at `/usr/lib/libMobileGestalt.dylib` that acts as a database, storing device models, hardware capabilities, and the availability of certain features for other system components to query.
*   **Eligibility**, comprising a daemon at `/usr/libexec/eligibilityd` and a system library at `/usr/lib/system/libsystem_eligibility.dylib`, considers factors like model, location, locale, and account region per the instructions in code logic and configuration files, to determine whether the device is “eligible” to use a managed feature.

More details below.

**Notes:**

1.  There’s also a system library called Feature Flags located at `/usr/lib/system/libsystem_featureflags.dylib`. It reads plist files under `/var/preferences/FeatureFlags` to toggle some experimental features. For instance, there is a flag that can revert the confusing new layout in the Photos app in iOS 18. However, Feature Flags aren’t commonly used for the regional restrictions discussed here, so I’d left it for future discussion.
2.  This article assumes a basic understanding of the [iOS file system layout](https://theapplewiki.com/wiki/Filesystem:/) and [plist files](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130-SW1).

MobileGestalt
-------------

MobileGestalt, a system library located at `/usr/lib/libMobileGestalt.dylib`, was introduced in iOS 7, taking over the functionality previously handled by GSCapability. _Gestalt_ (German for “form”) refers philosophically to a whole that is greater than the sum of its parts due to its organization. Currently, the most comprehensive (but slightly outdated) researches on MobileGestalt are Jonathan Levin’s article “[Guess-Talt](https://newosxbook.com/articles/guesstalt.html)” and his book [_macOS and iOS Internals, Volume I: User Mode_](https://www.amazon.com/MacOS-iOS-Internals-User-Mode/dp/099105556X) (pp. 111–114).

You can think of MobileGestalt as a database. If other system components need information about the device’s model, capabilities, status, etc., they can query MobileGestalt through its API. For example, iTunes uses MobileGestalt to display the model and specifications of a connected iPhone.

Some of the information stored in MobileGestalt is dynamically acquired at runtime, while other information is static and stored in

```
/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist
```

Despite being deeply buried, the file can be accessed without jailbreaking by the Shortcuts app. To do so, create a shortcut with a “Get Contents of URL” action and set the URL to

```
file://private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist
```

On an iPhone 16 Pro, the file looks like (abridged):

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CacheData</key>
    <data>
    ...
    </data>
    <key>CacheExtra</key>
    <dict>
        <key>+3Uf0Pm5F8Xy7Onyvko0vA</key>
        <string>iPhone</string>
        <key>/YYygAofPDbhrwToVsXdeA</key>
        <string>D93AP</string>
        <key>0+nc/Udy4WNG8S+Q7a/s1A</key>
        <string>iPhone17,1</string>
        ...
        <key>zHeENZu+wbg7PUprwNwBWg</key>
        <string>LL/A</string>
    </dict>
    ...
</dict>
</plist>
```

The key information is stored in the `CacheExtra` dictionary, with the property names (unsurprisingly) obfuscated. Brute-force efforts by others have revealed that the obfuscation process involves prepending the string `MGCopyAnswer` to the actual property name, calculating the MD5 hash, encoding it in Base64, and finally removing the trailing `==` (because converting MD5 to Base64 always leaves two extra bytes). In pseudocode:

```
obfs_key = base64Encode(md5Hash("MGCopyAnswer" + orig_key))[:-2]
```

MobileGestalt has accumulated [a thousand and so properties](https://github.com/PoomSmart/MGKeys/blob/master/deobfuscated.py) over the years, and is set to grow with future upgrades of software and hardware. Here are some interesting findings:

Property (Plaintext)

Property (Obfuscated)

Meaning

ArtworkTraits

oPeik/9e8lQWMszEjbPzng

Display specs (related to Dynamic Island, wide color gamut, etc.)

device-name

JUWcn+5Ss0nvr5w/jk4WEg

Device class (e.g., `iPhone`)

DeviceSupportsAlwaysOnTime

j8/Omm6s1lsmTDFsXjsBfA

Availability of Always-On Display

DeviceSupportsBreathingDisturbancesMeasurements

e0HV2blYUDBk/MsMEQACNA

Availability of sleep apnea detection

DeviceSupportsCollisionSOS

HCzWusHQwZDea6nNhaKndw

Availability of Collision SOS

DeviceSupportsEnhancedMultitasking

qeaj75wk3HF4DwQ8qbIi7g

Availability of Stage Manager

DeviceSupportsGenerativeModelSystems

A62OafQ85EJAiiqKn4agtg

Availability of on-device generative models

DeviceSupportsTapToWake

yZf3GTRMGTuwSV/lD7Cagw

Availability of Raise to Wake

green-tea

iyfxmLogGVIaH7aEgqwcIA

Whether the device is a Chinese-market model

RegionCode

h63QSdBCiT/z0WU6rdQv6Q

Region code (e.g., `US`, `CH`)

RegionInfo

zHeENZu+wbg7PUprwNwBWg

Suffix in the model to identify the region (e.g., `LL/A`, `CH/A`)

SupportedDeviceFamilies

9MZ5AdH43csAUajl/dU+IQ

Supported device families, with `1` and `2` for iPhone and iPad apps, respectively

ProductType

h9jDsbgj7xIVeIQ8S3/X3Q

Model identifier (e.g., `iPhone17,1`)

Known methods to enable Apple Intelligence on China and or EU devices commonly involve modifying `RegionCode` and `RegionInfo` to match those of US devices, thereby bypassing the regional restrictions on AI features (but this is only one of the required steps).

There is also a [tweak](https://gist.github.com/f1shy-dev/23b4a78dc283edd30ae2b2e6429129b5) that modifies `DeviceSupportsGenerativeModelSystems` and `ProductType` on older devices to trick Apple’s server, thus enabling the new AI-powered Siri (but not other on-device Gen AI features).

### A Note on the Exploit Used by Non-Jailbreaking Unlockers

“Unlocker” tools like [MisakaX](https://github.com/straight-tamago/misakaX) and [Nugget](https://github.com/leminlimez/Nugget/) have emerged after the release of the iOS 18 beta to facilitate the modification of the system files. How is this possible without jailbreaking?

Indeed, these tools exploit a long-standing vulnerability since iOS 15.2 known as sparserestore. The method was initially used for installing [TrollStore](https://theapplewiki.com/wiki/TrollStore), a famous tool to sideload arbitrary apps. Although the vulnerability exploited by TrollStore itself has been patched, sparserestore persists as a general modification method, and many unlockers just include the same [code](https://github.com/JJTech0130/TrollRestore/tree/main/sparserestore) with few modifications.

In essence, sparserestore is a directory traversal vulnerability targeting the iOS’ backup restore functionality. It works by crafting a backup with manipulated paths and attributes to trick the system into writing designated content outside the intended backup scope during restoration.

(Directory traversal is a familiar sight for the iOS hacking scene. Jailbreak tools like Spirit for iOS 3 and TaiG for iOS 8 utilized similar vulnerabilities.)

Specifically, the iOS backup mechanism normally restricts the scope of restorable files and organizes them into several “domains” based on type and role. Each backup domain can be considered an alias with a policy of writable subpaths. During restoration, the system resolves the backup domains (stored in the backup manifest) and proceeds only if the path conforms to the domain’s policy.

Somehow, the sanity of the file paths within the `SysContainerDomain` was not checked, allowing the inclusion of the infamously unsafe string `../` (parent directory of the current directory). Because `SysContainerDomain` files are unpacked under

```
/var/.backup.i/var/mobile/Library/Backup/System Containers/Data/
```

during restoration, the path

```
SysContainerDomain-../../../../../../../..
```

resolves to `/`, the root of the file system. Appending a protected path after this crafted string thus allows access to system files.

Besides directory traversal, sparserestore utilizes another [trick](https://github.com/leminlimez/Nugget/blob/main/Sparserestore/restore.py#L13-L70) to bypass iOS’ system file protections. Instead of directly overwriting system files (possibly because this would be detected and blocked), it temporarily restores the replacement content to a seemingly “normal” backup path. Then, it creates a hard link from the system file to be modified to this temporary file by setting the same inode — iOS somehow allowed this, which is likely also part of the vulnerability.

Finally, the temporary file is overwritten with an empty file. Due to the mechanism of hard links, the targeted system file now independently points to the disk data previously jointly referenced by it and the temporary file, completing the “bait and switch.”

Unfortunately, although this vulnerability has existed in the wild for several years, it has been patched with the release of iOS 18.1 beta 5, just ahead of the general availability of Apple Intelligence.

Eligibility
-----------

The recently introduced Eligibility system is an “innovation” to the traditional approach represented by MobileGestalt. Initially implemented in response to South Korea’s Telecommunications Business Act of 2021, which mandates that the App Store allow third-party payments, Eligibility emerged fully-fledged with the EU’s Digital Markets Act of 2022 enforcing similar regulations in a much larger market.

The core of Eligibility is the daemon `/usr/libexec/eligibilityd`. Apple being Apple is tight-lipped about its inner workings. However, thanks to the admirable works of Kyle Ye, we have access to an [open-source implementation](https://github.com/Kyle-Ye/eligibility/) of Eligibility. The following analysis is based on his code.

### Eligibility’s Inputs

Eligibility impresses with its “thoroughness.” For each feature managed by it (referred to as a “domain”), `eligibilityd` considers a series of “[inputs](https://github.com/Kyle-Ye/eligibility/tree/main/eligibilityd/Input/Inputs),” or determining factors. Currently known inputs are:

*   `ChinaCellular`
*   `CountryBilling`
*   `DeviceClass`
*   `DeviceLanguage`
*   `DeviceLocale`
*   `DeviceRegionCode`
*   `LocatedCountry`
*   `SiriLanguage`
*   `GenerativeModelSystem` (availability of on-device Gen AI)
*   `GreyMatterOnQueue` (Apple Intelligence waitlist status)

etc.

Some of these inputs are acquired by querying MobileGestalt, such as `ChinaCellular` and `GenerativeModelSystem`, while others are obtained by reading system settings, such as `DeviceLanguage` and `SiriLanguage`.

Most noteworthy, however, is `LocatedCountry`. Existing research suggests it’s not just simple GPS locating, but a complex process carried out by another dedicated daemon, `/usr/libexec/countryd`.

You can run `man countryd` in the terminal to see Apple’s vague, yet chilling, description of `countryd`:

> Receives country code updates from user location, mobile country code (when available) and nearby 802.11d wifi access points. This information is then stored in a cache and used to compute a country code estimate which combines both the on-device code computed from local sensors, and answers about which country nearby devices believe they are in.

As is well known, if it determines the device is in mainland China, you’re in for a treat (of disabled features).

### Scope of Managed Features

So, which features are currently within the purview of `eligibilityd`? Apple, in yet another attempt at obfuscation, poetically turns to the periodic table for codenames, and has used element names from `Hydrogen` all the way to `Cobalt`, with more undoubtedly on the way. Some examples are:

*   `Hydrogen`: Enabling installation of marketplace-distributed apps, available in the EU;
*   `Carbon`: Enabling installation of web browsers with non-WebKit engines, available in the EU;
*   `Sodium`: Enabling NFC access for third-party contactless payment apps, available in the EEA;
*   `Phosphorus`: Enabling apps to use external purchase links, available to varying extents in the EU, Russia, and the US;
*   `Sulfur`: Enabling in-app purchases to use third-party payment systems, available to varying extents in South Korea and the US;
*   `Calcium`: Adding “(China)” suffix to Hong Kong, Macao, and Taiwan, enforced on China SKUs;
*   `Iron`: Enabling iPhone mirroring, available outside the EU.

A few exceptions to the taxonomy include:

*   `PodcastsTranscripts`: Enabling transcripts in the Podcasts app, available outside Belarus, Russia, and China;
*   `XcodeLLM`: Enabling Generative AI in Xcode, primarily available to US devices;
*   `Greymatter`: Enabling Apple Intelligence ([codenamed](https://archive.is/0aVR1) Greymatter), primarily available to US devices;

[and more](https://theapplewiki.com/wiki/Eligibility#Domains).

### Associating Inputs with Features

Apple is apparently using two methods to associate inputs with managed features: either with code or with configuration files, presumably for easier hot updates.

For instance, the availability of Apple Intelligence is primarily coded in ([`GreymatterDomain.m`](https://github.com/Kyle-Ye/eligibility/blob/main/eligibilityd/Domain/Domains/GreymatterDomain.m)), from which we can tell the following conditions:

1.  The device is not a China SKU, i.e., the region code queried from MobileGestalt cannot be `CH`;
2.  The Siri language must be US English (`en-US`); and
3.  The display language must be English, and it cannot be Indian or Singaporean English (`en-IN` or `en-SG`).

On the other hand, the configurations are currently located at

```
/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_OSEligibility/purpose_auto/$HASH.asset/AssetData/Config.plist
```

where `HASH` appears to be a randomly generated SHA-1 with [two possible known values](https://old.reddit.com/r/jailbreak/comments/1fazxsy/jailbroken_ipad_users_174_and_higher_we_need_your/).

As of this writing, Kyle Ye’s open-source implementation hasn’t completed the code for reading these configuration files, but the format is mostly self-explanatory. `Config.plist` is in binary format; converting it with `plutil -convert xml1` reveal content that looks like (abridged):

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    ...
    <key>Sulfur</key>
    <dict>
        <key>Grace Period</key>
        <integer>2592000</integer>
        <key>Policies</key>
        <array>
            <dict>
                <key>OS_ELIGIBILITY_INPUT_COUNTRY_BILLING</key>
                <array>
                    <string>AT</string>
                    <string>AX</string>
                    ...
                </array>
                <key>OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION</key>
                <array>
                    <string>AT</string>
                    <string>AX</string>
                    ...
                </array>
            </dict>
            <dict>
                <key>OS_ELIGIBILITY_INPUT_COUNTRY_BILLING</key>
                <array>
                    <string>KR</string>
                </array>
                <key>OS_ELIGIBILITY_INPUT_DEVICE_CLASS</key>
                <array>
                    <string>iPhone</string>
                    <string>iPad</string>
                </array>
            </dict>
        </array>
    </dict>
    ...
</dict>
</plist>
```

The above snippet shows the policies for the feature `Sulfur`, which, as mentioned earlier, refers to allowing third-party payments for in-app purchases. Its `Policies` allow —

1.  an iPhone physically located in the EU (`OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION`) _and_ with an EU account logged in (`OS_ELIGIBILITY_INPUT_COUNTRY_BILLING`); _or_
2.  an iPhone or iPad physically located in South Korea;

to use third-party payment systems.

Once these conditions are no longer met, there is a 30-day (2592000 seconds) grace period (`Grace Period`), after which the feature will be disabled.

Readers familiar with App Store policy changes will recognize this as a code representation of Apple’s regional specific guidelines.

### Caching of Eligibility Status

`eligibilityd` also caches the status of features it has checked for future retrievals. The cache can be found at:

```
/private/var/db/os_eligibility/eligibility.plist
```

The content of `eligibility.plist` looks like (abridged):

```
<?xml version=“1.0” encoding=“UTF-8″?>
<!DOCTYPE plist PUBLIC ”-//Apple//DTD PLIST 1.0//EN” “http://www.apple.com/DTDs/PropertyList-1.0.dtd”>
<plist version=“1.0″>
<dict>
    ...
    <key>OS_ELIGIBILITY_DOMAIN_GREYMATTER</key>
    <dict>
        <key>context</key>
        <dict>
            <key>OS_ELIGIBILITY_CONTEXT_ELIGIBLE_DEVICE_LANGUAGES</key>
            <array>
                <string>en</string>
            </array>
        </dict>
        <key>os_eligibility_answer_source_t</key>
        <integer>1</integer>
        <key>os_eligibility_answer_t</key>
        <integer>4</integer>
        <key>status</key>
        <dict>
            <key>OS_ELIGIBILITY_INPUT_DEVICE_LANGUAGE</key>
            <integer>3</integer>
            <key>OS_ELIGIBILITY_INPUT_DEVICE_REGION_CODE</key>
            <integer>3</integer>
            <key>OS_ELIGIBILITY_INPUT_EXTERNAL_BOOT_DRIVE</key>
            <integer>3</integer>
            <key>OS_ELIGIBILITY_INPUT_GENERATIVE_MODEL_SYSTEM</key>
            <integer>3</integer>
            <key>OS_ELIGIBILITY_INPUT_SHARED_IPAD</key>
            <integer>3</integer>
            <key>OS_ELIGIBILITY_INPUT_SIRI_LANGUAGE</key>
            <integer>3</integer>
        </dict>
    </dict>
    ...
</dict>
</plist>
```

The snippet above shows the cached status after Apple Intelligence has been successfully enabled, where:

*   `os_eligibility_answer_source_t` records how the eligibility was determined, with `0`, `1`, or `2`, [representing](https://github.com/Kyle-Ye/eligibility/blob/main/EligibilityCore/include/EligibilityAnswerSource.h) an invalid, computed (as expected), or forced (during debugging) answer, respectively;
*   `os_eligibility_answer_t` records the determined eligibility, with `2` and `4` [representing](https://github.com/Kyle-Ye/eligibility/blob/main/EligibilityCore/include/EligibilityAnswer.h) the feature being determined as ineligible or eligible, respectively; and
*   `status` records the inputs considered, with `2` or `3` for each input [representing](https://github.com/Kyle-Ye/eligibility/blob/main/EligibilityCore/include/EligibilityInputStatus.h) a failed or successful check, respectively.

Indeed, the unlocker tools for Apple Intelligence or EU-specific features work by [adding](https://github.com/leminlimez/Nugget/blob/main/tweaks/eligibility_tweak.py#L59-L68) the current device’s region code to `Config.plist` and [crafting](https://github.com/leminlimez/Nugget/blob/main/tweaks/eligibility_tweak.py#L70-L88) successful records in `eligibility.plist`, thus tricking iOS into believing the device is eligible.
