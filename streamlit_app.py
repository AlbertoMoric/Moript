import streamlit as st
import time
import random

# Nombre del asistente
assistant_name = "Moript"

# Función para generar respuesta personalizada
def response_generator(prompt):
    if "hola" in prompt.lower():
        return "¡Hola! ¿Cómo estás?"
    elif "qué tal" in prompt.lower():
        return "Todo bien, ¿y tú? ¿En qué puedo ayudarte?"
    elif "ayuda" in prompt.lower():
        return "Claro, ¿en qué necesitas ayuda?"
    elif "tu nombre" in prompt.lower():
        return f"Me llamo {assistant_name}, soy tu asistente virtual."
    elif "chiste" in prompt.lower():
        return "¿Sabías que el libro de matemáticas estaba triste? Porque tenía demasiados problemas 😂"
    else:
        return "No estoy seguro de qué decir, pero ¡estoy aquí para ayudarte!"

# Función para mostrar opciones de menú
def show_options():
    options = ["Ver clima", "Contar chiste", "Preguntar sobre mí", "Ayuda"]
    return st.selectbox("¿Qué te gustaría hacer?", options)

# Inicializar el historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

# Título del asistente
st.title(f"{assistant_name} V_0.1")  

# Mostrar los mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Mostrar un selectbox con opciones para interactuar
selected_option = show_options()

# Mostrar la respuesta según la opción seleccionada
if selected_option:
    if selected_option == "Ver clima":
        # Aquí podrías integrar una API de clima, por ejemplo
        response_text = "El clima está soleado hoy 🌞."
    elif selected_option == "Contar chiste":
        response_text = "¿Sabías que el libro de matemáticas estaba triste? Porque tenía demasiados problemas 😂"
    elif selected_option == "Preguntar sobre mí":
        response_text = f"Soy {assistant_name}, tu asistente virtual. Estoy aquí para ayudarte."
    elif selected_option == "Ayuda":
        response_text = "Puedo ayudarte con muchas cosas. ¿Qué te gustaría saber?"

    # Mostrar la respuesta del asistente después de seleccionar la opción
    with st.chat_message("assistant"):
        st.markdown(f"{assistant_name}: {response_text}")
    
    # Agregar la respuesta del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": f"{assistant_name}: {response_text}"})

# Aceptar entrada del usuario (en caso de que el usuario quiera escribir algo)
if prompt := st.chat_input("Mera cabra dimeloo"):
    # Agregar el mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Mostrar el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(prompt)

    # Crear un espacio vacío para el mensaje de "Escribiendo..."
    typing_placeholder = st.empty()

    # Mostrar "Escribiendo..." de manera dinámica (puntos suspensivos)
    typing_placeholder.markdown(f"**{assistant_name} está pensando...**")

    # Simula un pequeño retraso antes de mostrar la respuesta completa
    time.sleep(2)  # Puedes ajustar este tiempo de retraso para que se vea más natural
    
    # Generar la respuesta completa del asistente según el input
    response_text = response_generator(prompt)

    # Limpiar el mensaje de "Escribiendo..."
    typing_placeholder.empty()

    # Mostrar la respuesta del asistente después del retraso
    with st.chat_message("assistant"):
        st.markdown(f"{assistant_name}: {response_text}")
    
    # Agregar la respuesta del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": f"{assistant_name}: {response_text}"})

# Botón para descargar el historial de conversación
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
    st.experimental_rerun()  # Recargar la página para limpiar el chat
