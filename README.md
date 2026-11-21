# Common Ground: food and movement planner

A student design prototype for **Common Ground**, a 2035 future-community concept for adults aged 60 and over that links everyday movement, meal planning and time with others. Shared with the project group and tutors for testing and feedback.

**Live page:** https://echo-yz.github.io/common-ground-planner/

- Educational planning only. Not medical advice and not an NHS service.
- Activity and food guidance is current UK public guidance (NHS, UK Chief Medical Officers, NHS Eatwell Guide). Sunday Table, Cooking Club and other community ideas are design concepts, not real services.
- Built with AI assistance as a prototype for discussion. It has not been tested with real participants.

## Privacy and what is counted

- Everything a person types stays in their browser. Nothing is saved or sent.
- The page counts **anonymous events only** (for example "reached step 3", "made a plan", "pressed Print", and answers to four optional fixed-choice feedback questions) using [GoatCounter](https://www.goatcounter.com/), which uses no cookies and keeps no IP addresses. GoatCounter also records the country, browser and device type, and time of each count.
- Age, sex, height, weight, health answers and plans are **never** sent.
- Nothing is counted if the browser sends Do Not Track or Global Privacy Control, and visitors can switch counting off on the page.
- A Content-Security-Policy in the page blocks requests to any other site.

## Where the counts go

Counts go to the GoatCounter site `future-community` (dashboard: https://future-community.goatcounter.com, visible only to the account owner). Event paths start with `/event/`, for example `/event/step/3-activity`, `/event/plan-made/own` or `/event/feedback/easy/yes`.

To change the site code, rebuild the page:

```
python3 tools/build.py <site-code> index.html
```

Running `python3 tools/build.py '' index.html` switches counting off.

## Editing content

All rules and content (activity ideas, meals, safety rules, sources) are plain tables at the top of the `<script>` in `tools/template.html`. Edit there, then rebuild as above.

Typeface: Atkinson Hyperlegible Next by the Braille Institute, SIL Open Font License 1.1 (see `FONT-LICENSE-OFL.txt`).
