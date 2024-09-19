Title: Things I’ve learned serving on the board of the Python Software Foundation

URL Source: https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/

Markdown Content:
18th September 2024

Two years ago [I was elected](https://simonwillison.net/2022/Jul/30/psf-board/) to the board of directors for the [Python Software Foundation](https://www.python.org/psf-landing/)—the PSF. I recently returned from the annual PSF board retreat (this one was in Lisbon, Portugal) and this feels like a good opportunity to write up some of the things I’ve learned along the way.

*   [What is the PSF?](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#what-is-the-psf)
*   [The PSF employs staff](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#the-psf-employs-staff)
*   [A lot of this is about money](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#a-lot-of-this-is-about-money)
*   [The PSF does not directly develop Python itself](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#the-psf-does-not-directly-develop-python-itself)
*   [PyPI—the Python Package Index](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#pypi-the-python-package-index)
*   [PyCon is a key commitment](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#pycon-is-a-key-commitment)
*   [Other PSF activities](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#other-psf-activities)
*   [Work Groups](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#work-groups)
*   [Acting as a fiscal sponsor](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#acting-as-a-fiscal-sponsor)
*   [Life as a board member](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#life-as-a-board-member)
*   [The kinds of things the board talks about](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#the-kinds-of-things-the-board-talks-about)
*   [Want to know more?](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#want-to-know-more-)

#### What is the PSF? [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#what-is-the-psf)

The PSF is a [US 501(c)(3)](https://en.wikipedia.org/wiki/501/(c/)/(3/)_organization) non-profit organization with the following [mission](https://www.python.org/psf/mission/):

> The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers.

That mission definition is _really important_. Board members and paid staff come and go, but the mission remains constant—it’s the single most critical resource to help make decisions about whether the PSF should be investing time, money and effort into an activity or not.

The board’s 501(c)(3) status is predicated on following the [full expanded mission statement](https://www.python.org/psf/mission/). When our finances get audited (we conduct an annual “friendly audit”, which is considered best practice for organizations at our size), the auditors need to be able to confirm that we’ve been supporting that mission through our management of the tax-exempt funds that have been entrusted to us.

This auditability is an interesting aspect of how 501(c)(3) organizations work, because it means you can donate funds to them and know that the IRS will ostensibly be ensuring that the money is spent in a way that supports their stated mission.

Board members have fiduciary responsibility for the PSF. A good explanation of this can be found [here on BoardSource](https://boardsource.org/resources/fiduciary-responsibilities/), which also has other useful resources for understanding [the roles and responsibilities](https://boardsource.org/fundamental-topics-of-nonprofit-board-service/roles-responsibilities/) of non-profit board members.

(Developing at least a loose intuition for US tax law around non-profits is one of the many surprising things that are necessary to be an effective board member.)

#### The PSF employs staff [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#the-psf-employs-staff)

The PSF currently employs [12 full-time staff members](https://www.python.org/psf/records/staff/). Members of the board do not directly manage the activities of the staff—in fact board members telling staff what to do is highly inappropriate.

Instead, the board is responsible for hiring an Executive Director—currently Deb Nicholson—who is then responsible for hiring and managing (directly on indirectly) those other staff members. The board is responsible for evaluating the Executive Director’s performance.

I joined the board shortly after Deb was hired, so I have not personally been part of a board hiring committee for a new Executive Director.

While paid staff support and enact many of the activities of the PSF, the foundation is fundamentally a volunteer-based organization. Many PSF activities are carried out by [these volunteers](https://www.python.org/psf/volunteer/), in particular via [Work Groups](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#work-groups).

#### A lot of this is about money [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#a-lot-of-this-is-about-money)

A grossly simplified way to think about the PSF is that it’s a bucket of money that is raised from [sponsors](https://www.python.org/psf/sponsors/) and the Python community (via donations and membership fees), and then spent to support the community and the language in different ways.

The PSF spends money on staff, on grants to Python-related causes and on infrastructure and activities that support Python development and the Python community itself.

You can see how that money has been spent in the [2023 Annual Impact Report](https://www.python.org/psf/annual-report/2023/). The PSF had $4,356,000 revenue for that year and spent $4,508,000—running a small loss, but not a concerning one given our assets from previous years.

The most significant categories of expenditure in 2023 were PyCon US ($1,800,000), our Grants program ($677,000), Infrastructure (including PyPI) ($286,000) and our Fiscal Sponsorees ($204,000)—I’ll describe these in more detail below.

#### The PSF does not directly develop Python itself [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#the-psf-does-not-directly-develop-python-itself)

This is an important detail to understand. The PSF is responsible for protecting and supporting the Python language and community, but development of [CPython](https://github.com/python/cpython) itself is not directly managed by the PSF.

Python development is handled by the [Python core team](https://devguide.python.org/core-developers/developer-log/), who are governed by the 5-person [Python Steering Council](https://github.com/python/steering-council/blob/main/README.md). The Steering Council is elected by the core team. The process for becoming a core developer [is described here](https://devguide.python.org/core-developers/become-core-developer/).

How this all works is defined by [PEP 13: Python Language Governance](https://peps.python.org/pep-0013/) (and several subsequent PEPs). This structure was created—with much discussion—after Guido van Rossum stepped down from his role as Python BDFL in 2018.

The PSF’s executive director maintains close ties with the steering council, meeting with them 2-3 times a month. The PSF provides financial support for some Python core activities, such as infrastructure used for Python development and sponsoring travel to and logistics for core Python sprints.

More recently, the PSF has started employing Developers in Residence to directly support the work of both the core Python team and initiatives such as the Python Package Index.

#### PyPI—the Python Package Index [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#pypi-the-python-package-index)

One of the most consequential projects directly managed by the PSF is [PyPI](https://pypi.org/), the Python Package Index. This is the system that enables `pip install name-of-package` to do its thing.

Having PyPI managed by a non-profit that answers directly to the community it serves is a very good thing.

PyPI’s numbers are staggering. Today there are 570,000 projects consisting of 12,035,133 files, serving 1.9 billion downloads a day (that number from [PyPI Stats](https://pypistats.org/packages/__all__)). Bandwidth for these downloads is donated by [Fastly](https://www.fastly.com/), a PSF Visionary Sponsor who recently signed [a five year agreement](https://fosstodon.org/@ThePSF/112456715341751673) to continue this service.

(This was a big deal—prior to that agreement there was concern over what would happen if Fastly ever decided to end that sponsorship.)

#### PyCon is a key commitment [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#pycon-is-a-key-commitment)

The annual US Python Conference—[PyCon US](https://us.pycon.org/)—is a big part of the PSF’s annual activities and operations. With over 3,000 attendees each year (and a $1.8m budget for 2023) running that conference represents a full-time job for several PSF staff members.

In the past PyCon US has also been responsible for the majority of the PSF’s operating income. This is no longer true today—in fact it ran at a slight loss this year. This is not a big problem: the PSF’s funding has diversified, and the importance of PyCon US to the Python community is such that the PSF is happy to lose money running the event if necessary.

#### Other PSF activities [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#other-psf-activities)

Many of these are detailed in [the full mission statement](https://www.python.org/psf/mission/).

*   Operating [python.org](https://www.python.org/) and making Python available to download. It’s interesting to note that Python is distributed through many alternative routes that are not managed by the PSF—through Linux packaging systems like Ubuntu, Debian and Red Hat, via tools like Docker or Homebrew, by companies such as [Anaconda](https://www.anaconda.com/download) or through newer channels such as [uv](https://docs.astral.sh/uv/guides/install-python/).
*   Owning and protecting the Python trademarks and the Python intellectual property rights under the ([OSI compliant](https://opensource.org/license/python-2-0)) Python license. This is one of the fundamental reasons for the organization to exist, but thankfully is one of the smaller commitments in terms of cost and staff time.
*   Running the annual PyCon US conference.
*   Operating the Python Packaging Index. Fastly provide the CDN, but the PSF still takes on the task of developing and operating the core PyPI web application and the large amounts of moderation and user support that entails.
*   Supporting infrastructure used for core Python development, and logistics for core Python sprints.
*   Issuing grants to Python community efforts.
*   Caring for fiscal sponsorees.
*   Supporting the work of PSF Work Groups.

#### Work Groups [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#work-groups)

A number of PSF initiatives take place in the form of Work Groups, [listed here](https://www.python.org/psf/workgroups/). Work Groups are teams of volunteers from the community who collaborate on projects relevant to the PSF’s mission.

Each Work Group sets its own cadence and ways of working. Some groups have decisions delegated to them by the board—for example the Grants Work Group for reviewing grant proposals and the Code of Conduct Work Group for enforcing Code of Conduct activity. Others coordinate technical projects such as the [Infrastructure Working Group](https://wiki.python.org/psf/InfrastructureWG), who manage and make decisions on various pieces of technical infrastructure relevant to Python and the PSF.

Work Groups are formed by a board vote, with a designated charter. Most recently the board approved [a charter](https://github.com/psf/user-success-wg/blob/main/WG-charter.md) for a new User Success Work Group, focusing on things like improving the new Python user onboarding experience.

This is another term I was unfamiliar with before joining the board: the idea of a **fiscal sponsor**, which is a key role played by the PSF.

Running a non-profit organization is decidedly not-trivial: you need a legal structure, a bank account, accounting, governance, the ability to handle audits—there’s a whole lot of complexity behind the scenes.

Looking to run an annual community conference? You’ll need a bank account, and an entity that can sign agreements with venues and vendors.

Want to accept donations to support work you are doing? Again, you need an entity, and a bank account, and some form of legal structure that ensures your donors can confidently trust you with their money.

Instead of forming a whole new non-profit for this, you can instead find an existing non-profit that is willing to be your “fiscal sponsor”. They’ll handle the accounting and various other legal aspects, which allows you to invest your efforts in the distinctive work that you are trying to do.

The PSF acts as a fiscal sponsor for a number of different organizations—20 as-of the 2023 report—including PyLadies, Twisted, Pallets, Jazzband, PyCascades and North Bay Python, The PSF’s accounting team invest a great deal of effort in making all of this work.

The PSF generally takes a 10% cut of donations to its fiscal sponsorees. This doesn’t actually cover the full staffing cost of servicing these organizations, but this all still makes financial sense in terms of the PSF’s mission to support the global Python community.

#### Life as a board member [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#life-as-a-board-member)

There are 12 board members. Elections are held every year after PyCon US, voted on by the PSF membership—by both paid members and members who have earned voting rights through being acknowledged as PSF fellows.

Board members are elected for three year terms. Since 1-3 new board members are likely to join annually, these terms ensure there is overlap which helps maintain institutional knowledge about how the board operates.

The board’s activities are governed by [the PSF Bylaws](https://www.python.org/psf/bylaws/), and there is a documented process for modifying them (see ARTICLE XI).

We have board members from all over the world. This is extremely important, because the PSF is responsible for the health and growth of the global Python community. A perennial concern is how to ensure that board candidates are nominated from around the world, in order to maintain that critical global focus.

The board meets once a month over Zoom, has ongoing conversations via Slack and meets in-person twice a year: once at PyCon US and once at a “retreat” in a different global city, selected to try and minimize the total amount of travel needed to get all of our global board members together in the same place.

Our most recent retreat was in Lisbon, Portugal. The retreat before that was in Malmö in Sweden.

I considered using an analogy that describes each board member as 1/12th of the “brain” of the PSF, but that doesn’t hold up: the paid, full-time staff of the PSF make an enormous number of decisions that impact how the PSF works.

Instead, the board acts to set strategy, represent the global community and help ensure that the PSF’s activities are staying true to that mission. Like I said earlier, the mission definition really is _critical_. I admit that in the past I’ve been a bit cynical about the importance of mission statements: being a board member of a 501(c)(3) non-profit has entirely cured me of that skepticism!

Board members can also sit on board committees, of which there are currently four: the Executive Committee, Finance Committee, PyCon US Committee and Membership Committee. These mainly exist so that relevant decisions can be delegated to them, helping reduce the topics that must be considered by the full board in our monthly meetings.

#### The kinds of things the board talks about [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#the-kinds-of-things-the-board-talks-about)

Our Lisbon retreat involved two full 9-hour days of discussion, plus social breakfasts, lunches and dinners. It was an _intense_ workload.

I won’t even attempt to do it justice here, but I’ll use a couple of topics to illustrate the kind of things we think about on the board.

The first is our **grants strategy**. The PSF financially sponsors Python community events around the world. In the past this grants program has suffered from low visibility and, to simplify, we’ve felt that we weren’t giving away enough money.

Over the past year we’ve fixed that: board outreach around the grants program and initiatives such as grants office hours have put our grants program in a much healthier position... but potentially _too_ healthy.

We took steps to improve that visibily and streamline that process, and they worked! This gives us a new problem: we now have no shortage of applicants, so we need to figure out how to stick within a budget that won’t harm the financial sustaianibility of the PSF itself.

Does this mean we say no to more events? Should we instead reduce the size of our grants? Can we take other initiatives, like more actively helping events find alternative forms of sponsorship?

Grants shouldn’t just be about events—but if we’re making grants to other initiatives that support the Python community how can we fairly select those, manage the budget allocated to supporting them and maximize the value the Python community gets from the money managed by the PSF?

A much larger topic for the retreat was **strategic planning**. What should our the goals be for the PSF that can’t be achieved over a short period of time? Projects and initiatives that might require a one-year, three-year or five-year margin of planning.

Director terms only last three years (though board members can and frequently do stand for re-election), so having these long-term goals planned and documented in detail is crucial.

A five-year plan is not something that can be put together over two days of work, but the in-person meeting is a fantastic opportunity to kick things off and ensure each board member gets to participate in shaping that process.

#### Want to know more? [#](https://simonwillison.net/2024/Sep/18/board-of-the-python-software-foundation/#want-to-know-more-)

The above is by no means a comprehensive manual to the PSF, but it’s a good representation of the things I would have found most valuable to understand when I first got involved with the organization.

For a broader set of perspectives on how the board works and what it does, I recommend the [FAQs about the PSF Board](https://www.youtube.com/watch?v=kD6cPBfR4A4) video on YouTube.

If you’re interested in helping the PSF achieve its mission, we would love to have you involved:

*   Encourage your company to sponsor the PSF directly, or to sponsor Python events worldwide
*   Volunteer at PyCon US or help with other suitable PSF initiatives
*   Join a Work Group that’s addressing problems you want to help solve
*   Run your own event and [apply for a grant](https://www.python.org/psf/grants/)
*   Join the PSF as a voting member and vote in our elections
*   Run for the board elections yourself!

We’re always interested in hearing from our community. We host public office hours on the PSF Discord every month, at different times of day to to cater for people in different timezones—here’s [the full calendar of upcoming office hours](https://pyfound.blogspot.com/2024/08/ask-questions-or-tell-us-what-you-think.html).
