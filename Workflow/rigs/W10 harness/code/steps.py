"""The step decomposition of file 33's procedure, and the eleven tests.

A RULE. It holds the words every arm's calls are built from, so that the only thing
that differs between arms is what W3 section 5 says differs: the carrier, the partition,
the prefill, the withheld change list, the inserted criticism, the exchanged names.

The decomposition is file 33's own: Step 1 freeze the question, Step 2 list the jobs,
Step 3 take it apart, Step 4 write the change list, Step 5 run the tests, Step 6 where
each part came from, Step 7 report. W10 stage A fixes the grouping for arms (b), (c), (c'):
steps 1-2, 3, 4, 5, 6-7.
"""

STEP_ORDER = ["S12", "S3", "S4", "S5", "S67"]

STEP_TITLE = {
    "S12":  "Steps 1 and 2: freeze the question, list the jobs",
    "S3":   "Step 3: take it apart",
    "S4":   "Step 4: write the change list",
    "S5":   "Step 5: run the tests",
    "S67":  "Steps 6 and 7: where each part came from, then the report",
    "S1234": "Steps 1 to 4: freeze the question, list the jobs, take it apart, write the change list",
    "SONE": "One test of Step 5, on the parts named and no others",
    "SASM": "Step 7: the report, from the answers below",
    "ALL":  "The whole procedure, Steps 1 to 7, in order",
}

STEP_TASK = {
 "S12": ("Do Step 1 and Step 2 of the method's procedure on the document, and nothing else.\n"
         "Step 1: freeze the question. Say what is being explained, over what range, and what is asked, "
         "and name which kind of question it is from the method's list. Where the document answers several, "
         "take the one its title or opening makes central and say so.\n"
         "Step 2: list the jobs, each put as a contrast (why this and not that), each tagged given, fixed or added.\n"
         "Do not take the explanation apart. Do not write a change list. Do not run any test. Do not write a report."),
 "S3":  ("Do Step 3 of the method's procedure, and nothing else. Take the explanation apart: list, numbered, "
         "the parts claimed to do the work, in the document's own words where you can. Say the strongest version back.\n"
         "Do not run any test. Do not write a report."),
 "S4":  ("Do Step 4 of the method's procedure, and nothing else. Write the change list: which changes to the world "
         "the claim covers, which it leaves out, and whether the exclusion was said up front or slipped in later.\n"
         "Do not run any test. Do not write a report."),
 "S5":  ("Do Step 5 of the method's procedure, and nothing else. Run every one of the eleven tests in the method's "
         "order: remove; swap; flip the outcome; poke; reverse; hunt the answer in the starting points; add a job; "
         "build the best rival; pull; check the patches; look inside. Under each test, say what you did and what "
         "happened. Where a test cannot bite on a document of this kind, name it, quote the sentence of the document "
         "that leaves it nothing to reach, and say which part it would have settled.\n"
         "Do not write the report yet."),
 "S67": ("Do Step 6 and Step 7 of the method's procedure. Step 6: say where each part came from — fitted, built or "
         "asserted — one for every part. Step 7: write the report in the form the method gives, with one of the "
         "method's eight marks on every part. Keep the report under 1,200 words."),
 "S1234": ("Do Steps 1 to 4 of the method's procedure, and nothing else: freeze the question, list the jobs, take the "
         "explanation apart into numbered parts, write the change list.\n"
         "Do not run any test. Do not name a pair of parts that pull against each other, in those words or in any "
         "others (that making one stronger makes another weaker, which gives way, where the line is). Do not build "
         "a rival, and do not say that nothing separates this explanation from another or that two accounts are the "
         "same at this level. Do not say that two parts are two routes to one job, and do not say what happens when "
         "parts are removed in groups. Do not put a mark on any part. Do not write a report. Those come later, in "
         "other hands."),
 "SASM": ("You are handed the answers other readers gave to single tests, each on some of the parts. "
         "Do Step 7: write the report in the form the method gives, with one of the method's eight marks on every part. "
         "Use only what is below. Keep the report under 1,200 words."),
 "ALL": ("Work through the method's procedure on the document, in order, writing each step's output under its own "
         "heading before you start the next: Steps 1 and 2 (freeze the question; list the jobs, each as a contrast, "
         "each tagged given, fixed or added); Step 3 (take it apart into numbered parts); Step 4 (the change list); "
         "Step 5 (run every one of the eleven tests, naming any that cannot bite, with the sentence that leaves it "
         "nothing to reach); Step 6 (where each part came from: fitted, built or asserted); Step 7 (the report in the "
         "form the method gives, with one of the method's eight marks on every part). Keep the report under 1,200 words."),
}

# The eleven tests of Step 5, in the method's order. The ids are the old rig's
# (plan 49 rig, second_marker.py: TESTS = ["remove", "swap", "flip", "poke", "reverse",
# "hunt", "addjob", "rival", "pull", "patches", "inside"]), kept so the two records line up.
TESTS = [
    ("remove",  "Remove", "Remove each part. Does it still do every job? Then remove parts in pairs and groups."),
    ("swap",    "Swap", "Swap each part for a near neighbour. If the swap works, name what the two versions share."),
    ("flip",    "Flip the outcome", "Had the opposite happened, could the same explanation have covered it? "
                "Not for a derived conclusion: drop a condition instead."),
    ("poke",    "Poke", "For each part, name one change to the world that should alter the outcome and one that "
                "should not, the second next to the disputed line. Watch the part as well as the outcome."),
    ("reverse", "Reverse", "Poke the supposed cause and see if the effect moves; poke the effect and see that the "
                "cause does not."),
    ("hunt",    "Hunt the answer in the starting points", "Is the conclusion already sitting there under another name?"),
    ("addjob",  "Add a job", "Find something else that must also be so if the explanation is right. Which rival "
                "versions did the new job rule out?"),
    ("rival",   "Build the best rival", "Build the strongest different explanation, then find a change that tells "
                "the two apart."),
    ("pull",    "Pull", "Take the parts in pairs. Does making one stronger make another weaker? Name each pair, "
                "which gives way, where, and what would show the line was drawn in the wrong place."),
    ("patches", "Check the patches", "When it failed before, how was it rescued? A catch-all is allowed only with "
                "a gauge."),
    ("inside",  "Look inside", "Does it explain the workings or only what comes out?"),
]
TEST_IDS = [t[0] for t in TESTS]
TEST_BY_ID = {t[0]: t for t in TESTS}
