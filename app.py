"""
Spotify 2023 — EDA Dashboard
Streamlit + Plotly · Estilo editorial premium
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Spotify 2023 · EDA",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500;700&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0a0a0a;
    color: #e8e6df;
}
.stApp { background-color: #0a0a0a; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background-color: #111111 !important;
    border-right: 1px solid #1a1a1a;
    padding-top: 0 !important;
}
section[data-testid="stSidebar"] > div { padding: 0 !important; }

/* ── Sidebar logo block ── */
.sidebar-logo {
    background: linear-gradient(135deg, #1DB954 0%, #158a3e 100%);
    padding: 28px 24px 22px;
    margin-bottom: 8px;
}
.sidebar-logo .logo-text {
    font-family: 'Syne', sans-serif;
    font-size: 22px;
    font-weight: 800;
    color: #000;
    letter-spacing: -0.5px;
    line-height: 1;
}
.sidebar-logo .logo-sub {
    font-size: 11px;
    color: rgba(0,0,0,0.6);
    margin-top: 4px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* ── Sidebar filter labels ── */
section[data-testid="stSidebar"] label {
    color: #888 !important;
    font-size: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}
section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div,
section[data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] > div {
    background-color: #1a1a1a !important;
    border-color: #2a2a2a !important;
    color: #e8e6df !important;
    border-radius: 8px !important;
}
section[data-testid="stSidebar"] p { color: #555 !important; font-size: 12px !important; }

/* ── Slider ── */
[data-testid="stSlider"] [role="slider"] { background-color: #1DB954 !important; }
[data-testid="stSlider"] [data-baseweb="slider"] div:nth-child(3) { background-color: #1DB954 !important; }

/* ── Hero header ── */
.hero {
    padding: 48px 0 36px;
    border-bottom: 1px solid #1a1a1a;
    margin-bottom: 40px;
}
.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-radius: 100px;
    padding: 5px 14px;
    font-size: 11px;
    font-weight: 600;
    color: #1DB954;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 20px;
}
.hero-eyebrow::before {
    content: '';
    width: 6px; height: 6px;
    background: #1DB954;
    border-radius: 50%;
    display: inline-block;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(36px, 5vw, 64px);
    font-weight: 800;
    color: #ffffff;
    line-height: 1.0;
    letter-spacing: -2px;
    margin: 0 0 16px;
}
.hero-title span { color: #1DB954; }
.hero-sub {
    font-size: 16px;
    color: #666;
    font-weight: 300;
    max-width: 560px;
    line-height: 1.6;
}

/* ── KPI cards ── */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-bottom: 40px;
}
.kpi-card {
    background: #111;
    border: 1px solid #1a1a1a;
    border-radius: 16px;
    padding: 20px 20px 18px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--accent, #1DB954);
}
.kpi-card:hover { border-color: #2a2a2a; }
.kpi-icon {
    font-size: 18px;
    margin-bottom: 12px;
    display: block;
}
.kpi-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #555;
    margin-bottom: 6px;
}
.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: #fff;
    line-height: 1;
    letter-spacing: -1px;
}
.kpi-value span { color: var(--accent, #1DB954); }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid #1a1a1a !important;
    gap: 0 !important;
    padding: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #555 !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    padding: 14px 28px !important;
    border-radius: 0 !important;
    border-bottom: 2px solid transparent !important;
    transition: all 0.2s !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #e8e6df !important;
    background: transparent !important;
}
.stTabs [aria-selected="true"] {
    background: transparent !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border-bottom: 2px solid #1DB954 !important;
}

/* ── Section headers ── */
.section-header {
    margin: 8px 0 32px;
    padding-bottom: 20px;
    border-bottom: 1px solid #1a1a1a;
}
.section-number {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #1DB954;
    margin-bottom: 8px;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: #fff;
    letter-spacing: -0.5px;
    line-height: 1.2;
    margin: 0;
}
.section-desc {
    font-size: 14px;
    color: #555;
    margin-top: 8px;
    font-weight: 300;
}

/* ── Insight box ── */
.insight {
    background: #111;
    border: 1px solid #1a1a1a;
    border-left: 3px solid #1DB954;
    border-radius: 0 12px 12px 0;
    padding: 18px 22px;
    margin: 24px 0 8px;
    font-size: 14px;
    line-height: 1.7;
    color: #888;
}
.insight strong { color: #e8e6df; }
.insight .hl { color: #1DB954; font-weight: 600; }
.insight.warn { border-left-color: #E8563A; }
.insight.warn .hl { color: #E8563A; }
.insight.amber { border-left-color: #F59B23; }
.insight.amber .hl { color: #F59B23; }
.insight.purple { border-left-color: #9B72CF; }
.insight.purple .hl { color: #9B72CF; }

/* ── Divider ── */
hr { border-color: #1a1a1a !important; margin: 40px 0 !important; }

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    overflow: hidden !important;
    border: 1px solid #1a1a1a !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0a; }
::-webkit-scrollbar-thumb { background: #2a2a2a; border-radius: 2px; }
</style>
""", unsafe_allow_html=True)

# ── Paleta ────────────────────────────────────────────────────────────────────
GREEN  = "#1DB954"
CORAL  = "#E8563A"
AMBER  = "#F59B23"
PURPLE = "#9B72CF"
BLUE   = "#4FC3F7"
GRAY   = "#888888"
BG     = "#0a0a0a"
BG2    = "#111111"
BG3    = "#161616"

ERA_COLORS = {
    "Pré-2000":  "#555555",
    "2000s":     "#9B72CF",
    "2010s":     "#4FC3F7",
    "2020–2021": "#1DB954",
    "2022–2023": "#E8563A",
}

def spotify_layout(fig, title="", height=420, showlegend=False,
                   xaxis_title="", yaxis_title=""):
    fig.update_layout(
        title=dict(text=title, font=dict(color="#e8e6df", size=14,
                   family="DM Sans"), x=0.01),
        paper_bgcolor=BG,
        plot_bgcolor=BG2,
        font=dict(family="DM Sans", color=GRAY, size=12),
        xaxis=dict(gridcolor="#1a1a1a", linecolor="#1a1a1a",
                   tickcolor="#2a2a2a", zerolinecolor="#1a1a1a",
                   title_text=xaxis_title,
                   title_font=dict(color="#555", size=11)),
        yaxis=dict(gridcolor="#1a1a1a", linecolor="#1a1a1a",
                   tickcolor="#2a2a2a", zerolinecolor="#1a1a1a",
                   title_text=yaxis_title,
                   title_font=dict(color="#555", size=11)),
        legend=dict(bgcolor=BG2, bordercolor="#1a1a1a", borderwidth=1,
                    font=dict(color=GRAY)),
        margin=dict(l=50, r=30, t=50, b=50),
        hoverlabel=dict(bgcolor="#1a1a1a", bordercolor="#2a2a2a",
                        font=dict(color="#e8e6df", size=12,
                                  family="DM Sans")),
        colorway=[GREEN, CORAL, AMBER, PURPLE, BLUE, GRAY],
        height=height,
        showlegend=showlegend,
    )
    return fig

# ── ETL ───────────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df_raw = pd.read_csv("spotify-2023.csv", encoding="utf-8",
                         encoding_errors="replace")
    bad = pd.to_numeric(df_raw["streams"], errors="coerce").isna()
    df  = df_raw[~bad].copy()
    df["streams"] = pd.to_numeric(df["streams"])
    num_cols = [
        "artist_count","released_year","released_month","released_day",
        "in_spotify_playlists","in_spotify_charts","in_apple_playlists",
        "in_apple_charts","in_deezer_playlists","in_deezer_charts",
        "in_shazam_charts","bpm","danceability_%","valence_%","energy_%",
        "acousticness_%","instrumentalness_%","liveness_%","speechiness_%",
    ]
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["key"] = df["key"].replace("", np.nan).fillna("Unknown")
    df["in_shazam_charts"] = df["in_shazam_charts"].fillna(0)
    df["streams_M"] = df["streams"] / 1e6
    df["era"] = pd.cut(
        df["released_year"],
        bins=[0,1999,2009,2019,2021,2023],
        labels=["Pré-2000","2000s","2010s","2020–2021","2022–2023"],
    ).astype(str)
    df["collab"] = df["artist_count"].apply(
        lambda x: "Colaboração" if x > 1 else "Solo")
    return df

df = load_data()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="logo-text">● Spotify</div>
        <div class="logo-sub">2023 · EDA Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='padding:0 16px'>", unsafe_allow_html=True)

    st.markdown("<p style='color:#333;font-size:10px;font-weight:600;"
                "letter-spacing:0.1em;text-transform:uppercase;"
                "margin:16px 0 12px'>Filtros</p>",
                unsafe_allow_html=True)

    eras_all  = ["Pré-2000","2000s","2010s","2020–2021","2022–2023"]
    eras_sel  = st.multiselect("Era de lançamento", eras_all, default=eras_all)

    modes_all = sorted(df["mode"].dropna().unique().tolist())
    modes_sel = st.multiselect("Modo", modes_all, default=modes_all)

    year_min = int(df["released_year"].min())
    year_max = int(df["released_year"].max())
    year_range = st.slider("Ano de lançamento",
                           year_min, year_max, (year_min, year_max))

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div style='padding:24px 16px 16px;margin-top:auto'>"
                "<p style='color:#2a2a2a;font-size:10px;line-height:1.6'>"
                "Dataset: Kaggle<br>Most Streamed Spotify Songs 2023</p>"
                "<p style='color:#2a2a2a;font-size:10px;margin-top:8px'>"
                "Desenvolvido por<br>"
                "<a href='https://github.com/SanderAugustoGarcia' "
                "style='color:#1DB954;text-decoration:none'>"
                "Sander Augusto Garcia</a></p>"
                "</div>", unsafe_allow_html=True)

# ── Filtro ────────────────────────────────────────────────────────────────────
mask = (
    df["era"].isin(eras_sel) &
    df["mode"].isin(modes_sel) &
    df["released_year"].between(year_range[0], year_range[1])
)
dff = df[mask].copy()

# ── KPIs ──────────────────────────────────────────────────────────────────────
s_arr = dff["streams"].dropna().values
if len(s_arr) > 1:
    s_sorted    = np.sort(s_arr)
    cum_s       = np.cumsum(s_sorted) / s_sorted.sum()
    cum_p       = np.arange(1, len(s_sorted)+1) / len(s_sorted)
    gini        = float(1 - 2 * np.trapezoid(cum_s, cum_p))
    share_top10 = float((1 - cum_s[int(0.9*len(s_sorted))]) * 100)
else:
    s_sorted = cum_s = cum_p = np.array([0])
    gini = share_top10 = 0.0

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
    <div class="hero-eyebrow">Análise Exploratória de Dados · 2023</div>
    <h1 class="hero-title">Spotify<br><span>em números.</span></h1>
    <p class="hero-sub">Pipeline completo ETL → EDA sobre as
    <strong style="color:#e8e6df">{len(dff):,} músicas</strong>
    mais ouvidas no Spotify em 2023 — atributos musicais,
    plataformas e tendências de mercado.</p>
</div>
""", unsafe_allow_html=True)

# ── KPI grid ──────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="kpi-grid">
  <div class="kpi-card" style="--accent:#1DB954">
    <span class="kpi-icon">🎵</span>
    <div class="kpi-label">Músicas</div>
    <div class="kpi-value">{len(dff):,}</div>
  </div>
  <div class="kpi-card" style="--accent:#4FC3F7">
    <span class="kpi-icon">▶</span>
    <div class="kpi-label">Streams total</div>
    <div class="kpi-value">{dff['streams'].sum()/1e9:.1f}<span>B</span></div>
  </div>
  <div class="kpi-card" style="--accent:#F59B23">
    <span class="kpi-icon">~</span>
    <div class="kpi-label">Mediana streams</div>
    <div class="kpi-value">{dff['streams_M'].median():.0f}<span>M</span></div>
  </div>
  <div class="kpi-card" style="--accent:#9B72CF">
    <span class="kpi-icon">⊘</span>
    <div class="kpi-label">Gini</div>
    <div class="kpi-value">{gini:.2f}</div>
  </div>
  <div class="kpi-card" style="--accent:#E8563A">
    <span class="kpi-icon">↑</span>
    <div class="kpi-label">Top 10% = X% streams</div>
    <div class="kpi-value">{share_top10:.0f}<span>%</span></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Distribuição",
    "Sazonalidade",
    "Eras",
    "Colaborações",
    "Top músicas",
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — Distribuição
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("""
    <div class="section-header">
        <div class="section-number">Q1 · Distribuição</div>
        <h2 class="section-title">Quão desigual é a<br>distribuição de streams?</h2>
        <p class="section-desc">Histograma, escala logarítmica, Curva de Lorenz e Coeficiente de Gini</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        log_s = np.log10(dff["streams"].clip(lower=1))
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=log_s, nbinsx=40,
            marker_color=GREEN, opacity=0.9,
            hovertemplate="log₁₀: %{x:.2f}<br>Músicas: %{y}<extra></extra>",
        ))
        fig.add_vline(x=float(np.log10(dff["streams"].median())),
                      line_dash="dash", line_color=CORAL, line_width=1.5,
                      annotation_text=f"Mediana {dff['streams_M'].median():.0f}M",
                      annotation_font_color=CORAL,
                      annotation_font_size=11)
        fig.add_vline(x=float(np.log10(dff["streams"].mean())),
                      line_dash="dot", line_color=AMBER, line_width=1.5,
                      annotation_text=f"Média {dff['streams_M'].mean():.0f}M",
                      annotation_font_color=AMBER,
                      annotation_position="top left",
                      annotation_font_size=11)
        spotify_layout(fig, title="Distribuição em log₁₀",
                       xaxis_title="log₁₀ (streams)",
                       yaxis_title="Nº de músicas", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=cum_p*100, y=cum_s*100, mode="lines",
            line=dict(color=GREEN, width=2.5),
            fill="tonexty", fillcolor="rgba(29,185,84,0.08)",
            name="Curva de Lorenz",
            hovertemplate="Top %{x:.1f}% músicas<br>= %{y:.1f}% streams<extra></extra>",
        ))
        fig2.add_trace(go.Scatter(
            x=[0,100], y=[0,100], mode="lines",
            line=dict(color="#2a2a2a", width=1.2, dash="dash"),
            name="Igualdade perfeita",
        ))
        fig2.add_annotation(
            x=65, y=22,
            text=f"<b>Top 10% = {share_top10:.0f}% streams</b><br>"
                 f"Gini = {gini:.2f}",
            showarrow=True, arrowhead=2, ax=0, ay=-50,
            bgcolor=BG3, bordercolor=GREEN, borderwidth=1,
            font=dict(color=GREEN, size=12, family="DM Sans"),
        )
        spotify_layout(fig2, title="Curva de Lorenz",
                       xaxis_title="% músicas (acumulado)",
                       yaxis_title="% streams (acumulado)",
                       height=380, showlegend=True)
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown(f"""
    <div class="insight">
        💡 <strong>Insight:</strong> A distribuição segue uma
        <span class="hl">lei de potência</span> —
        a média (<span class="hl">{dff['streams_M'].mean():.0f}M</span>)
        é quase o dobro da mediana
        (<span class="hl">{dff['streams_M'].median():.0f}M</span>).
        Um Gini de <span class="hl">{gini:.2f}</span> indica concentração
        moderada-alta: o top 10% das músicas gera
        <span class="hl">{share_top10:.0f}%</span> de todos os streams.
        A transformação log₁₀ aproxima os dados de uma normal —
        relevante para modelação futura.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — Sazonalidade
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("""
    <div class="section-header">
        <div class="section-number">Q2 · Sazonalidade</div>
        <h2 class="section-title">Existe sazonalidade<br>nos lançamentos?</h2>
        <p class="section-desc">Volume de lançamentos e streams mediana por mês — músicas de 2022–2023</p>
    </div>
    """, unsafe_allow_html=True)

    month_names = ["Jan","Fev","Mar","Abr","Mai","Jun",
                   "Jul","Ago","Set","Out","Nov","Dez"]
    df_rec  = dff[dff["released_year"] >= 2022].copy()
    m_count = df_rec.groupby("released_month").size()\
                    .reindex(range(1,13), fill_value=0)
    m_str   = df_rec.groupby("released_month")["streams_M"].median()\
                    .reindex(range(1,13), fill_value=0)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        colors_vol = [CORAL if v == m_count.max() else GREEN
                      for v in m_count.values]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=month_names, y=m_count.values,
            marker_color=colors_vol, opacity=0.9,
            text=m_count.values, textposition="outside",
            textfont=dict(color="#e8e6df", size=11),
            hovertemplate="%{x}: <b>%{y} músicas</b><extra></extra>",
        ))
        fig.add_hline(y=m_count.mean(), line_dash="dash",
                      line_color="#2a2a2a", line_width=1.2,
                      annotation_text=f"Média {m_count.mean():.0f}",
                      annotation_font_color="#444")
        spotify_layout(fig, title="Lançamentos por mês",
                       yaxis_title="Nº de músicas", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        colors_str = [AMBER if v == m_str.max() else GREEN
                      for v in m_str.values]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=month_names, y=m_str.values,
            marker_color=colors_str, opacity=0.9,
            text=[f"{v:.0f}M" for v in m_str.values],
            textposition="outside",
            textfont=dict(color="#e8e6df", size=11),
            hovertemplate="%{x}: mediana <b>%{y:.0f}M</b><extra></extra>",
        ))
        spotify_layout(fig2, title="Streams mediana por mês",
                       yaxis_title="Streams mediana (M)", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    best_vol = month_names[m_count.idxmax()-1]
    best_str = month_names[m_str.idxmax()-1]
    worst    = month_names[m_count.idxmin()-1]

    st.markdown(f"""
    <div class="insight amber">
        💡 <strong>Insight:</strong>
        <span class="hl">{best_vol}</span> lidera em lançamentos
        ({m_count.max()} músicas). <strong>{worst}</strong> é o mês mais
        calmo ({m_count.min()} músicas). Mas músicas lançadas em
        <span class="hl">{best_str}</span> têm a maior mediana de streams —
        há um <span class="hl">trade-off entre volume e visibilidade</span>:
        lançar com menos concorrência pode valer mais do que lançar
        na época alta.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — Eras
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("""
    <div class="section-header">
        <div class="section-number">Q3 · Eras</div>
        <h2 class="section-title">Músicas antigas ainda<br>dominam os charts?</h2>
        <p class="section-desc">Comparação de streams por era de lançamento · viés de sobrevivência</p>
    </div>
    """, unsafe_allow_html=True)

    era_order   = ["Pré-2000","2000s","2010s","2020–2021","2022–2023"]
    era_order_f = [e for e in era_order if e in dff["era"].unique()]

    col1, col2 = st.columns(2, gap="large")

    with col1:
        era_counts = dff["era"].value_counts()\
                               .reindex(era_order_f, fill_value=0)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=era_counts.index.tolist(), y=era_counts.values,
            marker_color=[ERA_COLORS.get(e, GREEN) for e in era_counts.index],
            opacity=0.9,
            text=era_counts.values, textposition="outside",
            textfont=dict(color="#e8e6df", size=11),
            hovertemplate="%{x}: <b>%{y} músicas</b><extra></extra>",
        ))
        spotify_layout(fig, title="Músicas no dataset por era",
                       yaxis_title="Nº de músicas", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = go.Figure()
        for era in era_order_f:
            sub   = dff[dff["era"] == era]
            if not len(sub): continue
            color = ERA_COLORS.get(era, GREEN)
            r, g, b = int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)
            fig2.add_trace(go.Box(
                y=sub["streams_M"], name=era,
                marker_color=color, line_color=color,
                fillcolor=f"rgba({r},{g},{b},0.12)",
                boxmean=True,
                hovertemplate=f"<b>{era}</b><br>%{{y:.0f}}M<extra></extra>",
            ))
        spotify_layout(fig2, title="Streams por era (boxplot)",
                       yaxis_title="Streams (M)", height=380)
        st.plotly_chart(fig2, use_container_width=True)

    era_summary = (
        dff.groupby("era")["streams_M"]
        .agg(["count","median","mean","max"])
        .reindex(era_order_f)
        .rename(columns={"count":"Músicas","median":"Mediana (M)",
                         "mean":"Média (M)","max":"Máx (M)"})
        .round(0)
        .astype({"Músicas": int})
    )
    st.dataframe(era_summary, use_container_width=True)

    st.markdown("""
    <div class="insight purple">
        ⚠️ <strong>Viés de sobrevivência:</strong> Os
        <span class="hl">anos 2000</span> têm a maior mediana — mas as
        únicas músicas antigas aqui são os
        <span class="hl">maiores clássicos de sempre</span>.
        As milhares de faixas "normais" dessa era simplesmente não estão
        neste dataset. O catálogo histórico é um
        <span class="hl">activo de alto valor passivo</span>
        para as editoras.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — Colaborações
# ══════════════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown("""
    <div class="section-header">
        <div class="section-number">Q4 · Colaborações</div>
        <h2 class="section-title">Colaborações geram mais<br>streams do que solos?</h2>
        <p class="section-desc">Solo vs. Colaboração (2+ artistas) · análise por número de artistas</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        counts = dff["collab"].value_counts()\
                              .reindex(["Solo","Colaboração"], fill_value=0)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=counts.index.tolist(), y=counts.values,
            marker_color=[GREEN, CORAL], opacity=0.9,
            text=[f"{v}<br><span style='font-size:10px'>"
                  f"({v/max(len(dff),1)*100:.0f}%)</span>"
                  for v in counts.values],
            textposition="outside",
            textfont=dict(color="#e8e6df", size=12),
            hovertemplate="%{x}: <b>%{y}</b><extra></extra>",
        ))
        spotify_layout(fig, title="Volume no dataset",
                       yaxis_title="Nº de músicas", height=360)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        medians = dff.groupby("collab")["streams_M"].median()\
                     .reindex(["Solo","Colaboração"], fill_value=0)
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=medians.index.tolist(), y=medians.values,
            marker_color=[GREEN, CORAL], opacity=0.9,
            text=[f"{v:.0f}M" for v in medians.values],
            textposition="outside",
            textfont=dict(color="#e8e6df", size=14),
            hovertemplate="%{x}: mediana <b>%{y:.0f}M</b><extra></extra>",
        ))
        spotify_layout(fig2, title="Streams mediana",
                       yaxis_title="Streams mediana (M)", height=360)
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        dff["_ac"] = dff["artist_count"].clip(upper=5)
        by_n       = dff.groupby("_ac")["streams_M"].median()
        x_lab      = {1:"1 (solo)",2:"2",3:"3",4:"4",5:"5+"}
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(
            x=[x_lab.get(int(k), str(k)) for k in by_n.index],
            y=by_n.values,
            marker_color=[GREEN, BLUE, AMBER, CORAL, PURPLE][:len(by_n)],
            opacity=0.9,
            text=[f"{v:.0f}M" for v in by_n.values],
            textposition="outside",
            textfont=dict(color="#e8e6df", size=11),
            hovertemplate="Nº artistas %{x}: <b>%{y:.0f}M</b><extra></extra>",
        ))
        spotify_layout(fig3, title="Mediana por nº de artistas",
                       xaxis_title="Nº de artistas",
                       yaxis_title="Streams mediana (M)", height=360)
        st.plotly_chart(fig3, use_container_width=True)

    solo_m   = dff[dff["collab"]=="Solo"]["streams_M"].median()
    collab_m = dff[dff["collab"]=="Colaboração"]["streams_M"].median()
    diff_pct = (solo_m/collab_m - 1)*100 if collab_m > 0 else 0

    st.markdown(f"""
    <div class="insight warn">
        💡 <strong>Resultado contra-intuitivo:</strong> Solos têm mediana
        <span class="hl">{diff_pct:.0f}% superior</span> às colaborações
        ({solo_m:.0f}M vs {collab_m:.0f}M). A hipótese mais plausível:
        artistas com bases de fãs consolidadas lançam maioritariamente solos.
        <strong>O factor determinante é a base de fãs do artista principal</strong>,
        não o número de artistas na faixa.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 5 — Top músicas
# ══════════════════════════════════════════════════════════════════════════════
with tab5:
    st.markdown("""
    <div class="section-header">
        <div class="section-number">Top · Ranking</div>
        <h2 class="section-title">As músicas<br>mais ouvidas.</h2>
        <p class="section-desc">Ranking dinâmico — filtra e ordena por qualquer métrica</p>
    </div>
    """, unsafe_allow_html=True)

    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns([1,1,2])
    with col_ctrl1:
        n_top = st.slider("Nº de músicas", 5, 50, 15)
    with col_ctrl2:
        sort_by = st.selectbox("Ordenar por", [
            "streams","in_spotify_playlists","in_spotify_charts",
            "danceability_%","energy_%","bpm",
        ])

    top_df = (
        dff.nlargest(n_top, sort_by)
        [["track_name","artist(s)_name","released_year","streams_M",
          "in_spotify_playlists","bpm","danceability_%","energy_%",
          "mode","key","collab","era"]]
        .rename(columns={
            "track_name":"Música","artist(s)_name":"Artista(s)",
            "released_year":"Ano","streams_M":"Streams (M)",
            "in_spotify_playlists":"Playlists","bpm":"BPM",
            "danceability_%":"Dance","energy_%":"Energy",
            "mode":"Modo","key":"Key","collab":"Tipo","era":"Era",
        })
        .reset_index(drop=True)
    )
    top_df.index += 1
    top_df["Streams (M)"] = top_df["Streams (M)"].round(0).astype(int)
    st.dataframe(top_df, use_container_width=True, height=480)

    st.markdown("<div style='margin-top:32px'></div>", unsafe_allow_html=True)

    top15 = dff.nlargest(15, "streams_M")
    fig   = go.Figure()
    fig.add_trace(go.Bar(
        x=top15["streams_M"],
        y=top15["track_name"] + "  ·  " + top15["artist(s)_name"],
        orientation="h",
        marker=dict(
            color=top15["streams_M"],
            colorscale=[[0,"#0f5c28"],[1,GREEN]],
            showscale=False,
        ),
        opacity=0.95,
        text=[f"{v:.0f}M" for v in top15["streams_M"]],
        textposition="outside",
        textfont=dict(color=GREEN, size=11),
        hovertemplate="<b>%{y}</b><br>%{x:.0f}M streams<extra></extra>",
    ))
    spotify_layout(fig, title="Top 15 — streams totais",
                   xaxis_title="Streams (M)", height=520)
    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        margin=dict(l=320, r=100, t=50, b=50),
    )
    st.plotly_chart(fig, use_container_width=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<hr>
<div style="display:flex;justify-content:space-between;align-items:center;
            padding:8px 0 24px;color:#2a2a2a;font-size:12px">
    <span>🎵 Spotify 2023 EDA · Dataset: Kaggle</span>
    <span>Desenvolvido por
        <a href="https://github.com/SanderAugustoGarcia"
           style="color:#1DB954;text-decoration:none">
           Sander Augusto Garcia</a>
    </span>
</div>
""", unsafe_allow_html=True)
