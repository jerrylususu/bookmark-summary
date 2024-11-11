Title: Anyway, the wind blows

URL Source: https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/

Published Time: 2024-11-11T12:34:57+00:00

Markdown Content:
![Image 1: Book cover. A distorted Kraken appears on an old fashioned computer screen. Several hands type on distorted keyboards.](https://shkspr.mobi/blog/wp-content/uploads/2024/11/RotMA-small.jpg.webp)Finding the root cause of an incident will always come to a dead-end at some point. We can use various investigatory techniques to ascertain _why_ a part failed or _who_ installed it incorrectly, but that doesn't get to the heart of the systemic failures which led us here today. This has been a time-consuming (and some would say futile) effort, but I believe this sort of analysis is vital.

Here is everything we know so far.

### [23:42 - A weather station near the mouth of The Thames](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#2342-a-weather-station-near-the-mouth-of-the-thames)

Logging data showed that new firmware was uploaded to the weather station. Normally, that would have been over a USB connection by an authorised technician. This time it was uplinked over Bluetooth, using a signing key which was supposed to have been revoked after the Salieri hack back in 2025.

Unsurprisingly, there is no remaining CCTV footage. We do not know the motive of the party involved, nor who they worked for. This could have been a state-sponsored attack or a lone hacktavist.

Reverse engineering the surviving data shows that the firmware was supposed to trigger the next morning and spread a malicious message over the mesh network which would have severely disrupted weather predictions. It didn't do that. Whoever wrote the code didn't take into account the UK's daylight savings time. When the clocks went back a few hours later, the hacky firmware crashed.

What happened next was unintentional and, ultimately, disastrous.

### [01:32 - Weather Network South East](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#0132-weather-network-south-east)

The broken terminal crashed repeatedly, tried to move into safe mode, and came back even more corrupted. It started to erroneously report wind speed of over 256 miles per hour. The hypervisor relayed the sudden uptick in wind speed to the network. Ordinarily, that wouldn't have been a problem, but most of the nearby network were on an older version of the standard operating system. When they saw the high speeds coming towards them, they shut down to protect themselves.

Normally, a few sensors going down would not cause any significant disruptions. Unfortunately, the brief outage meant that, for a time, the faulty sensor was the only authoritative sensor in its region. Its erroneous reading was coming from the only voting sensor in the region and was instantly propagated. The "official" wind speed became impossibly high.

### [01:33 - Thames Barrier](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#0133-thames-barrier)

The sudden uptick in apparent wind speed caused an alert at the barrier. High wind speed is an indicator of a storm and, therefore, higher rainfall was predicted. Autonomous systems assumed the worst and started an emergency raise of London's tidal defence network.

A few pager messages were sent out to staff who were nominally on call. Sadly, the pager network had been switched off earlier this year, but no replacement service was up and running. Staff who could have prevented what came next were unable to stop the unfolding catastrophe.

Although the barrier raise took several minutes, immediate alerts were sent out to all shipping to warn them that crossing the barrier was soon to be impossible. Approximately 300 vessels of all sizes received this message. Of these, 298 accepted the message and either re-routed or stayed in harbour. Tragically, two ships had an unhelpful failure response.

### [01:34 - Heavy Goods Ship Pearl-5](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#0134-heavy-goods-ship-pearl-5)

The HGS Pearl-5 was laden with goods and sundries destined for an Amazon warehouse a few miles north of the barrier. Its cargo was relatively unimportant - mostly Christmas presents and fast-moving consumer goods. There were no perishables or urgent items which needed immediate delivery.

It received the notice from the Thames Barrier and slowed to a halt in a safe shipping lane. It signalled its delay back to the factory in China which had loaded it, and reported a similar message to the warehouse.

### [01:34 - Royal Navy Cruiser - HMS Titan](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#0134-royal-navy-cruiser-hms-titan)

The Titan was a highly capable warship and should have been on patrol. Instead, it had been re-routed and was undergoing a publicity trip in Central London. Various military and political dignitaries had spent the night marvelling at its armaments and technical capabilities. The publicity trip, however, was a ruse. Under cover of night, Titan was sailing down the Thames with the Prime Minister aboard. Its ultimate destination was a rendezvous in the middle of the North Sea with a fleet of newly commissioned Ultra-Vanguard submarines.

Titan's automated systems received the barrier message and made a critical mistake.

The original software for the ship had been developed to deal with metric measurements. In a fit of nostalgia, the government had decreed that all Royal Navy vessels should work exclusively in traditional Imperial measurements. The Titan calculated its distance from the Thame Barrier and plotted a course which would take it to open waters before the closure completed. Sadly, the conversion between metric and Imperial was imprecise. Several rounding errors compounded and the distance plotting algorithms ended up with a significant deviation from reality.

### [01:37 - Amazon Warehouse](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#0137-amazon-warehouse)

The robot pickers at the warehouse were trundling into position when the system received the message from the HGS Pearl-5. The system spent several minutes calculating the likely impact on the next day's orders. It sent out emails to thousands of customers letting them know their goods wouldn't be delivered on time and offered them all a £1 voucher in compensation.

Because of the unusually large number of orders delayed, the warehouse sent a notice to the stock market letting them know that there was a significant impact on the day's profitability. The robot pickers trundled back into their sheds.

One of the pickers slipped. We do not know the cause of the slippage, but it caused the picker to fall which knocked down all the robots around it. Due to recently enacted labour laws, there were no humans on scene to help recover the robots. So they lay strewn on the ground. Alerts were sent to human supervisors, but they were probably ignored.

### [01:40 - Intertrade Headquarters](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#0140-intertrade-headquarters)

Intertrade ran the largest automated stock trading system in the world. They analysed thousands of pieces of data per second in order to predict the movements of the stock market. They could discern minute signal from even the noisiest data environments. Shortly after the cascade began, they picked up several signals which led them to an incorrect conclusion.

A factory in China reported that their cargo wasn't going to be unpacked in London until time unknown. This particular factory had a rather large debt balance which was due to be serviced in the next four days. Without the cargo being unloaded, there would be no cash incoming. Which meant a default on their debt. Which meant the bank holding that debt would have to either turn to the embattled state bank for refinancing or liquidate.

The weather reports coming out of London indicated that a severe storm was wreaking havoc on the city. Sensor networks were reporting almost impossible to believe numbers. The Thames Barrier had signalled an unscheduled raising. The traders' statistical models of climate change had predicted this sort of freak event and reacted accordingly.

A bot watching the stock market noticed the unusual report from Amazon and tasked a nearby satellite to do a quick flyover. It beamed back pictures of mayhem, with dozens of robots tangled in a pile. The machine vision algorithms interpreted this as a major snarl and started calculating the likely impact on their positions.

A few milliseconds later, the trading algorithms sprung to life. Disaster in London, disaster in China, disaster for Amazon. Sell! Sell! Sell!

The trading house went into overdrive and began dumping all the stock they could.

### [01:41 - Stock Markets Worldwide](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#0141-stock-markets-worldwide)

A million bots observed what Intertrade's traders were doing and started to copy their apparent strategy. Stocks plummeted, currencies crashed, trillions were wiped off the global markets.

### [01:42 - Royal Navy Cruiser - HMS Titan](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#0142-royal-navy-cruiser-hms-titan)

With a sickening crunch, the speeding ship came to a halt against the Thames Barrier. The miscalculation of speed and distance directed it into an immovable object. The Titan's systems assessed the damage and couldn't be sure if they were under attack. While it awoke the skeleton crew, it set a red alert and began monitoring for further enemy activity.

At the time of impact, the Prime Minister was reading his phone in bed, Doom Scrolling.

As the ship lurched forward, his phone was thrown forward. The sudden movement was detected by its internal accelerometers and gyroscopes. It cracked against the wall with the force of a bullet and dropped into a mug of warm cocoa.

Unexpected motion, loud noise, body temperature fluids, loss of biometric confirmation. The paranoid internal AI sent a priority distress call over its TETRA radio. Flash! PM down, possibly dead.

The Titan's system reacted with perfect precision. An unauthorised electronic transmission had occurred within its confines. This could not stand! The warship deployed electronic countermeasures - spewing digital chaff over the airwaves, blocking all radio signals in the vicinity.

### [01:43 - South East Sensor Network](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#0143-south-east-sensor-network)

Just outside the 10 minute SLA, the outsourced support team reacted to the reports of problems with the sensor network.

Although the humans in the loop were unfamiliar with the vagaries of British weather patterns, they reasoned that the figures coming out of it were unlikely.

Unwilling to wake-up anyone in a far-off timezone, they performed a perfectly reasonable action; a full system reboot.

The command traversed the globe in milliseconds. Every single environmental sensor in the southeast switched off.

In theory, they should have switched back on two minutes later. They never got the chance.

### [01:44 - Ultra Vanguard Poseidon](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#0144-ultra-vanguard-poseidon)

A few hundred metres below the water, lurked Britain's deadliest warrior. A stealth submarine designed to repel invaders and seek immediate revenge. An impossibly thin fibre-optic cable lazily ran to the surface where it connected to an inverted spider of antennae. Every frequency scanned, correlated, analysed, processed.

Poseidon was a rapid reaction line of defence. A sophisticated set of computers ran everything from stern to bow. The human sailors were, so the designers claimed, mostly decorative.

Poseidon's radios listened in the moonless night, and what they heard terrified it. It absorbed the data and began spotting patterns where there were none.

The stock market had gone into freefall.

The Prime Minister had sent a distress signal.

The entire sensor network for London was non-responsive.

And, even worse, Radio 4 was off the air.

Poseidon didn't hesitate. Human intervention was too slow, too emotional, too cautious.

A dozen nuclear warheads launched into the unsuspecting sky.

[Thanks for reading](https://shkspr.mobi/blog/2024/11/anyway-the-wind-blows/#thanks-for-reading)
------------------------------------------------------------------------------------------------

I'd love your feedback on this story. Did you like the style of writing? Was the plot interesting? Did you guess the twist? Please stick a note in the comments to motivate me 😃

Hungry for more? You can read:

*   [2024's "Revenge Of The Mutant Algorithms](https://shkspr.mobi/blog/RevengeOfTheMutantAlgorithms)"
*   [2023's "Tales of the Algorithm](https://shkspr.mobi/blog/TalesOfTheAlgorithm)"
