import streamlit as st
import random

st.title("1부터 100까지 숫자 맞추기 게임")

if 'answer' not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.result = ""

def reset_game():
    st.session_state.answer = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.result = ""

st.button("게임 리셋", on_click=reset_game)

guess = st.number_input("1부터 100 사이의 숫자를 입력하세요.", min_value=1, max_value=100, step=1)

if st.button("확인"):
    st.session_state.tries += 1
    if guess < st.session_state.answer:
        st.session_state.result = "더 큰 숫자입니다."
    elif guess > st.session_state.answer:
        st.session_state.result = "더 작은 숫자입니다."
    else:
        st.session_state.result = f"정답입니다! 시도 횟수: {st.session_state.tries}"

st.write(st.session_state.result)

