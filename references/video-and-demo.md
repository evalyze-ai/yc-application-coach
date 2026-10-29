# Founder video and demo

## YC's rules for the founder video (ycombinator.com/video, checked October 28, 2026)

- "The video should be 1 minute long and should contain nothing except the founders talking." Accepted videos often run a little longer (see below), so treat a minute as the target.
- Every founder on camera. If you can't be in the same room, screen-record a video call. Record one joint call rather than splicing separate clips together.
- Not the place for a demo or promotional video; the demo has its own upload.
- Don't recite a written script. Use bullet points. YC says reading a script doesn't convey communication skills.
- Introduce yourselves and explain what you're doing and why. Anything else about the founders or the project is fine.
- The Fall 2026 form capture marks the video as required and says the file shouldn't exceed 100 MB.
- YC links these as successful application videos: Kernel (S25), Gumloop (W24), Medplum (S22), Whatnot (W20), Teespring (W13).

Paul Graham said when the video was introduced that it exists to show what the founders are like, not to pitch, and production values don't matter. That has stayed YC's position.

## What the coach produces: bullets, not a script

Never write sentences for founders to read. Give each founder 3 to 5 short bullets (a few words each) and the order of speakers.

Suggested shape, about a minute:
1. Names and roles, and who builds (about 10 seconds).
2. What you make and for whom, in the same words as the one-liner (about 15 seconds).
3. The strongest proof: users, revenue, a result, or why you saw this problem first (about 20 seconds).
4. Why this team: how long you've known each other and what you've shipped together (about 10 seconds).
5. Every founder speaks at least once.

With three or more founders, organize by segment and put a speaker name on each, so everyone speaks and nobody runs long. If the company has no one-liner yet, draft one from the founder's own words before writing the bullets, since segment 2 repeats it.

Example bullet cards (invented companies, for format only). Each line is a prompt for the founder, not a sentence to read.

**One founder**
> **Sam:** name, builds it alone / "invoice reconciliation for Shopify stores" / 9 years running finance ops at a 40-store retailer / 23 paying stores, $2.1K last month / why solo works now and the hiring plan

**Two founders**
> **Ines (CEO):** names + roles / "inspection reports for elevator contractors" / ran a 30-technician service crew, reports ate 2 hours a job
> **Kofi (CTO):** built the report app / 9 contractors pay, ~1,200 reports last month / met in a robotics lab in 2018, shipped 2 projects together

**Three founders** (organize by segment so nobody gets squeezed)
> **Segment 1, all three:** each says their own name and role, one line each, and who builds
> **Segment 2, Ben:** the one-liner / what a user does with it
> **Segment 3, Chloe:** strongest proof (a number with a date)
> **Segment 4, Ana, then Ben:** how you met, what you've shipped together

Two founders can share a segment. If a founder was missing from the last take, have them speak in the first 15 seconds of the next one.

**Four founders**
> Same as three: everyone introduces themselves in segment 1, then one segment each with a hard 10 to 15 seconds per person. Agree on the order before recording, and have the last speaker close on the team, not a slogan or a thank-you.

## What accepted videos look like (REPORTED)

One research guide measured 102 accepted application videos that companies made public on YC's directory (lengths measured October 28, 2026; not re-measured here): median 64 seconds, about two-thirds past a minute. Of 51 recorded from 2023 to 2026, 37 showed the founders side by side in one room, usually at home or in a plain office on a laptop or phone; 8 were recorded video calls with split screens; 5 showed one person; none used slides or music. The same guide transcribed four of YC's linked examples:

| Company | Length | When they say what they do | What else they cover |
|---|---|---|---|
| Kernel (S25) | 68 s | within about 12 seconds | why now, developer-first approach; no backgrounds or traction |
| Gumloop (W24) | 60 s | about 30 seconds in, after the problem and why now | founder backgrounds, first customers placing thousands of orders a month, why now |
| Medplum (S22) | 61 s | within about 10 seconds | founders had built this kind of system before, a named customer, why now |
| Whatnot (W20) | 79 s | within about 13 seconds | founder backgrounds tied to the market, the starting category, early hires |

All four open with names, none shows the product, three show founder-market fit and three give a reason why now. So treat one minute as a target, not a cliff, and spend the time sounding like people a partner would want to meet rather than repeating the written answers.

## Practical notes

- A quiet room and clear audio matter more than lighting, cameras or editing. A laptop or phone is fine. Hardware teams are tempted to film next to the machine; noise and distraction usually make that worse, so show the product in the demo instead.
- Talk to each other or to the camera like explaining it to a smart friend. Let personality show.
- Record a handful of takes and keep the one where you sound most like yourselves. Dozens of takes make people look tired; a small stumble with real energy reads better than a perfect, flat delivery.
- Don't add music, slides, B-roll, jokes or skits. Paul Graham once said gags hurt because readers are already working to understand you.
- Awkward or introverted is fine. Reviewers usually see founders more positively than founders see themselves.
- Treat one minute as the target. YC's own example videos run roughly a minute, some a bit longer.
- Match the application: same product description, same numbers.

## Recording checklist

- Every founder in frame and audible. Test with a 10-second clip and listen back with headphones.
- A quiet room, light on faces (a window in front of you, not behind), camera at eye level.
- Bullet card off camera or beside the lens, never a script on the screen.
- Same one-liner wording as the application, and the same numbers.
- Check the file against the upload limit on your form (the Fall 2026 form said 100 MB). A minute of phone video is often under that, but high-resolution settings can push it over; export at 1080p or lower if needed.
- Watch the final take once all the way through before uploading.

## Reviewing a recorded take from its transcript

1. Ask for the transcript with a name at the start of each turn ("Ines: ..."). Phones, Zoom and Meet can usually produce one; a Zoom or Meet .vtt export works as is. Confirm who the founders on the application are, since a missing founder won't show up in the transcript.
2. Run `scripts/video_check.py` if you can run code, listing every founder on the application, including anyone missing from this take:
   `python scripts/video_check.py take3.txt --founders "Ines,Kofi,Lena" --one-liner "Inspection reports for elevator contractors"`
   It reports words spoken, estimated length at 130, 150 and 170 words a minute, words per founder, and where the one-liner gets said. Then it sorts flags into two groups. Retake for these: a founder who doesn't speak, well over a minute, or sounding read (expanded forms like "we are" with no contractions, plus written-sounding words or pitch lines). Fix if retaking anyway: one founder dominating relative to team size, a founder barely heard, no sentence saying the one-liner, saying it late, no proof number, vague proof ("strong engagement"), market-size figures, written-sounding words, pitch lines with their timing, sign-offs, demo talk, and long sentences (only when a person punctuated the transcript).
3. Without code, check the same list by hand. About 150 to 170 words is roughly a minute of natural speech.
4. Read for truth too: anything described in the present tense on camera must be live, and numbers must match the application.
5. Ask the founders what the transcript can't show: can you hear everyone, are faces visible and lit, does it sound like you talking to a friend.
6. Report in the chat reply: answers to their direct questions first, then estimated length, who spoke how much, the flags, the top three fixes, and whether to retake. Recommend a retake only for something material. When you do, give talking-point bullets for the next take. A small stumble with real energy is fine.

## Common video mistakes

- Reading a script, including an AI-written one. Some paid services sell video script templates; that runs straight into YC's rule.
- One founder doing all the talking while the others nod.
- Opening with the problem's history or a market statistic instead of names and what you make.
- Repeating the written application word for word.
- Demo footage, slides, music, B-roll or a skit.
- Dozens of takes. Tyler Maran (OmniAI, W24) reported about 50 takes; Anh Nguyen (PlateTale) said the video that got them an interview took five minutes to film. A handful is plenty. REPORTED.

## The demo

The Fall 2026 form: "If you have a demo, attach it below. Anything that shows us how the product works. Please limit to 3 minutes / 100 MB." Then a product link and an optional login credentials field.

**Always include one.** YC's own application tip video on demos says partners wish more founders included one, that unpolished is fine (even something running locally, or a CSV output), and that going from nothing to something makes a big difference. Founders who were rejected and later accepted have listed a missing demo among the fixes.

**Shot list**
1. Open inside the product, already at the point of value. Skip splash screens, logins and slides.
2. Do the core job once, start to finish, as a real user would.
3. Show the output or result.
4. Optional: one line on who uses it today.
5. Narrate plainly; say what's real and what's a mockup. Disclose manual steps happening behind the scenes.

**Length.** Under two minutes is a safe default, inside the 3-minute limit. Get to the point within the first several seconds.

**Product link.** Give working credentials with sample data loaded, so a partner who clicks sees the product doing something, not an empty dashboard. Test logged out in a private window.

**Hardware.** Show the device working on video; in the interview, have it on camera.

**Honesty.** Never present a mockup, a hand-run process or a staged result as a working product. If something is simulated, label it.

**Demo stories founders tell (REPORTED).** Max Prilutskiy lists the demo he skipped as one reason his first Lingo.dev application was rejected. Lennert Jansen (Airweave) says they applied with a very ugly prototype frontend and didn't wait for polish. Hendrik Van Hove shared a message from partner Pete Koomen saying their application looked quickly written and asking for a demo; they built one in a scramble and were rejected a few days later, which is a reason to have it ready before submitting. Paul Graham said in 2009 that if a demo doesn't get to the point in about 10 seconds, readers move on. One published Winter 2027 demo ran 26 seconds.

