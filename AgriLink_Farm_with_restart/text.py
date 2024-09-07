notify_briefing = '''AgriLink: Good morning, {0} \n\nAs of {1}, you have:\n\n{2}👋🏼 Do not hesitate to use our 24/7 support line in case of any questions or concerns\n\nAgriLink is here to assist you'''
notify_empty = '''AgriLink: Good morning, {0} \n\nAs of {1},\n\nYou do not have any outstanding tasks. Great job!\n\n👋🏼 Do not hesitate to use our 24/7 support line in case of any questions or concerns'''
notify_upcoming = '''AgriLink: 💤\n\nDo not forget about the upcoming *{0}* scheduled for *{1}*. Check your calendar to learn more about the task!'''
notify_outstanding = '''AgriLink: 🚀\n\nDo not forget to completed the outstanding *{0}* before *{1}*. Check your calendar to learn more about the task!'''
notify_overdue = '''AgriLink: 🚨\n\nUnfortunately, we have not received a confirmation of completion for *{0}*. You are *{1}* days past the preferred end day, so try your best to complete it as soon as possible.\n\nCheck your calendar to learn more about the task!'''
calendar = '''Here you can keep track of your tasks and crop growth stages 🗓️\n\nUse arrows for navigation, or press ‘back’ to return to the menu.\n\n*Select a category to learn more:*'''
help = '''If you have any questions, first create a conversation on this topic by clicking *Create new problem*\n\n \
Then you can start or continue chatting about your problems by clicking *Chating* and selecting the problem\n\n \
If you have no more questions on the topic, you can delete the conversation'''
start_new_problem = '''Thank you! Now, explain the problem in greater details. Feel free to upload any supporting images (up to 5).\nPress *‘Submit’* to send the description off to an agronomist, otherwise press *‘Back’* to return to the help menu.'''
start_new_record = '''Thank you! Now, explain the record in greater details. Feel free to upload any supporting images (up to 5).\nPress *‘Submit’* to send the description off, otherwise press *‘Back’* to return to the help menu.'''
support = '''Hi {0}, I’m sorry to hear you are experiencing issues. Luckily, we have a dedicated team of agronomists to offer their help!\n\nPress *‘New problem’* to raise a new issue, otherwise press *‘Existing problems’* to explore your present issues.'''
notify_sent = '''Hi {0}, our agronomist has responded to you about *{1}*, *{2}*. You can resume the conversation by replying through our *‘Agronomist Support’* service.\n\n⚠️ Respond within the next three days, otherwise the problem would resolve itself automatically. If you need more time, just let the agronomist know!'''
solved_problem = '''Hi {0}, you have recently raised a problem *{1}, {2}* with your agronomist. It would really help us if you could rate the conversation and your experience.\n\nRespond with one of the numbers below:\n\n*5* - excellent \n*4* - good \n*3* - okay\n*2* - poor \n*1* - very bad'''
bad_grade_text = '''I am sorry to hear you were unhappy with the experience of using our agronomist support line 😔\n\nCould you let us know what we could do better?\n\nJust type in your response and press Submit, otherwise press Skip.'''


def msg_from_chating(doc, black=False):
    doc = doc.to_dict()
    if black:
        msg = f"*_{doc['person']}_\n_{doc['time'].strftime('%Y-%m-%d %H:%M:%S')}_\n\n{doc['text']}*"
    else:
        msg = f"_{doc['person']}_\n_{doc['time'].strftime('%Y-%m-%d %H:%M:%S')}_\n\n{doc['text']}"
    return msg

def img_from_chating(doc, black=False):
    doc = doc.to_dict()
    if black:
        msg = f"*_{doc['person']}_\n_{doc['time'].strftime('%Y-%m-%d %H:%M:%S')}_*"
    else:
        msg = f"_{doc['person']}_\n_{doc['time'].strftime('%Y-%m-%d %H:%M:%S')}_"
    return msg
