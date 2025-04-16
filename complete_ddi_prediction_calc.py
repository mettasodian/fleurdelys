import streamlit as st

#investigational drug physiological parameter
def calculate_Ih(Fa, Fg, ka, Rb, fup, MW, Qh, Cmax, dose):
    return fup * (Cmax + ( Fa * Fg * ka * (dose / MW ) / Qh / Rb))

#CYP1A2 Ah, Bh, Ch, AUCR
def calculate_CYP1A2ki(CYP1A2IC50, CYP1A2Km, CYP1A2S):
    return CYP1A2IC50 / (1 + (CYP1A2S / CYP1A2Km))

def calculate_CYP1A2Ah(CYP1A2Ih, CYP1A2ki):
    return 1 / (1 + (CYP1A2Ih / CYP1A2ki))

def calculate_CYP1A2Bh(CYP1A2kdegh, CYP1A2Ih, CYP1A2kinact, CYP1A2KI):
    if CYP1A2kdegh is None or CYP1A2kinact is None or CYP1A2KI is None or CYP1A2Ih == 0:
        return 1
    return CYP1A2kdegh / (CYP1A2kdegh + ((CYP1A2Ih * CYP1A2kinact) / (CYP1A2Ih + CYP1A2KI)))

def calculate_CYP1A2Ch(CYP1A2Emax, CYP1A2EC50, CYP1A2I):
    if CYP1A2Emax is None or CYP1A2EC50 is None or CYP1A2I is None:
        return 1
    return 1 + ((CYP1A2Emax - 1) * CYP1A2I / (CYP1A2I + CYP1A2EC50))

def calculate_CYP1A2AUCR(CYP1A2Ah, CYP1A2Bh, CYP1A2Ch, CYP1A2fm):
    return 1 / ((CYP1A2Ah * CYP1A2Bh * CYP1A2Ch * CYP1A2fm) + (1 - CYP1A2fm))

#CYP3A4 Ah, Bh, Ch, AUCR
def calculate_CYP3A4ki(CYP3A4IC50, CYP3A4Km, CYP3A4S):
    return CYP3A4IC50 / (1 + (CYP3A4S / CYP3A4Km))

def calculate_CYP3A4Ah(CYP3A4Ih, CYP3A4ki):
    return 1 / (1 + (CYP3A4Ih / CYP3A4ki))

def calculate_CYP3A4Bh(CYP3A4kdegh, CYP3A4Ih, CYP3A4kinact, CYP3A4KI):
    if CYP3A4kdegh is None or CYP3A4kinact is None or CYP3A4KI is None or CYP3A4Ih == 0:
        return 1
    return CYP3A4kdegh / (CYP3A4kdegh + ((CYP3A4Ih * CYP3A4kinact) / (CYP3A4Ih + CYP3A4KI)))

def calculate_CYP3A4Ch(CYP3A4Emax, CYP3A4EC50, CYP3A4I):
    if CYP3A4Emax is None or CYP3A4EC50 is None or CYP3A4I is None:
        return 1
    return 1 + ((CYP3A4Emax - 1) * CYP3A4I / (CYP3A4I + CYP3A4EC50))

def calculate_CYP3A4AUCR(CYP3A4Ah, CYP3A4Bh, CYP3A4Ch, CYP3A4fm):
    return 1 / ((CYP3A4Ah * CYP3A4Bh * CYP3A4Ch * CYP3A4fm) + (1 - CYP3A4fm))

#CYP2B6 Ah, Bh, Ch, AUCR 
def calculate_CYP2B6ki(CYP2B6IC50, CYP2B6Km, CYP2B6S):
    return CYP2B6IC50 / (1 + (CYP2B6S / CYP2B6Km))

def calculate_CYP2B6Ah(CYP2B6Ih, CYP2B6ki):
    return 1 / (1 + (CYP2B6Ih / CYP2B6ki))

def calculate_CYP2B6Bh(CYP2B6kdegh, CYP2B6Ih, CYP2B6kinact, CYP2B6KI):
    if CYP2B6kdegh is None or CYP2B6kinact is None or CYP2B6KI is None or CYP2B6Ih == 0:
        return 1
    return CYP2B6kdegh / (CYP2B6kdegh + ((CYP2B6Ih * CYP2B6kinact) / (CYP2B6Ih + CYP2B6KI)))

def calculate_CYP2B6Ch(CYP2B6Emax, CYP2B6EC50, CYP2B6I):
    if CYP2B6Emax is None or CYP2B6EC50 is None or CYP2B6I is None:
        return 1
    return 1 + ((CYP2B6Emax - 1) * CYP2B6I / (CYP2B6I + CYP2B6EC50))

def calculate_CYP2B6AUCR(CYP2B6Ah, CYP2B6Bh, CYP2B6Ch, CYP2B6fm):
    return 1 / ((CYP2B6Ah * CYP2B6Bh * CYP2B6Ch * CYP2B6fm) + (1 - CYP2B6fm))

#CYP2C19 Ah, Bh, Ch, AUCR
def calculate_CYP2C19ki(CYP2C19IC50, CYP2C19Km, CYP2C19S):
    return CYP2C19IC50 / (1 + (CYP2C19S / CYP2C19Km))

def calculate_CYP2C19Ah(CYP2C19Ih, CYP2C19ki):
    return 1 / (1 + (CYP2C19Ih / CYP2C19ki))

def calculate_CYP2C19Bh(CYP2C19kdegh, CYP2C19Ih, CYP2C19kinact, CYP2C19KI):
    if CYP2C19kdegh is None or CYP2C19kinact is None or CYP2C19KI is None or CYP2C19Ih == 0:
        return 1
    return CYP2C19kdegh / (CYP2C19kdegh + ((CYP2C19Ih * CYP2C19kinact) / (CYP2C19Ih + CYP2C19KI)))

def calculate_CYP2C19Ch(CYP2C19Emax, CYP2C19EC50, CYP2C19I):
    if CYP2C19Emax is None or CYP2C19EC50 is None or CYP2C19I is None:
        return 1
    return 1 + ((CYP2C19Emax - 1) * CYP2C19I / (CYP2C19I + CYP2C19EC50))

def calculate_CYP2C19AUCR(CYP2C19Ah, CYP2C19Bh, CYP2C19Ch, CYP2C19fm):
    return 1 / ((CYP2C19Ah * CYP2C19Bh * CYP2C19Ch * CYP2C19fm) + (1 - CYP2C19fm))

#CYP2C8 Ah, Bh, Ch, AUCR
def calculate_CYP2C8ki(CYP2C8IC50, CYP2C8Km, CYP2C8S):
    return CYP2C8IC50 / (1 + (CYP2C8S / CYP2C8Km))

def calculate_CYP2C8Ah(CYP2C8Ih, CYP2C8ki):
    return 1 / (1 + (CYP2C8Ih / CYP2C8ki))

def calculate_CYP2C8Bh(CYP2C8kdegh, CYP2C8Ih, CYP2C8kinact, CYP2C8KI):  
    if CYP2C8kdegh is None or CYP2C8kinact is None or CYP2C8KI is None or CYP2C8Ih == 0:
        return 1
    return CYP2C8kdegh / (CYP2C8kdegh + ((CYP2C8Ih * CYP2C8kinact) / (CYP2C8Ih + CYP2C8KI)))

def calculate_CYP2C8Ch(CYP2C8Emax, CYP2C8EC50, CYP2C8I):
    if CYP2C8Emax is None or CYP2C8EC50 is None or CYP2C8I is None:
        return 1
    return 1 + ((CYP2C8Emax - 1) * CYP2C8I / (CYP2C8I + CYP2C8EC50))

def calculate_CYP2C8AUCR(CYP2C8Ah, CYP2C8Bh, CYP2C8Ch, CYP2C8fm):
    return 1 / ((CYP2C8Ah * CYP2C8Bh * CYP2C8Ch * CYP2C8fm) + (1 - CYP2C8fm))


#CYP2C9 Ah, Bh, Ch, AUCR
def calculate_CYP2C9ki(CYP2C9IC50, CYP2C9Km, CYP2C9S):
    return CYP2C9IC50 / (1 + (CYP2C9S / CYP2C9Km))

def calculate_CYP2C9Ah(CYP2C9Ih, CYP2C9ki):
    return 1 / (1 + (CYP2C9Ih / CYP2C9ki))

def calculate_CYP2C9Bh(CYP2C9kdegh, CYP2C9Ih, CYP2C9kinact, CYP2C9KI):
    if CYP2C9kdegh is None or CYP2C9kinact is None or CYP2C9KI is None or CYP2C9Ih == 0:
        return 1
    return CYP2C9kdegh / (CYP2C9kdegh + ((CYP2C9Ih * CYP2C9kinact) / (CYP2C9Ih + CYP2C9KI)))

def calculate_CYP2C9Ch(CYP2C9Emax, CYP2C9EC50, CYP2C9I):
    if CYP2C9Emax is None or CYP2C9EC50 is None or CYP2C9I is None:
        return 1
    return 1 + ((CYP2C9Emax - 1) * CYP2C9I / (CYP2C9I + CYP2C9EC50))

def calculate_CYP2C9AUCR(CYP2C9Ah, CYP2C9Bh, CYP2C9Ch, CYP2C9fm):
    return 1 / ((CYP2C9Ah * CYP2C9Bh * CYP2C9Ch * CYP2C9fm) + (1 - CYP2C9fm))   

#CYP2D6 Ah, Bh, Ch, AUCR
def calculate_CYP2D6ki(CYP2D6IC50, CYP2D6Km, CYP2D6S):
    return CYP2D6IC50 / (1 + (CYP2D6S / CYP2D6Km))

def calculate_CYP2D6Ah(CYP2D6Ih, CYP2D6ki): 
    return 1 / (1 + (CYP2D6Ih / CYP2D6ki))

def calculate_CYP2D6Bh(CYP2D6kdegh, CYP2D6Ih, CYP2D6kinact, CYP2D6KI):                  
    if CYP2D6kdegh is None or CYP2D6kinact is None or CYP2D6KI is None or CYP2D6Ih == 0:
        return 1
    return CYP2D6kdegh / (CYP2D6kdegh + ((CYP2D6Ih * CYP2D6kinact) / (CYP2D6Ih + CYP2D6KI)))

def calculate_CYP2D6Ch(CYP2D6Emax, CYP2D6EC50, CYP2D6I):
    if CYP2D6Emax is None or CYP2D6EC50 is None or CYP2D6I is None:
        return 1
    return 1 + ((CYP2D6Emax - 1) * CYP2D6I / (CYP2D6I + CYP2D6EC50))

def calculate_CYP2D6AUCR(CYP2D6Ah, CYP2D6Bh, CYP2D6Ch, CYP2D6fm):
    return 1 / ((CYP2D6Ah * CYP2D6Bh * CYP2D6Ch * CYP2D6fm) + (1 - CYP2D6fm))

def calculate_AUCR(CYP1A2AUCR, CYP3A4AUCR, CYP2B6AUCR, CYP2C19AUCR, CYP2C8AUCR, CYP2C9AUCR, CYP2D6AUCR):
    return (CYP1A2AUCR + CYP3A4AUCR + CYP2B6AUCR + CYP2C19AUCR + CYP2C8AUCR + CYP2C9AUCR + CYP2D6AUCR)

# Streamlit App UI
st.title("Drug-Drug Interaction (DDI) Calculator")

# Custom CSS to control font sizes and spacing
st.markdown("""
    <style>
    .subheader {
        font-size: 14px;
        font-weight: bold;
    }
    .column-spacing {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Input Parameters Section
st.header("Input Parameters")

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

# Column 1 - Investigational drug physiological parameter
with col1:
    st.markdown('<p class="subheader">Investigational drug physiological parameter</p>', unsafe_allow_html=True)
    Fa = st.number_input("Fa", min_value=0.0, value=0.5)
    Fg = st.number_input("Fg", min_value=0.0, value=0.5)
    ka = st.number_input("ka (1/min)", min_value=0.0, value=0.5)
    Rb = st.number_input("Rb", min_value = 0.0, value=0.5)
    fup = st.number_input("fup", min_value = 0.0, value=0.5)
    MW = st.number_input("MW", min_value = 0.0, value=0.5)
    Qh = st.number_input("Qh (mL/min)", min_value = 0.0, value=0.5)
    Cmax = st.number_input("Cmax (uM)", min_value = 0.0, value=0.5)
    dose = st.number_input("dose (ng)", min_value = 0.0, value=0.5)
    
    Ih = calculate_Ih(Fa, Fg, ka, Rb, fup, MW, Qh, Cmax, dose)
    st.write(f"Ih: {Ih:.4f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)  # Adding space between columns

# Column 2 - CYP1A2 parameters
with col2:
    st.markdown('<p class="subheader">CYP1A2 parameters</p>', unsafe_allow_html=True)
    CYP1A2IC50 = st.number_input("CYP1A2 Investigational Drug IC50 (uM)", min_value=0.0, value=0.5)
    CYP1A2S = st.number_input("CYP1A2 Substrate concentration [S] (uM)", min_value=0.0, value=0.5)
    CYP1A2Km = st.number_input("CYP1A2 Substrate Km (uM)", min_value=0.0, value=0.5)
    CYP1A2ki = st.number_input("CYP1A2 Ki (uM)", value=calculate_CYP1A2ki(CYP1A2IC50, CYP1A2Km, CYP1A2S))
    CYP1A2kdegh = st.number_input("CYP1A2 Degradation rate (kdeg, set 0 if not used)", min_value=0.0, value=0.5)
    CYP1A2kinact = st.number_input("CYP1A2 Kinact (set 0 if not used)", min_value=0.0, value=0.5)
    CYP1A2KI = st.number_input("CYP1A2 KI (set 0 if not used)", min_value=0.0, value=0.5)
    CYP1A2Emax = st.number_input("CYP1A2 Emax (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP1A2EC50 = st.number_input("CYP1A2 EC50 (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP1A2fm = st.number_input("CYP1A2 fm (fraction metabolized)", min_value=0.0, value=0.5)
    CYP1A2I = st.number_input("CYP1A2 Inducer concentration (I, set 0 if not applicable)", min_value=0.0, value=0.5)

    CYP1A2ki = calculate_CYP1A2ki(CYP1A2IC50, CYP1A2Km, CYP1A2S)
    CYP1A2Ah = calculate_CYP1A2Ah(Ih, CYP1A2ki)
    CYP1A2Bh = calculate_CYP1A2Bh(CYP1A2kdegh, Ih, CYP1A2kinact, CYP1A2KI)
    CYP1A2Ch = calculate_CYP1A2Ch(CYP1A2Emax, CYP1A2EC50, CYP1A2I)
    CYP1A2AUCR = calculate_CYP1A2AUCR(CYP1A2Ah, CYP1A2Bh, CYP1A2Ch, CYP1A2fm)

    st.write(f"CYP1A2 Ah: {CYP1A2Ah:.2f}")
    st.write(f"CYP1A2 Bh: {CYP1A2Bh:.2f}")
    st.write(f"CYP1A2 Ch: {CYP1A2Ch:.2f}")
    st.write(f"CYP1A2 AUCR: {CYP1A2AUCR:.2f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)  # Adding space between columns

# Column 3 - CYP3A4 parameters
with col3:
    st.markdown('<p class="subheader">CYP3A4 parameters</p>', unsafe_allow_html=True)
    CYP3A4IC50 = st.number_input("CYP3A4 Investigational Drug IC50 (uM)", min_value=0.0, value=0.5)
    CYP3A4S = st.number_input("CYP3A4 Substrate concentration [S] (uM)", min_value=0.0, value=0.5)
    CYP3A4Km = st.number_input("CYP3A4 Substrate Km (uM)", min_value=0.0, value=0.5)
    CYP3A4ki = st.number_input("CYP3A4 Ki (uM)", value=calculate_CYP3A4ki(CYP3A4IC50, CYP3A4Km, CYP3A4S))
    CYP3A4kdegh = st.number_input("CYP3A4 Degradation rate (kdeg, set 0 if not used)", min_value=0.0, value=0.5)
    CYP3A4kinact = st.number_input("CYP3A4 Kinact (set 0 if not used)", min_value=0.0, value=0.5)
    CYP3A4KI = st.number_input("CYP3A4 KI (set 0 if not used)", min_value=0.0, value=0.5)
    CYP3A4Emax = st.number_input("CYP3A4 Emax (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP3A4EC50 = st.number_input("CYP3A4 EC50 (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP3A4fm = st.number_input("CYP3A4 fm (fraction metabolized)", min_value=0.0, value=0.5)
    CYP3A4I = st.number_input("CYP3A4 Inducer concentration (I, set 0 if not applicable)", min_value=0.0, value=0.5)

    CYP3A4ki = calculate_CYP3A4ki(CYP3A4IC50, CYP3A4Km, CYP3A4S)
    CYP3A4Ah = calculate_CYP3A4Ah(Ih, CYP3A4ki)
    CYP3A4Bh = calculate_CYP3A4Bh(CYP3A4kdegh, Ih, CYP3A4kinact, CYP3A4KI)
    CYP3A4Ch = calculate_CYP3A4Ch(CYP3A4Emax, CYP3A4EC50, CYP3A4I)
    CYP3A4AUCR = calculate_CYP3A4AUCR(CYP3A4Ah, CYP3A4Bh, CYP3A4Ch, CYP3A4fm)

    st.write(f"CYP3A4 Ah: {CYP3A4Ah:.2f}")
    st.write(f"CYP3A4 Bh: {CYP3A4Bh:.2f}")
    st.write(f"CYP3A4 Ch: {CYP3A4Ch:.2f}")
    st.write(f"CYP3A4 AUCR: {CYP3A4AUCR:.2f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)  # Adding space between columns

# Column 4 - CYP2B6 parameters  
with col4:
    st.markdown('<p class="subheader">CYP2B6 parameters</p>', unsafe_allow_html=True)
    CYP2B6IC50 = st.number_input("CYP2B6 Investigational Drug IC50 (uM)", min_value=0.0, value=0.5)
    CYP2B6S = st.number_input("CYP2B6 Substrate concentration [S] (uM)", min_value=0.0, value=0.5)
    CYP2B6Km = st.number_input("CYP2B6 Substrate Km (uM)", min_value=0.0, value=0.5)
    CYP2B6ki = st.number_input("CYP2B6 Ki (uM)", value=calculate_CYP2B6ki(CYP2B6IC50, CYP2B6Km, CYP2B6S))
    CYP2B6kdegh = st.number_input("CYP2B6 Degradation rate (kdeg, set 0 if not used)", min_value=0.0, value=0.5)
    CYP2B6kinact = st.number_input("CYP2B6 Kinact (set 0 if not used)", min_value=0.0, value=0.5)
    CYP2B6KI = st.number_input("CYP2B6 KI (set 0 if not used)", min_value=0.0, value=0.5)
    CYP2B6Emax = st.number_input("CYP2B6 Emax (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP2B6EC50 = st.number_input("CYP2B6 EC50 (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP2B6fm = st.number_input("CYP2B6 fm (fraction metabolized)", min_value=0.0, value=0.5)
    CYP2B6I = st.number_input("CYP2B6 Inducer concentration (I, set 0 if not applicable)", min_value=0.0, value=0.5)

    CYP2B6ki = calculate_CYP2B6ki(CYP2B6IC50, CYP2B6Km, CYP2B6S)
    CYP2B6Ah = calculate_CYP2B6Ah(Ih, CYP2B6ki)
    CYP2B6Bh = calculate_CYP2B6Bh(CYP2B6kdegh, Ih, CYP2B6kinact, CYP2B6KI)
    CYP2B6Ch = calculate_CYP2B6Ch(CYP2B6Emax, CYP2B6EC50, CYP2B6I)
    CYP2B6AUCR = calculate_CYP2B6AUCR(CYP2B6Ah, CYP2B6Bh, CYP2B6Ch, CYP2B6fm)

    st.write(f"CYP2B6 Ah: {CYP2B6Ah:.2f}")
    st.write(f"CYP2B6 Bh: {CYP2B6Bh:.2f}")
    st.write(f"CYP2B6 Ch: {CYP2B6Ch:.2f}")
    st.write(f"CYP2B6 AUCR: {CYP2B6AUCR:.2f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)  # Adding space between columns

# Column 5 - CYP2C19 parameters
with col5:
    st.markdown('<p class="subheader">CYP2C19 parameters</p>', unsafe_allow_html=True)
    CYP2C19IC50 = st.number_input("CYP2C19 Investigational Drug IC50 (uM)", min_value=0.0, value=0.5)
    CYP2C19S = st.number_input("CYP2C19 Substrate concentration [S] (uM)", min_value=0.0, value=0.5)
    CYP2C19Km = st.number_input("CYP2C19 Substrate Km (uM)", min_value=0.0, value=0.5)
    CYP2C19ki = st.number_input("CYP2C19 Ki (uM)", value=calculate_CYP2C19ki(CYP2C19IC50, CYP2C19Km, CYP2C19S))
    CYP2C19kdegh = st.number_input("CYP2C19 Degradation rate (kdeg, set 0 if not used)", min_value=0.0, value=0.5)
    CYP2C19kinact = st.number_input("CYP2C19 Kinact (set 0 if not used)", min_value=0.0, value=0.5)
    CYP2C19KI = st.number_input("CYP2C19 KI (set 0 if not used)", min_value=0.0, value=0.5)
    CYP2C19Emax = st.number_input("CYP2C19 Emax (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP2C19EC50 = st.number_input("CYP2C19 EC50 (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP2C19fm = st.number_input("CYP2C19 fm (fraction metabolized)", min_value=0.0, value=0.5)
    CYP2C19I = st.number_input("CYP2B6 Inducer concentration (I, set 0 if not applicable)", min_value=0.0, value=0.5)

    CYP2C19ki = calculate_CYP2C19ki(CYP2C19IC50, CYP2C19Km, CYP2C19S)
    CYP2C19Ah = calculate_CYP2C19Ah(Ih, CYP2C19ki)
    CYP2C19Bh = calculate_CYP2C19Bh(CYP2C19kdegh, Ih, CYP2C19kinact, CYP2C19KI)
    CYP2C19Ch = calculate_CYP2C19Ch(CYP2C19Emax, CYP2C19EC50, CYP2C19I)
    CYP2C19AUCR = calculate_CYP2C19AUCR(CYP2C19Ah, CYP2C19Bh, CYP2C19Ch, CYP2C19fm)

    st.write(f"CYP2C19 Ah: {CYP2C19Ah:.2f}")
    st.write(f"CYP2C19 Bh: {CYP2C19Bh:.2f}")
    st.write(f"CYP2C19 Ch: {CYP2C19Ch:.2f}")
    st.write(f"CYP2C19 AUCR: {CYP2C19AUCR:.2f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)  # Adding space between columns 

# Column 6 - CYP2C8 parameters
with col6:
    st.markdown('<p class="subheader">CYP2C8 parameters</p>', unsafe_allow_html=True)
    CYP2C8IC50 = st.number_input("CYP2C8 Investigational Drug IC50 (uM)", min_value=0.0, value=0.5)
    CYP2C8S = st.number_input("CYP2C8 Substrate concentration [S] (uM)", min_value=0.0, value=0.5)
    CYP2C8Km = st.number_input("CYP2C8 Substrate Km (uM)", min_value=0.0, value=0.5)
    CYP2C8ki = st.number_input("CYP2C8 Ki (uM)", value=calculate_CYP2C8ki(CYP2C8IC50, CYP2C8Km, CYP2C8S))
    CYP2C8kdegh = st.number_input("CYP2C8 Degradation rate (kdeg, set 0 if not used)", min_value=0.0, value=0.5)
    CYP2C8kinact = st.number_input("CYP2C8 Kinact (set 0 if not used)", min_value=0.0, value=0.5)
    CYP2C8KI = st.number_input("CYP2C8 KI (set 0 if not used)", min_value=0.0, value=0.5)
    CYP2C8Emax = st.number_input("CYP2C8 Emax (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP2C8EC50 = st.number_input("CYP2C8 EC50 (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP2C8fm = st.number_input("CYP2C8 fm (fraction metabolized)", min_value=0.0, value=0.5)
    CYP2C8I = st.number_input("CYP2B6 Inducer concentration (I, set 0 if not applicable)", min_value=0.0, value=0.5)

    CYP2C8ki = calculate_CYP2C8ki(CYP2C8IC50, CYP2C8Km, CYP2C8S)
    CYP2C8Ah = calculate_CYP2C8Ah(Ih, CYP2C8ki)
    CYP2C8Bh = calculate_CYP2C8Bh(CYP2C8kdegh, Ih, CYP2C8kinact, CYP2C8KI)
    CYP2C8Ch = calculate_CYP2C8Ch(CYP2C8Emax, CYP2C8EC50, CYP2C8I)
    CYP2C8AUCR = calculate_CYP2C8AUCR(CYP2C8Ah, CYP2C8Bh, CYP2C8Ch, CYP2C8fm)

    st.write(f"CYP2C8 Ah: {CYP2C8Ah:.2f}")
    st.write(f"CYP2C8 Bh: {CYP2C8Bh:.2f}")
    st.write(f"CYP2C8 Ch: {CYP2C8Ch:.2f}")
    st.write(f"CYP2C8 AUCR: {CYP2C8AUCR:.2f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)  # Adding space between columns

# Column 7 - CYP2C9 parameters
with col7:
    st.markdown('<p class="subheader">CYP2C9 parameters</p>', unsafe_allow_html=True)
    CYP2C9IC50 = st.number_input("CYP2C9 Investigational Drug IC50 (uM)", min_value=0.0, value=0.5)
    CYP2C9S = st.number_input("CYP2C9 Substrate concentration [S] (uM)", min_value=0.0, value=0.5)
    CYP2C9Km = st.number_input("CYP2C9 Substrate Km (uM)", min_value=0.0, value=0.5)
    CYP2C9ki = st.number_input("CYP2C9 Ki (uM)", value=calculate_CYP2C9ki(CYP2C9IC50, CYP2C9Km, CYP2C9S))
    CYP2C9kdegh = st.number_input("CYP2C9 Degradation rate (kdeg, set 0 if not used)", min_value=0.0, value=0.5)
    CYP2C9kinact = st.number_input("CYP2C9 Kinact (set 0 if not used)", min_value=0.0, value=0.5)
    CYP2C9KI = st.number_input("CYP2C9 KI (set 0 if not used)", min_value=0.0, value=0.5)
    CYP2C9Emax = st.number_input("CYP2C9 Emax (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP2C9EC50 = st.number_input("CYP2C9 EC50 (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP2C9fm = st.number_input("CYP2B6 fm (fraction metabolized)", min_value=0.0, value=0.5)
    CYP2C9I = st.number_input("CYP2B6 Inducer concentration (I, set 0 if not applicable)", min_value=0.0, value=0.5)

    CYP2C9ki = calculate_CYP2C9ki(CYP2C9IC50, CYP2C9Km, CYP2C9S)
    CYP2C9Ah = calculate_CYP2C9Ah(Ih, CYP2C9ki)
    CYP2C9Bh = calculate_CYP2C9Bh(CYP2C9kdegh, Ih, CYP2C9kinact, CYP2C9KI)
    CYP2C9Ch = calculate_CYP2C9Ch(CYP2C9Emax, CYP2C9EC50, CYP2C9I)
    CYP2C9AUCR = calculate_CYP2C9AUCR(CYP2C9Ah, CYP2C9Bh, CYP2C9Ch, CYP2C9fm)

    st.write(f"CYP2C9 Ah: {CYP2C9Ah:.2f}")
    st.write(f"CYP2C9 Bh: {CYP2C9Bh:.2f}")
    st.write(f"CYP2C9 Ch: {CYP2C9Ch:.2f}")
    st.write(f"CYP2C9 AUCR: {CYP2C9AUCR:.2f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)  # Adding space between columns

# Column 8 - CYP2D6 parameters
with col8:
    st.markdown('<p class="subheader">CYP2D6 parameters</p>', unsafe_allow_html=True)
    CYP2D6IC50 = st.number_input("CYP2D6 Investigational Drug IC50 (uM)", min_value=0.0, value=0.5)
    CYP2D6S = st.number_input("CYP2D6 Substrate concentration [S] (uM)", min_value=0.0, value=0.5)
    CYP2D6Km = st.number_input("CYP2D6 Substrate Km (uM)", min_value=0.0, value=0.5)
    CYP2D6ki = st.number_input("CYP2D6 Ki (uM)", value=calculate_CYP2D6ki(CYP2D6IC50, CYP2D6Km, CYP2D6S))
    CYP2D6kdegh = st.number_input("CYP2D6 Degradation rate (kdeg, set 0 if not used)", min_value=0.0, value=0.5)
    CYP2D6kinact = st.number_input("CYP2D6 Kinact (set 0 if not used)", min_value=0.0, value=0.5)
    CYP2D6KI = st.number_input("CYP2D6 KI (set 0 if not used)", min_value=0.0, value=0.5)
    CYP2D6Emax = st.number_input("CYP2D6 Emax (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP2D6EC50 = st.number_input("CYP2D6 EC50 (set 0 if not applicable)", min_value=0.0, value=0.5)
    CYP2D6fm = st.number_input("CYP2B6 fm (fraction metabolized)", min_value=0.0, value=0.5)
    CYP2D6I = st.number_input("CYP2B6 Inducer concentration (I, set 0 if not applicable)", min_value=0.0, value=0.5)

    CYP2D6ki = calculate_CYP2D6ki(CYP2D6IC50, CYP2D6Km, CYP2D6S)
    CYP2D6Ah = calculate_CYP2D6Ah(Ih, CYP2D6ki)
    CYP2D6Bh = calculate_CYP2D6Bh(CYP2D6kdegh, Ih, CYP2D6kinact, CYP2D6KI)
    CYP2D6Ch = calculate_CYP2D6Ch(CYP2D6Emax, CYP2D6EC50, CYP2D6I)
    CYP2D6AUCR = calculate_CYP2D6AUCR(CYP2D6Ah, CYP2D6Bh, CYP2D6Ch, CYP2D6fm)

    st.write(f"CYP2D6 Ah: {CYP2D6Ah:.2f}")
    st.write(f"CYP2D6 Bh: {CYP2D6Bh:.2f}")
    st.write(f"CYP2D6 Ch: {CYP2D6Ch:.2f}")
    st.write(f"CYP2D6 AUCR: {CYP2D6AUCR:.2f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)  # Adding space between columns 


# Final DDI calculation
AUCR = calculate_AUCR(CYP1A2AUCR, CYP3A4AUCR, CYP2B6AUCR, CYP2C19AUCR, CYP2C8AUCR, CYP2C9AUCR, CYP2D6AUCR) 

st.header("Results")
st.write(f"**Predicted AUCR:** {AUCR:.2f}")

if AUCR > 5.00:
    st.warning("Strong Inhibitor")
elif AUCR > 2.00:
    st.warning("Moderate Inhibitor")
elif AUCR > 1.25:
    st.warning("Weak Inhibitor")
else:
    st.success("Low likelihood of significant DDI")



