Title: Storing times for human events

URL Source: https://simonwillison.net/2024/Nov/27/storing-times-for-human-events/

Markdown Content:
27th November 2024

I’ve worked on [various](https://en.wikipedia.org/wiki/Lanyrd) event [websites](https://en.wikipedia.org/wiki/Eventbrite) in the past, and one of the unintuitively difficult problems that inevitably comes up is the best way to store the time that an event is happening. Based on that past experience, here’s my current recommendation.

This is the expanded version of a [comment I posted on lobste.rs](https://lobste.rs/s/sorhro/postgresql_timestamp_with_time_zone_s_set#c_xjj8ci) a few days ago, which ended up attracting a bunch of attention [on Twitter](https://twitter.com/iavins/status/1861468050748514547).

*   [The problem](https://simonwillison.net/2024/Nov/27/storing-times-for-human-events/#the-problem)
*   [The “best practice” that isn’t](https://simonwillison.net/2024/Nov/27/storing-times-for-human-events/#the-best-practice-that-isn-t)
*   [Things that can go wrong](https://simonwillison.net/2024/Nov/27/storing-times-for-human-events/#things-that-can-go-wrong)
*   [User error](https://simonwillison.net/2024/Nov/27/storing-times-for-human-events/#user-error)
*   [International timezone shenanigans](https://simonwillison.net/2024/Nov/27/storing-times-for-human-events/#international-timezone-shenanigans)
*   [My recommendation: store the user’s intent time and the location/timezone](https://simonwillison.net/2024/Nov/27/storing-times-for-human-events/#my-recommendation-store-the-user-s-intent-time-and-the-location-timezone)
*   [Timezone UIs suck, generally](https://simonwillison.net/2024/Nov/27/storing-times-for-human-events/#timezone-uis-suck-generally)

#### The problem

An event happens on a date, at a time. The precise details of that time are very important: if you tell people to show up to your event at 7pm and it turns out they should have arrived at 6pm they’ll miss an hour of the event!

Some of the worst bugs an events website can have are the ones that result in human beings traveling to a place at a time and finding that the event they came for is not happening at the time they expected.

So how do you store the time of an event?

#### The “best practice” that isn’t

Any time you talk to database engineers about dates and times you’re likely to get the same advice: store everything in UTC. Dates and times are complicated enough that the only unambiguous way to store them is in UTC—no daylight savings or timezones to worry about, it records the exact moment since the dawn of the universe at which the event will take place.

Then, when you display those times to users, you can convert them to that user’s current timezone—neatly available these days using the [Intl.DateTimeFormat().resolvedOptions().timeZone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions) browser API.

There’s a variant of this advice which you’re more likely to hear from the PostgreSQL faithful: use [TIMESTAMP WITH TIME ZONE](https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-DATETIME-INPUT-TIME-STAMPS) or its convenient alias `timestamptz`. This stores the exact value in UTC and _sounds_ like it might store the timezone too... but it doesn’t! [All that’s stored](https://stackoverflow.com/questions/5876218/difference-between-timestamps-with-without-time-zone-in-postgresql#comment32979814_5876276) is that UTC value, converted from whatever timezone was active or specified when the value was inserted.

In either case, we are losing _critical_ information about when that event is going to happen.

#### Things that can go wrong

What’s wrong with calculating the exact UTC time the event is starting and storing only that?

The problem is that we are losing crucial details about the event creator’s original intent.

If I arrange an evening meetup for next year on December 3rd at 6pm, I mean 6pm local time, by whatever definition of local time is active on that particular date.

There are a number of ways this time can end up misinterpreted:

*   User error: the user created the event **with an incorrect timezone**
*   User error: the user created the event **in the wrong location**, and later needs to fix it
*   International timezone shenanigans: the location in which the event is happening **changes its timezone rules** at some point between the event being created and the event taking place

#### User error

By far the most common issue here is **user error** with respect to how the event was initially created.

Maybe you asked the user to select the timezone as part of the event creation process. This is not a particularly great question: most users don’t particularly care about timezones, or may not understand and respect them to the same extent as professional software developers.

If they pick the wrong timezone we risk showing the wrong time to anyone else who views their event later on.

My bigger concern is around location. Imagine a user creates their event in Springfield, Massachusetts... and then a few days later comes back and corrects the location to Springfield, Illinois.

That means the event is happening in a different timezone. If the user fails to update the time of the event to match the new location, we’re going to end up with an incorrect time stored in our database.

#### International timezone shenanigans

One of my favourite niche corners of the internet is the [tz@iana.org mailing list](https://lists.iana.org/hyperkitty/list/tz@iana.org/latest). This is where the maintainers of the incredible open source [tz database](https://en.wikipedia.org/wiki/Tz_database) hang out and keep track of global changes to timezone rules.

It’s easy to underestimate how much work this is, and how weird these rule changes can be. Here’s a [recent email](https://lists.iana.org/hyperkitty/list/tz@iana.org/thread/5KMKN3JXZZHTUHGQWBCJSPTQXXYOPIPP/) proposing a brand new timezone: `Antarctica/Concordia`:

> Goodmorning. I’m writing here to propose a new time zone for an all-year open Antarctic base. The base is a French–Italian research facility that was built 3,233 m (10,607 ft) above sea level at a location called Dome C on the Antarctic Plateau, Antarctica. [https://en.wikipedia.org/wiki/Concordia\_Station](https://en.wikipedia.org/wiki/Concordia_Station)
> 
> The timezone is UTC+8 without DST.

That’s a pretty easy one. Here’s a much more complicated example from March 2023: [Lebanon DST change internally disputed](https://lists.iana.org/hyperkitty/list/tz@iana.org/thread/EIBJYDJT3XQT5OWCNPIVVVH6U7INA2LW/):

> Lebanon is going through many internal disputes surrounding the latest decision to delay DST. Many institutions are refusing to comply with the change and are going to adopt regular DST on Sunday Mar 26th. Those institutions include but are not limited to:
> 
> *   News agencies
> *   Religious organizations
> *   Schools, universities, etc...
> 
> The refusal is mainly centered the legality of that decision and, obviously, the technical chaos it will create because of its short notice. Moreover, as some of the below articles mention, this is also causing sectarian strife.

Lebanon ended up with more than one timezone active at the same time, depending on which institution you were talking to!

It’s surprisingly common for countries to make decisions about DST with very little notice. Turkey and Russia and Chile and Morocco are four more examples of countries that can often cause short-term chaos for software developers in this way.

If you’ve stored your event start times using UTC this is a _big_ problem: the new DST rules mean that an already-existing event that starts at 6pm may now start at 5pm or 7pm local time, according to the UTC time you’ve stored in your database.

#### My recommendation: store the user’s intent time and the location/timezone

My strong recommendation here is that the most important thing to record is the **original user’s intent**. If they said the event is happening at 6pm, store that! Make sure that when they go to edit their event later they see the same editable time that they entered when they first created it.

In addition to that, try to get the most accurate possible indication of the timezone in which that event is occurring.

For most events I would argue that the best version of this is the exact location of the venue itself.

User’s may find timezones confusing, but they hopefully understand the importance of helping their attendees know where exactly the event is taking place.

If you have the venue location you can _almost certainly_ derive the timezone from it. I say _almost_ because, as with anything involving time, there are going to be edge-cases—most critically for venues that are exactly on the line that divides one timezone from another.

I haven’t sat down to design my ideal UI for this, but I can imagine something which makes it _abundantly_ clear to the user exactly where and when the event is taking place at that crucial local scale.

Now that we’ve precisely captured the user’s intent and the event location (and through it the exact timezone) we can denormalize: **figure out the UTC time of that event and store that as well**.

This UTC version can be used for all sorts of purposes: sorting events by time, figuring out what’s happening now/next, displaying the event to other users with its time converted to their local timezone.

But when the user goes to edit their event, we can show them exactly what they told us originally. When the user edits the location of their event we can maintain that original time, potentially confirming with the user if they want to modify that time based on the new location.

And if some legislature somewhere on earth makes a surprising change to their DST rules, we can identify all of the events that are affected by that change and update that denormalized UTC time accordingly.

#### Timezone UIs suck, generally

As an aside, here’s my least favorite time-related UI on the modern internet, from Google Calendar:

![Image 3: Google Calendar dialog for Event time zone, has a checkbox for Use separate start and end time zones and then a dropdown box with visible options (GMT-11:00) Niue Time, (GMT-11:00) Samoa Standard Time, (GMT-10:00) Cook Islands Standard Time, (GMT-10:00) Hawaii-Aleutian Standard Time, (GMT-10:00) Hawaii-Aleutian Time, (GMT-10:00) Tahiti Time, (GMT-09:30) Marquesas Time, (GMT-09:00) Alaska Time - Anchorage](https://static.simonwillison.net/static/2024/google-calendar-timezones.jpg)

There isn’t even a search option! Good luck finding America/New\_York in there, assuming you knew that’s what you were looking for in the first place.
