import streamlit as st
import random
import time

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Que dicesss! Que tienes pensado para hoy?",
            "Que pasa cachorrita, estoy para lo que necesites!",
            "Necesitas que te ayude en algo?",
        ]
    )
    return response  # Regresamos toda la respuesta a la vez, sin dividirla palabra por palabra


st.title("Moript V_0.1")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Mera cabra dimeloo"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Crear un espacio vacío para el mensaje de "Escribiendo..."
    typing_placeholder = st.empty()

    # Mostrar "Escribiendo..." mientras el asistente genera la respuesta
    typing_placeholder.markdown("**Dejame que de un pensamiento...**")

    # Simula un pequeño retraso antes de mostrar la respuesta completa
    time.sleep(10)  # Puedes ajustar este tiempo de retraso para que se vea más natural
    
    # Generar la respuesta completa del asistente
    response_text = response_generator()

    # Limpiar el mensaje de "Escribiendo..."
    typing_placeholder.empty()

    # Mostrar la respuesta del asistente después del retraso
    with st.chat_message("assistant"):
        st.markdown(response_text)
    
    # Agregar la respuesta del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": response_text})

# Botón para que el usuario califique la respuesta
#'''if st.session_state.messages and st.session_state.messages[-1]["role"] == "assistant":
#    rating = st.radio("Te queda clarinete?", options=["👍", "👎"])
#    if rating:
#        st.session_state.messages.append({"role": "user", "content": f"Rating: {rating}"})'''

# Botón para limpiar el historial de chat
if st.button("Clear chat"):
    st.session_state.messages = []
    st.rerun()

# Descargar historial de chat
if st.button("Download chat history"):
    chat_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
    st.download_button(
        label="Download as text file",
        data=chat_history,
        file_name="chat_history.txt",
        mime="text/plain"
    )
