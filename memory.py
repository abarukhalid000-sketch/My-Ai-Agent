conversation_history = []
user_memory = {}


def remember(role, message):
    conversation_history.append({
        "role": role,
        "content": message
    })

    # Remember the user's name
    if role == "user":
        words = message.split()

        for i, word in enumerate(words):
            if word.lower() in ["name", "called"]:
                if i + 2 < len(words) and words[i + 1].lower() == "is":
                    user_memory["name"] = words[i + 2].strip(".,!?")

                elif i + 1 < len(words):
                    user_memory["name"] = words[i + 1].strip(".,!?").title()


def get_memory():
    return conversation_history


def get_user_memory():
    return user_memory