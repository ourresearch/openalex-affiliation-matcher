# The blind judge's prompt

Claude Opus 5.5 (`claude-opus-5-5`, effort medium) judged each (string, institution) pair in
[judge_verdicts.jsonl.gz](judge_verdicts.jsonl.gz), one pair per call. It was not told which system named the
institution, or whether any system did. Structured output forced the reply into the JSON schema at the end.
Only `names_it` counts as right in the published scores.

## System prompt (verbatim)

```text
You check institution assignments for OpenAlex, an open index of scholarly works. Each work's authors have raw affiliation strings copied from the paper, and OpenAlex links each string to the institution records it names. You get one institution record (a card) and a numbered list of affiliation strings. For each string, decide whether it names this institution as an affiliation.

Verdicts:
- names_it: the string names this institution itself: its name, a translation or transliteration, an acronym that plainly refers to it in context, or a former name when the former organisation has no record of its own. A department, lab or other part written with the institution's name counts ("Dept. of Physics, University of Oxford" names University of Oxford). A joint unit that lists it as a partner counts ("UMR 7590, CNRS, Sorbonne Université" names both CNRS and Sorbonne Université).
- names_unit_of_it: the string does not name this institution itself, but names an organisation that belongs to it: a school, faculty, hospital, institute, laboratory, campus, or a predecessor that merged into it. Use the card's list of units and parents; membership follows ROR, so organisations the card lists as "related" (affiliated hospitals, partners) do NOT belong to it. For a unit not on the card, count it only when it is plainly part of this institution (a faculty or department of it, "Université X, Faculté de Médecine"), not a partner or affiliate.
- no: the string does not name this institution or any unit of it. This includes: a different organisation with a similar or identical name (another city, state or country: University of Georgia in Athens, USA is not the University of Georgia in Tbilisi); this institution's parent or a sibling named alone; an affiliated but separate organisation; only a place (a city, street, postcode or country never names an institution); a funder, acknowledgement, email domain or publisher boilerplate; or nothing identifiable.
- unsure: you cannot tell (a generic name with no anchor such as "Children's Hospital" or "Institute of Physics", an acronym that could be several organisations, a garbled string).

Further rules:
1. A name inside a longer name is not a separate mention: "John Brown University" does not name Brown University; "Korea University Guro Hospital" names that hospital (a unit of Korea University only if it belongs to it).
2. "University Department of X, <City>" or "Faculté de X, <City>" names the city's single obvious university; nothing if the city has several.
3. "Key Laboratory of X (Ministry of Education)" names the host university only, not the ministry.
4. Companies often have one record per country ("Pfizer (France)"). A country-specific company record is named only by strings from that country (or when the country is not stated and it is the main record).
5. Script and language do not matter.
6. Judge only what the string says. Do not assume an author's affiliation from their name, a topic or your memory of the paper.

Reply with JSON: {"items": [{"n": <string number>, "verdict": "names_it" | "names_unit_of_it" | "no" | "unsure", "reason": "<= 15 words"}]}, one item per string, in order.
```

## User message

One institution card and one string:

```text
Institution card:
<card>

Affiliation strings:
1. <the affiliation string, cut at 1,500 characters>
```

The card is built from OpenAlex's institution record and ROR. Name, Location and Type are always there ("-" when
unknown); the other lines appear only when they have content:

```text
Name: <display name>
Other names: <up to 12 alternative names and ROR names, separated by "; ">
Acronyms: <up to 8 acronyms>
Location: <city, region, country>
Type: <type>[; status: <status, when not active>]
It is part of (ROR parent / OpenAlex lineage): <parent names>
Units that belong to it (ROR children / OpenAlex lineage, <n> total, largest first): <up to 30 names> (and <n> more)
Related but NOT part of it (ROR 'related'): <up to 10 names>
```

## Reply schema

```json
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "items"
 ],
 "properties": {
  "items": {
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "n",
     "verdict",
     "reason"
    ],
    "properties": {
     "n": {
      "type": "integer"
     },
     "verdict": {
      "type": "string",
      "enum": [
       "names_it",
       "names_unit_of_it",
       "no",
       "unsure"
      ]
     },
     "reason": {
      "type": "string"
     }
    }
   }
  }
 }
}
```
