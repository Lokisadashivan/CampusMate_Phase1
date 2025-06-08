# response.py
def get_response(intent):
    responses = {
        
        # New responses
      "CLASS_TIME": "Your next class is at 10 AM in Lecture Hall A.",
        "LIBRARY": "The library is in Building B, 2nd Floor.",
        "CONTACT": "You can contact your lecturer via email on the course portal or ask during tutorial hours.",
        "EVENTS": "This week’s events include a coding bootcamp and cultural fest.",
        "RESET_PW": "Visit the IT helpdesk portal to reset your university password.",
        "GREETING": "Hello! How can I assist you today?",
        "CAFETERIA": "The cafeteria is next to the admin block and open from 8 AM to 6 PM.",
        "COLLEGE_INFO": "College is open from 8 AM to 5 PM on weekdays.",
        "CAMPUS_MAP": "You can view the campus map at the main entrance or on the student portal."
    }
    return responses.get(intent, "Sorry, I didn't understand your question.")
