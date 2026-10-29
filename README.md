# YC Application Coach

A Claude skill that helps founders write a Y Combinator application a partner can understand in one read, record a founder video that sounds like them, and walk into the 10-minute interview ready.

It drafts every answer from facts you can back up, in your own voice, and tells you plainly when the weak spot is the company and not the wording. Built for founders applying to YC (and similar accelerators) by [Evalyze](https://www.evalyze.ai/?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach), the AI fundraising platform for pre-seed to Series A founders. Free to use, MIT licensed.

---

## The problem

YC partners read thousands of applications a batch, and in 2026 a lot of them read like the same chatbot wrote them. In August 2026, YC partner Pete Koomen published data showing the word "wedge" in over 20% of Summer 2026 applications, up from under 1% a year earlier, and em dashes in more than half of them since mid-2025. Partner Tyler Bosmeny noted applications got about 60% longer over three years.

Polished, generic answers make a real company harder to see, and they fall apart the moment a founder talks differently on the interview call. The other common failures are just as fixable: a product answer that never says what the product does, a progress answer that leads with what's launching next week, a competitor answer that claims there are no competitors, and a founder video read off a script.

The other YC tools we compared either write those polished answers for you or only critique them. This skill does the work a good YC alum would do with you: pull out the facts, write them plainly, find the hole a partner will poke at, and make sure you can defend every line.

---

## What it does

- Drafts every answer in the order the current form asks for them, using your real numbers, and marks anything missing as `[NEED]` so nothing gets made up.
- Reviews a draft the way a busy partner reads it. You get one verdict on the writing and a separate one on company risk, the three fixes that matter most, scores and rewrites.
- Coaches you while you write it yourself, one question at a time, and doesn't move on until you can back every claim in the interview.
- Pressure-tests your idea before you write anything, using six forcing questions adapted from Garry Tan's open-source [gstack](https://github.com/garrytan/gstack) diagnostic.
- Writes talking points for the founder video, never a script, since YC asks you not to read one. It then checks your recorded take from its transcript: length, a missing cofounder, and lines that sound read.
- Plans a demo that gets to the point in the first few seconds.
- Runs a realistic mock interview with two or three "partners," then a debrief on the answers that ran long, dodged the question or didn't match the application.
- Shows you how to write 21 uncomfortable facts honestly, including no revenue, a cofounder who left, a product an agency built, and a recent pivot.
- Helps after you submit too: which updates are worth sending, how to read a rejection, and whether to reapply now or wait.
- In Claude Code, it reads your repo and git history to build a dated record of what you shipped, and checks that history before trusting it.

---

## What makes it different

### It never invents anything

No made-up users, revenue, customers, quotes or credentials. Missing facts become visible `[NEED: ...]` markers and claims to confirm become `[CHECK: ...]`, so the gaps are obvious before you submit. YC's interview guide says the numbers you state may be verified, and a fabricated detail can cost a founder the whole application.

### It writes like you, not like a model

It drafts from your own words, strips the common AI tells (the words, the em dashes, the "it's not X, it's Y" constructions), and checks your answers with a bundled linter. If your chat messages sound like you, those become the voice sample.

### Two verdicts, never odds

Every review ends with a verdict on the writing and a separate verdict on company risk: the weakest link a partner will see, whether it's a company, evidence or communication problem, and the fastest real test to fix it. It never quotes acceptance odds, because nobody can predict them.

### Dated facts, labeled sources

Deadlines, the deal, form fields and video rules change every batch. Every time-sensitive fact carries the date it was checked and the YC page to re-check, and every claim in the reference files is labeled verified, likely or reported.

---

## Before / after

An invented company, used for teaching. None of these numbers are real.

**Before:**

> We are building an AI-native platform that empowers home-care agencies to streamline operations, unlock efficiency and deliver better outcomes for patients and caregivers alike. Our vision is to become the operating system for care.

**After:**

> Home-care agencies schedule hundreds of caregiver visits a week by phone and spreadsheet, and payroll takes their office manager two days every two weeks. Our software builds the weekly schedule from caregiver availability and client needs, sends shifts by text, and turns completed visits into payroll. 14 agencies use it, scheduling about 3,100 visits a week.

The rewrite leads with the plain fact, says what the product does, and ends with a number a partner can check. With your own company, the skill only uses facts you give it.

---

## What it's built on

- Five deep research reports, which together cite about 490 unique sources.
- 72 YC applications that founders published (44 accepted, 26 rejected, 2 with unknown outcomes), plus answers 63 companies chose to post on their YC pages.
- About 30 long-form founder write-ups and roughly 180 LinkedIn and X posts from founders who got in, got rejected, or both.
- Lengths of 102 accepted founder videos, plus transcripts of four of the example videos YC links on its own video page.
- YC's own pages (apply, FAQ, deal, video, interview guide and Early Decision), re-checked live on October 28 and 29, 2026, along with talks and posts from Paul Graham, Dalton Caldwell, Michael Seibel, Pete Koomen and other partners.
- A side-by-side comparison with four other public Claude skills and tools for YC applicants, to cover what each of them misses.

It was tested in eight sessions on realistic founder cases, including a draft built from a real-looking repo, a three-founder video review and a full pressure test, and the parts that broke were rewritten.

---

## Install

### Claude (web or desktop app)

1. Download [`yc-application-coach.zip`](./yc-application-coach.zip) from this repo. The [`.skill`](./yc-application-coach.skill) file has the same contents if you prefer it.
2. Make sure code execution is on. On Free, Pro and Max plans that's under Settings > Capabilities ("Code execution and file creation"). On Team and Enterprise plans, an owner turns on Skills in organization settings.
3. Go to Customize > Skills, click "+", then "Create skill", then "Upload a skill", and choose the zip.
4. Leave it switched on. It triggers by itself when you mention applying to YC, paste an application answer, share a founder video transcript, or say you got a YC interview.

Anthropic's guide, if you get stuck: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Claude Code

```bash
git clone https://github.com/evalyze-ai/yc-application-coach ~/.claude/skills/yc-application-coach
```

The two scripts need only Python 3 (standard library).

---

## How to use it

Talk to Claude normally. Some things that trigger it:

- "Help me write our YC application" (full draft, in form order)
- "Roast my YC application" (paste your answers)
- "Coach me, I want to write it myself"
- "Poke holes in our idea before we apply to YC"
- "Fix our 50-character description"
- "We have no revenue yet, how do we answer that?"
- "Here's the transcript of our founder video" (paste it)
- "We got a YC interview on Thursday, mock interview us"
- "We got rejected after the interview. Should we reapply now or wait?"

Add "deep mode" to any of these for live fact checks, competitor research and three independent partner reads.

---

## What's inside

```
yc-application-coach/
├── SKILL.md                      the workflow and rules (works on its own)
├── references/
│   ├── question-playbook.md      every question: what it tests, real examples, templates, self-checks
│   ├── hard-answers.md           21 uncomfortable situations and how to write them honestly
│   ├── worked-examples.md        before-and-after rewrites and editing exercises
│   ├── how-partners-read.md      how applications are read and what partners have said they weigh
│   ├── evidence-and-metrics.md   metric definitions and formulas, commercial states, dot plots
│   ├── video-and-demo.md         bullet cards for 1 to 4 founders, what accepted videos look like
│   ├── interview.md              reported questions, what tipped decisions, 40-question diligence bank
│   ├── reapply-update-rejection.md
│   ├── plans-and-timelines.md    what to do with four weeks, a few days, a weekend or 48 hours
│   ├── special-situations.md     solo, non-technical, international, students, hardware
│   ├── case-studies.md           real applications and founder stories, labeled by confidence
│   ├── review-rubric.md
│   ├── live-facts.md             dated facts and where to re-check them
│   └── sources.md
├── assets/
│   ├── application-template.md   every field in form order, ready to fill
│   ├── fact-sheet-template.md
│   ├── interview-cheat-sheet.md
│   └── pre-submit-checklist.md
└── scripts/
    ├── lint_application.py       AI tells, dashes, traps, missing numbers, the 50-character limit
    └── video_check.py            founder video transcript check
```

---

## Status

**v1.0, October 2026.** Facts were checked against YC's pages on October 28 and 29, 2026, when YC was taking Winter 2027 applications. YC changes its form and calendar every batch, so always check [ycombinator.com/apply](https://www.ycombinator.com/apply) before you submit.

If you use it and something feels off, please [open an Issue](https://github.com/evalyze-ai/yc-application-coach/issues). A real example of where it went wrong is more useful than a compliment.

---

## A note on honesty

Nothing can buy you a spot at YC, and this skill doesn't pretend otherwise. YC says introductions aren't needed and every application is read the same way. The skill helps you show what's true about your company, in plain words, and find the weak spot before a partner does.

---

## About Evalyze

[Evalyze](https://www.evalyze.ai/?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach) is an AI fundraising platform for pre-seed to Series A founders, with 15K+ founders and 20K+ verified investors on it. Founders use it to find investors who fit their stage and sector, sharpen their deck, and run outreach from one place. A YC application and a seed round ask a lot of the same questions, so if you're raising alongside or after YC, these are good places to start:

- [Investor Matching](https://www.evalyze.ai/investor-matching?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach) ranks investors by stage, sector, location, check size and investment history, and you decide who to approach.
- [Investor Outreach](https://www.evalyze.ai/outreach?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach) drafts personalized emails you approve before anything sends from your own inbox, then tracks replies and follow-ups.
- [Startup Analyzer](https://www.evalyze.ai/startup-analyzer?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach) scores your startup across six areas against companies at your stage, including an investor readiness score.
- [Pitch Deck Coach](https://www.evalyze.ai/pitch-coach?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach) gives your deck a score out of 100 with slide-by-slide feedback.
- [Managed Fundraising](https://www.evalyze.ai/managed-fundraising?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach) is for founders who want an ex-VC-led team to run the raise with them, for one flat monthly fee with no equity or success fee.
- The Starter plan is free with no card required. See [pricing](https://www.evalyze.ai/pricing?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach).

Free guides on the [Evalyze blog](https://www.evalyze.ai/blog?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach), including the [pre-seed fundraising playbook](https://www.evalyze.ai/blog/pre-seed-fundraising-playbook?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach) and the [startup fundraising checklist](https://www.evalyze.ai/blog/startup-fundraising-checklist?utm_source=github&utm_medium=readme&utm_campaign=yc-application-coach).

### More free tools from Evalyze

- [founder-fundraising-outreach](https://github.com/evalyze-ai/founder-fundraising-outreach): a Claude skill for investor outreach that reads like a human wrote it, covering cold emails, follow-ups, investor replies and post-meeting recaps.
- [awesome-startup-fundraising](https://github.com/evalyze-ai/awesome-startup-fundraising): a curated list of tools for evaluating startups, improving pitch materials and running a raise.
- All of them live at [github.com/evalyze-ai](https://github.com/evalyze-ai).

---

## License

MIT. Use it, change it, share it.
