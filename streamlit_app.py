import streamlit as st
import clips
import logging

#setup working environment 
logging.basicConfig(leverl=15,format='%(message)s')

env=clips.Environment()
router=clips.LoggingRouter()
env.add_router(router)

#input
name=st.text input ("Enter your name")

#knowledge base
env.build('(deftemplate result(sul)
