"""Rebuild index.html from data/kit.json.

Usage (from the repo folder):  python scripts/build.py

data/kit.json holds everything shown on the page:
  topics: [{id, name, intro, group ("academy" for Course Notes, omit for Interview Prep),
            qs: [{q, s (Hinglish explanation), b (English answer), t (memory trick)}]}]
  quiz:   [{t (topic id), q, o (4 options), a (0-based correct index), w (why)}]
Edit kit.json, run this script, then open index.html in a browser.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = json.loads((root / "data" / "kit.json").read_text(encoding="utf-8"))

ids = {t["id"] for t in data["topics"]}
for q in data["quiz"]:
    assert q["t"] in ids, f"quiz topic not found: {q['t']}"
    assert len(q["o"]) == 4 and 0 <= q["a"] < 4, f"bad quiz item: {q['q']}"

topics = []
for t in data["topics"]:
    t = dict(t)
    if t.get("group") == "prep":
        t.pop("group")
    topics.append(t)

block = ("const T = " + json.dumps(topics, ensure_ascii=False, indent=0) + ";\n\n"
         "const QUIZ = " + json.dumps(data["quiz"], ensure_ascii=False, indent=0) + ";\n\n")
block = block.replace("</", "<\\/")

page = (root / "index.html").read_text(encoding="utf-8")
start = page.index("/*DATA-START*/") + len("/*DATA-START*/\n")
end = page.index("/*DATA-END*/")
(root / "index.html").write_text(page[:start] + block + page[end:], encoding="utf-8")

cards = sum(len(t["qs"]) for t in data["topics"])
print(f"index.html rebuilt: {len(topics)} topics, {cards} cards, {len(data['quiz'])} quiz questions")
