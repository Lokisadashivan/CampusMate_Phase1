# matcher_setup.py
from spacy.matcher import Matcher

def create_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    # CLASS_TIME
    matcher.add("CLASS_TIME", [
        [{"LOWER": "next"}, {"LOWER": "class"}],
        [{"LOWER": "class"}, {"LOWER": "time"}],
        [{"LOWER": "when"}, {"LOWER": "class"}]
    ])

    # LIBRARY
    matcher.add("LIBRARY", [
        [{"LOWER": "where"}, {"LOWER": "library"}],
        [{"LOWER": "library"}]
    ])

    # CONTACT
    matcher.add("CONTACT", [
        [{"LOWER": "contact"}, {"LOWER": "lecturer"}],
        [{"LOWER": "how"}, {"LOWER": "contact"}, {"LOWER": "lecturer"}],
        [{"LOWER": "email"}, {"LOWER": "lecturer"}],
        [{"LOWER": "contact"}],
        [{"LOWER": "how"}, {"LOWER": "contact"}, {"LOWER": "faci"}],
        [{"LOWER": "faci"}],
        [{"LOWER": "doubt"}]
    ])

    # EVENTS
    matcher.add("EVENTS", [
        [{"LOWER": "events"}],
        [{"LOWER": "any"}, {"LOWER": "events"}],
        [{"LOWER": "recent"}, {"LOWER": "events"}],
        [{"LOWER": "this"}, {"LOWER": "week"}, {"LOWER": "events"}]
    ])

    # RESET_PW
    matcher.add("RESET_PW", [
        [{"LOWER": "reset"}, {"LOWER": "password"}],
        [{"LOWER": "forgot"}, {"LOWER": "password"}],
        [{"LOWER": "change"}, {"LOWER": "password"}]
    ])

    # GREETING
    matcher.add("GREETING", [
        [{"LOWER": "hello"}],
        [{"LOWER": "hi"}],
        [{"LOWER": "hey"}],
        [{"LOWER": "good"}, {"LOWER": "morning"}],
        [{"LOWER": "good"}, {"LOWER": "afternoon"}],
        [{"LOWER": "good"}, {"LOWER": "evening"}]
    ])

    # CAFETERIA
    matcher.add("CAFETERIA", [
        [{"LOWER": "where"}, {"LOWER": "cafeteria"}],
        [{"LOWER": "cafeteria"}],
        [{"LOWER": "cafe"}],
        [{"LOWER": "any"}, {"LOWER": "cafe"}]
    ])

    # COLLEGE_INFO
    matcher.add("COLLEGE_INFO", [
        [{"LOWER": "college"}, {"LOWER": "hours"}],
        [{"LOWER": "college"}, {"LOWER": "timing"}],
        [{"LOWER": "what"}, {"LOWER": "time"}, {"LOWER": "college"}],
        [{"LOWER": "college"}],
        [{"LOWER": "how"}, {"LOWER": "about"}, {"LOWER": "college"}, {"LOWER": "hours"}],
        [{"LOWER": "college"}, {"LOWER": "open"}]
    ])

    # CAMPUS_MAP
    matcher.add("CAMPUS_MAP", [
        [{"LOWER": "campus"}, {"LOWER": "map"}],
        [{"LOWER": "map"}],
        [{"LOWER": "where"}, {"LOWER": "map"}],
        [{"LOWER": "how"}, {"LOWER": "about"}, {"LOWER": "campus"}, {"LOWER": "map"}]
    ])

    return matcher
