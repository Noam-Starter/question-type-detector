question = input("Ask a question: ")

if "when" in question:
    print("This is a time-related question.")
elif "what is" in question or "define" in question:
    print("This is a definition question.")
elif "why" in question:
    print("This is a question about cause.")
else:
    print("I couldn't understand the question type.")