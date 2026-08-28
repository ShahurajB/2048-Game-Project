import numpy as np
import streamlit as st
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import configs.globals as globals
from engine import (
    left_move,
    right_move,
    top_move,
    down_move,
    generate_random_number,
    has_won,
    is_board_full,
    undo_function,
    redo_function,
)


st.set_page_config(
    page_title="2048-Game",
    page_icon="🎮",
    layout="centered",
)

image = "images/Logo.png"
st.logo(image, size="large")

# ---------------------------------------------------------------------------
# Session-state bridge
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

    if has_won():
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
# Styling - CSS is embedded only for visual appearance.
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>

    /* Reduce overall Streamlit spacing */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 600px;
    }

    /* Reduce vertical spacing between elements */
    div[data-testid="stVerticalBlock"] {
        gap: 0.35rem;
    }

    /* Title */
    .game-title {
        text-align: center;
        font-size: 30px;
        font-weight: 600;
        color: #776e65;
        margin: 0;
        padding: 0;
        line-height: 1.0;
    }

    .game-subtitle {
        text-align: center;
        color: #776e65;
        font-size: 13px;
        margin: 0 0 4px 0;
        padding: 0;
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        padding: 0 !important;
        margin: 0 !important;
    }

    div[data-testid="stMetricLabel"] {
        font-size: 11px !important;
    }

    div[data-testid="stMetricValue"] {
        font-size: 20px !important;
    }

    /* Buttons */
    div[data-testid="stButton"] {
        margin: 0 !important;
        padding: 0 !important;
    }

    div[data-testid="stButton"] button {
        width: 100%;
        min-height: 38px;
        height: 38px;
        padding: 2px 5px;
        border-radius: 7px;
        font-size: 13px;
        font-weight: 700;
    }

    /* 2048 board */
    .board {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 5px;
        background: #bbada0;
        border-radius: 6px;
        padding: 5px;
        width: 220px;
        height: 220px;
        margin: 4px auto 5px auto;
        box-sizing: border-box;
    }

    /* Tiles */
    .tile {
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        font-weight: 600;
        background: #cdc1b4;
        color: #776e65;
    }

    .tile-2 {
        background: #eee4da;
    }

    .tile-4 {
        background: #ede0c8;
    }

    .tile-8 {
        background: #f2b179;
        color: #f9f6f2;
    }

    .tile-16 {
        background: #f59563;
        color: #f9f6f2;
    }

    .tile-32 {
        background: #f67c5f;
        color: #f9f6f2;
    }

    .tile-64 {
        background: #f65e3b;
        color: #f9f6f2;
    }

    .tile-128 {
        background: #edcf72;
        color: #f9f6f2;
        font-size: 14px;
    }

    .tile-256 {
        background: #edcc61;
        color: #f9f6f2;
        font-size: 14px;
    }

    .tile-512 {
        background: #edc850;
        color: #f9f6f2;
        font-size: 14px;
    }

    .tile-1024 {
        background: #edc53f;
        color: #f9f6f2;
        font-size: 12px;
    }

    .tile-2048 {
        background: #edc22e;
        color: #f9f6f2;
        font-size: 12px;
    }

    /* Game status */
    .game-message {
        text-align: center;
        font-size: 13px;
        font-weight: 700;
        padding: 3px;
        margin: 0;
    }

    .win-message {
        color: #2e7d32;
    }

    .over-message {
        color: #b71c1c;
    }

    /* Footer */
    .footer {
        text-align: center;
        font-size: 10px;
        color: #888;
        margin-top: 3px;
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

st.markdown("""
    <style>
    /* Make the game wrapper relative so the popup positions over it */
    .game-container {
        position: relative;
        width: 100%;
        max-width: 500px; /* Match your game board width */
        margin: 0 auto;
    }
    
    /* Absolute overlay positioning */
    .win-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(250, 248, 239, 0.9); /* Semi-transparent background */
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 999; /* Ensures it renders in front */
        border-radius: 8px;
    }

    /* Styled victory message */
    .status {
        color: #2e7d32; /* Rich green color */
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
    }
        /* Styled victory message */
    .over-status {
        color: #B71C1C; /* Dark Ruby Red color */
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)


if has_won():
    st.markdown("""
            <div class="game-container">
                <div class="win-overlay">
                    <div class="status">🎉 Congratulations!<br>You reached 2048!</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

if is_board_full() and not has_won():
    st.markdown("""
        <div class="game-container">
            <div class="win-overlay">
                <div class="over-status"> Game Over — start a new game!!</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption(
    "Powered by YaanTechKnow."
)