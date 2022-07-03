# Li Fo => Last In - First Out

# stack like we have browsing session, where we can visit the last session, and wanna backward to previous session
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

last = browsing_session.pop()
print("current session", last)

print(browsing_session)
print("redirect previous session to", browsing_session[-1])


if not browsing_session:
    print("disable")

# conlusion this operations that perform on stacks
browsing_sessions = []
browsing_sessions.append(1)
# browsing_sessions.append(2)
browsing_sessions.pop()
# check empty or not, is empty, return error
if not browsing_sessions:
    browsing_sessions[-1]
