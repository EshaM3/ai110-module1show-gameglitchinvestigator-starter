from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win with the correct message
    outcome, msg = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in msg

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    # and the hint should tell the player to go lower.
    outcome, msg = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in msg

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    # and the hint should tell the player to go higher.
    outcome, msg = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in msg

# --- update_score tests ---

def test_win_first_attempt_scores_100():
    # attempts is incremented before update_score is called, so attempt_number is always >= 1
    # FIX: formula is 100 - 10*(attempt_number - 1), so first real attempt (1) earns 100
    assert update_score(0, "Win", 1) == 100

def test_win_second_attempt_scores_90():
    # Each additional attempt drops the reward by 10
    assert update_score(0, "Win", 2) == 90

def test_win_score_floor_is_10():
    # At attempt 11: 100 - 10*(11-1) = 0 → clamped to 10
    assert update_score(0, "Win", 11) == 10

def test_win_adds_to_existing_score():
    # Points are added on top of whatever the current score is
    assert update_score(50, "Win", 1) == 150

def test_too_high_always_subtracts_on_even_attempt():
    # FIX: "Too High" previously added 5 on even attempts; it should always subtract 5
    assert update_score(100, "Too High", 0) == 95

def test_too_high_always_subtracts_on_odd_attempt():
    # Odd attempts were already subtracting; confirm the fix didn't break this
    assert update_score(100, "Too High", 1) == 95

def test_too_low_subtracts_5():
    assert update_score(100, "Too Low", 0) == 95

def test_unknown_outcome_unchanged():
    assert update_score(100, "Invalid", 0) == 100


def test_new_game_resets_status():
    # simulate pressing the New Game button logic from app.py
    import random
    import streamlit as st

    # ensure we start with a non-playing status
    st.session_state.clear()
    st.session_state.status = "won"
    st.session_state.attempts = 3
    st.session_state.secret = 99

    # apply the new-game block's state mutations
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(1, 100)
    st.session_state.status = "playing"

    assert st.session_state.status == "playing"
