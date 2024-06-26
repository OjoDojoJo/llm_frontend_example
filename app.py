import streamlit as st
import requests

headers = {
    "Content-Type": "application/json",
}
st.title('🦜🔗 My Chatbot')

def run_model_request(text):
    text_input = f"Answer the following question as concisely as possible: {text}"
    request_json = {"inputs" : text_input, "parameters":{"max_new_tokens":6}}
    resp = requests.post(f"http://tgi-server/generate", json=request_json, headers=headers)
    resp_json = resp.json()["generated_text"]
    return resp_json

with st.form('my_form'):
    text = st.text_area('Enter a question')
    submitted = st.form_submit_button('Submit')
    if len(text) > 0 and submitted:
        st.session_state.disabled = True
        output_text = ""
        with st.spinner("Please wait"):
            output_text = run_model_request(text)
        st.info(output_text)
