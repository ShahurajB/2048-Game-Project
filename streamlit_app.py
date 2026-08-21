import copy
import numpy as np
import streamlit as st

import globals
from Models import (
    left_move,
    right_move,
    top_move,
    down_move,
    generate_random_number,
    check_game_over,
    is_array_full,
    undo_function,
    redo_function,
)


st.set_page_config(
    page_title="2048-Game",
    page_icon="🎮",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Session-state bridge
#
# Your original game uses module-level state in globals.py.
# We do NOT refactor that code. Streamlit reruns the Python script after
# every button click, so we copy the current game state into Streamlit's
# session state before each rerun and restore it before calling your
# original movement/undo/redo functions.
# ---------------------------------------------------------------------------

def save_globals_to_session():
    st.session_state.board = globals.arr.copy()
    st.session_state.score = int(globals.score)
    st.session_state.undo_arr = [x.copy() for x in globals.undo_arr]
    st.session_state.redo_arr = [x.copy() for x in globals.redo_arr]
    st.session_state.undo_score = list(globals.undo_score)
    st.session_state.redo_score = list(globals.redo_score)


def restore_globals_from_session():
    globals.arr = st.session_state.board.copy()
    globals.score = st.session_state.score
    globals.undo_arr = [x.copy() for x in st.session_state.undo_arr]
    globals.redo_arr = [x.copy() for x in st.session_state.redo_arr]
    globals.undo_score = list(st.session_state.undo_score)
    globals.redo_score = list(st.session_state.redo_score)


def initialize_game():
    st.session_state.board = np.zeros((4, 4), dtype=int)
    st.session_state.score = 0
    st.session_state.undo_arr = []
    st.session_state.redo_arr = []
    st.session_state.undo_score = []
    st.session_state.redo_score = []

    restore_globals_from_session()
    generate_random_number()
    generate_random_number()
    save_globals_to_session()


def new_game():
    initialize_game()


def perform_move(move_function):
    restore_globals_from_session()

    moved = move_function()

    # Your original game adds a new tile only after a successful move.
    if moved:
        generate_random_number()

    save_globals_to_session()

    if check_game_over():
        st.session_state.won = True


def perform_undo():
    restore_globals_from_session()
    undo_function()
    save_globals_to_session()


def perform_redo():
    restore_globals_from_session()
    redo_function()
    save_globals_to_session()


if "board" not in st.session_state:
    initialize_game()

if "won" not in st.session_state:
    st.session_state.won = False


# ---------------------------------------------------------------------------
# Styling - CSS is embedded only for visual appearance. No JavaScript is used.
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .game-title {
        text-align: center;
        font-size: 72px;
        font-weight: 900;
        color: #776e65;
        margin-bottom: 0;
    }

    .game-subtitle {
        text-align: center;
        color: #776e65;
        margin-top: -12px;
        margin-bottom: 20px;
    }

    div[data-testid="stButton"] button {
        width: 100%;
        min-height: 46px;
        border-radius: 8px;
        font-weight: 700;
    }

    .tile {
        aspect-ratio: 1 / 1;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        font-weight: 800;
        background: #cdc1b4;
        color: #776e65;
    }

    .tile-2 { background: #eee4da; }
    .tile-4 { background: #ede0c8; }
    .tile-8 { background: #f2b179; color: #f9f6f2; }
    .tile-16 { background: #f59563; color: #f9f6f2; }
    .tile-32 { background: #f67c5f; color: #f9f6f2; }
    .tile-64 { background: #f65e3b; color: #f9f6f2; }
    .tile-128 { background: #edcf72; color: #f9f6f2; font-size: 28px; }
    .tile-256 { background: #edcc61; color: #f9f6f2; font-size: 28px; }
    .tile-512 { background: #edc850; color: #f9f6f2; font-size: 28px; }
    .tile-1024 { background: #edc53f; color: #f9f6f2; font-size: 23px; }
    .tile-2048 { background: #edc22e; color: #f9f6f2; font-size: 23px; }

    .board {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        background: #bbada0;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 12px;
        max-width: 450px;
        margin-left: auto;
        margin-right: auto;
    }

    .status {
        text-align: center;
        font-size: 22px;
        font-weight: 800;
        color: #776e65;
        padding: 10px;
    }

    @media (max-width: 600px) {
        .game-title { font-size: 56px; }
        .tile { font-size: 24px; }
        .tile-128, .tile-256, .tile-512 { font-size: 21px; }
        .tile-1024, .tile-2048 { font-size: 17px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="game-title">2048</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="game-subtitle">Python version — powered by YaanTechKnow </div>',
    unsafe_allow_html=True,
)

score_col, best_col = st.columns(2)
with score_col:
    st.metric("SCORE", st.session_state.score)
with best_col:
    best = max(
        st.session_state.score,
        st.session_state.get("best_score", 0),
    )
    st.session_state.best_score = best
    st.metric("BEST", best)


# Top controls
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🔄 New Game", use_container_width=True):
        new_game()
        st.rerun()

with c2:
    if st.button("↩ Undo", use_container_width=True):
        perform_undo()
        st.rerun()

with c3:
    if st.button("↪ Redo", use_container_width=True):
        perform_redo()
        st.rerun()


# Board
board_html = ['<div class="board">']
for row in st.session_state.board:
    for value in row:
        value = int(value)
        label = "" if value == 0 else str(value)
        tile_class = "tile" if value == 0 else f"tile tile-{value}"
        board_html.append(
            f'<div class="{tile_class}">{label}</div>'
        )
board_html.append("</div>")

st.markdown(
    "".join(board_html),
    unsafe_allow_html=True,
)


# Python Streamlit buttons — no custom JavaScript.
st.markdown("### Controls")

up = st.columns([1, 1, 1])
with up[1]:
    if st.button("⬆ UP", key="up", use_container_width=True):
        perform_move(top_move)
        st.rerun()

middle = st.columns([1, 1, 1])
with middle[0]:
    if st.button("⬅ LEFT", key="left", use_container_width=True):
        perform_move(left_move)
        st.rerun()

with middle[1]:
    if st.button("⬇ DOWN", key="down", use_container_width=True):
        perform_move(down_move)
        st.rerun()

with middle[2]:
    if st.button("➡ RIGHT", key="right", use_container_width=True):
        perform_move(right_move)
        st.rerun()


if check_game_over():
    st.markdown(
        '<div class="status">🎉 Congratulations! You reached 2048!</div>',
        unsafe_allow_html=True,
    )

if is_array_full() and not check_game_over():
    st.markdown(
        '<div class="status">Game Over — start a new game!</div>',
        unsafe_allow_html=True,
    )

st.markdown("---")
st.caption(
    "Powered by YaanTechKnow."
)