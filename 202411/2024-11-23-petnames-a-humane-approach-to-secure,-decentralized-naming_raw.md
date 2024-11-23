Title: Petnames: A humane approach to secure, decentralized naming

URL Source: https://files.spritely.institute/papers/petnames.html

Markdown Content:
One system that is already very similar to a petnames system is a smartphone's contact list application. Contact list applications use phone numbers as a global namespace without making phone numbers the primary user experience. Human meaningful names are mapped to phone numbers with no pretense that the names have global experience; the names are chosen by each human operator according to what is useful to them.[2](https://files.spritely.institute/papers/petnames.html#fn.not-just-phone-numbers) The UI uses this mapping both to search and select entities from a contact list to display a name in an incoming call, or to review call history. The rendering it done in terms of a live mapping; should an entity's petname be updated, that petname will be retroactively updated on the call history.

So a smartphone contact list brings us reasonably far, but not quite far enough. Let's consider a scenario in which we can explore the rest of the pieces to complete this puzzle.

Alyssa receives a phone call from 1-324-555-8953. However, when she checks her phone to answer it, she does not see the phone number itself, she sees "Mom", which is the petname she has bound locally to the phone number.

![Image 15: incoming-call-mom.svg](https://files.spritely.institute/papers/imgs/petnames-pictures/incoming-call-mom.svg)

Alyssa answers the call and her mother, Dr. Nym, mentions that she's giving a special lecture on mathematics that she would like help organizing, and wonders if any of Alyssa's friends may be interested in attending or assisting. Alyssa offers to help and suggests that her long-time friend Ben Bitdiddle may be interested in both attending and helping.

Dr. Nym says goodbye to her daughter and hangs up the phone. She searches for "Ben" in her contact list:

![Image 16: search-interface.png](https://files.spritely.institute/papers/imgs/petnames-pictures/search-interface.png)

The "personal contacts" section shows ****petnames**** of people she knows, and "Ben Grossmeier" is a research colleague of Dr. Nym's. The "network contacts" shows ****edge names**** published by entities Dr. Nym has stored locally as[3](https://files.spritely.institute/papers/petnames.html#fn.sorting-in-petname-systems), [4](https://files.spritely.institute/papers/petnames.html#fn.how-are-edge-names-shared) petnames. Dr. Nym has stored her daughter as "Alyssa", and so when she sees "Alyssa ⇒ Ben Bitdiddle" ("Ben Bitdiddle" being the edge name supplied by Alyssa) she is confident this must be her daughter's friend. She clicks this entry and dials Ben.

Ben hears an incoming call and sees that the caller is labeled "Alyssa ⇒ Jane Nym" and in smaller text "Faculty ⇒ Dr. Nym".

![Image 17: incoming-call-edge-names.png](https://files.spritely.institute/papers/imgs/petnames-pictures/incoming-call-edge-names.png)

While Ben did not have Dr. Nym saved with a local petname, he has both Alyssa and the university's Faculty directory saved as local petnames, and from the both of those remembers that Alyssa's mother is named Jane Nym and that she is a professor on campus. Ben accepts the call and enthusiastically agrees to help Dr. Nym set up the event. Ben offers to coordinate food for the event, and Dr. Nym enthusiastically states that while she will place an order for pizza, she would not have time to pick it up beforehand, and so help there would be greatly appreciated.

Ben decides that since he is helping out that he should store Dr. Nym's contact information permanently in his address book. Ben checks the call history and sees that the first item says a call from "Alyssa ⇒ Jane Nym". He selects "Save Contact" from a menu.

On the edit screen that appears, a "local name" widget is immediately selected with a suggested entry of "Jane Nym" highlighted in such a way that if Ben were to begin typing he could override this text.

![Image 18: edit-contact.png](https://files.spritely.institute/papers/imgs/petnames-pictures/edit-contact.png)

Ben decides this name is good enough; since he knows Alyssa's mother on a personal basis through Alyssa, he is comfortable thinking about her as Jane Nym. Ben decides that he would also like to share this contact as an edge name with the rest of his contacts, and so presses the "share with contacts" button. Once again Ben is presented with an editable field with the name "Jane Nym" preselected, but Ben decides to edit this edge name to be called "Dr. Nym".

![Image 19: edit-contact-with-edgename.png](https://files.spritely.institute/papers/imgs/petnames-pictures/edit-contact-with-edgename.png) ![Image 20: edit-contact-with-edgename-dr-nym.png](https://files.spritely.institute/papers/imgs/petnames-pictures/edit-contact-with-edgename-dr-nym.png)

While Ben knows Dr. Nym on a first name basis in a personal context, Ben and Dr. Nym both work in an academic setting, and in such contexts he thinks it would be respectful for others to hear Dr. Nym referred to with her full title. Dr. Nym's phone number is already entered, and with the mapping established, Ben presses save.[5](https://files.spritely.institute/papers/petnames.html#fn.composite-values) Returning to the recent calls page, he sees that the contact list's display has been updated to saying simply "Jane Nym" for the most recent call.

Meanwhile Dr. Nym is wasting no time in placing the order for the pizzas for the event. She finds on her desk an advertisement for "Pizza Piano", a local pizza chain, which includes a QR code that she can scan.[6](https://files.spritely.institute/papers/petnames.html#fn.why-a-qr-code) The QR code only supplied the number to be called for the local restaurant, but Dr. Nym's phone supplies the identifier "bizdir ⇒ Pizza Piano East". "bizdir" is a business directory naming hub that Dr. Nym uses which independently verifies that local businesses are who they say they are. Dr. Nym is satisfied enough by this to be confident calling the establishment and paying for pizzas. She calls, pays, and tells the cashier who is taking the order that Ben will be the one picking up the pizzas and handling any additional details and supplies them with Ben's number.

Time passes, and just hours before the event Ben gets an incoming phone call from a number he has not saved as a petname and for which none of his contacts have provided a petname (including that Ben does not have the same business directory Dr. Nym does as a contact either). "Caller ID" does provide an ****proposed name**** of "Pizza Piano" for this context (though there is no guarantee that "caller ID" provides the same proposed name to others for this phone number), however since this is a contextual name and Ben's contact and phone applications do not want Ben to be confused, this renders as "Pizza Piano.2".

![Image 21: incoming-call-self-proclaimed-name.png](https://files.spritely.institute/papers/imgs/petnames-pictures/incoming-call-self-proclaimed-name.png)

"Pizza Piano" is the proposed name, but Ben has already had contact with one of the other Pizza Piano franchise locations, and so the system distinctively marks this one as entry 2. Ben's petname system will automatically increment this number until it exceeds 9, at which case any new encounters with a proposed name of "Pizza Piano" will simply render as "Pizza Piano…"

Ben answers the call; the pizza parlor employee merely wanted to let Ben know that they were all out of olives and wanted to know if another ingredient would be acceptable. Even though Ben is trusting that caller ID is correct, he can't imagine any reason why someone would be trying to phish him to authorize a topping change, so he suggests changing from olives to mushrooms. Now all that's left for Ben to do is pick up the pizzas!
