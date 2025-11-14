Title: Visual Effect - Interactive Effect Playground

URL Source: https://effect.kitlangton.com/

Published Time: Wed, 05 Nov 2025 19:56:50 GMT

Markdown Content:
Here are some interactive examples of TypeScript's beautiful [Effect](https://effect.website/) library. Tap the following effects to run, interrupt, or reset them.

CONSTRUCTORS
------------

Effect.succeed
--------------

Create an effect that always succeeds with a given value

value

const value = Effect.succeed(42)

Effect.fail
-----------

Create an effect that represents a recoverable error

error

const error = Effect.fail("Kaboom!")

Effect.die
----------

Create an effect that terminates with an unrecoverable defect

death

const death = Effect.die(new Error("FATAL: System corrupted"))

Effect.sync
-----------

Create an effect from a synchronous side-effectful computation

random

const random = Effect.sync(() => Math.random())

Effect.promise
--------------

Create an effect from an asynchronous computation guaranteed to succeed

london

function readTemperature(location) {

return Effect.promise(() =>

fetch(`slow.weather.com/api/${location}`)

.then(r => r.json())

)

}

const london = readTemperature("London")

Effect.sleep
------------

Create an effect that suspends execution for a given duration

sleep

const sleepEffect = Effect.gen(function* () {

yield* Effect.sleep("3 seconds");

return "Refreshed!";

});

CONCURRENCY
-----------

Effect.all
----------

Combine multiple effects into one, returning results based on input structure

nyc

berlin

tokyo

london

result

const nyc = readTemperature("New York")

const berlin = readTemperature("Berlin")

const tokyo = readTemperature("Tokyo")

const london = readTemperature("London")

const result = Effect.all([nyc, berlin, tokyo, london])

Effect.race
-----------

Race two effects and return the result of the first successful one

tortoise

achilles

winner

const tortoise = runFast("tortoise")

const achilles = runFast("achilles")

const winner = Effect.race(tortoise, achilles)

Effect.raceAll
--------------

Race multiple effects and return the first successful result

cat

dog

mouse

rabbit

winner

const cat = runFast("cat")

const dog = runFast("dog")

const mouse = runFast("mouse")

const rabbit = runFast("rabbit")

const winner = Effect.raceAll([cat, dog, mouse, rabbit])

Effect.forEach
--------------

Execute an effectful operation for each element in an iterable

newYork

london

tokyo

result

const locations = ["New York", "London", "Tokyo"];

const result = Effect.forEach(locations, getWeather);

ERROR HANDLING
--------------

Effect.all short circuit
------------------------

Stop execution on the first error encountered

balance

credit

payment

result

const balance = readAccountBalance();

const credit = checkCreditScore();

const payment = chargeCreditCard();

const result = Effect.all([balance, credit, payment]);

Effect.orElse
-------------

Try one effect, and if it fails, fall back to another effect

shoot

question

result

const shoot = shootFirst();

const question = askQuestions();

const result = Effect.orElse(shoot, () => question);

Effect.timeout
--------------

Add a time limit to an effect, failing with timeout if exceeded

pizza

result

const pizza = orderDelivery();

const result = Effect.timeout(pizza, "1 second");

Effect.eventually
-----------------

Run an effect repeatedly until it succeeds, ignoring errors

swipeCard

result

const swipeCard = swipeCard();

const result = Effect.eventually(swipeCard);

Effect.partition
----------------

Execute effects and partition results into successes and failures

iceCream

battery

popsicle

toad

lollipop

result

const result = Effect.partition(

[iceCream, battery, popsicle, toad, lollipop],

performLick

).pipe(

Effect.map(([fails, successes]) =>

`👹 ${fails.length} 😇 ${successes.length}`

)

);

Testing password: ThisIsWayTooLongForAnyReasonablePasswordManagerToHandle2024!

Effect.validate
---------------

Accumulate validation errors instead of short-circuiting

length

complexity

vibes

result

const length = checkLength(password);

const complexity = checkComplexity(password);

const vibes = checkVibes(password);

const result = length.pipe(

Effect.validate(complexity),

Effect.validate(vibes)

);

SCHEDULE
--------

Effect.repeat spaced
--------------------

Repeat an effect with a fixed delay between each execution

phone

checking

const phone = checkNotifications();

const checking = Effect.repeat(phone, Schedule.spaced("2 seconds"));

Effect.repeat whileOutput
-------------------------

Repeat while output matches a condition

hotdog

contest

const hotdog = eatHotdog()

const contest = Effect.repeat(hotdog,

Schedule.intersect(

Schedule.spaced("400 millis"),

Schedule.whileOutput(

Schedule.elapsed,

(elapsed) => Duration.lessThan(elapsed, Duration.seconds(10))

)

)

)

)

Effect.retry recurs
-------------------

Retry an effect a fixed number of times

wakeUp

result

const wakeUp = attemptToWakeUp();

const snoozeSchedule = Schedule.intersect(

Schedule.spaced("2 seconds"),

Schedule.recurs(4)

);

const result = Effect.retry(wakeUp, snoozeSchedule);

Effect.retry exponential
------------------------

Retry with exponential backoff

park

result

const park = attemptParallelPark();

const result = Effect.retry(park, Schedule.exponential("700 millis"));

REF
---

Ref.make
--------

Create a concurrency-safe mutable reference

counter

0

increment

repeat

const increment = (counter: Ref<number>) =>

Ref.updateAndGet(counter, n => n + 1)

const repeat = Effect.gen(function* () {

const counter = yield* Ref.make(0)

yield* Effect.repeat(increment(counter), Schedule.recurs(4))

})

Ref.updateAndGet
----------------

Update a ref and return the new value

counter

0

increment1

increment2

increment3

increment4

increment5

concurrent

const increment = (counter: Ref<number>) => Effect.gen(function* () {

yield* Effect.sleep(Duration.millis(Math.random() * 1000 + 500))

return yield* Ref.updateAndGet(counter, n => n + 1)

})

const concurrent = Effect.gen(function* () {

const counter = yield* Ref.make(0)

return yield* Effect.all(

Array.from({ length: 5 }, () => increment(counter)),

{ concurrency: "unbounded" }

)

})

SCOPE
-----

Effect.addFinalizer
-------------------

Register cleanup actions in a scope

effect

FINALIZERS

const effect = Effect.gen(function* () {

yield* Effect.addFinalizer(() => console.log("cleanup"))

return "Done"

}).pipe(Effect.scoped)

Effect.acquireRelease
---------------------

Acquire resources with guaranteed cleanup

database

cache

logger

result

FINALIZERS

const makeDatabase = Effect.acquireRelease(

connectDatabase(),

(db) => Effect.sync(() => db.close())

);

const makeCache = Effect.acquireRelease(

connectCache(),

(cache) => Effect.sync(() => cache.flush())

);

const makeLogger = Effect.acquireRelease(

openLogFile(),

(file) => Effect.sync(() => file.close())

);

const result = Effect.gen(function* () {

const db = yield* makeDatabase

const cache = yield* makeCache

const logger = yield* makeLogger

return yield* doWork(db, cache, logger)

})

.pipe(Effect.scoped)