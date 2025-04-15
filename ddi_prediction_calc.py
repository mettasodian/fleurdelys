import streamlit as st

def calculate_Ih(Fa, Fg, ka, Rb, fup, MW, Qh, Cmax, dose):
    return fup * (Cmax + ( Fa * Fg * ka * (dose / MW ) / Qh / Rb))

def calculate_ki(IC50, Km, S):
    return IC50 / (1 + (S / Km))

def calculate_Ah(Ih, ki):
    return 1 / (1 + (Ih / ki))

def calculate_Bh(kdegh, Ih, kinact, KI):
    if kdegh is None or kinact is None or KI is None or Ih == 0:
        return 1
    return kdegh / (kdegh + ((Ih * kinact) / (Ih + KI)))

def calculate_Ch(Emax, EC50, I):
    if Emax is None or EC50 is None or I is None:
        return 1
    return 1 + ((Emax - 1) * I / (I + EC50))

def ddi_prediction(Ah, Bh, Ch, fm):
    return 1 / ((Ah * Bh * Ch * fm) + (1 - fm))

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

col1, col2, col3, col4, col5 = st.columns(5)

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
    IC50 = st.number_input("IC50", min_value=0.0, value=0.5)
    S = st.number_input("Substrate concentration [S] (uM)", min_value=0.0, value=0.5)
    
    Ih = calculate_Ih(Fa, Fg, ka, Rb, fup, MW, Qh, Cmax, dose)
    st.write(f"Ih: {Ih:.2f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)  # Adding space between columns

# Column 2 - Substrate/victim drug parameter
with col2:
    st.markdown('<p class="subheader">Substrate/victim drug parameter</p>', unsafe_allow_html=True)
    fm = st.number_input("Fraction metabolized (fm)", min_value=0.0, value=0.5)
    Km = st.number_input("Km (uM)", min_value=0.0, value=0.5)
    ki = calculate_ki(IC50, Km, S)
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)

# Column 3 - Reversible Inhibition
with col3:
    st.markdown('<p class="subheader">Reversible Inhibition</p>', unsafe_allow_html=True)
    ki = st.number_input("ki", value=ki)
    Ih = st.number_input("Substrate concentration [S]", value=Ih)
    
    Ah = calculate_Ah(Ih, ki)
    st.write(f"Ah: {Ah:.2f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)

# Column 4 - Time-Dependent Inhibition
with col4:
    st.markdown('<p class="subheader">Time-Dependent Inhibition</p>', unsafe_allow_html=True)
    kinact = st.number_input("kinact (set 0 if not used)", min_value=0.0, value=0.5)
    KI = st.number_input("KI (for time-dependent inhibition, set 0 if not used)", min_value=0.0, value=0.5)
    kdegh = st.number_input("kdegh (degradation rate, set 0 if not used)", min_value=0.0, value=0.5)

    Bh = calculate_Bh(kdegh, Ih, kinact, KI)
    st.write(f"Bh: {Bh:.2f}")
    st.markdown('<div class="column-spacing"></div>', unsafe_allow_html=True)

# Column 5 - Inducer
with col5:
    st.markdown('<p class="subheader">Inducer</p>', unsafe_allow_html=True)
    Emax = st.number_input("Emax (set 0 if not applicable)", min_value=0.0)
    EC50 = st.number_input("EC50 (set 0 if not applicable)", min_value=0.0)
    I = st.number_input("Inducer concentration (I, set 0 if not applicable)", min_value=0.0)

# Convert 0s to None where needed
kinact = None if kinact == 0 else kinact
KI = None if KI == 0 else KI
kdegh = None if kdegh == 0 else kdegh
Emax = None if Emax == 0 else Emax
EC50 = None if EC50 == 0 else EC50
I = None if I == 0 else I

# Calculate DDI
Ah = calculate_Ah(Ih, ki)
Bh = calculate_Bh(kdegh, Ih, kinact, KI)
Ch = calculate_Ch(Emax, EC50, I)
AUCR = ddi_prediction(Ah, Bh, Ch, fm)

# Results Section
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
