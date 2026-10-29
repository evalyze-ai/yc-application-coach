#!/usr/bin/env python3
"""Check a YC founder video transcript (a take you recorded, not a script).

Usage:
    python video_check.py transcript.txt --founders "Ines,Kofi,Lena" [--one-liner "Inspection reports for elevator contractors"]

--founders: every founder on the application, including anyone who isn't in
this take. That's how a missing founder gets caught.

The transcript can be plain text, "Name: ..." lines, or a Zoom/Meet .vtt or
.srt export. The script estimates length, checks that every founder is named
and speaks, and flags signs the take sounds read or pitched rather than spoken.
It can't see or hear the video, so it can't judge audio, lighting or energy.
Standard library only.
"""

import argparse
import re

# Words people rarely say out loud. Superset of the AI-tell list in SKILL.md.
WRITTEN_WORDS = ["wedge", "delve", "leverage", "unlock", "unlocks", "seamless", "seamlessly",
                 "robust", "game-changer", "cutting-edge", "next-generation", "revolutionize",
                 "revolutionizing", "empower", "empowering", "streamline", "landscape", "paradigm",
                 "ecosystem", "solution", "solutions", "journey", "innovative", "synergy",
                 "transformative", "ai-powered", "ai-driven", "ai-native", "unprecedented",
                 "holistic", "end-to-end"]

PITCH_LINES = ["in today's", "imagine a world", "on a mission", "at the intersection of",
               "we believe", "massive opportunity", "huge opportunity", "huge market",
               "massive market", "disrupt", "transform the", "the future of"]

MARKET_STAT = [r"\bmarket is worth\b", r"\bmarket size\b", r"\bbillion\b", r"\btrillion\b",
               r"\btam\b", r"\bpercent of the market\b"]

VAGUE_PROOF = ["strong engagement", "very strong", "great traction", "strong traction",
               "great feedback", "amazing feedback", "positive feedback", "lots of interest",
               "huge demand", "strong demand", "really excited", "incredible response"]

CLOSERS = ["thanks for watching", "thank you for watching", "thank you so much for watching",
           "hope to talk soon", "hope to hear from you", "looking forward to", "thanks for your time"]

DEMO_PHRASES = ["on the screen", "on screen", "as you can see", "let me show", "this button",
                "click here", "if i click", "dashboard here", "you can see here", "on the left",
                "on the right", "screen share", "here's the app"]

EXPANDED = [r"\bwe are\b", r"\bit is\b", r"\bdo not\b", r"\bdoes not\b", r"\bi am\b",
            r"\bthey are\b", r"\bwe have been\b", r"\bcannot\b", r"\bwe will\b", r"\bthat is\b"]
CONTRACTED = [r"\bwe're\b", r"\bit's\b", r"\bdon't\b", r"\bdoesn't\b", r"\bi'm\b",
              r"\bthey're\b", r"\bwe've\b", r"\bcan't\b", r"\bwe'll\b", r"\bthat's\b"]

NUMBER_WORDS = (r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
                r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|"
                r"forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|dozen|"
                r"percent|half|doubled|tripled)\b")

TEAM_TIME = re.compile(r"\b(known each other|met|worked together|been friends|friends for|"
                       r"years at|years of experience)\b")

NOT_SPEAKERS = {"our", "the", "we", "note", "notes", "so", "and", "but", "today", "here",
                "this", "that", "it", "my", "a", "an", "number", "numbers", "update", "why", "what"}

STOP = set("a an the for of to and or in on with by at from is are we our your".split())
WPM = 150


def tokens(text):
    return re.findall(r"[a-z0-9$%']+", text.lower().replace("-", " "))


def word_count(text):
    return len(re.findall(r"[A-Za-z0-9$%']+(?:[-.,][A-Za-z0-9]+)*", text))


def has(phrases, low):
    return [p for p in phrases if re.search(r"(?<![a-z])" + re.escape(p) + r"(?![a-z])", low)]


def second_at(full, phrase):
    m = re.search(r"(?<![a-z])" + re.escape(phrase) + r"(?![a-z])", full.lower())
    if not m:
        return None
    return round(word_count(full[:m.start()]) / WPM * 60)


def read_lines(path):
    raw = open(path, encoding="utf-8").read().replace("’", "'").replace("﻿", "")
    out = []
    for line in raw.splitlines():
        s = line.strip()
        if not s or s.upper().startswith("WEBVTT") or s.startswith("NOTE ") or "-->" in s or re.fullmatch(r"\d+", s):
            continue
        s = re.sub(r"<v\s+([^>]+)>", r"\1: ", s)   # VTT voice tags
        s = re.sub(r"</?[^>]+>", "", s)            # any other tags
        out.append(s)
    return out


def split_speaker(line, founders):
    m = re.match(r"^\s*([A-Za-z][\w .'-]{0,30}?)\s*(\([^)]*\))?\s*:\s+(.*)$", line)
    if not m:
        return None, line
    label = m.group(1).strip()
    if re.match(r"(?i)^(speaker|person|participant)\s*\d+$", label):
        return label, m.group(3)
    if founders:
        for f in founders:
            if label.lower() == f.lower() or label.lower().startswith(f.lower() + " "):
                return f, m.group(3)
        return None, line
    if len(label.split()) <= 3 and label[0].isupper() and label.split()[0].lower() not in NOT_SPEAKERS:
        return label, m.group(3)
    return None, line


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("transcript")
    ap.add_argument("--founders", default="", help="every founder on the application, comma-separated, including anyone missing from this take")
    ap.add_argument("--one-liner", default="", help="the application's 50-character description")
    args = ap.parse_args()

    founders = [x.strip() for x in args.founders.split(",") if x.strip()]
    per_speaker = {}
    plain = []
    for line in read_lines(args.transcript):
        who, said = split_speaker(line, founders)
        if who:
            per_speaker.setdefault(who, []).append(said)
        plain.append(said)
    text = " ".join(plain)
    low = text.lower()
    total = word_count(text)
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]

    retake, fix = [], []

    print("# Founder video check\n")
    if founders:
        print(f"Founders on the application: {len(founders)} ({', '.join(founders)})")
    else:
        print("No --founders given, so a missing founder can't be detected.")
    print(f"Words spoken: {total}")
    for wpm in (130, 150, 170):
        print(f"- at {wpm} words a minute: about {round(total / wpm * 60)} seconds")
    if total > 190:
        retake.append("TOO LONG: likely well past a minute (YC's page says the video should be 1 minute long). Cut a point rather than talking faster.")
    elif total > 170:
        fix.append("A LITTLE LONG: probably 60 to 80 seconds. Many accepted videos run a bit over a minute, so this is fine unless there's filler to cut.")
    elif total < 100:
        fix.append("SHORT: under about 45 seconds. Fine if names, what you make and your strongest proof are all there.")

    # Who spoke
    if per_speaker:
        print("\nWords by speaker:")
        for name, parts in per_speaker.items():
            n = word_count(" ".join(parts))
            print(f"- {name}: {n} ({round(100 * n / max(total, 1))}%)")
    generic = bool(per_speaker) and all(re.match(r"(?i)^(speaker|person|participant)\s*\d+$", s) for s in per_speaker)
    if generic:
        fix.append("GENERIC LABELS: rename 'Speaker 1' and so on to each founder's name so the split between founders can be checked.")
    elif len(founders) > 1:
        if not per_speaker:
            fix.append("NO SPEAKER LABELS: put each founder's name and a colon at the start of their turns ('Ines: ...') so the split can be checked.")
        else:
            for f in founders:
                if f not in per_speaker:
                    named = re.search(r"(?<![a-z])" + re.escape(f.lower()) + r"(?![a-z])", low)
                    retake.append(f"MISSING FOUNDER: {f} doesn't speak{'' if named else ' and is never named'}. YC asks for all founders in the video; if you can't be in one room, screen-record a video call.")
            fair = 1 / len(founders)
            shares = {f: word_count(" ".join(per_speaker.get(f, []))) / max(total, 1) for f in founders}
            top = max(shares, key=shares.get)
            if shares[top] > min(0.75, 2 * fair):
                fix.append(f"ONE VOICE: {top} has {round(100 * shares[top])}% of the words across {len(founders)} founders. Give each founder a real segment.")
            for f, s in shares.items():
                if f in per_speaker and s < 0.5 * fair:
                    fix.append(f"BARELY HEARD: {f} has only {round(100 * s)}% of the words.")

    # What you make, in the one-liner's words, in one sentence
    if args.one_liner:
        keys = [w for w in tokens(args.one_liner) if w not in STOP]
        best, best_i = 0.0, None
        for i, s in enumerate(sentences):
            st = set(tokens(s))
            score = sum(1 for k in keys if k in st) / max(len(keys), 1)
            if score > best:
                best, best_i = score, i
        if best < 0.6:
            fix.append("ONE-LINER MISMATCH: no sentence says what you make in the application's one-liner words. Say it in one sentence, the way the form does.")
        else:
            sec = round(word_count(" ".join(sentences[:best_i])) / WPM * 60)
            print(f"\nWhat you make, in the one-liner's words: about {sec} second{'s' if sec != 1 else ''} in.")
            if sec > 25:
                fix.append(f"LATE: what you make first comes up about {sec} seconds in. Say it right after names.")

    # Proof: a number that isn't a market size or how long the team has known each other
    proof = [s for s in sentences
             if (re.search(r"\d", s) or re.search(NUMBER_WORDS, s.lower()))
             and not any(re.search(p, s.lower()) for p in MARKET_STAT)
             and not TEAM_TIME.search(s.lower())]
    if not proof:
        fix.append("NO PROOF NUMBER: no users, customers, revenue or results with a number (market size and years known don't count). Add the strongest real proof point.")
    vague = has(VAGUE_PROOF, low)
    if vague:
        fix.append("VAGUE PROOF: " + ", ".join(f'"{v}"' for v in vague) + ". Swap for a number with a period (\"40 loads through it last week\").")
    if any(re.search(p, low) for p in MARKET_STAT):
        fix.append("MARKET STAT: a market-size figure. Partners get nothing from it in a video; use the time for proof or the team.")

    # Sounding read or pitched
    written = has(WRITTEN_WORDS, low)
    pitch = has(PITCH_LINES, low)
    exp = sum(len(re.findall(p, low)) for p in EXPANDED)
    con = sum(len(re.findall(p, low)) for p in CONTRACTED)
    read_aloud = exp >= 3 and exp > con
    if read_aloud and (len(written) + len(pitch)) >= 2:
        retake.append(f"SOUNDS READ: {exp} expanded forms ('we are', 'it is') vs {con} contractions, plus written-sounding words or pitch lines. YC says not to recite a script; talk from bullets.")
    elif read_aloud:
        fix.append(f"MAYBE READ: {exp} expanded forms vs {con} contractions. Some transcription tools expand contractions, so listen before deciding.")
    if written:
        fix.append("WRITTEN-SOUNDING WORDS: " + ", ".join(written) + ". People rarely say these out loud.")
    for p in pitch:
        fix.append(f"PITCH LINE: \"{p}\" at about {second_at(text, p)} seconds. Cut it.")
    closers = has(CLOSERS, low)
    if closers:
        fix.append("SIGN-OFF: " + ", ".join(f'"{c}"' for c in closers) + ". End on the team or the proof, then stop.")
    demo = has(DEMO_PHRASES, low)
    if demo:
        fix.append("DEMO TALK: " + ", ".join(f'"{d}"' for d in demo) + ". YC says the video isn't for a demo; that goes in the separate demo upload.")

    # Long sentences only mean something when a person punctuated the transcript
    punct = len(re.findall(r"[.!?]", text)) / max(total, 1) * 100
    if punct >= 3:
        long_s = [s for s in sentences if word_count(s) > 25]
        if long_s:
            fix.append(f"LONG SENTENCES: {len(long_s)} sentence(s) over 25 words. Spoken sentences are shorter; long ones usually mean a script.")

    print("\nRetake for these:")
    print("\n".join(f"- {i}" for i in retake) if retake else "- None found in the words.")
    print("\nFix if you're retaking anyway:")
    print("\n".join(f"- {i}" for i in fix) if fix else "- None.")
    print("\nThis checks the words only. Watch the take: can you hear everyone clearly, are all faces visible, does it sound like you talking to a friend?")


if __name__ == "__main__":
    main()
