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

for i in range(9):
    if st.button(game.board[i] or " ", key=i):
        if game.make_move(i, "X"):
            tracker.log_move(i)
            ai.record_player_move(i)
            log_move("X", i)

            if not game.current_winner:
                ai_move = ai.choose_move(game)
                game.make_move(ai_move, "O")
                log_move("O", ai_move)

st.write("Board:", game.board)

if game.current_winner:
    st.success(f"Winner: {game.current_winner}")
