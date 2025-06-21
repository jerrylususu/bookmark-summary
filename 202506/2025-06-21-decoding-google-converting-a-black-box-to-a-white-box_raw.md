Title: Decoding Google: Converting a Black Box to a White Box

URL Source: https://brutecat.com/articles/decoding-google

Markdown Content:
[< Back](https://brutecat.com/)
2024-11-01

![Image 1](https://brutecat.com/assets/decoding-google.jpeg)
We've all been there - staring at Google's search box, overwhelmed by the maze of complexity hiding behind that minimalist interface, thinking it's impossible to break in. The key to decoding Google? Converting the attack surface from a black box to a white box. The first step is finding all the endpoints that exist, and all of their respective parameters, especially ones that are hidden and aren't used in the actual app and were left from some developer testing, since they likely contain security bugs.

‎

#### Table of Contents

*   [How Google API authentication works on the web](https://brutecat.com/articles/decoding-google#how-google-api-authentication-works-on-the-web)

*   ["Secret" visibility labels](https://brutecat.com/articles/decoding-google#-quot-secret-quot-visibility-labels)

*   [How Google API authentication works on Android](https://brutecat.com/articles/decoding-google#how-google-api-authentication-works-on-android)

*   [A word on X-Goog-Spatula](https://brutecat.com/articles/decoding-google#a-word-on-x-goog-spatula)

*   [Leaking request parameters through error messages](https://brutecat.com/articles/decoding-google#leaking-request-parameters-through-error-messages)

‎

In Google, there's something known as [discovery documents](https://developers.google.com/discovery/v1/reference/apis) that are essentially like swagger documents, intended for listing API methods on Google's public APIs such as their [YouTube Data API](https://developers.google.com/youtube/v3) ([discovery](https://youtube.googleapis.com/$discovery/rest)). As it turns out, these discovery documents aren't just available for their public APIs but also for their private ones such as the Internal People API ([discovery](https://people-pa.googleapis.com/$discovery/rest)).

‎

While this discovery document doesn't require any authentication to view, if we try fetching something like the Takeout Private API, we get the following error:

‎

**Request**

```
GET /$discovery/rest
Host: takeout-pa.googleapis.com
```

**Response**

```
HTTP/2 403 Forbidden
Content-Type: application/json; charset=UTF-8

{
  "error": {
    "code": 403,
    "message": "Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.",
    "status": "PERMISSION_DENIED"
  }
}
```

Thankfully, by looking into how Google authentication works, it's possible to get past this.

### How Google API authentication works on the web

If we look at a random request to the People Internal API to lookup a Google user from the web that we can find from DevTools on [https://chat.google.com](https://chat.google.com/):

```
POST /$rpc/google.internal.people.v2.minimal.InternalPeopleMinimalService/GetPeople HTTP/2
Host: people-pa.clients6.google.com
Cookie: <redacted>
Content-Type: application/json+protobuf
X-Goog-Api-Key: AIzaSyB0RaagJhe9JF2mKDpMml645yslHfLI8iA
Origin: https://chat.google.com
Authorization: SAPISIDHASH <redacted>
...
```

> Note: clients6.google.com is an alias for googleapis.com

‎

The first important header here is `X-Goog-Api-Key`. This API key gives us permission to call endpoints in the Internal People API. This specific endpoint requires us to be authenticated with our Google account, which is done through the `Cookie` header and `SAPISIDHASH` (this value is generated [using the SAPISID cookie](https://stackoverflow.com/a/32065323))

‎

If you're worked with Google Cloud before, you might know that APIs need to be enabled for your project before you can make calls to them. If we tried taking this key and doing a call to some random unrelated API like the Play Atoms Private API `playatoms-pa.googleapis.com`

```
GET /$discovery/rest
Host: playatoms-pa.googleapis.com
X-Goog-Api-Key: AIzaSyB0RaagJhe9JF2mKDpMml645yslHfLI8iA
```

We would get the following error:

```
{
  "error": {
    "code": 403,
    "message": "Play Atoms Private API has not been used in project 576267593750 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/playatoms-pa.googleapis.com/overview?project=576267593750 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.",
    ...
  }
}
```

This is because just like Google Cloud projects we can make ourselves, the API key we found is tied to some Google-owned Cloud project, which doesn't have the Play Atoms Private API enabled for it.

‎

However, this key does in fact work for the **staging environment** of the Internal People API which otherwise without authentication isn't public:

‎

**Request**

```
GET /$discovery/rest
Host: staging-people-pa.sandbox.googleapis.com
Referer: https://chat.google.com
X-Goog-Api-Key: AIzaSyB0RaagJhe9JF2mKDpMml645yslHfLI8iA
```

> Note: all staging/test endpoints are under *.sandbox.googleapis.com. This API key also requires the use of the chat.google.com Referer header.

‎

**Response**

```
HTTP/2 200 OK
Content-Type: application/json; charset=UTF-8

{
  "title": "Internal People API - Staging",
  "documentationLink": "http://boq/java/com/google/social/boq/release/socialgraphapiserver",
  "discoveryVersion": "v1",
  "id": "people_pa:v2",
  "revision": "20241031",
  ...
}
```

‎

Unlike the public discovery document, this version contains comments for everything, leaking a lot of how stuff works behind-the-scenes:

```
...
    "InAppNotificationTarget": {
      "id": "InAppNotificationTarget",
      "description": "How and where to send notifications to this person in other apps, and why the requester can do so. See go/reachability for more info. \"How\" and \"where\" identify the recipient in a P2P Bridge (glossary/p2p bridge), and \"why\" may be helpful in a UI to disambiguate which of several ways may be used to contact the recipient. How: Via a Google profile or a reachable-only phone number that the requester has access to. Specified in the target \"type\" and \"value\". Where: Apps in which the profile/phone number owner may receive notifications. Specified in the repeated \"app\". Why: Which fields in, e.g., a contact associated with this person make the notification target info visible to the requester. Specified in the repeated originating_field param. Example: Alice has a contact Bob, with: Email 0 = bob@gmail.com Phone 0 = +12223334444 Phone 1 = +15556667777 Email 0 and Phone 0 let Alice see Bob's public profile (obfuscated gaia ID = 123). Public profiles are visible by email by default, and Bob has explicitly made it visible via Phone 0. Bob says people can send notifications to his public profile in YouTube. Phone 2 is associated with another Google profile that Bob owns, but he doesn't want others to see it. He is okay with people sending notifications to him in Who's Down if they have this phone number, however. There will be separate InAppNotificationTargets: one for Bob's public Google profile, and one for the second phone number, which is in his private profile. IANT #1 - targeting Bob's public profile (visible via Email 0 and Phone 0): app = [YOUTUBE] type = OBFUSCATED_GAIA_ID value = 123 originating_field: [ { field_type = EMAIL, field_index = 0 } // For Email 0 { field_type = PHONE, field_index = 0 } // For Phone 0 ] IANT #2 - targeting Bob's private profile phone number Phone 1: app = [WHOS_DOWN] type = PHONE value = +15556667777 originating_field: [ { field_type = PHONE, field_index = 1 } // For Phone 1 ]",
...
```

> **Update 2025-02-06:** Google has [removed all comments](https://x.com/brutecat/status/1887436162744410509) from the staging discovery doc.

### "Secret" visibility labels

As it turns out, certain Google cloud projects have visibility labels enabled for them, giving them more access than others. Endpoints can be hidden behind visibility labels, and they won't show up in the discovery document unless the secret `labels` parameter is provided. This [was discovered](https://www.youtube.com/watch?v=9pviQ19njIs) by an awesome researcher [Ezequiel Pereira](https://www.ezequiel.tech/) who now works at Google.

‎

For instance, if we use the API key `AIzaSyCI-zsRP85UVOi0DjtiCwWBwQ1djDy741g` that we can find from [console.cloud.google.com](https://console.cloud.google.com/) and try fetching the discovery document for `servicemanagement.googleapis.com`

**Request**

```
GET /$discovery/rest HTTP/2
Host: servicemanagement.googleapis.com
Content-Type: application/json
X-Goog-Api-Key: AIzaSyCI-zsRP85UVOi0DjtiCwWBwQ1djDy741g
Referer: https://console.cloud.google.com
```

The response would have 214k bytes. However, if we try this same request with `&labels=PANTHEON`

```
GET /$discovery/rest?labels=PANTHEON HTTP/2
Host: servicemanagement.googleapis.com
Content-Type: application/json
X-Goog-Api-Key: AIzaSyCI-zsRP85UVOi0DjtiCwWBwQ1djDy741g
Referer: https://console.cloud.google.com
```

The response now has 329k bytes and there's a lot more hidden documentation revealed.

‎

Additionally, certain APIs like the Internal People API provide extra permissions for specific API clients. So far, we've covered how we can use API keys to fetch discovery documents or access endpoints in the context of Google Cloud projects that have their keys used in Google web services. However, by learning how authorization works on Android, we can get access to the context of lot more Google Cloud projects.

### How Google API authentication works on Android

If you've ever logged into a Google account via Google Play Services (GPS) on an Android device, you might have noticed that all Google apps are able to authenticate as your Google account seamlessly, without having to manually log into each one.

‎

The way this works is your Google account's Android session is actually tied to a refresh token that's generated the first time you log in. Unlike on the web where Google internal APIs use cookies for authentication, on Android and iOS scoped bearer tokens generated from a refresh token are used instead.

On Android, that same Internal People API request would look something like this:

```
POST /$rpc/google.internal.people.v2.minimal.InternalPeopleMinimalService/GetPeople HTTP/2
Host: people-pa.clients6.google.com
Content-Type: application/json+protobuf
Authorization: ya29.<redacted>
...
```

There is no need for an API key for this request, as the bearer token actually includes the context of the Google API project that you used to generate the bearer token. (this will make more sense once we look into how bearer tokens are generated from an android refresh token)

‎

The interesting thing about some Google APIs is that requests from the context of certain Google Cloud project IDs have extra functionality/permissions enabled just for that project on that API. This is usually based on the requirements of the client (ex. the Google Chat app may need to be able to fetch extra information on other Google users from the Internal People API as compared to something like Google Earth)

### Android Refresh Tokens (aas/xx)

So, how can we generate an Android refresh token to use for testing? It's actually quite simple. We can simply visit [https://accounts.google.com/EmbeddedSetup](https://accounts.google.com/EmbeddedSetup), go through the authentication flow, and at the end there will be a cookie set called `oauth_token`

‎

We can then do the following request to exchange this oauth_token for an Android refresh token:

```
POST /auth
Host: android.googleapis.com
User-Agent: com.google.android.gms/243530022
Content-Type: application/x-www-form-urlencoded

androidId=fb213fefa471dcde&Token=<oauth_token>&service=ac2dm&get_accountid=1&ACCESS_TOKEN=1&callerPkg=com.google.android.gms&add_account=1&callerSig=38918a453d07199354f8b19af05ec6562ced5788
```

The `androidId` is just any random 16 character hex string. At the moment you don't require this for generating a bearer token, but this could change in the future so it's advisable to store it along with your Android refresh token.

‎

> On newer Android versions, a DroidGuard token is also supplied to this request. My guess is that it's likely an anti-abuse measure. However, they're unable to enforce this token without breaking Google Play Services support for older Android devices. It's possible this could be changed in the future though.

‎

The response to the request will look something like this:

```
HTTP/2 200 OK
Content-Type: text/plain; charset=utf-8

Token=aas_et/<redacted>
Auth=g.a000<redacted>
SID=BAD_COOKIE
LSID=BAD_COOKIE
services=mail,hist,dynamite,cl,youtube,jotspot,uif,multilogin,analytics
Email=<redacted>@gmail.com
GooglePlusUpdate=0
firstName=<redacted>
lastName=<redacted>
capabilities.canHaveUsername=1
capabilities.canHavePassword=1
...
```

You can actually see this Android device on [https://myaccount.google.com/device-activity](https://myaccount.google.com/device-activity)

### Generating a Bearer Token

Now that you have an Android refresh token, you can use this to generate a bearer token in the context of a Android app's Google Cloud project with the scopes that you require.

‎

This is an example request to generate scopes for Google Play Games to use with `playgateway-pa.googleapis.com`

```
POST /auth HTTP/2
Host: android.googleapis.com
User-Agent: GoogleAuth/1.4
Content-Length: 808
Content-Type: application/x-www-form-urlencoded

androidId=fb213fefa471dcde&app=com.google.android.play.games&service=oauth2:https://www.googleapis.com/auth/games.firstparty https://www.googleapis.com/auth/googleplay&client_sig=38918a453d07199354f8b19af05ec6562ced5788&has_permission=1&Token=<redacted>
```

Let's breakdown everything in that request:

| Parameter | Explanation |
| --- | --- |
| android_id | This isn't validated, it can be any 16 character hex string |
| app | Package name of the app that's cloud project context you wish to use. |
| service | Space seperated scopes |
| client_sig | SHA1 hash in hex format of the app's signature |
| has_permission | Only required on few android clients that don't have auto mode enabled for them. |
| Token | Your Android refresh token |

> It's actually possible to omit `client_sig` and `app` for certain scopes, but you wouldn't have the context of the Google API project and this does not work for most scopes.

‎

The first problem we have is, let's say we want to get authentication on the following Google Internal People API endpoint: `https://people-pa.googleapis.com/v2/people` to start playing around with it, how would we know what scopes this endpoint needs?

‎

In this case, there's a [public discovery document](https://people-pa.googleapis.com/$discovery/rest) that lists all the endpoints and the scopes for each of them, but many Google APIs may require an API key to access the discovery document which we may not always have (ex. [gameswhitelisted](https://gameswhitelisted.googleapis.com/$discovery/rest)).

‎

Turns out, if we send a request to an endpoint with a bearer token with insufficient scopes, it actually tells us all the scopes we need:

**Request**

```
GET /v2/people
Host: people-pa.googleapis.com
Authorization: Bearer ya29.<redacted>
```

**Response**

```
HTTP/2 403 Forbidden
Www-Authenticate: Bearer realm="https://accounts.google.com/", error="insufficient_scope", scope="https://www.googleapis.com/auth/peopleapi.legacy.readwrite https://www.googleapis.com/auth/plus.peopleapi.readwrite https://www.googleapis.com/auth/peopleapi.readonly https://www.googleapis.com/auth/peopleapi.readwrite openid https://www.googleapis.com/auth/plus.me"
Content-Type: application/json; charset=UTF-8

{
  "error": {
    "code": 403,
    "message": "Request had insufficient authentication scopes.",
    ...
        "metadata": {
          "service": "people-pa.googleapis.com",
          "method": "google.internal.people.v2.InternalPeopleService.GetPeople"
        }
    ...
  }
}
```

> Something interesting to note: `google.internal.people.v2.InternalPeopleService.GetPeople` is actually the gRPC service name of the endpoint.

‎

To simply this process, I wrote a Go script that I've [published on GitHub](https://github.com/ddd/req2proto/tree/main/tools/gapi-service) that we can use to easily get this information:

```
$ export ANDROID_REFRESH_TOKEN="<redacted>"
$ git clone https://github.com/ddd/req2proto
$ cd tools/gapi-service
$ go build # this requires golang to be installed, see https://go.dev/doc/install
$ ./gapi-service -e https://people-pa.googleapis.com/v2/people
scopes: https://www.googleapis.com/auth/peopleapi.legacy.readwrite https://www.googleapis.com/auth/plus.peopleapi.readwrite https://www.googleapis.com/auth/peopleapi.readwrite
method: google.internal.people.v2.InternalPeopleService.InsertPerson
service: people-pa.googleapis.com
```

Now that we have the scopes we need. Let's say we want to call this endpoint in the context of Google Chat. We can get the package name `com.google.android.apps.dynamite` from the Play Store web URL ([https://play.google.com/store/apps/details?id=com.google.android.apps.dynamite](https://play.google.com/store/apps/details?id=com.google.android.apps.dynamite)) but we still need the `client_sig` of the app.

‎

While this is true for most cases, the client signature isn't necessarily always the SHA1 hash of the target app's signature. To solve this problem, I collected the package names as well as SHA1 client signature of all Google apps and wrote a [Rust program](https://github.com/ddd/req2proto/tree/main/tools/aas-rs) that bruteforces all SHA1 signature and package name combinations to find working ones. You can find the output of this script [here](https://github.com/ddd/req2proto/blob/main/tools/data/android_clients.json)

‎

We can simply search this file for `com.google.android.apps.dynamite` and we can see that the client_sig `519c5a17a60596e6fe5933b9cb4285e7b0e5eb7b` works for this app:

```
"com.google.android.apps.dynamite": [
    {
      "spatula": "CkAKIGNvbS5nb29nbGUuYW5kcm9pZC5hcHBzLmR5bmFtaXRlGhxVWnhhRjZZRmx1YitXVE81eTBLRjU3RGw2M3M9GLingOeJmKD6Ng==",
      "sig": "519c5a17a60596e6fe5933b9cb4285e7b0e5eb7b"
    }
  ],
```

### A word on X-Goog-Spatula

Even though we may have authentication in the context of an app's Google API project, we can't just fetch the discovery document with it. That's where `X-Goog-Spatula` comes in. If you've ever looked at Android traffic to Google APIs, you might have noticed this header.

‎

It's actually just a keyless authentication header. Similar to an API key, it's used to provide context to a specific Google Cloud project.

‎

They look like this (base64-encoded protobuf):

`Cj0KHWNvbS5nb29nbGUuYW5kcm9pZC5wbGF5LmdhbWVzGhxPSkdLUlQwSEdaTlUrTEdhOEY3R1ZpenRWNGc9GLingOeJmKD6Ng==`
If we look at how this is formed:

```
$ echo -n "Cj0KHWNvbS5nb29nbGUuYW5kcm9pZC5wbGF5LmdhbWVzGhxPSkdLUlQwSEdaTlUrTEdhOEY3R1ZpenRWNGc9GLingOeJmKD6Ng==" | base64 -d | protoc --decode_raw
1 {
  1: "com.google.android.play.games" // package name
  3: "6Zi8TwQNyiOD+us24/5aYpwxt5A=" // base64 of SHA1 hash of the app signature
}
3: 3959931537119515576 // this is generated from DroidGuard using the device_key
```

> This example is from some Spatula header I [found on the internet](https://github.com/4kumano/reftoken/blob/99d1d980c0015c8b1113cb65b02ee0ede96ae471/sumber.txt)

‎

If you wish to dive into how this DroidGuard value is generated, there's [an awesome gist](https://gist.github.com/Romern/e58e634e4d70b2be5b57d7abdb77f7ef) on this, but we don't actually need to care about that in order to utilize it. As it turns out, this value isn't actually validated, and we can impersonate any client we want by simply changing the package name and SHA1 hash of the app signature.

‎

Since just like API keys, they provide context of a Google Cloud project, we're actually able to use this to fetch discovery documents of several Android Google APIs like `gameswhitelisted.googleapis.com`:

‎

**Request**

```
GET /$discovery/rest
Host: gameswhitelisted.googleapis.com
X-Goog-Spatula: Cj0KHWNvbS5nb29nbGUuYW5kcm9pZC5wbGF5LmdhbWVzGhxPSkdLUlQwSEdaTlUrTEdhOEY3R1ZpenRWNGc9GLingOeJmKD6Ng==
```

**Response**

```
HTTP/2 200 OK
Content-Type: application/json; charset=UTF-8

{
  "kind": "discovery#restDescription",
  "description": "Internal-only 1P access to the oneup APIs.",
  ...
```

> We can actually use this along with Cookie authentication on the web, as a direct replacement for `X-Goog-Api-Key` to get us access to the context of an Android app's Google Cloud project

### Leaking request parameters through error messages

Occasionally we may come across Google APIs where there's seemingly no way to access the discovery document. This could be due to not being able to find a working API key/spatula, 404 page or otherwise. One such example is YouTube's Internal API:

**Request**

```
GET /$discovery/rest
Host: youtubei.googleapis.com
```

**Response**

```
HTTP/2 405 Method Not Allowed
Content-Type: text/html; charset=UTF-8
Referrer-Policy: no-referrer
...
```

> Fun fact: there's actually 2 workaround methods to leaking the discovery document of the Innertube API. Are you able to find them? :)
> 
> **Update 2025-03-01:** Google has [removed](https://x.com/brutecat/status/1894282218929037727) both the prod ([archive](https://tracker.brute.network/api/documents/youtubei.googleapis.com)) and staging ([archive](https://tracker.brute.network/api/documents/green-youtubei.sandbox.googleapis.com)) discovery documents.

‎

If we take a look at a random Innertube API endpoint, such as `/youtubei/v1/browse` endpoint and clean it up:

```
POST /youtubei/v1/browse HTTP/2
Host: youtubei.googleapis.com
Content-Type: application/json
Content-Length: 164

{
  "context": {
    "client": {
      "clientName": "WEB",
      "clientVersion": "2.20241101.01.00",
    }
  },
  "browseId": "UCX6OQ3DkcsbYNE6H8uQQuVA"
}
```

The request payload is in the json format. The `browseId` seems to be accepting the YouTube Channel ID as a string. What happens if we change that to a boolean like `true`

‎

**Request**

```
POST /youtubei/v1/browse HTTP/2
Host: youtubei.googleapis.com
Content-Type: application/json
Content-Length: 141

{
  "context": {
    "client": {
      "clientName": "WEB",
      "clientVersion": "2.20241101.01.00",
    }
  },
  "browseId":true
}
```

**Response**

```
HTTP/2 400 Bad Request
Content-Type: application/json; charset=UTF-8
Server: scaffolding on HTTPServer2

{
  "error": {
    "code": 400,
    "message": "Invalid value at 'browse_id' (TYPE_STRING), true",
    "errors": [
      {
        "message": "Invalid value at 'browse_id' (TYPE_STRING), true",
        "reason": "invalid"
      }
    ],
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.BadRequest",
        "fieldViolations": [
          {
            "field": "browse_id",
            "description": "Invalid value at 'browse_id' (TYPE_STRING), true"
          }
        ]
      }
    ]
  }
}
```

It tells us that `browse_id` is a TYPE_STRING. So awesome, we can leak the parameter type if we know the parameter name. But how can we take this a step further?

‎

As it turns out, in Google, there's 4 different content types:

1.   application/json (aka. JSON)
2.   application/json+protobuf (aka. ProtoJson)
3.   application/x-protobuf (aka. [Proto over HTTP fallback](https://googleapis.github.io/HowToRPC.html))
4.   application/grpc

‎

In Google, all endpoints are defined in `.proto` files such that they can be queried over gRPC. To allow for JSON, ProtoJson and Proto over HTTP, there's a Extensible Service Proxy (ESP) that [transcodes these requests to gRPC](https://cloud.google.com/endpoints/docs/grpc/transcoding) before they hit the actual Google microservice.

‎

For instance, if a requests JSON payload looks like this:

```
{
  "name": "John Smith",
  "age": 25,
  "favoriteColor": "orange"
}
```

The protobuf representation of this would look like this:

```
message Request {
  string name = 1;
  string age = 2;
  string favourite_color = 3;
}
```

The idea with protobuf is that sending `"name"`, `"age"` and `"favoriteColor"` from the client to the server in every request is a waste of bandwidth especially if the server knows what to expect from the client. Hence, protobuf is just a binary format compressing the data as much as possible. It does this by assigning everything an index (ex. name is 1, age is 2 etc.)

‎

ProtoJson is similar to this, except you just send an array rather than compressing it to protobuf:

```
[
  "John Smith",
  25,
  "orange"
]
```

You can probably see where we're going with this, what if we just sent the following to this endpoint:

`[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]`
**Request**

```
POST /youtubei/v1/browse HTTP/2
Host: youtubei.googleapis.com
Content-Type: application/json+protobuf
Content-Length: 22

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
```

**Response**

```
HTTP/2 400 Bad Request
Content-Type: application/json; charset=UTF-8
Server: scaffolding on HTTPServer2

{
  "error": {
    "code": 400,
    "message": "Invalid value at 'context' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.InnerTubeContext), 1\nInvalid value at 'browse_id' (TYPE_STRING), 2\nInvalid value at 'params' (TYPE_STRING), 3\nInvalid value at 'continuation' (TYPE_STRING), 7\nInvalid value at 'force_ad_format' (TYPE_STRING), 8\nInvalid value at 'player_request' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.PlayerRequest), 10\nInvalid value at 'query' (TYPE_STRING), 11\nInvalid value at 'has_external_ad_vars' (TYPE_BOOL), 12\nInvalid value at 'force_ad_parameters' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.ForceAdParameters), 13\nInvalid value at 'previous_ad_information' (TYPE_STRING), 14\nInvalid value at 'offline' (TYPE_BOOL), 15\nInvalid value at 'unplugged_sort_filter_options' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.UnpluggedSortFilterOptions), 16\nInvalid value at 'offline_mode_forced' (TYPE_BOOL), 17\nInvalid value at 'form_data' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.BrowseFormData), 18\nInvalid value at 'suggest_stats' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.SearchboxStats), 19\nInvalid value at 'lite_client_request_data' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.LiteClientRequestData), 20\nInvalid value at 'unplugged_browse_options' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.UnpluggedBrowseOptions), 22\nInvalid value at 'consistency_token' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.ConsistencyToken), 23\nInvalid value at 'intended_deeplink' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.DeeplinkData), 24\nInvalid value at 'android_extended_permissions' (TYPE_BOOL), 25\nInvalid value at 'browse_notification_params' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.BrowseNotificationsParams), 26\nInvalid value at 'recent_user_event_infos' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.RecentUserEventInfo), 28\nInvalid value at 'detected_activity_info' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.DetectedActivityInfo), 30",
    ...
}
```

We can find every non-integer parameter this way. We can then send only booleans instead to find all non-boolean parameters (including integer parameters). We can repeat this for nested messages to find the entire possible request payload.

To simplify this process, I wrote a Go tool called [req2proto](https://github.com/ddd/req2proto) which we can use to automate this.

```
$ git clone https://github.com/ddd/req2proto
$ go build # this requires golang to be installed, see https://go.dev/doc/install
$ ./req2proto -X POST -u https://youtubei.googleapis.com/youtubei/v1/browse -p youtube.api.pfiinnertube.GetBrowseRequest -o output -d 3 -v
```

If we look at `output/youtube/api/pfiinnertube/message.proto`, we can see the full request proto for this endpoint:

```
syntax = "proto3";

package youtube.api.pfiinnertube;

message GetBrowseRequest {
  InnerTubeContext context = 1;
  string browse_id = 2;
  string params = 3;
  string continuation = 7;
  string force_ad_format = 8;
  int32 debug_level = 9;
  PlayerRequest player_request = 10;
  string query = 11;
  bool has_external_ad_vars = 12;
  ForceAdParameters force_ad_parameters = 13;
  string previous_ad_information = 14;
  bool offline = 15;
  UnpluggedSortFilterOptions unplugged_sort_filter_options = 16;
  bool offline_mode_forced = 17;
  BrowseFormData form_data = 18;
  SearchboxStats suggest_stats = 19;
  LiteClientRequestData lite_client_request_data = 20;
  UnpluggedBrowseOptions unplugged_browse_options = 22;
  ConsistencyToken consistency_token = 23;
  DeeplinkData intended_deeplink = 24;
  bool android_extended_permissions = 25;
  BrowseNotificationsParams browse_notification_params = 26;
  int32 installed_sharing_service_ids = 27;
  RecentUserEventInfo recent_user_event_infos = 28;
  InlineSettingStatus inline_setting_status = 29;
  DetectedActivityInfo detected_activity_info = 30;
  BrowseRequestContext browse_request_context = 31;
  DeviceContextEvent device_context_info = 32;
  BrowseRequestSupportedMetadata browse_request_supported_metadata = 33;
  string target_id = 35;
  MySubsSettingsState subscription_settings_state = 36;
  MdxContext mdx_context = 37;
  CustomTabContext custom_tab_context = 38;
  ProducerAssetRequestData producer_asset_request_data = 39;
  LatestContainerItemEventsInfo latest_container_item_events_info = 40;
  ScrubContinuationClientData scrub_continuation_client_data = 41;
}
...
```

‎

That's all for now! Happy hacking and feel free to reach out to me if you have any questions.

* * *

You can contact me via [![Image 2: signal icon](blob:http://localhost/0523eebd37f9a43878c1d7fe7f36e92e)](https://signal.me/#eu/oidvqsq7SHvxe38GffjT5yQ83INy6av8eFkW6B06Lu5jeUn4ipVOx5Gf2q5eCkBN) or [![Image 3: email icon](blob:http://localhost/68aa0f3639e7bba86c11334de6c60881)](mailto:root@brutecat.com)
