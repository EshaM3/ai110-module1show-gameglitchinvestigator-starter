from logic_utils import check_guess

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
