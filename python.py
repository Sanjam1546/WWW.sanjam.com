from flask import Flask, render_template, request

app = Flask(__name__)

def get_vote_input():
    """
    Function to get input for voting.

    Returns:
        str: The selected option for voting.
    """
    print("Please select your vote:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice in [1, 2, 3]:
                return f"Option {choice}"
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number (1/2/3).")

@app.route('/', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        vote = get_vote_input()
        return f"You voted for: {vote}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
