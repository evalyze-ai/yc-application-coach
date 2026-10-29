# Question playbook

Every recurring YC application question, in form order: what it tests, what works, real examples, what to avoid, and a starting template.

How to use this file: read the section for the question you're working on. Templates are scaffolding for getting facts onto the page. Rewrite every filled-in template in the founder's own words, because a template answer that reads like everyone else's defeats the point.

Source notes. Question wording follows a public capture of the Fall 2026 form (github.com/withkynam/YC-application-tentative, captured July 23, 2026), a founder-published Summer 2024 application (Clearly AI, choigreene.com/guides/our-yc-application) and Metorial's published Summer and Fall 2025 applications. Examples are paraphrased from applications that founders published themselves unless marked otherwise. A published accepted application shows what was submitted, not why it was accepted, and accepted applications contain mistakes too.

## Contents

1. Founder profiles
2. How long have the founders known one another?
3. Who writes code?
4. Are you looking for a cofounder?
5. Company name and 50-character description
6. URL, demo, product link, credentials
7. What is your company going to make?
8. Location, and explaining the decision
9. How far along are you?
10. How long have you worked on it, and full-time?
11. Tech stack, AI models and coding tools
12. Optional AI-building evidence
13. Are people using your product?
14. Do you have revenue?
15. Previous application or pivot
16. Other accelerators
17. Why this idea? Domain expertise? How do you know people need it?
18. Competitors and what you understand
19. How will you make money? How much?
20. Other ideas
21. Equity, entity, investment, fundraising
22. What convinced you to apply? How did you hear about YC?
23. Batch preference
24. Fields that appeared on older forms

## Before drafting any answer: the completion sentence and a self-check

Write a private sentence first: "This answer is complete when the reader knows [specific thing]." For revenue, that's the monthly amount, currency, basis and parts. For how the founders met, it's the timeline, the shared work and the current arrangement. Cut anything that doesn't help finish that job. Then run the self-check for the question before calling it done (these come from one research guide; they're review prompts, not interview predictions):

| Question | Self-check |
|---|---|
| 50-character description | Would the line fit ten unrelated companies? Does it describe today's product or an unbuilt future? |
| What you're making | What's the output, who acts on it, what happens after the demo's last screen? Which promised step is still manual, done by someone else, or not built? |
| Who writes code | Can the named founder explain a core feature, how it fails and a real tradeoff? Would progress stop if a contractor disappeared? |
| How the founders met | Which hard decision have you made together? Do all profiles tell the same timeline? |
| Founder achievements | What did the founder do, as opposed to the organization around them? Is the strongest part buried behind a famous employer or school? Would a former colleague recognize it as accurate? |
| Hacking a system | Is it really about your action? Is the "hack" just a normal discount or request? |
| Why this idea | What did a real person do last time the problem happened? What did you believe at first that changed? What's still untested? |
| Domain expertise | Could an outsider write this from a quick web search? What detail would a customer recognize? |
| Evidence of need | Which statement depends on the customer doing something costly or repeated? Did any prospect refuse, and what did you learn? |
| How far along, time worked | What changed for a user? Does the timeline match the profiles, the demo and any previous application? |
| Users | Is this registration, activation or continued use? Can you reproduce the count with the same definition every time? |
| Revenue | Is it cash, invoiced, contracted value or a run rate? Are one-time services mixed into recurring? Does growth come from more customers, more use or one big deal? |
| Competitors | Are you comparing against the customer's best real option (including spreadsheets and doing nothing)? If the advantage is speed or cost, what changed structurally? |

---

## 1. Founder profiles

Each founder fills in their own profile through an emailed link, and the application can't be submitted until every profile is complete. Profile fields have varied by batch. The Summer 2024 published application showed these prompts for each founder:

- Please tell us in one or two sentences about the most impressive thing other than this startup that you have built or achieved.
- Please tell us about a time you most successfully hacked some (non-computer) system to your advantage.
- Tell us about things you've built before.
- List any competitions or awards you have won, or papers you've published.

Confirm the current fields with the founder. Other guides report education, work history, links (LinkedIn, GitHub, personal site) and a technical-founder checkbox; treat those as likely but check.

**What it tests.** Whether each founder is unusually effective. Paul Graham's How to Apply essay says it's the magnitude of an achievement that matters, not the type, and that the best answers are the most specific. Partners have said for years that they look at what founders did, more than school or employer prestige.

**What works**
- One specific achievement per founder, with a number and, if possible, a link: users, revenue, downloads, a ranking, a result.
- Achievements that show building or selling, ideally connected to the idea.
- Concrete details are memorable. Paul Graham once recalled an application years later because it named the exact open-source project a founder maintained.
- For the non-computer hack: a short true story with a constraint, a clever and legal move, and a result. It's testing relentless resourcefulness.

**Examples (founder-published applications, paraphrased)**
- A solo founder (Agent37, F26) cited building his employer's internal ChatGPT tool as a weekend project, which grew to about 120,000 monthly users.
- Cruise (W14) founders had built devices that crack high-security safes and finished the DARPA Grand Challenge.
- Make School (W12): a paid iPhone game with 50,000 downloads, built at 16.
- Clearly AI (S24) answered the hack question with a social engineering competition result at DEF CON.

**Avoid**
- Leaving profiles thin or empty. Dalton Caldwell has said weak applications often skip founder bios.
- Titles and logos with nothing about what the person did.
- Team results claimed as personal ones.
- Achievements no one can check, or a campus event when a hard business result exists.
- An illegal or ethically dubious "hack."

**Template**
> [Name] [did specific thing] in [time or context], which [result with a number]. [Link if public.]

---

## 2. How long have the founders known one another and how did you meet? Have any of the founders not met in person?

**What it tests.** Whether this team survives a hard year. Cofounder breakups kill a lot of young companies, and partners have asked about founder history for as long as the form has existed.

**What works**
- The year and context you met, and something you built or shipped together, with a result.
- How you split responsibilities and how you settle disagreements, in a sentence.
- If you haven't met in person, say so plainly, how long you've worked together remotely, and when you'll meet.

**Examples**
- Hyperspell (F25, published by a cofounder): met at a founder fellowship in early 2024, built a working product and signed paying customers within days of teaming up, and won the program's demo award. A short history, with proof they ship together.
- Goodly (S18): worked together for over a year as early employees at Rippling.

**Avoid**
- Recruiting a cofounder to improve the application. Michael Seibel has said not to apply to YC to find cofounders.
- Inventing a long history.
- Hiding a current ownership dispute or a cofounder who's leaving.

**Template**
> We met in [year] at [place/context]. We worked together on [project] for [time] and shipped [thing, result]. [A] leads [area], [B] leads [area]; when we disagree, [how you decide].

---

## 3. Who writes code, or does other technical work on your product? Was any of it done by a non-founder? Please explain.

**What it tests.** Whether the founders can build and keep building the product themselves. YC's FAQ says the founding team should be able to build the product, which for most businesses means a technical cofounder. Dalton Caldwell has said the biggest variable in getting an interview is the quality and quantity of technical talent on the founding team.

**What works**
- Name each founder and what they built, with stack and dates.
- If a non-founder contributed, say exactly what, under what agreement, and who owns and maintains it now.
- AI coding tools are normal. In March 2025 YC's Jared Friedman said about a quarter of the W25 batch had codebases roughly 95% AI-generated, while stressing YC still funds technical founders who direct that work. Say the founders design, review, debug and maintain the system.

**Examples.** In the published record, disclosure itself isn't penalized: accepted teams disclosed employees and paid contractors who had signed agreements. Rejected examples include outsourced development defended at length, and contractors with no formal agreements.

**Avoid**
- "Our agency handles engineering."
- "The team built it" with no names.
- Hiding a contractor. It comes out in the interview.

**Template**
> [Name] wrote most of the code ([stack], [main components]) since [month year]. [Name] built [part] and handles [area]. [Contractor] built [specific part] in [month] under a work-for-hire agreement; we own the code and have maintained it ourselves since [month].

---

## 4. Are you looking for a cofounder?

**What it tests.** Self-awareness about gaps and how they're covered.

**What works.** A straight answer. If yes, the role you're looking for and what you're doing (YC Co-Founder Matching counts). If no, one or two sentences on why you can cover building and selling for now.

**Examples.** Accepted solo founders stated it flatly and moved on. A rejected solo founder opened by calling solo founding a "cardinal sin" and spent hundreds of words defending it.

**Context.** YC said in September 2026 that nearly one in five of its companies has a solo founder. The FAQ still says one-person startups are tough and more likely to succeed with a cofounder.

---

## 5. Company name and "Describe what your company does in 50 characters or less."

**What it tests.** Whether you can say what you do plainly. It's the first line a reader sees, so it frames everything else.

**What works.** A product and a buyer in plain nouns. A study of YC's directory in one of the source guides found a median one-liner of about 42 characters and six words.

**Examples**

| Company, batch | Result | Line |
|---|---|---|
| Fly.io, W20 | Accepted | "Global Heroku" |
| Slite, W18 | Accepted | "The first note app designed for teams" |
| Clearly AI, S24 | Accepted | "Software security and privacy reviews using AI." |
| Hyperspell, F25 | Accepted | "Context and memory infra for AI agents" |
| Metorial, F25 | Accepted | "The MCP integration platform for agentic AI." |
| Agent37, F26 | Accepted | "Persistent sandboxes for always-on AI agents" |
| Courier, S19 | Accepted | "A single API for multi-channel user notifications." |
| Bubblin, W18 | Rejected | "We help people read more books." |
| Swelly, W17 | Rejected | "Make great decisions with friends." |

The one-liner rarely decides an application on its own, and some accepted teams went over the limit. Treat it as a clarity check.

**Avoid**
- Vague benefits ("help people," "make better decisions").
- Technology without a buyer ("AI-based X").
- Stacked features.
- "Stripe for X" analogies unless the reader gets it instantly.

**Templates**
> [What it is] for [who uses it]
> [Job it does] for [who]

Count characters including spaces. Write it last, after the product answer is solid.

---

## 6. Company URL, demo, product link and login credentials

**What it tests.** Whether something real exists.

**What works**
- A working URL.
- A demo upload (the Fall 2026 capture said "Anything that shows us how the product works. Please limit to 3 minutes / 100 MB"). Always include one, even rough. YC's own demo tip video says unpolished is fine and the difference between nothing and something is large.
- A product link that doesn't require a sales call, with test credentials in the format the form asks for (username / password) and sample data loaded so a partner doesn't land on an empty state.
- Test every link logged out, in a private window.

**Demo and access checklist**
- The demo file plays in a browser (MP4 is safest) and fits the form's limits.
- It opens inside the product and shows the core job within the first several seconds.
- Anything simulated or done by hand is labeled.
- No real customer, patient or financial data on screen or in the test account.
- Test credentials work, have sample data, and won't expire before decisions go out.
- The product link doesn't require a sales call, a waitlist approval or a VPN.
- The website, demo and application describe the same product with the same numbers.

See `video-and-demo.md`.

---

## 7. What is your company going to make? Please describe your product and what it does or will do.

**What it tests.** Can a stranger picture the product after one read?

**What works**
- What it is and what the user does with it, in the present tense.
- How it works, in one or two sentences.
- Who uses it today, if anyone, with the most impressive fact near the top.
- Mark what's built versus planned. If a human does part of the work behind the scenes, say so.
- Save the big vision for one closing line, if at all.

A study of 44 answers to this question published on YC's directory (in one of the source guides) found a median of about 76 words, with the middle half between about 43 and 130.

**Examples**
- GitLab (W15), the example Dalton Caldwell uses for clarity: says what the product is and who uses it, with the most impressive fact (over 100,000 organizations using it) at the top.
- Agent37 (F26): purely mechanical. One API call creates a sandbox with its own URL that keeps files and memory and runs scheduled jobs; an existing chatbot changes one base URL and becomes a persistent agent. Then two short customer examples.
- Cruise (W14): one sentence on what it does, then how they made it tractable (handle most highway driving with commodity hardware and leave the rest to the driver), then the product's shape and price.

**Rejected patterns.** One line on the product, then most of the answer on future-of-work statistics. Five product areas packed into one answer. Hundreds of words of theses before reaching the product. Metorial's founder said their rejected version opened with implementation details that hid what the product was and who it served.

**Template**
> [Product] lets [specific user] [do the job]. Today they [current workaround], which costs them [time, money or risk]. With us they [action] and get [result]. It works by [one-sentence mechanism]. [N] [users] use it today, including [type].

---

## 8. Where do you live now, and where would the company be based after YC? Explain your decision regarding location.

**Format.** `City A, Country A / City B, Country B` (exactly as the form asks).

**What it tests.** Whether you'll be at the in-person batch in San Francisco, and whether you'll build where your customers and talent are.

**What works.** The true answer and a real reason. If the product is tied to a market elsewhere, explain why that location is right.

**Avoid.** Listing San Francisco as where you live after a short visit. Partners ask, and it sits badly next to YC's emphasis on honesty.

---

## 9. How far along are you?

**What it tests.** How fast you move, measured from wherever you started.

**What works**
- Three to five dated facts: started, shipped what and when, users, paying customers, revenue, growth over a stated period.
- Time-box it ("in the last eight weeks we...").
- Say plainly what isn't built yet.
- End with the single next milestone and its date.

**Examples**
- Agent37 (F26): over 1,150 paid instances; July revenue of $13.6K, split into $8.1K recurring and $7.5K from one-time paid pilots; bootstrapped, $0 raised, solo; then specific pipeline items.
- Clearly AI (S24), pre-product: talked to 46 prospective customers over 8 weeks.
- Cruise (W14): about two weeks in, had met experts, bought a car to use as a demo vehicle and started fitting it; said plainly they weren't launched.
- Standard Treasury (S13): zero code and both founders still employed, with a clear reason (no point writing code until a bank signed).
- Metorial: the rejected Summer 2025 version led with what was coming; the accepted Fall 2025 version led with what existed (350 developers signed up for early access, about 2,600 GitHub stars, an enterprise pilot).

**Avoid.** Forecasts in place of facts, "launching next week," a single number with no trend, rounding up.

**Template**
> Started [month year]; full-time since [month year].
> Launched [what] on [date]. [N] users ([definition of active]), [N] paying.
> $[X] revenue in [month], up from $[Y] in [month].
> Biggest customer: [who or precise description], $[Z]/month.
> Next: [one milestone] by [date].

---

## 10. How long have each of you been working on this? How much of that has been full-time? Please explain.

**What it tests.** Commitment and speed. Partners read this against "how far along."

**What works.** Months per founder, with full-time dates. Accepted answers here are short. If someone isn't full-time yet, give the date and reason. One accepted solo founder named the Monday he'd go full-time, right after submitting.

**Context.** In the published record, teams with a founder still employed or in school and no firm date show up much more often among rejected applications. Paul Graham listed cofounders who won't quit among the yellow flags that add up, and Sam Altman called wanting to do the startup only if YC funds it a big red flag.

**Template**
> [A]: [N] months, full-time since [date]. [B]: [N] months, part-time while [reason], full-time from [date].

---

## 11. What tech stack are you using, or planning to use, to build this product? Include AI models and AI coding tools you use.

**What it tests.** Whether you build quickly with current tools and your choices make sense for the product.

**What works.** The real stack in one or two lines; the models in production and the coding tools you use every day; one non-obvious technical choice with its reason, if you have one. For AI products, say briefly what the model does, what deterministic code does, and how quality is checked.

**Avoid.** Listing every tool you've touched, naming fashionable tools you don't use, a three-paragraph essay on commodity hosting.

---

## 12. Optional AI-building evidence

- **Coding agent session.** YC added an experimental optional question for Spring 2026 asking applicants to attach a coding agent session they're particularly proud of, as a markdown or text export (most coding agents have an /export command). It did not appear in the public Fall 2026 capture, so check the live form.
- **Paxel.** YC's optional builder report reads local AI coding session transcripts and produces a profile across steering, execution, engineering, product instinct and planning. The FAQ says it's optional and applicants who don't opt in are evaluated as usual. Paxel's own page says transcript excerpts are sent to model providers through its proxy during analysis and a scored summary is uploaded to YC, so review what you're sharing.

**How to choose, if attaching anything.** A real session on an important feature where the founder scoped the problem, caught the agent's mistakes, asked for tests and made decisions. Nothing staged, nothing cleaned up by AI afterwards. If the founder's sessions don't show disciplined work, skip it.

---

## 13. Are people using your product? (follow-ups when yes)

Recent published applications showed follow-ups like: How many active users or customers do you have? How many are paying? Who is paying you the most, and how much do they pay you?

**What it tests.** Whether real people outside the team want this, and whether you know your own numbers.

**What works**
- Exact counts, with what "active" means (daily, weekly, monthly, and the action that counts).
- Paying versus free, separately.
- The biggest customer and what they pay, or a precise description ("a 40-person fintech in New York, $1,200 a month").
- Even small numbers. One beta customer is real.

**Examples.** Shotput (S15) reported one beta customer and about $110 in revenue and got in. Agent37 split its 1,150+ instances into consumer and API usage.

**What doesn't save an application.** Big free consumer user counts without retention or revenue. In the published record, a consumer app with 30,000 monthly users and no revenue was rejected after interview, and another with 450,000 users was rejected.

---

## 14. Do you have revenue? (follow-ups when yes)

**What it tests.** Momentum, and whether your numbers are honest.

**What works**
- Monthly revenue by month, zeros included.
- Recurring and one-time separated; services separated from software.
- Where it comes from, and growth over a stated period.
- Currency stated; USD is easiest for the reader.
- Explain a dip honestly in a line.

**Examples.** Quo (OpenPhone, S18) showed monthly revenue going $0, $0, $30, $20, $20, then $320 after turning on billing. Hyperspell (F25) showed months of $0 then revenue, with a one-line note about a contract that started mid-month.

**What the record says.** Revenue helps when it shows outside demand, but it's not a threshold either way. YC's FAQ says most funded companies have no revenue. Applications with real revenue have been rejected (one published rejected application showed about $3,300 a month recurring; Buffer was rejected at about $280 a month), and many with none got in.

**Avoid.** Annualizing without saying so (Dalton Caldwell gave making annual revenue look monthly as an example of disqualifying misrepresentation), counting signed-but-unpaid deals, calling GMV revenue, mixing an older business's revenue into a new product.

---

## 15. If you are applying with the same idea as a previous batch, did anything change? If you applied with a different idea, why did you pivot and what did you learn from the last idea?

**What it tests.** How fast you learn.

**What works**
- A before-and-after in comparable numbers.
- The decision you made and why (the lever). Time passing isn't a reason.
- For a pivot: the lesson in one or two sentences and evidence the new direction is working.

**Examples**
- Agent37 (F26): had applied before with a dashboard product, and explained that its biggest accounts asked to embed agents in their own products, with one customer paying for a pilot before the API existed.
- Metorial: the founder said their accepted application described what they'd built in response to the earlier rejection's concern, instead of insisting the original position was right.
- 80,000 Hours (S15): a tight before-and-after list (new technical and business founders, 173 career plan changes against 20 previously, and more).

**Context.** A quantified delta looks necessary but not sufficient; some teams showed strong deltas and were rejected again. Sam Altman said the bad signal is reapplying with nothing changed.

**Template**
> Last application ([batch]): [metric A], [metric B], [status].
> Now: [metric A], [metric B], [status].
> What changed: we [decision] because [what we learned], which led to [result].

---

## 16. If you have already participated or committed to participate in an incubator, "accelerator" or "pre-accelerator" program, please tell us about it.

Name it, the dates, and what happened since. YC's FAQ says past participation is allowed but they may expect more progress. Don't describe Startup School as a funded accelerator unless it was one.

---

## 17. Why did you pick this idea to work on? Do you have domain expertise in this area? How do you know people need what you're making?

**What it tests.** Founder-market fit and contact with real users.

**What works**
- How you met the problem, in one or two sentences. Living it is strongest.
- Expertise as specific facts: where you worked, what you built, what you saw.
- Evidence of need as behavior: how many users you talked to, what they did (paid, signed up, asked repeatedly, refused to give it back).
- One sentence of why now: the change that makes this possible or urgent today.

**Examples**
- Agent37 (F26): the idea came from running his own fleet of agents, customers paid before he finished building, and new users found him through search.
- Hyperspell (F25): the founders hit the problem building their own AI product; one had spent a decade on language and data pipelines, the other had built and sold data API products.
- Prolific (S19): the founder was the target customer during her PhD, and researchers were citing the product without any outreach.

**The pre-traction pattern.** In one guide's coding of published applications with no users or revenue, most accepted ones named a checkable credential tied directly to the idea (an employer, a product, a research result), and fewer rejected ones did. Small sample, but it fits the logic: without traction, the credential is the evidence, so make it specific.

**Tarpits.** Dalton Caldwell has warned that the most dangerous ideas get lots of easy early validation (his example: an app for coordinating nights out with friends) because many teams have tried and failed. If the idea is in a category like that, say why this team will succeed where others didn't.

**Avoid.** Passion without proof. Long belief essays. Pitching an industry you've never talked to a customer in.

**Template**
> [Founder] spent [N years] doing [X] at [place], where [specific pain] cost [measure]. Since [date] we've talked to [N] [buyers]; [M] described [pain, in their words]. [K] now [pay / use it weekly]. Why now: [change].

---

## 18. Who are your competitors? What do you understand about your business that they don't?

**What it tests.** Whether you have an insight others missed. Paul Graham once said the standard for "non-obvious" is what your competitors don't see. This answer is also where many post-interview rejections come from: founders who share their rejection feedback most often cite unclear differentiation or a crowded market.

**What works**
- Name the real alternatives, including ones that aren't startups: the spreadsheet, the in-house build, the incumbent, doing nothing.
- One line each on where they fall short for your specific user.
- One insight you earned from users or building, in a sentence.
- Evidence, if you have it: who switched from what, and why.
- If you'll get "we've seen this before," answer it here.

**Examples**
- Agent37 (F26): named the real incumbent as developers building it themselves on cloud servers, then gave a price comparison against sandbox startups and the technical reason it could be cheaper.
- Apptimize (S13): named seven competitors with a specific flaw each, said which it feared most, and gave its insight that the people deciding on tests aren't programmers.
- Standard Treasury (S13): framed its insight as the reason nobody else would do it (bank people don't care about technology and technology people don't want to work with banks).
- Metorial (F25): one clear line separating who others serve from who they serve, after a rejection that cited unclear differentiation.

**Avoid.** "We have no competitors." Lists of incumbents with no insight. Feature grids. Attacking competitors. Calling incumbents "slow" as the whole argument.

**Context.** YC's FAQ says funding a similar company isn't a factor in decisions. YC often funds several teams attacking the same problem.

**Template**
> Today [users] solve this with [A], [B] or [a spreadsheet / in-house build]. [A] is built for [different user], so [specific gap]. [B] costs [X] / takes [Y]. What we understand that they don't: [one sentence, learned from users or building]. That's why [customer type] switched from [A] to us.

---

## 19. How do or will you make money? How much could you make?

The form adds that YC realizes you can't know precisely and wants your best estimate.

**What it tests.** Business sense, and whether this could become very large.

**What works**
- How you charge (per seat, usage, transaction, outcome) and the price.
- Bottom-up math: price times a realistic count of a customer type you can name.
- The step to a bigger market: where you start and the adjacent markets that make it large. Paul Graham has said he cared less about the initial market's size than about some people wanting it a lot and an easy path into bigger markets next door.

**Examples**
- Agent37: near-term revenue from a named customer's upcoming launch, then a long-term figure built from a few hundred customers shaped like an existing one.
- Hyperspell: usage pricing, current price points, a long-term contract size, and a simple bottom-up line to $1B, plus the observation that raising prices made customers take them more seriously.
- Metorial's founder later criticized their own estimate, which started from a large developer population and assumed a 5% share; he'd now reason from customers upward.

**What the record says.** Method doesn't separate accepted from rejected applications much: thin answers got in and careful math got rejected. Market size sinks applications when partners don't believe the company can get big. So keep this short, credible and bottom-up, and spend effort elsewhere.

**Avoid.** Top-down "1% of a huge market." Several vague revenue streams. "Ads" or "virality" as the whole plan.

**Template**
> We charge [price] per [unit]. Today [N] customers pay an average of $[X]/month. There are about [M] [named customer type] like them: [M] x $[annual] = $[size]. From there, [adjacent market] adds [why it's reachable].

---

## 20. If you had any other ideas you considered applying with, please list them.

The form says one may be something YC has been waiting for, and that often when YC funds people it's to do something listed here and not in the main application.

**What works.** One to three serious ideas, one line each, ideally in areas where the team has an edge. Founders have reported interviews pivoting to a listed side idea, and others who were asked for alternatives they didn't have.

**What the record says.** Some accepted teams left it blank; some listed six or more. A long unrelated list can read as unfocused but isn't disqualifying.

List only ideas the founders actually considered. The coach may suggest candidates in a separate note, labeled as suggestions, but never puts them in the answer.

**Template**
> 1. [Idea] for [user], because [our edge].
> 2. [Idea] for [user], because [our edge].

---

## 21. Equity: legal entity, investment, fundraising

The Fall 2026 capture shows yes/no questions ("Have you formed ANY legal entity yet?" covering the US, your home country or another country; "Have you taken any investment yet?"; "Are you currently fundraising?"), with follow-ups when yes. The 2024 form asked teams without an entity to describe the planned equity breakdown.

**What works**
- Exact facts: entity type, jurisdiction, date, ownership per founder, vesting.
- Every round: instrument, amount, cap or valuation, lead investor.
- If raising now, say so.
- An equal or near-equal split, or one sentence on why not. Michael Seibel's guidance favors equal or near-equal splits; reasons that don't hold up include "it was my idea" and "I started six months earlier."

**Context.** You don't need to incorporate before applying. YC invests in US, Canada, Cayman and Singapore corporations; companies elsewhere create a parent company after acceptance with YC's help. Prior funding isn't a barrier; many batch companies have raised over $1M. Jessica Livingston has described YC's software flagging a big equity gap between founders and companies already mostly owned by outsiders, as prompts for partners to look closer.

**Avoid.** A technical cofounder building most of the product with a small stake. Undocumented promises to advisors or investors. Odd structures with no reason.

---

## 22. What convinced you to apply to Y Combinator? Did someone encourage you? Have you been to any YC events? How did you hear about YC?

Two honest sentences. Naming the YC founder who encouraged you is fine if it's true. This doesn't decide anything.

---

## 23. Batch preference

The next batch, or "a batch after" it. YC's Early Decision page is aimed at students who want to finish school first: same application and interview, funded on acceptance, a spot held for a later batch.

---

## 24. Fields that appeared on older forms

Prepare these if the founder's form shows them:
- **When will you have a version people can use?** (shown when not yet launched, on the 2024 form) A real date tied to what's left to build.
- **How do users find your product? How did you get the users you have now?** Name the channel that's working now, with numbers.
- **Where will most of your initial users be located?**
- **Which category best applies to your company?** Pick the honest one. Michael Seibel has said not to guess what sectors YC wants.

Outdated advice to ignore: uploading the founder video to YouTube as an unlisted link, two batches a year, the old $120K or $150K deals.
