Title: The Many Lives of Null Island | Stamen

URL Source: https://stamen.com/the-many-lives-of-null-island/

Published Time: 2024-07-23T16:29:10+00:00

Markdown Content:
Last year we rebuilt our well-loved Stamen basemaps from scratch, re-creating them on [a totally new tech stack in partnership with Stadia Maps](https://stamen.com/here-comes-the-future-of-stamen-maps/). This was a bittersweet and challenging process, trying to build new styles that matched the aesthetics of the old maps, while still giving us a fresh start to keep these maps running efficiently for the years ahead. There were some annoying old bugs we were happy to be done with, but also some charming old quirks and a few hidden [Easter Eggs](https://en.wikipedia.org/wiki/Easter_egg_/(media/)) we had to decide whether or not we could (or should) try to bring into the new styles. Last month I gave a presentation about this topic at the State of the Map US conference (and you can view the video of my talk [here](https://www.youtube.com/watch?v=qewW7-z8W2I&list=PLqjPa29lMiE3msEjJS-QE5MTq1Ew0djYd&index=59)), but today I want to go a bit deeper into just one of those little details in the original maps, one we knew for sure that we absolutely had to include in the new styles: Null Island.

Null What?
----------

At risk of ruining the secret for you, [Null Island](https://en.wikipedia.org/wiki/Null_Island) is a long-running inside joke among cartographers. It is an imaginary island located at a real place: the coordinates of 0º latitude and 0º longitude, a location in the Atlantic Ocean off the coast of Africa where the Prime Meridian meets the Equator, hundreds of miles from any real dry land.

Null Island is not just a silly place to think about when cartographers are bored, it is a phenomenon that repeatedly and annoyingly asserts itself in the middle of day-to-day cartographic work, often when you least expect it. Sometimes you load a new dataset into your GIS program, but the coordinates aren’t parsed correctly and they turn into all zeroes: your data is on Null Island. Or sometimes if the [map projection](https://en.wikipedia.org/wiki/Map_projection) file for your data is wrong, you’ll find a tiny scaled-down copy of your coordinates floating around Null Island. Or even worse, maybe _most_ of your data is showing up in the right place, but only a few of your records are missing coordinates; if you don’t think to check for it, you won’t even realize that some of your data points have “taken a trip to Null Island.”

Let me try to explain with a few examples.

If you know to look for it, you’ll find data showing up on Null Island all the time. Right now it looks like someone has a [misconfigured PurpleAir sensor](https://map.purpleair.com/1/mAQI/a10/p604800/cC0#5.65/0.632/-1.267) which shows a delightful Air Quality Index of 19 in the central Atlantic (no, that sensor is not really there).

![Image 1](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf4UoTtFeCDZiB4TUclC8-l76cCjmZ2z182hu_Clj7pnNRK3gO4wGf3buCyBquG6l2ZcvMUMnAjNLy3PSyvaz5SGNaylXYfv92WMK-R2R-J9dC8OMJktR1Ss_GRMbzyU-3PrSvc3vxe9UvCoGBgGnv4-BPB?key=mXe81QAiHmFSe59nzgZ-sw)

_Null Island on [PurpleAir](https://map.purpleair.com/1/mAQI/a10/p604800/cC0#5.65/0.632/-1.267)_

On Weather Underground’s map of amateur weather measurements, several stations are also reporting their results on Null Island, even though the stations themselves are in places like [Schwertberg, Austria](https://www.wunderground.com/dashboard/pws/ISCHWE343) and [Ahwatukee, Arizona](https://www.wunderground.com/dashboard/pws/KAZPHOEN125).

![Image 2](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeqMPMQcMNH0BrDUkL03jPV6YlajUHGXUNYNaxBC8q8gJTPg6CEKp6N3_26MNMOMpTwjW0AfLYju6PwjNPGJ2ALp05u5Ctutix9CjC3zFohpJ5RUyUdhENqr65gpZ8d7n1BRNwuI4a9sBRsv88RzNCJmJsM?key=mXe81QAiHmFSe59nzgZ-sw)

_Null Island on [Weather Underground](https://www.wunderground.com/dashboard/pws/KAZPHOEN125)_

If you look at [Strava’s global map of public GPS traces](https://www.strava.com/maps/global-heatmap?sport=Run&style=dark&terrain=false&labels=true&poi=true&cPhotos=true&gColor=blue&gOpacity=100#15.5/0/0), you see a lot of ghostly traces of running tracks and city blocks floating around Null Island, and lots of bizarre patterns perhaps created by glitches in athletes’ GPS trackers?

![Image 3](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd0Zy2QvtYlyf6iOIAv6goaKlT8rawwBk2sVtGATQ9k4QH9238Akgkt0wxtajBjkn8c2eDh1eUnwrsr9kM6-rXYPeclcWvRvZ7VCXql6q-L2U_pqV56GVf2b2sxWgMXGxQHgaACGr5dc6WD1zouhSsTY8h4?key=mXe81QAiHmFSe59nzgZ-sw)

_[Strava’s heatmap](https://www.strava.com/maps/global-heatmap?sport=Run&style=dark&terrain=false&labels=true&poi=true&cPhotos=true&gColor=blue&gOpacity=100#15.5/0/0) around Null Island (Note, you need to create a Strava account to zoom in all the way)_ 

OpenStreetMap’s public collection of volunteered GPS traces also contains [a scribble-like hairball of lines around Null Island](https://www.openstreetmap.org/?#map=15/0/0&layers=G). These are either due to miscalibrated or broken GPS devices or faulty data translation software; you can be sure that nobody was walking (or sailing) around that spot in the ocean with their GPS tracker turned on.

![Image 4](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdBL0xhs4jS-WVGQrc-DKFljrrNRMqZB6QbDlFMxY0dEi-IAYqjKqzelT7oziL9J6KiX1K40gKAfeX_gAZYYOl4qfHkK1ZgGHRSE77EAy8FtbjBK4yaoHHQcXUnIPyLu6PkxwO3vQGzIqQZghNseOC_zOSJ?key=mXe81QAiHmFSe59nzgZ-sw)

_Null Island GPS traces on [OpenStreetMap](https://www.openstreetmap.org/?#map=15/0/0&layers=G)_

As an aside, if you go looking around Null Island trying to find misplaced data, you’ll sometimes see glitches in the basemap itself. Because bathymetry data (the measurements of the depth of the ocean floor) often comes in square chunks that have edges along the Equator or Prime Meridian, the shaded terrain effects on the seafloor often have stitching errors at 0º, 0º. On Apple Maps you can see something that looks like a little whirlpool, while on Google Maps there appears to be a seamount with a rougher texture that doesn’t look like any of the other features on the ocean floor, and if you stare at it long enough you might start to see a scary version of the famous “face on Mars” photo.

 ![Image 5](https://stamen.com/wp-content/uploads/2024/07/Null-Island-whirlpool-Apple-Maps-1016x1024.png)

 ![Image 6](https://stamen.com/wp-content/uploads/2024/07/Null-Island-face-on-Mars-seamount-Google-Maps-1024x944.png)

_A mysterious whirlpool at Null Island (or perhaps a [_fountain_](https://x.com/CA_22562_AN/status/1477257698903158787)_?)_ on Apple Maps (left), and “Null Seamount” on the ocean floor on Google’s Satellite layer (right)_

And sometimes it’s not the data _itself_ that is wrong, but through the design and usage of the default settings of geographic tools, you can see signs of Null Island by inspecting server logs of web traffic. For example, when we first launched our public basemaps back in 2012, we were curious to see where in the world people were looking at. When you parse the logs of which parts of the map users requested, and then [make a map of those requests](https://stamen.com/log-maps-2f360713fb5f/) (a map of map views, if you will) you see a surprising amount of map tiles loaded for the area around Null Island. There’s not much to see there, just empty ocean, so what are people looking for? Probably what we are seeing is software that loads a zoomed in map of 0,0 and then refreshes the map for the user’s location after it loads.

![Image 7](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe8HZf_Jyj2AAg86HirSwVpR9u-xIgeVADw7cFG6teEuzSLgMoScL4XceWbn1_TpHNKWIRdmpTt9_eeIDuW_3strmTBPR-y5PoaabtlrSfLF5PGPk2_WU-iCasxkpLlD3l0V-7FvEjNMmmmnHEJpdLyhPUx?key=mXe81QAiHmFSe59nzgZ-sw)

_A map of which map tiles were loaded in the 10 days after [the launch of maps.stamen.com in 2012](https://stamen.com/log-maps-2f360713fb5f/)_. _Note the dark spot southwest of the Africa label, that’s not actually on Africa, that’s 0º, 0º. Null Island!_

Maps of OpenStreetMap’s tile server logs show a similar pattern, with lots of tile requests for that specific spot in the middle of the ocean. See if you can spot Null Island in each of these maps:

 ![Image 8](https://stamen.com/wp-content/uploads/2024/07/18116898788_a913d287aa_o-edited.png)

 ![Image 9](https://stamen.com/wp-content/uploads/2024/07/Screenshot_osm-tile-access-log-viewer.png)

 ![Image 10](https://stamen.com/wp-content/uploads/2024/07/osm-tile-traffic-kgjenkins.png)

_Maps of OpenStreetMap tile views, by [Steven Kay](https://www.flickr.com/photos/stevefaeembra/18116898788), [Martin Raifer](https://www.openstreetmap.org/user/tyr_asd/diary/39434), and [Keith Jenkins](https://mapstodon.space/@kgjenkins/110980518633036297)_

Paul Norman even made [an animated version of these access log maps](https://x.com/penorman/status/1417350508285624321), showing tile requests over time. Many interesting and mysterious temporal quirks and glitches appear and disappear as you watch the video, but Null Island shines on and on like a beacon:

![Image 11](https://stamen.com/wp-content/uploads/2024/07/paul-norman-tile-log-traffic-animation.gif)

_Animated map showing OpenStreetMap tile access logs, by [Paul Norman](https://x.com/penorman/status/1417350508285624321)_

Similarly, our Field Papers tool has [a database of every printed map people created](https://stamen.com/a-new-home-for-field-papers/) from OpenStreetMap data, and if you map centers of all of those printed maps, you see some lines converging on Null Island (and some even stronger lines converging on a point in Morocco which happens to be the center of the map view when you get started creating a Field Papers atlas:

![Image 12](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeTrNggTOeV22OfxTaVednFyLsXrum8mk6hhOWgKzSXwxEU0uRmE3DsnOXZ0ALAK3ybAGBJ4i4fYFf_c82b_tvytNxojVwseEaG05oNRkGyl_h8FX_9771jsrjGoVejeqe42ZK4LNmNakMs_leUCqLTsY8B?key=mXe81QAiHmFSe59nzgZ-sw)

_The centroids of every Field Papers atlas as of 2021, by [Eric Brelsford](https://stamen.com/people/eric-brelsford/)_

The mythology of Null Island
----------------------------

Every cartographer has countless stories of messy data like these. So, to make light of these frustrating problems, the whimsical story of Null Island was born.

There have been several excellent histories written about Null Island, such as “[Null Island Is One of the Most Visited Places on Earth. Too Bad It Doesn’t Exist](https://www.atlasobscura.com/articles/null-island-is-one-of-the-most-visited-places-on-earth-too-bad-it-doesnt-exist)” by Tim St. Onge, “[Welcome to Null Island, where lost data goes to die](https://bigthink.com/strange-maps/null-island/)” by Frank Jacobs or “[Null Island: the island that doesn’t exist but lives on maps](https://culturacolectiva.com/en/technology/null-island-maps-unreal-place/)” by Isabel Carrasco. Any of these articles gives a good overview of how the idea of Null Island came to be, but far the most thoroughly researched history of the Null Island phenomenon is this recent open-access academic article by Levente Juhász and Peter Mooney “[Null Island, the most real of fictional places](https://arxiv.org/abs/2204.08383)”.

Of these articles, only the one by Juhász and Mooney is also the only one that digs into the history of the fictional Null Island _shape_ that we see on [T-shirts](https://www.zazzle.com/s/%22null+island%22) and [stickers](https://www.ektad.com/projects/null-island), and occasionally hidden on basemaps. Null Island as a data glitch really only exists as a point in space (precisely at 0º, 0º) so where did this imaginary polygon come from?

It turns out, the first [Null Island shape](https://github.com/ajturner/acetate/tree/master/tiles/shp) on a basemap (based on the island from Myst) was added by Mike Migurski to the [“Acetate” style basemap](https://web.archive.org/web/20110202103334/http://blog.fortiusone.com/2011/01/19/announcing-acetate-better-thematic-mapping/) that Stamen designed with GeoIQ in 2010. That Acetate basemap no longer exists on the web, but we used the same Null Island shapefile in our Toner and Terrain styles starting in 2011, where it has been visible ever since.

![Image 13](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe0RCUzUlQ5pT5Klk7umQ43DGfthESzqLB2Dm5bjRFRhKh7Cswc3dOpA6pop6znTyT6BHwyyiF8zFUnlHGMln7KptQwHZsqm2T_hva2SDvjze1ahhiRzlrXz_d29u8ZRtBaZbM4-oB5Q3DQWSzMkuaakkY?key=mXe81QAiHmFSe59nzgZ-sw)

_The map of the island from the game Myst_

When it came time to re-create our old raster map styles using Stadia’s modern vector maps platform, we had to start completely from scratch. None of the old map styling code could be adapted to the new vector styling paradigm, and similarly the old database setup wasn’t relevant given that Stadia already had a complete OpenMapTiles pipeline running that we would use as the basis of the new styles. The only thing missing that we might need to pull from [the old github repository](https://github.com/stamen/toner-carto/tree/master/shp-local) was Null Island.

I knew that we had a shapefile of Null Island in the old repo for the raster-based Toner style, but instead of downloading the shapefile and converting it to GeoJSON (really not hard to do at all, but I was lazy) I figured someone else must have already done that conversion, so I just Googled for “null island geojson” and downloaded the first one I saw.

But something wasn’t right. When I compared the shape of Null Island in the old raster Toner map with the new vector style we were developing, they didn’t line up at all. In fact, they weren’t even remotely the same size!

It turns out that the [GeoJSON I downloaded](https://github.com/nixta/null-island/tree/master/GeoJSON) was from Nicholas Furness (github handle [@nixta](https://github.com/nixta/)), a developer at ESRI, who had created a Null Island geojson that is way bigger than the one we had been using. Ours is about 100 meters across, but this one is nearly 10 _kilometers_ across.

![Image 14](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd_ZgMePjxEFipCrN_gLVmfIjhyGTO-V-foEiZHvsfHm9GPi9TmUB2aaXbCSTBjbwedX1M667I0HZVR-bm0Zwb6rBg4pIAUHVLSjBFwhmWKCiLsj3HY72STlVP3SVTuCwKF3ThNY-zc8pqzPzsvRPsHKMkp?key=mXe81QAiHmFSe59nzgZ-sw)

_The_ [_“nixta” Null Island_](https://github.com/nixta/null-island/blob/master/GeoJSON/null-island.geo.json)_, with the tiny Myst-inspired original Null Island visible in the center._

The size difference is dramatic! The original Null Island at 100m could fit inside Yankee Stadium, the Zocalo plaza in Mexico City, or St. Peter’s Square in the Vatican. While the new version at 10km wide is nearly the size of Disney World, or the city of Paris, or the entire country of Liechtenstein.

Or to put it in terms more familiar to Stamen’s home base in the Bay Area, the original Null Island would fit inside the AT&T Park baseball stadium, while the new one is as big as the whole city of San Francisco.

![Image 15](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdwBXqjXWeXH1RzCG-h-VaD5C8kwvo8seBDsdijTonoAhXDxGDuvea_nZCZ23NBJn0FAx0Nm-ysYKPCk7SiLPZ9fk41KfcYKClpXVRv4kCf57UO62t_peH8YC9E8Utl82fW6oLoq27yJqo8Tg3zpUa1MbY?key=mXe81QAiHmFSe59nzgZ-sw)

_The original Null Island shape overlaid on AT&T Park in San Francisco_

![Image 16](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdxlVednGB9z3X63DoO-PYVetx-YTnqHOb7tjRiGkohQwU73M8QLLdlykxmzxsX5Udpe2-6FmZtEr0toN3C1JMU-fIuXwUyoH62WhNTCaXc-ZpkckrvaWUjCOdtrcrOvyRV-hOVcJzb46D7VDb6-a6Z1-0d?key=mXe81QAiHmFSe59nzgZ-sw)

_The larger Null Island shape covers the entire 7 mile width of San Francisco_

So why is this second Null Island shape so big? Well, the area of 63.8 km2 I calculate for that shape in my GIS matches nearly exactly the 6,400 hectares mentioned on an old joke website for the “[Republic of Null Island](https://nullis.land/)” created way back in 2008. As far as I can tell, the creator of that website, Steve Pellegrin (who also coined the name “Null Island”) just pulled that number out of thin air. But when Nicholas Furness set out to trace the shape of the island and create a GeoJSON file (not knowing that the Stamen shapefile was already available) he adjusted the size of his tracing until it fit Pellegrin’s 6,400 hectares.

So, how big “should” Null Island be? If we note that it’s based on the shape of the island in Myst, (and that you can see from the shape of the island that it actually includes a ship docked to the lower part of the island) then the 100m shape is closer to “accurate” and perhaps even a little too large.

And if we think about the extent of “normal” erroneous data, in the cases where data shows up at Null Island not because of lack of coordinates (which would have all your points piling up exactly at 0,0) there are the less common cases where the wrong projection information is applied to your data. In this case, a location of 122ºW and 48ºN might be misconstrued by your GIS as a point 122 meters west and 48 meters north of the center of your map, which is often aligned right at Null Island (for the Mercator projection in particular). In that case, the 100m shape of the Null Island polygon is also a nice “canvas” to help you locate your messed up data, even though it’s not quite big enough to keep the points from falling in the water:

![Image 17](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe006MP0_nEPaK-y1jDUxeNfroDDfsX5uruwXw4pztPgbThs4KdiJr1W4YSV93EHPp8_wPWdpbEaEcdIfZNlmfcYtyUM_A2KWpnMQZAIiJgZ0AbJ9t_9jhxyqSVMv9CBulOUdZHd-L14OG0Q38h7ifprFUU?key=mXe81QAiHmFSe59nzgZ-sw)

_Example map using major cities of the world sourced by Natural Earth, but with the deliberate error where we interpret latitude and longitude degrees as meters instead._

The Myst-inspired version of Null Island isn’t the only Null Island that is experiencing geographic inflation! Not long after we included the first Null Island in the Acetate Map, a year later in 2011 an even smaller version, in the form of a 1 meter square, was added to version 1.3 of the Natural Earth dataset used by countless maps around the world. But apparently, 1 meter isn’t large enough! In 2018, version 4.1 of Natural Earth bumped the size to 1 square kilometer. If you [download the “land” or “coastline” layers](https://www.naturalearthdata.com/downloads/10m-physical-vectors/) from [Natural Earth](https://www.naturalearthdata.com/), you’ll still see it today.

![Image 18](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeyx8ezB6mgAm_WCEQdD0LBdSBgRbTtmUOptfvKjcm6m0EbPSMXwHL240ftjRAHNicO_TKweMVDUKsuDhEsy3vRPKQi3DFVm2Vsl_vDV5RzwlmVrWwDch5rnvGTm0Adu7pie1Ds3BEcSVVuo2_LYh7UiY-G?key=mXe81QAiHmFSe59nzgZ-sw)

_Zooming in on the original Null Island, with the Natural Earth first “Null Island Square” visible in the center._

![Image 19](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdzvHZeq7wlh1WAeAWaBRRgz0Gp8KAy-W9revlvjC7mDZgUn1oK0denY68VFewxd2YU9QxIrnz1PigHBl8qtmxQ2KdOt3lyOABQmvInqcfrV-Cmy1TKvfzjLOVcTXkvVpIwrCMleyUhhRcS1JzjbjmF-44?key=mXe81QAiHmFSe59nzgZ-sw)

_Zooming out to see the new 1km square version of Natural Earth surrounding the original Null Island._

To put these sizes into context, the one meter Natural Earth Null Island is: about the size of 9 laptops looking at a map of Null Island in this blog post; [the width of 5.6 bananas](https://www.converttobananas.com/); about half the [surface area](https://en.wikipedia.org/wiki/Body_surface_area) of an average human. One meter is also about half the size of the real-world weather buoy that is moored at 0º, 0º (but more on that later).

![Image 20](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfXe5uFXNzFdNh1oVRQZ5KoDGhkKJjLTxTCt9kVRbnVZp-6L8n5OQhOv_rYZBSEP18cmMcctW9xsMxUq4bDsVNXqYY7DJxoC6hdJDVnznjKXO1BHaxw9LcRgZA04ebqcReizg3jYqzB00rJ4I_RmXJIsJo?key=mXe81QAiHmFSe59nzgZ-sw)

_The original Null Island square from Natural Earth, compared to the one meter reference square centered on two picnickers in a park, from the classic short film_ [_Powers of Ten_](https://www.youtube.com/watch?v=0fKBhvDjuy0) _by Charles and Ray Eames_

The one kilometer Null Island, on the other hand, is: the size of the Kingdom of Monaco; a bit wider than the Burj Khalifa is tall; almost the length of the Golden Gate Bridge.

![Image 21](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdOHoXv8igUZXXaobkfa5ne9bOVLu6-KBBTE55RgfGvQPGufSQwbbQ04EVCiweDKbSEANk83ZBKShjkGHvY9TBwi7OLNbk8ixGuLN4MmV8FFIsXQPMTb5mMELMq5bc-WHFVJ_Gb4kKJ_CffZoZiFn99Qb53?key=mXe81QAiHmFSe59nzgZ-sw)

_The updated Null Island square in Natural Earth version 4, compared to the Golden Gate._

In this case, it does seem to make a lot of sense to make the Null Island square a bit bigger. If its purpose is to catch bad data, 1 square meter probably isn’t big enough.

When your Easter Egg is an an ostrich egg
-----------------------------------------

In the end, Null Island is a totally made up thing, so we can pick whatever size for it we want. Sure we can debate whether our imaginary world is _internally consistent_ (that is, if we’re literal about the Myst reference, the size of the boat docked to island ought be be the correct scale) or we can come up with a _post hoc_ rationale that we need it to be a useful size for debugging. But ultimately, it’s an Easter Egg and the process of creating a good Easter Egg of any kind has its own rules and logic.

Choosing the right size for Null Island (or any Easter Egg) is a design decision, a balance of exclusivity and accessibility, of form versus function. An Easter Egg should be a surprise, a treat, and it should make someone pleased and a little bit proud of themselves when they find it.

It’s not much fun if it’s too hard to find, and it’s not worth the work of creating it if no one will ever see it! But if it’s too big and too obvious, it loses all of its charm.

The location of Null Island presents an especially tricky design challenge, precisely because it is so far from everything else. There’s nothing around to orient you, so if you are actually going looking for it, it can be very hard to find! Some mapping websites have the zoom and coordinates right there for you to see in the URL hash (which is something we try to do on most of our Stamen projects) and if that’s the case, it’s easy to type in “18/0/0” in the URL (that means zoom level 18, latitude 0, longitude 0) and find your way right to Null Island: [https://maps.stamen.com/toner/#18/0/0](https://maps.stamen.com/toner/#18/0/0). But if there is no way to control the latitude and longitude from the URL, it can be very hard to zoom in from a global view and find it without getting lost.

If we want Null Island to be _just barely_ findable, but not too obvious, I’d argue that the “right” size would be such that it’s just one pixel at the edge of your screen while the coast of Africa is still in view. We can do some back of the envelope calculations, assuming a screen size of about 2000 pixels, and zoom level around 7, where [one pixel represents an area about 1,200 meters wide](https://wiki.openstreetmap.org/wiki/Zoom_levels). Which means that the original 100m Null Island is just a bit too small to easily find, and the new 10km version just a bit too big to easily hide without _everybody_ noticing it.

Adding an Easter Egg to a map is also a different undertaking than putting one in a video game. Maps are (usually) meant to be serious, functional, trustworthy, and, you know, _accurate_. Once we start tampering with the map, showing things that aren’t really there, it makes people doubt the validity of the rest of the map. And even if people understand that it’s an obvious joke, an Easter Egg that is too big can get in the way of the “real” work that someone is doing. Ultimately, if an Easter Egg draws too much attention to itself you might be obligated to remove it.

We ran into this problem when we implemented Null Island in the basemap we worked on for Meta. We originally had full buy-in from the team we were working with, and we all enjoyed knowing that Null Island would live on in another map, even if few people would ever see it. Or rather, we _expected_ that not many people would see it. Unfortunately it certainly had many more eyes on it than we expected when Facebook’s recommendations tool started showing a zoomed-in map of Null Island when people asked for recommendations but hadn’t gotten any suggestions yet (thanks to [Andrew Wiseman](https://x.com/wisemana/status/1353821034453946370) and [Chris Whong](https://x.com/chris_whong/status/1359126193413488645) for catching screenshots for posterity).

 ![Image 22](https://stamen.com/wp-content/uploads/2024/07/null-island-facebook-awiseman-twitter-crop.jpg)

_Null Island shown on Meta’s basemap in a Facebook recommendations post in 2021 (_[_image via Twitter_](https://x.com/wisemana/status/1353821034453946370)_)_

If you look closely at that shape, you’ll notice that for Meta we used the larger version of Null Island. I don’t recall whether we consciously picked the larger version, or if we grabbed it accidentally, as we almost did again for the reboot of our Toner and Terrain styles. While we can’t know for sure, had we picked the smaller original Null Island, perhaps it wouldn’t even have been visible in those recommendations pages? The smaller version of Null Island likely would have been little more than a single white pixel in a sea of blue.

In a later iteration, we even added lovingly hand-drawn bathymetry rings around it, as seen in this screenshot of the Meta basemap in use as the background of Mapillary:

Sadly, in the latest iteration of the Meta map, Null Island is no more. Coincidentally, around the time we wrapped up our work with Meta, they silently dropped Null Island from their maps. While we aren’t privy to the specific reasons for dropping Null Island, the attention it had gotten by showing up in all those recommendation posts surely did not help. When an Easter Egg can’t fly under the radar, it stops being an Easter Egg and starts just being a bug.

Null-flation?
-------------

It does feel like every time you turn around, Null Island is getting bigger, giving me flashbacks of the guy who claimed on Twitter: “Every time I’m drunk I make Missouri slightly larger on its Wikipedia page”. Just like the ever-growing Null Island, it was only a matter of time before too many people noticed it.

![Image 23](https://lh7-rt.googleusercontent.com/docsz/AD_4nXchHpxB_3xjycioYzKc3FZSu9OnAZ50cDb4uo1Y8eMUiCguYEA6fD3KMm1lR46ore2_fqFLwNn0EAHifkoZ7MQOHgkAmopMpB9wNhC5-9xLUK-sNh0Au9zwexY6ZEwNTxm8Tu8wglRDyffianFOWGSF1QxL?key=mXe81QAiHmFSe59nzgZ-sw)

_Constantly making things bigger on maps: a common compulsion (via_ [_Reddit_](https://www.reddit.com/r/madlads/comments/wrcb4i/this_madman/)_)_

Hopefully, the Null Islands we have now are big enough; we already have four different versions of Null Island circulating in the wild, let’s not add to the confusion.

To help clear things up, and to get a sense of the relative sizes of these four Null Islands, [here is an interactive map](https://stamen.github.io/null-island) showing the four Null Island shapes that are actually circulating in the wild. It includes the two Myst-inspired islands (the original 100 meter wide “smol” version and Nixta’s hypertrophied 10km wide follow-up), and the two Natural Earth rectangles (the 1 meter square and the 1km square) which give results in a pleasing homage to the classic Eames Office “[Powers of Ten](https://www.youtube.com/watch?v=0fKBhvDjuy0)” video.

![Image 24](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdzsMhAFbupdxPFL9ofmkSGwy-G_uq43JrKv6S1PwSSOle44GUAEizZ_xPoHixGWJuqCjRYwQUylBH6H_JIvWasGg6M2G-biSBanfics5aw1kgyZEu6iLbv9L25NJBmwP6SbCjHbiEkRPjqNZ-ulXEmp5xl?key=mXe81QAiHmFSe59nzgZ-sw)

_Try our interactive map yourself at [stamen.github.io/null-island](https://stamen.github.io/null-island)_

Getting the data on the map
---------------------------

But back to adding Null Island to [our Stadia Maps basemaps](https://stadiamaps.com/stamen). After finding the correct file, there’s still the matter of how do we get it into the map? Our new basemap styles now hosted on Stadia were designed to use an unmodified copy of OpenStreetMap using the OpenMapTiles schema. For various reasons we didn’t want to tamper with this database and insert our own data for Null Island. The island, at least at the moment, doesn’t exist in OSM (or if it has been added to OSM in the past, it has since been deleted… which is probably for the best).

Originally we considered including the Null Island GeoJSON with every request of the stylesheet. We could get the file down to 12KB, which is really quite small, and it was amusing to think that everyone who loaded the map would be downloading the shape of Null Island even if they were looking at some completely different part of the world. In the end, though, we didn’t go down this path, and instead decided to do things the “right” way. So now Null Island lives on in its own very small tile layer, which means your browser only loads it if you are looking at the exact right spot and the right zoom level to actually see it. This also means that if you’re making a Very Serious Map and you don’t want Null Island on it, we can remove it for you.

![Image 25](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcxEyzxdgK4Whozr4jkGHdnbILA83JPji-pxxlnuFzTjIHqQTKuAHelGvsgZUlNU0iABZSC-YwDX_5KnpOWaV-CrLC-v0Q4jDHjOEWmJA_77gjS8S2efDAnH_y4gVAl-gieQtzZPpeh2ccSlHnx6g2yU40d?key=mXe81QAiHmFSe59nzgZ-sw)

_The raw Null Island tile data as seen in Maputnik’s Inspect view_

Also, check out all those lovely name translations we have in the data! Those aren’t present in our original shapefile, because the old raster versions of Toner and Terrain were English-only, and it would have been prohibitively expensive to render separate world-wide raster layers to support additional languages. But [as we wrote about in an earlier blog post](https://stamen.com/stamen-x-stadia-harnessing-modern-vector-cartography/), one of the fantastic things about modern vector-based web maps is that it’s easy to swap out the language on the client side, enabling users to view Toner or Terrain in any language they prefer. The OpenMapTiles schema already pulls every available language from OpenStreetMap, so if we wanted our Null Island shapefile to work in the same way, I needed to find the name of Null Island in as many languages as I could. One of the powerful ways that OpenStreetMap extends their multilingual coverage is by linking OSM features with their WikiData counterparts, so I figured I’d try the same thing with Null Island.

I was delighted to find that the [WikiData entry for Null Island](https://www.wikidata.org/wiki/Q16896007) (there known as item “Q16896007”) contained dozens of translations of Null Island in other languages. In some cases, other languages just use the English word, which is no fun, but there are still plenty that do not. So if you ever wanted to learn the name of Null Island in Breton, Hungarian, or Igbo (or in constructed languages like Esperanto and Lojban) now you can. Or even better, you could easily make the first-ever map to show Null Island labeled in Macedonian. Give it a try!

![Image 26](https://lh7-rt.googleusercontent.com/docsz/AD_4nXerqNoj9aZtsvrcTO2MriMiHqaE-rEX2exzfuCQGvhiXcdg4rWNB3bpg9PONJamIdFnCN0rSy_H0oAJ62L18SWDaALBnbFuGcWV8XIyya66xr94uGPpscsLv_YlQv8exMTCO3PkuRsb7ik84y3FPhFlo9sa?key=mXe81QAiHmFSe59nzgZ-sw)

_Multilingual support for Null Island in [WikiData](https://www.wikidata.org/wiki/Q16896007)_

Digital signposts and virtual journeys
--------------------------------------

WikiData is a fascinating project if you’re a data nerd like me (and if you’ve read this far, well…) not only because of the way it provides connections between different languages on Wikipedia, but also how it connects diverse open data projects together. By giving a unique numeric identifier to every Wikipedia page (including structured information about how each concept relates to other concepts) it’s like a trail of breadcrumbs that we can follow from idea to idea, and from virtual place to virtual place. But even these identifiers get broken and corrupted sometimes, perhaps leading you to the wrong page, much like corrupted geographic coordinates lead you to Null Island. (Also let’s take a moment for the unfortunate souls named “Null”, who have their own set of problems where [databases refuse to recognize their name is real](https://www.wired.com/2015/11/null/)).

Browsing the metadata identifiers for Null Island listed in WikiData, we see appropriately enough that in the [Where On Earth ID database](https://en.wikipedia.org/wiki/WOEID) (a project similar to WikiData, but only for geographic places) ID number 0 takes you to Null Island. While “Where On Earth” no longer exists, in its successor project “Who’s On First” [Null Island has an ID of 1](https://spelunker.whosonfirst.org/id/1/) (because they wanted to assign ID 0 to the planet Earth). Personally, I’m a bit disappointed that the WikiData identifier for Null Island (Q16896007) is so meaningless, while The Universe is “[Q1](https://www.wikidata.org/wiki/Q1)”, Earth is “[Q2](https://www.wikidata.org/wiki/Q2)”, and some other entries have appropriately silly Easter Eggs like author Douglas Adams as [Q42](https://www.wikidata.org/wiki/Q42). C’mon WikiData, ID “Q0” is just sitting there, unused. Can we redirect Null Island there? If any Wikipedians can help me with that, please get in touch!

The WikiData page also includes links to Null Island’s identifier on several other platforms, such as Instagram! So if you’re curious about any Instagram photos tagged at Null Island (whether or not, most likely not, the photo’s GPS coordinates are actually at 0º, 0º), you can browse them here: [https://www.instagram.com/explore/locations/634174294/](https://www.instagram.com/explore/locations/634174294/) On Instagram, the place name tagged on a photo doesn’t necessarily have to be the place the photo is taken (or where the GPS coordinates of the photo say they are), and in this case even the place named “Null Island” appears to be located somewhere in the suburbs of Southwest Philadelphia.

![Image 27](https://lh7-rt.googleusercontent.com/docsz/AD_4nXclyWSTR1CDTNUcyi4vnZlsWBUBG3mLriu2rCzrCbyv89TB2Mb01XGMLVsU-JGmiRhW2Fs_z8nAo-s6LI1JkDupmkXmICilJ7rvdyUogfa93FknKvpSDJllsNmDvKRhElmHIqyVoLKNpoTSHKsakhAL9LDE?key=mXe81QAiHmFSe59nzgZ-sw)

_Recent photos on the place page for_ [_“Null Island” on Instagram_](https://www.instagram.com/p/CzOSfaQAyFs/)

This feels like we’ve come full circle: Null Island has become such a phenomenon that people are deliberately tagging their photos at a place called “Null Island” just for fun. There’s no easy way to tell if the deliberate check-ins at this fake “Null Island” place outweigh the number of photos tagged erroneously at “0º, 0º” (that is, whether the _simulacra_ of Null Island has overtaken the original “real”, but also “fake”, Null Island).

If you really want to get your photos to Null Island so badly, you could always set up a GPS spoofing device to truly trick your phone into thinking it is at Null Island, as artist Simon Weckert did in a [2022 installation in Ljubljana](https://aksioma.org/the-republic-of-null-island)!

![Image 28](https://lh7-rt.googleusercontent.com/docsz/AD_4nXedNCksH3H1XQIhh1ed9rZ-WgcJqYfR7MHiGbTcGAHo8a4YELSe_hskgFM32km2LcZvdbQMtk81V5Zd5yhx6M72Qg9cRgCkbyTPmaWPtNkadudauKjjyhhrB36UPLXJvpwjT7b8gWNMHfWHVMzL9UVsA3Jr?key=mXe81QAiHmFSe59nzgZ-sw)

_A phone showing its location at Null Island at_ [_Simon Weckert’s installation_](https://www.simonweckert.com/nullisland.html) _in the Aksioma Institute for Contemporary Art in Ljubljana_

Finally, though, there is no substitute for actually going to Null Island, even if it does seem to me like missing the point. If you look closely at some of those Instagram photos, it appears that at least one cruise ship visited Null Island recently on a world tour. It’s even listed as [a destination on Holland America cruises](https://www.hollandamerica.com/en/us/cruise-destinations/grand-voyages/grand-voyages-world-cruises-ports/crossing-null-island-989). But did any of those cruise passengers _really_ visit the spot? The only real evidence of visiting Null Island is if they saw the weather buoy tethered at 0º, 0º, but there is [a five nautical mile exclusion zone](https://www.theguardian.com/news/2023/jun/08/null-island-weather-reports-place-does-not-exist) around that spot to prevent damage to the buoy. That would seem to prevent any cruise ships or other tourists from visiting. To officially go to 0º, 0º you must be part of the maintenance crew there to check on the buoy. Visiting Null Island is Very Serious Business.

![Image 29](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcqoQfZqTb7n_-SimKKCuOQTC6vxZ5fsxpA_ILAttRQMxxjQqJFSZRqneir7nM5FQOVxoFrUHQT-ksQlYJuDAGKEM3ZZJNIuO6WWYa_-rhKgCffYEo7Iuv5Z8V_8Nmyq5P9BUYMYZYUx8JZKQ5Fis_urabN?key=mXe81QAiHmFSe59nzgZ-sw)

_A visit to the Null Island Buoy by [Pål Torsgård on Instagram](https://www.instagram.com/p/CKjXs6anF2z), on the ship [MOU Island Constructor](https://www.islandoffshore.com/vessel/mv-island-constructor)_

In any case, it’s clear that Null Island is here to stay, no matter how you choose to visit it. And we’re pleased that for the foreseeable future, Null Island will survive on our basemaps, thanks to our friends at Stadia Maps.
