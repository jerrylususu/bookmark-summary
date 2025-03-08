Title: Every Line Is a Potential Bug

URL Source: https://www.teamten.com/lawrence/writings/every_line_is_a_potential_bug.html

Markdown Content:
September 19, 2009

Last summer I wrote some code to get a message out of a hash table. The message was going to be put there by another thread. There was a small chance of a race where it wouldn’t be there yet when I initially looked for it. The code looked something like this:

```
while((message=map.get(key))==null&&System.currentTimeMillis()<timeoutTime){
wait(1000);
}
```

The `wait()` call blocks the thread, waiting for the `notifyAll()` from the thread that puts the message into the map. The 1000 means one second. The timeout was going to be on the order of five seconds.

The above code is simple and correct. It’ll just keep looping until the value comes in or until it has timed out. The timeout may go over by up to one second, but that’s not a problem in this case. (Or rather, by the time that happens, you’ve got more serious problems.)

The code was reviewed by two other people. Both complained that the `wait()` should wait for the time between now and the timeout, not just one second. They argued that my code wakes up the thread five times unnecessarily. I replied that the key was very likely to be there within the first second, and that waking up a thread is not very expensive. I argued that their proposed code was more complex, and therefore more likely to have bugs.

They both said, “_One subtraction is not complex!_”, went back to their desks, and emailed me their modified versions, just to prove how simple it could be. Both introduced a bug. One person’s bug was straightforward: he used the wrong constant for the calculation. But the second person’s bug was subtle:

```
while((message=map.get(key))==null&&System.currentTimeMillis()<timeoutTime){
wait(timeoutTime-System.currentTimeMillis());
}
```

There’s a small chance that the current time will have advanced by the time the subtraction is done, resulting in a negative value passed to `wait()` and an `IllegalArgumentException` getting thrown. In order to save the computer one rare thread switch, he introduced a bug that would have occasionally and mysteriously caused operations to fail.

(Update 3-15-2010: Ajit Mandalay pointed out another bad scenario: the subtraction yields 0, which means “infinity”, and the loop potentially never exits.)

Every line of code you write is a potential bug. Do not write any line of code unless you absolutely need it _right now_ and your program will suffer for the lack of it. Do not write routines speculatively. Do not write abstraction layers you don’t need right now. If an optimization will add any complexity whatsoever, even a subtraction, resist it. You will be sorry in five years when your code is riddled with potentially-buggy code that you never really needed to write.

[~ See all writings ~](https://www.teamten.com/lawrence/writings/)
