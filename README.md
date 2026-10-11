# Manual Testing Practice Kit

Personal manual testing and QA interview study kit: topic-wise notes with Hinglish explanations, English interview answers, memory tricks and quizzes.

## What is inside

- 40 topics, 1042 study cards, 1086 quiz questions
- Interview Prep (17 topics): QA theory, test case writing, bug reports, API testing, SQL, automation (Playwright + pytest), web and mobile basics, Agile, Git and CI/CD, performance and security, experience and HR questions
- Course Notes (23 topics): crowdtesting platform basics, test cycles, issue reports, testing tools (screenshots, recordings, browser and device logs, web debugging proxy), PII, functional, localization, payment, usability, voice and API testing

Every card has four parts:

- Question
- Samjho: Hinglish explanation
- Interview me aise bolo: English answer for the interview
- Yaad trick: one-line memory hook

## How to use

Open `index.html` in any browser. No install needed.

- Pick a section (Interview Prep or Course Notes), then a topic tab
- Open a card, try to answer first, then read it
- Tick "Yaad ho gaya" when you know it (saved in your browser only)
- Quiz tab: choose a topic or all topics; at the end retry only the wrong ones

## Adding new content

All content lives in `data/kit.json`.

1. Add cards to a topic's `qs` list, or add a new topic
2. Add quiz items to `quiz` (exactly 4 options, `a` is the 0-based index of the correct option)
3. Rebuild the page:

```
python scripts/build.py
```

4. Open `index.html` to check, then commit and push:

```
git add .
git commit -m "Add <topic> notes"
git push
```

### Card format

```json
{ "q": "Question", "s": "Hinglish explanation", "b": "English interview answer", "t": "Memory trick" }
```

### Quiz format

```json
{ "t": "topic-id", "q": "Question", "o": ["A", "B", "C", "D"], "a": 1, "w": "Why this answer is right" }
```

### New topic format

```json
{ "id": "short-id", "name": "Tab name", "intro": "One line about the topic", "group": "academy", "qs": [] }
```

Leave out `group` to put the topic under Interview Prep; use `"group": "academy"` for Course Notes.
