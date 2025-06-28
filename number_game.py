# Streamlit을 이용한 1부터 100까지 숫자 맞추기 게임
import streamlit as st
import random

st.title("1부터 100까지 숫자 맞추기 게임")

if 'answer' not in st.session_state:
    st.session_state['answer'] = random.randint(1, 100)
    st.session_state['attempts'] = 0
    st.session_state['game_over'] = False

def reset_game():
    st.session_state['answer'] = random.randint(1, 100)
    st.session_state['attempts'] = 0
    st.session_state['game_over'] = False

st.button('게임 리셋', on_click=reset_game)

if not st.session_state.get('game_over', False):
    guess = st.number_input("숫자를 입력하세요 (1~100)", min_value=1, max_value=100, step=1, key='guess_input')
    if st.button("제출"):
        st.session_state['attempts'] += 1
        if guess < st.session_state['answer']:
            st.info("더 큰 숫자입니다.")
        elif guess > st.session_state['answer']:
            st.info("더 작은 숫자입니다.")
        else:
            st.success(f"정답입니다! 시도 횟수: {st.session_state['attempts']}")
            st.session_state['game_over'] = True
else:
    st.success(f"게임이 종료되었습니다! 정답: {st.session_state['answer']}, 시도 횟수: {st.session_state['attempts']}")
    st.info("'게임 리셋' 버튼을 눌러 새 게임을 시작하세요.")
