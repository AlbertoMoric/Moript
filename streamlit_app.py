import streamlit as st
import random
import time


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Mostrar "Escribiendo..." mientras el asistente genera la respuesta
    with st.chat_message("assistant"):
        st.markdown("**Assistant is typing...**")
    
    # Ahora, después de un breve retraso, mostrar la respuesta del asistente
    time.sleep(1)  # Puedes ajustar el tiempo para controlar el retraso
    response_text = ""
    for word in response_generator():
        response_text += word
        st.markdown(response_text)
    
    # Agregar la respuesta del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": response_text})
