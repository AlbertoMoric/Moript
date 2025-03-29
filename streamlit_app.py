import streamlit as st
import random
import time

# Nombre del asistente
assistant_name = "Moript"

# Respuestas predeterminadas basadas en el input del usuario
def response_generator(prompt):
    # Respuestas simples basadas en el input del usuario
    if "hola" in prompt.lower():
        return "¡Hola! ¿Cómo estás?"
    elif "qué tal" in prompt.lower():
        return "Todo bien, ¿y tú? ¿En qué puedo ayudarte?"
    elif "ayuda" in prompt.lower():
        return "Claro, ¿en qué necesitas ayuda?"
    elif "tu nombre" in prompt.lower():
        return f"Me llamo {assistant_name}, soy tu asistente virtual."
    else:
        return "No estoy seguro de qué decir, pero ¡estoy aquí para ayudarte!"

st.title(f"{assistant_name} V_0.1")  # Nombre del asistente en el título

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Mostrar el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(prompt)

# Accept user input
if prompt := st.chat_input("Mera cabra dimeloo"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Crear un espacio vacío para el mensaje de "Escribiendo..."
    typing_placeholder = st.empty()

   # Mostrar "Escribiendo..." de manera más dinámica (puntos suspensivos)
    typing_placeholder.markdown(f"**{assistant_name} está pensando...**")

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

# Descargar historial de chat
if st.button("Guardar conversacion"):
    chat_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
    st.download_button(
        label="Guardar como texto",
        data=chat_history,
        file_name="chat_history.txt",
        mime="text/plain"
    )

# Botón para limpiar el historial de chat
if st.button("Clear chat"):
    st.session_state.messages = []
    st.rerun()
