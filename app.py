import streamlit as st
from game_logic import Game
from ai_engine import AdaptiveAI
from player_tracker import PlayerTracker
from data_logger import log_move

st.title("🧠 MindGrid – Adaptive AI Game")

if "game" not in st.session_state:
    st.session_state.game = Game()
    st.session_state.ai = AdaptiveAI()
    st.session_state.tracker = PlayerTracker()

game = st.session_state.game
ai = st.session_state.ai
tracker = st.session_state.tracker

# Create 3 rows
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        index = row * 3 + col
        with cols[col]:
            if st.button(game.board[index] or " ", key=index):
                if game.make_move(index, "X"):
                    tracker.log_move(index)
                    ai.record_player_move(index)
                    log_move("X", index)

                    if not game.current_winner and game.available_moves():
                        ai_move = ai.choose_move(game)
                        game.make_move(ai_move, "O")
                        log_move("O", ai_move)


st.write("Board:", game.board)

if game.current_winner:
    st.success(f"Winner: {game.current_winner}")

