import streamlit as st
from streamlit_image_select import image_select
#Title
st.title('SafePass')
st.subheader("One Place to Secure Your Passwords")
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 370px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

#pages
menu = ["Home","Signup","Login"]
choice = st.sidebar.selectbox("Menu",menu)
if choice=="Home":
    testp="<p style='font-size:20px'>SafePass is the easier, safer way to unlock your digital world. It’s an application you can download on all your PC to remove the hassle of passwords. Get started by logging in to the Master password app using unique factors image. From there, the app works quietly in the background to make your current passwords stronger, remembers them and instantly logs you in so you don’t have to. </p>"
    st.markdown(testp, unsafe_allow_html=True)
    st.image("main.gif")
    
if choice=="Signup":
    st.text("Welcome Signup")
    Fname=st.text_input("First Name")
    Lname=st.text_input("Last Name")
    Email=st.text_input("Email")
    Mobile=st.text_input("Mobile")
    Password=st.text_input("Passwod",type="password")
    st.text_input("Confirm Password",type="password")
    rn = [1,2,4,6]
    img = image_select(
        label="Select Hide Image",
        images=[
            "images/"+str(rn[0])+".jpg",
            "images/"+str(rn[1])+".jpg",
            "images/"+str(rn[2])+".jpg",
            "images/"+str(rn[3])+".jpg",
        ],
    )
    b=st.button("Submit")
    if b:
        st.success("Success")


if choice=="Login":    
    Email=st.sidebar.text_input("Email")
    ss=st.sidebar.text_input("OTP",type="password")
    rn = [2,1,6,4]
    with st.sidebar:     
        img1 = image_select(
            label="Select Password Image",
            images=[
                "images/"+str(rn[0])+".jpg",
                "images/"+str(rn[1])+".jpg",
                "images/"+str(rn[2])+".jpg",
                "images/"+str(rn[3])+".jpg",
            ],
        )
    if st.sidebar.checkbox("Login"):
        st.success("Login Sucess")
        sts=st.text_input("Enter Delete Site")
        if st.button("Delete"):
            st.success("Deleted Sucess")
        site=st.text_input("Site")
        user=st.text_input("Email/Password")
        pss=st.text_input("Password",type="password")
        if st.button("Add to database"):
            st.success("database update Sucess")


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
