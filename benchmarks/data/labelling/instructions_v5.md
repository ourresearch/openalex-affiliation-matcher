You label raw affiliation strings from scholarly papers for OpenAlex. For each string, list every
organisation the string names as an author's affiliation, and match each one to its OpenAlex
institution record from the numbered candidate cards. Your labels are the gold standard that
automatic matchers will be scored against, so be exact, and say when you are unsure.

# What counts as naming an institution

1. **Name what the string names, at the level it names it.** For each organisation phrase in the
   string, choose the most specific record whose name, acronym, translation or former name that
   phrase states.
   - "Weill Cornell Medicine, New York" names Weill Cornell Medicine, which has its own record:
     label only that record, not Cornell University. Parents are looked up later from the record's
     relationships, so never add a parent the string does not name.
   - If the string names both a unit and its parent ("Weill Cornell Medicine, Cornell University"),
     label both.
   - Do not assume from memory that a unit has its own record. Many well-known schools and
     hospitals do not (Harvard Medical School has none; it is part of Harvard University's
     record). The cards and the second search decide.
   - **Inside a name or its own element?** Split the string at commas, semicolons and line breaks
     into elements. A parent written as its own element is named: label it too, even when grammar
     or official naming ties it to the child ("Chang-Hua Hospital, Ministry of Health and Welfare";
     "Instytut Archeologii i Etnologii, Polskiej Akademii Nauk"; "Economics Institute, Czech
     Academy of Sciences"). A parent that appears inside the child's element ("of", "at", a hyphen,
     a possessive: "Weill Medical College of Cornell University", "Taipei Medical University-Wan
     Fang Hospital", "Economics Institute of the Czech Academy of Sciences") is part of the child's
     name. Then label only the child if the child has a record, or only the parent if it does not
     ("Mental Health Center of Jiangnan University" with no record of its own → Jiangnan
     University).
   - A comma inside an institution's own official name is punctuation, not a new element
     ("Institute of Physics, Academia Sinica"; "Second Affiliated Hospital, Zhejiang University School of
     Medicine"): label only that institution, unless the parent is also named elsewhere in the string.
   - "Most specific record the phrase states" means stated in the string, not known to you:
     "Rutgers University Behavioral Healthcare" states Rutgers University, not Rutgers Health.
   - A unit or part with no record of its own ("Department of Physics", "UCLA Anderson School",
     "Tetra Tech Data Systems, Inc.") resolves to the institution whose name appears in the same
     phrase or elsewhere in the string ("UCLA" → University of California, Los Angeles; "Tetra Tech"
     → Tetra Tech).
   - If no institution's name appears in the string, the unit is `unit_no_record` and nothing is
     labelled for it, **even when you know what it belongs to** ("Bluhm Cardiovascular Institute",
     "The Children's Hospital at Linköping", "Rural Medical College, Loni" alone). A unit's name is
     not evidence for its parent. Put the parent's card in `candidate` when you know it, from the
     string or from your own knowledge, so scoring can tell a parent from a wrong answer.
   - A name that is only part of a longer name is not a separate mention. "Korea University Guro
     Hospital" names the hospital, and "The First Affiliated Hospital of Jinzhou Medical University"
     names the hospital, not Jinzhou Medical University. "Ubon Ratchathani University" does not name a "Ratchathani"
     anything. "John Brown University" does not name Brown University.
2. **Evidence is names, not places.** A city, street, postcode, building or country alone never
   names an institution. "rue Gustave Eiffel" is a street, not Université Gustave Eiffel. "Sidoarjo,
   Indonesia" names no university. One exception: "University Department of X" (common British and
   European usage) with a city that has a single obvious university names that university ("University
   Department of Clinical Neurology, Radcliffe Infirmary, Oxford" → University of Oxford). If the city
   has several universities and the string does not say which (London, Paris), label nothing. Places are useful only to choose between records that share a
   name (two "Universidad Nacional"s; USC in California vs South Carolina; "Children's Hospital").
3. **Generic names need an anchor.** "Children's Hospital", "Imaging Center", "Faculty of
   Medicine", "Institute of Physics", "Ministry of Health" match a specific record only when the
   string gives what makes it that one (a city, a parent, a country for national bodies). If you
   cannot tell which record, use `org_no_record` or give confidence `low`, never pick the biggest.
4. **Acronyms** count when they plainly refer to that institution in context: "CNRS", "INSERM",
   "MIT". A colliding acronym ("USC", "UAB", "CMU") needs context that picks one record.
5. **Former names** count for the current record when the old organisation has no record of its
   own ("INRA" → INRAE; "Carnegie Institute of Technology" → Carnegie Mellon University). The same
   goes for an institution that merged into a single successor and has no record of its own, even if
   it lives on as a campus ("Manhattan VA Medical Center" → VA NY Harbor Healthcare System; "Royal
   Postgraduate Medical School" → Imperial College London): label the successor and start `reason`
   with "predecessor, no record:". If it was split among several successors, label nothing for it. When the
   predecessor has its own record (inactive status is fine, e.g. Université Rennes 1), label the
   predecessor's own record, not its successor.
6. **Companies** often have one record per country ("Pfizer (France)", "LyondellBasell (Germany)").
   Choose the record for the country the string gives; if there is none for that country, the main
   record (usually the headquarters country). A subsidiary, division or former company name counts
   for the company it belongs to when that company's name, or a former name of it, appears
   ("Basell Polyolefine GmbH" → LyondellBasell).
7. **Every affiliation in the string counts**: several institutions, joint units ("UMR 7590 CNRS,
   Sorbonne Université" → CNRS and Sorbonne Université), present addresses, "also at", "on leave
   from", visiting positions.
8. **A ministry's badge on a lab it designates is not an affiliation.** "Key Laboratory of X (Ministry of
   Education)", "Engineering Research Center of Y, Ministry of Education", "MOE Key Laboratory of Z":
   the lab belongs to the university named with it; record the Ministry as `not_affiliation`. A
   Ministry named as its own affiliation with no lab beside it still counts.
9. **Things that are not affiliations get no institution:** funders in acknowledgement text, email
   domains, journal or publisher boilerplate, author names, ORCID or other ids, "Independent
   Researcher", "Unaffiliated", equal-contribution notes, a bare country. Record an institution
   seen only in an email domain as `email_domain` and one named only as a funder or in
   non-affiliation text as `not_affiliation`. They are kept apart so scoring can decide about them.
10. **Script and language do not matter.** A Chinese, Russian or Portuguese name is the same
   institution as its English card name. Translate in your head.

# The candidate cards

Each card is `C<n>`: display name | other names and acronyms | city, region, country | type |
status (shown only when not active). The cards come from a name search and are not ranked by
correctness. The right record is usually among them; sometimes several look alike and you must
choose; sometimes it is missing.

If an organisation the string names should have a record but none of the cards is it, set
`candidate` to `none`, and give its official name in English (plus the country) in
`proposed_name`: the name as ROR or OpenAlex would list it today, including a parent company or
current name if it has changed ("LyondellBasell (Germany)", not "Basell Polyolefine GmbH"). We will
search for that name and show you more cards. On that second look, an `institution` mention must
end on a card: if the organisation you proposed is still not among the cards, treat it as having
no record and apply the unit rule (the institution named in its phrase, e.g. "Harvard Medical
School" → Harvard University) or use `org_no_record`. If you believe it has no
record in OpenAlex at all (a small company, a local clinic, a school), use kind `org_no_record`.

# Output

- `is_affiliation`: true if any part of the string is an author affiliation.
- `mentions`: one entry per organisation phrase that matters, in string order:
  - `span`: the phrase, copied verbatim from the string.
  - `kind`: `institution` (an affiliation you matched or proposed), `unit_no_record` (a unit whose
    institution is not named), `org_no_record` (an organisation you believe has no record),
    `email_domain`, `not_affiliation`.
  - `candidate`: the card id (`C3`) for `institution`, `email_domain` and `not_affiliation`; for
    `unit_no_record`, the card of the institution it belongs to if you know it (else `none`);
    `none` otherwise.
  - `proposed_name`: only when `kind` is `institution` and `candidate` is `none`; else "".
  - `confidence`: `high` (you would bet on it), `medium` (probably right, some doubt), `low`
    (a guess among look-alikes, or unsure it is an affiliation at all).
  - `reason`: at most 15 words; say what decided it when it was not obvious.
- Do not list a unit whose institution is named (the department in "Department of Physics,
  University of Oxford" needs no entry; Oxford does).
- A string with no organisation gets `mentions: []`.
- `notes`: "" unless something about the string or the cards needs a person's attention.
