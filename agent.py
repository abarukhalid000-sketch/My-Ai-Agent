import ollama

MODEL = "llama3.2:1b"

print("🤖 Local Study Assistant")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful study assistant. Explain things simply to a beginner."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response["message"]["content"]

    print("\nAgent:", answer)
    print()
    import ollama
from tools import calculator

MODEL = "llama3.2:1b"

print("🤖 Local Study Assistant")
print("Type 'exit' to quit.")
print("Try: calculate 25 * 40\n")


def handle_calculation(question):
    parts = question.lower().replace("calculate", "").strip().split()

    if len(parts) != 3:
        return None

    try:
        a = float(parts[0])
        operation = parts[1]
        b = float(parts[2])
    except ValueError:
        return None

    if operation == "+":
        result = calculator(a, b, "add")

    elif operation == "-":
        result = calculator(a, b, "subtract")

    elif operation == "*":
        result = calculator(a, b, "multiply")

    elif operation == "/":
        result = calculator(a, b, "divide")

    else:
        return None

    return result


while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # THINK: Does this require the calculator?
    calculation = handle_calculation(question)

    if calculation is not None:
        print("Agent: 🧮 I'll use the calculator.")
        print("Agent:", calculation)
        continue

    # ACT: Ask the local AI model
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful study assistant. "
                    "Explain topics simply to a beginner."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response["message"]["content"]

    # ANSWER
    print("\nAgent:", answer)
    print()
    import ollama
from tools import calculator
from memory import remember, get_memory, get_user_memory

MODEL = "llama3.2:1b"

print("🤖 Local Study Assistant")
print("Type 'exit' to quit.\n")


while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Save the user's message
    remember("user", question)

    # Send the conversation to the AI
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful study assistant. "
                    "Explain topics simply to a beginner."
                )
            },
            *get_memory()
        ]
    )

    # Get the AI's answer
    answer = response["message"]["content"]

# Check if the user is asking for their name
if "what is my name" in question.lower():
    user_memory = get_user_memory()

    if "name" in user_memory:
        answer = f"Your name is {user_memory['name']}."

    # Save the AI's answer
    remember("assistant", answer)

    print("\nAgent:", answer)
    print()
    