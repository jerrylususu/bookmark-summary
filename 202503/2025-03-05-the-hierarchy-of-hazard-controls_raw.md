Title: The Hierarchy of Hazard Controls

URL Source: https://www.hillelwayne.com/post/hoc/

Published Time: 2025-03-04T00:00:00Z

Markdown Content:
The other day a mechanical engineer introduced me to the Hierarchy of Controls (HoC), an important concept in [workplace safety](https://en.wikipedia.org/wiki/Process_safety). [1](https://www.hillelwayne.com/post/hoc/#fn:hohc)

![Image 1](https://www.hillelwayne.com/post/hoc/img/hoc.svg)

[(source)](https://en.wikipedia.org/wiki/Hierarchy_of_hazard_controls)

To protect people from hazards, system designers should seek to use the most effective controls available. This means elimination over substitution, substitution over engineering controls, etc.

Can we use the Hierarchy of Controls in software engineering? Software environments are different than physical environments, but maybe there are some ideas worth extracting. Let’s go through the exercise of applying HoC to an example problem: a production outage I caused as junior developer.

### The problem

About ten years ago I was trying to debug an issue in production. I had an SSHed production shell and a local developer shell side by side, tabbed into the wrong one, and ran the wrong query.

That’s when I got a new lesson: how to restore a production database from backup.

In process safety, the hazard is whatever makes an injury possible: a ladder makes falls possible, a hydraulic press makes crushed fingers possible. In my case, the hazard might have been a production shell with unrestricted privileges, which made losing production data possible. The _specific_ injuries include both dropping the database directly (like I did) or running a delete query on the database. I’ll use both injuries to discuss different kinds of hazard controls.

### First, some caveats

The HoC was designed to protect people from machines, not machines from people! I found most of the concepts translate pretty well, but I ran into some issues with PPE.

There’s also lots of room to quibble over whether something is one category or the other. As part of writing this, I’m also trying to figure out the qualitative differences between the categories. This is my own interpretation as a total beginner.

Finally, the HoC is concerned with prevention of injury, not recovery from injury. Software best practices like “make regular database backups” and “have a postmortem after incidents” don’t fit into the hierarchy.

All quotes come from the [OSHA HoC worksheet](https://www.osha.gov/sites/default/files/Hierarchy_of_Controls_02.01.23_form_508_2.pdf).

### Elimination

> Elimination makes sure the hazard **no longer exists**.

Elimination is the most direct way to prevent an accident: don’t have the hazard. All the various OSHA materials use the same example: if you want to reduce falling injuries, stop making workers do work at heights. In our case, we could eliminate the production environment or we could eliminate the database.

Neither is exactly practical, and most HoC resources are quick to point out that proper elimination often isn’t possible. We work with hazardous materials because they are essential to our process. “Elimination” seems most useful as a check of “is this dangerous thing really _necessary_?” Essential hazards cannot be eliminated, but inessential hazards can. Before it was decommissioned in 2020, Adobe Flash was one of the biggest sources of security exploits. The easiest way to protect yourself? Uninstall Flash.

### Substitution

> Substitution means changing out a **material** or **process** to reduce the hazard.

Unlike elimination, substitution keeps the hazard but reduces how dangerous it is. If the hazard is toxic pesticides, we can use a lower-toxicity pesticide. If it’s a noisy machine, we can replace it with a quieter machine. If the hazard is a memory unsafe language, we use Rust.

For our problem I can see a couple of possible substitutions. We can substitute the production shell for a weaker shell. Consider if one “production” server could only see a read replica of the database. Delete queries would do nothing and even dropping the database wouldn’t lose data. Alternatively, we could use an immutable record system, like an [event source](https://martinfowler.com/eaaDev/EventSourcing.html) model. Then “deleting data” takes the form of “adding deletion records to the database”. Accidental deletions are trivially reversible by adding more “undelete” records on top of them.

### Engineering Controls

> Engineering controls reduce exposure by **preventing hazards from coming into contact with workers.** They still allow workers to do their jobs, though.

Engineering controls maintain the same danger of the hazard but use additional _physical_ designs to mitigate the risk and severity of accidents. We can do this in a lot of ways: we can reduce the need for workers to expose themselves to a hazard, make it less likely for a hazard to trigger an accident, or make accidents less likely to cause injury.

![Image 2](https://www.hillelwayne.com/post/hoc/img/sawstop.gif)

SawStop™ [(source)](https://imgur.com/human-analog-hot-dog-Q1RiVF2)

There is a lot more room for creativity in engineering controls than in elimination or substitution. Some ideas for engineering controls:

*   With better monitoring and observability, I might not need to log into production in the first place.
*   With better permissions policies, I could forbid the environment from dropping the database or require a special developer key to take this action.
*   Or maybe junior engineers shouldn’t have access to production environments at all. If I want to debug something, I must ask someone more experienced to do it.
*   [Autologouts](https://superuser.com/questions/1668679/how-to-set-bash-auto-logout-expiration-in-ubuntu-20-04) could keep me from having an idle production terminal just lying around, waiting to be accidentally alt-tabbed into.

Some engineering controls are more effective than others. A famously “weak” control is a confirmation box:

```
$ ./drop_db.sh

This will drop database `production`.
To confirm, type y: [y/N]
```

The problem with this is that if I run this a lot in my local environment, I’ll build up the muscle memory to press `y`, which will ruin my day when I do the same thing in prod.

A famously “strong” control is the “full name” confirmation box:[2](https://www.hillelwayne.com/post/hoc/#fn:full-name)

```
$ ./drop_db.sh

This will drop database `production`.
To confirm, type `production`:
```

Even if I have muscle memory, it’d be muscle memory to type `local`, which would block the action. You can see a real example of this if you try to delete a repo on Github:

![Image 3](https://www.hillelwayne.com/post/hoc/img/delete_type_name.png)

Some of OSHA’s examples of engineering controls look like substitutions to me, and vice versa. My heuristic for the distinction is that _engineering controls can fail, substitutions cannot._ What if permissions are misconfigured and they don’t actually prevent me from deleting the database? Whereas if the environment is only exposed to a read replica, I can’t magically destroy the write replica. I hope.

This is an imperfect heuristic, though! Swapping C for Rust would be a substitution, even though some of Rust’s guarantees are bypassable with `unsafe`.

### Administrative Controls

> Administrative controls **change the way work is done** or **give workers more information by providing workers** with relevant procedures, training, or warnings.

Engineering controls change the technology, administrative controls change the people. Controls that change how people interact with the technology could be in either category; I got into a long discussion over whether “full name” confirmation boxes are an administrative or engineering control. You could reasonably argue it either way.

Some ideas for administrative controls:

*   A company policy that juniors should not connect to prod
*   Showing us training videos about how easy it is to drop a database
*   Having only one terminal open at a time
*   Requiring that you can only connect to prod if you’re pairing with another developer
*   Reducing hours and crunch time [so engineers are less sleep-deprived](https://increment.com/teams/the-epistemology-of-software-quality/)
*   Regularly wargaming operational problems.

OSHA further classifies “automated warnings” as a kind of administrative control. That would be something like “logging into production posts a message to Slack”.

On the hierarchy, administrative controls are lower than engineering controls for a couple of reasons. One, engineering controls are embedded in the system, while administrative controls are social. Everybody needs to be trained to follow them. Second, in all of the HoC examples I’ve seen, it takes effort to _break_ the engineering control, while it takes effort to _follow_ the administrative control. You might not follow them if you are rushed, forgetful, inattentive, etc.

Some administrative controls can be lifted into engineering controls. A company policy that junior engineers should never SSH into prod is an administrative control, and relies on everybody following the rules. A setup where juniors don’t have the appropriate SSH keys is an engineering control.

### Personal Protective Equipment

> Personal protective equipment (PPE) includes clothing and devices to protect workers.

This is the lowest level of control: provide equipment to people to protect them from the hazard. PPE can reduce the risk of injury (I am less likely to be run over by a forklift if I am wearing a reflective vest) or the severity (a hard hat doesn’t prevent objects from falling on me, but it cushions the impact).

I think PPE is the least applicable control in software. First of all, HoC is meant to protect humans, while in software we want to protect systems. So is software PPE worn by people to prevent damage _to_ systems, or worn by systems to prevent damage _from_ people? An example of “human PPE” could be to use red background for production terminals and a blue background for development terminals. All the examples of “system PPE” I can come up with arguably count as engineering controls.

Second, PPE isn’t an engineering control because engineering controls modify hazards, while PPE is a third entity between people and the hazard. But anything between a person and the software is _also_ software! Even something like “use Postman instead of `curl`” is more a mix of engineering/admin than “true” PPE.

I can think of two places where PPE makes more sense. The first is security, where PPE includes things like secure browsers, 2FA, and password managers are all kinds of PPE. The second is PPE for reducing common software developer injuries, like carpal tunnel, back pain, and eyestrain. These places “work” because they involve people being injured, which was what the HoC was designed for in the first place.

PPE comes lower in the hierarchy than administrative controls because employees need discipline and training to use PPE effectively. In the real world, PPE is often bulky and uncomfortable, and 90% of the time isn’t actually protecting you (because you’re not in danger). [One paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC7809954/) on construction accidents found that injured workers were not wearing PPE in 65% of the studied accidents. To maximize the benefit of PPE you need to train people and enforce use, and that means already having administrative controls in place.

Misc Notes on HoC
-----------------

### Controls are meant to be combined

Higher tiers of controls do more to eliminate danger, but are harder to implement. Lower tiers are less effective, but more versatile and cheaper to implement.

### Software is fundamentally good at engineering controls

I’m still working out _exactly_ what this thought is, but: in the real world, people interact with hazards through “natural interfaces”, basically as an object situated in space. If I’m working with a hydraulic press, _by default_ I can put my hand in there. We need to add additional physical entities to the system to _prevent_ the injury, or train people on how to use the physical entity properly.

In software, all interfaces are constructed and artificial: hazards come from us _adding_ capabilities to do harm. It’s easier for us to construct the interface in a different way that diminishes the capacity for injury, or in a way that enforces the administrative control as a constraint.

This came up once at a previous job. Our usage patterns meant that it was safest to deploy new versions off-peak hours. “Only deploy off-peak” is an administrative control. So we added a line to the deploy script that checked when it was being run and threw an error if it during peak times. That’s turning an administrative control into an engineering one.[3](https://www.hillelwayne.com/post/hoc/#fn:script)

Also, real world engineering controls are _expensive_, which is a big reason to choose administrative controls and PPE. But [software can be modified much more quickly and cheaply than physical systems can](https://www.hillelwayne.com/post/we-are-not-special/), which makes engineering controls more effective.

(I think there’s a similar argument for substitutions, too.)

### Controls can be the source of hazards

If you looked at the [OSHA worksheet](https://www.osha.gov/sites/default/files/Hierarchy_of_Controls_02.01.23_form_508_2.pdf) I linked above, you’d see an interesting section here:

![Image 4](https://www.hillelwayne.com/post/hoc/img/worksheet_new_hazards.png)

[(source)](https://www.osha.gov/sites/default/files/Hierarchy_of_Controls_02.01.23_form_508_2.pdf)

Any possible control method can potentially introduce new risks into the workplace. Lots of administrative alarms cause alarm fatigue, so people miss the critical alerts. Forbidding personnel from entering a warehouse might force them to detour through a different hazard. Reflective vests can be caught on machinery. The safety of the whole system must be considered holistically: local improvements in safety can cause problems elsewhere.

We see this in software too. Lorin Hochstein [has a talk](https://www.usenix.org/conference/srecon18americas/presentation/hochstein) on how lots of Netflix outages were caused by software meant to protect the system.

How could my controls add new hazards?

*   Substituting an append-only database could require significant retraining and software changes, introducing more space for mistakes and new bugs
*   Strict access policies could slow me down while trying to fix an ongoing problem, making that problem more severe
*   Too many administrative controls could make people “go through the motions” on autopilot instead of being alert to possible danger.

I find that it’s harder to identify new hazards that _could be_ caused by controls than it is to identify existing hazards.

* * *

That’s HoC in a nutshell. I think it’s a good idea!

_If you liked this post, come join my [newsletter](https://buttondown.email/hillelwayne/)! I write new essays there every week._

_I train companies in formal methods, making software development faster, cheaper, and safer. Learn more [here](https://www.hillelwayne.com/consulting/)._
