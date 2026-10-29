#!/usr/bin/env python3
"""Mechanical checks for a YC application draft.

Usage:
    python lint_application.py draft.md [--max-words 250]

The draft should be markdown with each question as a heading (## or ###)
and the answer underneath. The script prints a report of issues per answer.
It only catches mechanical problems. It can't judge whether an answer is
true, clear or convincing, so a human (or the coach) still reviews it.
Standard library only.
"""

import argparse
import re
import sys

AI_TELLS = [
    "wedge", "delve", "delves", "delving", "unlock", "unlocks", "unlocking",
    "leverage", "leverages", "leveraging", "seamless", "seamlessly", "robust",
    "game-changer", "game changer", "game-changing", "cutting-edge",
    "next-generation", "next generation", "revolutionize", "revolutionizing",
    "revolutionary", "empower", "empowers", "empowering", "streamline",
    "streamlines", "streamlining", "landscape", "paradigm", "ecosystem",
    "synergy", "holistic", "best-in-class", "world-class", "disrupt",
    "disrupting", "disruptive", "at the intersection of", "harness",
    "elevate", "supercharge", "one-stop shop", "mission-critical",
    "tapestry", "journey", "pivotal", "transformative", "innovative",
    "ai-powered", "ai-driven", "ai-native",
]

# Words that often stand in for saying what the product does. Not always wrong.
WATCH = ["platform", "solution", "solutions", "with ai", "using ai", "powered by ai"]

# Traps the skill names explicitly.
TRAPS = [
    (re.compile(r"\bno (real |direct |true )?competit(ors|ion)\b", re.I), "says there are no competitors; name the real alternatives (spreadsheet, in-house, incumbent, doing nothing)"),
    (re.compile(r"\bnobody (else )?is doing (this|what we)\b", re.I), "claims nobody else does this; name the real alternatives"),
    (re.compile(r"\b(agency|dev shop|development partner|outsourc\w*)\b[^.]{0,60}\b(handles|handle|does|do|develops|takes care of)\b(?![^.]*\b(own|maintain))", re.I), "outsourced build with no ownership stated; say who owns and maintains the code and what the founders built"),
    (re.compile(r"\b(capture|get|take|win|grab)\s+(just\s+|only\s+|even\s+)?\d+(\.\d+)?\s?%", re.I), "top-down market share; build the estimate bottom-up from a named customer type"),
    (re.compile(r"\b\d+(\.\d+)?\s?%\s+of\s+(the|a|this)?\s*\$?[\d.,]+\s*(t|tn|trillion|b|bn|billion)\b", re.I), "percentage of a huge market; build the estimate bottom-up"),
]

VAGUE = [
    "significant traction", "strong traction", "great traction",
    "rapid growth", "rapidly growing", "strong demand", "huge market",
    "massive market", "many users", "lots of users", "a lot of interest",
    "very interested", "users love", "customers love", "exponential",
    "strong engagement", "great feedback", "positive feedback",
]

VAGUE_BENEFIT = ["optimize their operations", "optimize operations", "smarter decisions",
                 "better decisions", "data-driven insights", "actionable insights",
                 "improve efficiency", "increase efficiency", "save time and money",
                 "better outcomes", "operational excellence"]

OPENERS = [
    "we believe", "our mission", "we are on a mission", "in today's",
    "in today’s", "imagine a world", "imagine if", "at [", "we aim to",
    "we are passionate", "we're passionate",
]

HEDGES = ["essentially", "basically", "kind of", "sort of", "honestly",
          "we aim to", "we hope to", "we strive to"]

FUTURE = ["will launch", "launching soon", "launching next", "next week",
          "next month", "coming soon", "soon", "about to", "we plan to",
          "we will", "we'll be", "is going to"]

CONSTRUCTIONS = [
    (re.compile(r"\bnot just\b[^.]{0,80}\bbut\b", re.I), "'not just X but Y' construction"),
    (re.compile(r"\b(it's|it is|this is)\s+not\b[^.]{0,60}[,;]\s*(it's|it is)\b", re.I), "'it's not X, it's Y' construction"),
]

NOTE_LINE = re.compile(r"^\s*(>\s*)?[*_]*\s*(note|notes|check|why)\b[^:]*:", re.I)
ITALIC_LINE = re.compile(r"^\s*(>\s*)?([*_])[^*_].*\2\s*$")
PLACEHOLDER = re.compile(r"\[(NEED|CHECK)[^\]]*\]", re.I)

DEFAULT_SKIP = (r"^(the )?(story|verdict|weakest|fixes|open items|video|demo shot|running order|partner|"
                r"questions (to expect|partners)|fact sheet|appendix|rubric|scores|plan|fields you didn|"
                r"before.?and.?after|what i couldn|deep mode|readiness|notes?|audit|after you submit|"
                r"(the )?application$|what changed since|founder video|demo\b|three biggest|answer by answer|rewrites|fields you|"
                r"questions|verdict|consistency map|fixes before|open items|retelling|answers to|what to do|"
                r"(appendix|part) [a-z0-9]|status|time left|plan to|the 3-sentence|three-sentence)")

DASHES = re.compile("[\u2014\u2013]|\\s--\\s")


def split_answers(text):
    """Return (question, answer) pairs from ## and ### headings; # headings only end the previous answer."""
    parts = re.split(r"^(#{1,3}\s+.+)$", text, flags=re.M)
    items = []
    i = 1
    while i < len(parts):
        level = len(parts[i]) - len(parts[i].lstrip("#"))
        q = parts[i].lstrip("#").strip()
        a = parts[i + 1].strip() if i + 1 < len(parts) else ""
        if level >= 2:  # single-# lines are section titles, not questions
            items.append((q, a))
        i += 2
    return items


def find_terms(text, terms):
    low = text.lower()
    hits = []
    for t in terms:
        pattern = r"(?<![a-z])" + re.escape(t) + r"(?![a-z])"
        if re.search(pattern, low):
            hits.append(t)
    return hits


def check(question, answer, max_words):
    issues = []
    ql = question.lower()
    # Drop coach notes under an answer, then set placeholders aside.
    answer = "\n".join(l for l in answer.splitlines()
                       if not NOTE_LINE.match(l) and not ITALIC_LINE.match(l)
                       and not re.match(r"^\s*(-{3,}|\*{3,})\s*$", l)).strip()
    placeholders = PLACEHOLDER.findall(answer)
    text = PLACEHOLDER.sub(" ", answer)
    words = len(re.findall(r"\b\w[\w'’-]*\b", text))

    if not answer:
        if "optional" not in ql:
            issues.append("EMPTY: no answer under this heading (add the answer or a [NEED: ...] marker)")
        return issues, words, 0

    if "50 characters" in ql or "one-liner" in ql or "one liner" in ql:
        line = text.splitlines()[0].strip().strip('"').strip()
        if len(line) > 50:
            issues.append(f"TOO LONG: one-liner is {len(line)} characters (limit 50, spaces count)")

    if DASHES.search(text):
        issues.append("DASH: em/en dash or ' -- ' found; use a comma, period or parentheses")

    tells = find_terms(text, AI_TELLS)
    if tells:
        issues.append("AI TELL: " + ", ".join(sorted(set(tells))))

    vague = find_terms(text, VAGUE)
    if vague:
        issues.append("VAGUE: replace with a dated number: " + ", ".join(vague))

    vb = find_terms(text, VAGUE_BENEFIT)
    if vb:
        issues.append("VAGUE BENEFIT: " + ", ".join(vb) + " (say what the user does and what they get, with a number if you have one)")

    first = text.lstrip().lower()
    for o in OPENERS:
        if first.startswith(o):
            issues.append(f"OPENER: starts with '{o}'; put the answer in the first sentence")
            break

    hedges = find_terms(text, HEDGES)
    if hedges:
        issues.append("HEDGE: " + ", ".join(hedges))

    for rx, label in CONSTRUCTIONS:
        if rx.search(text):
            issues.append("PATTERN: " + label)

    if "how far along" in ql or "progress" in ql:
        first_sentence = re.split(r"(?<=[.!?])\s", text.strip(), maxsplit=1)[0]
        fut = find_terms(first_sentence, FUTURE)
        if fut:
            issues.append("FUTURE FIRST: the opening sentence is about plans (" + ", ".join(fut) + "); lead with what exists")

    for rx, label in TRAPS:
        if rx.search(text):
            issues.append("TRAP: " + label)

    watch = find_terms(text, WATCH)
    if watch:
        issues.append("PLAIN WORDS: " + ", ".join(watch) + " (say what it does instead, unless it's literally accurate)")

    if "?" in text:
        issues.append("QUESTION MARK: rhetorical questions rarely help; check it's intended")

    if "!" in text:
        issues.append("EXCLAMATION: remove")

    if words > max_words:
        issues.append(f"LENGTH: {words} words; most strong answers are well under {max_words}")

    has_number = (bool(re.search(r"\d", text)) or bool(placeholders)
                  or bool(re.search(r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\b", text, re.I)))
    numberish_q = any(k in ql for k in ["how far along", "revenue", "using your product", "users", "how long"])
    yes_no = re.fullmatch(r"(yes|no)\.?", text.strip().lower()) is not None
    if numberish_q and not has_number and not yes_no:
        issues.append("NO NUMBERS: this question usually needs dated numbers")

    return issues, words, len(placeholders)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft")
    ap.add_argument("--max-words", type=int, default=250)
    ap.add_argument("--skip", default=DEFAULT_SKIP,
                    help="regex for headings that aren't application answers (default skips the coach's own sections)")
    args = ap.parse_args()

    with open(args.draft, encoding="utf-8") as f:
        text = f.read()

    items = split_answers(text)
    if not items:
        print("No headings found. Put each question on its own '## ' heading line.")
        sys.exit(1)

    skip = re.compile(args.skip, re.I) if args.skip else None
    total_issues = 0
    total_words = 0
    total_open = 0
    linted = 0
    print(f"# Lint report for {args.draft}\n")
    for q, a in items:
        if skip and skip.search(q):
            continue
        linted += 1
        issues, words, n_open = check(q, a, args.max_words)
        total_words += words
        total_open += n_open
        status = "OK" if not issues else f"{len(issues)} issue(s)"
        extra = f", {n_open} open placeholder(s)" if n_open else ""
        print(f"## {q}\n{words} words, {status}{extra}")
        for i in issues:
            print(f"- {i}")
        print()
        total_issues += len(issues)

    print(f"Total: {linted} answers, {total_words} words, {total_issues} issue(s), {total_open} open placeholder(s).")
    print("Mechanical checks only. Still run the stress tests and the partner read.")


if __name__ == "__main__":
    main()
