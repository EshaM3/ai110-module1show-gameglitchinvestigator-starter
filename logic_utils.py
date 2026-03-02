def get_range_for_difficulty(difficulty: str):
    #FIX: Refactored get_range_for_difficulty into logic_utils.py using Copilot Agent mode
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    # FIX: Difficulty fixed manually (straightforward solution)
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str, low: int, high: int):
    #FIX: Refactored parse_guess into logic_utils.py using Copilot Agent mode
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    #FIX: Refactored and modified check_guess into logic_utils.py using Copilot Agent mode
    """
    The old implementation tried to alternate the type of `secret` between
    `int` and `str` and even wrapped the comparison in a `try/except` block.
    That behavior was causing the secret number to appear to change, so we
    always treat the secret as an integer and use straightforward
    comparisons.  If the guess is too high, we tell the player to go lower;
    if the guess is too low, we tell the player to go higher.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📈 Go LOWER!"
    else:
        # guess < secret
        return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    #FIX: Refactored update_score into logic_utils.py using Copilot Agent mode
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # FIX: Scoring formula fixed so that you lose points after the first guess. Not immediately. Done manually (straightforward solution) but with insight from Claude Code.
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    # FIX: "Too High" no longer alternates between adding and subtracting points. Completed manually (straightforward solution) but with insight from Claude Code.
    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
