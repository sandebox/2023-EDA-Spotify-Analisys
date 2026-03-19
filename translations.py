"""
Spotify 2023 Dashboard — Translations
Supported: PT (Português), EN (English), ES (Español)
"""

T = {

# ── Sidebar ───────────────────────────────────────────────────────────────────
"sidebar_sub": {
    "PT": "2023 · Dashboard",
    "EN": "2023 · Dashboard",
    "ES": "2023 · Panel",
},
"module_label": {
    "PT": "Módulo",
    "EN": "Module",
    "ES": "Módulo",
},
"module_options": {
    "PT": ["EDA", "Correlações", "Machine Learning"],
    "EN": ["EDA", "Correlations", "Machine Learning"],
    "ES": ["EDA", "Correlaciones", "Machine Learning"],
},
"filters_label": {
    "PT": "Filtros",
    "EN": "Filters",
    "ES": "Filtros",
},
"era_filter": {
    "PT": "Era de lançamento",
    "EN": "Release era",
    "ES": "Era de lanzamiento",
},
"mode_filter": {
    "PT": "Modo",
    "EN": "Mode",
    "ES": "Modo",
},
"year_filter": {
    "PT": "Ano de lançamento",
    "EN": "Release year",
    "ES": "Año de lanzamiento",
},
"footer_dataset": {
    "PT": "Dataset: Kaggle<br>Most Streamed Spotify Songs 2023",
    "EN": "Dataset: Kaggle<br>Most Streamed Spotify Songs 2023",
    "ES": "Dataset: Kaggle<br>Most Streamed Spotify Songs 2023",
},
"footer_dev": {
    "PT": "Desenvolvido por",
    "EN": "Developed by",
    "ES": "Desarrollado por",
},
"lang_label": {
    "PT": "Idioma",
    "EN": "Language",
    "ES": "Idioma",
},

# ── Hero ──────────────────────────────────────────────────────────────────────
"eda_eyebrow": {
    "PT": "Análise Exploratória de Dados · 2023",
    "EN": "Exploratory Data Analysis · 2023",
    "ES": "Análisis Exploratorio de Datos · 2023",
},
"eda_title_line1": {
    "PT": "Spotify",
    "EN": "Spotify",
    "ES": "Spotify",
},
"eda_title_line2": {
    "PT": "em números.",
    "EN": "by the numbers.",
    "ES": "en números.",
},
"eda_sub": {
    "PT": "Pipeline completo ETL → EDA sobre as",
    "EN": "Full ETL → EDA pipeline over",
    "ES": "Pipeline completo ETL → EDA sobre las",
},
"eda_sub2": {
    "PT": "músicas mais ouvidas no Spotify em 2023.",
    "EN": "most streamed songs on Spotify in 2023.",
    "ES": "canciones más escuchadas en Spotify en 2023.",
},

# ── KPI labels ────────────────────────────────────────────────────────────────
"kpi_songs": {
    "PT": "Músicas",
    "EN": "Songs",
    "ES": "Canciones",
},
"kpi_streams": {
    "PT": "Streams total",
    "EN": "Total streams",
    "ES": "Streams totales",
},
"kpi_median": {
    "PT": "Mediana streams",
    "EN": "Median streams",
    "ES": "Mediana streams",
},
"kpi_gini": {
    "PT": "Gini",
    "EN": "Gini",
    "ES": "Gini",
},
"kpi_top10": {
    "PT": "Top 10% streams",
    "EN": "Top 10% streams",
    "ES": "Top 10% streams",
},

# ── EDA Tab names ─────────────────────────────────────────────────────────────
"tab_dist": {
    "PT": "Distribuição",
    "EN": "Distribution",
    "ES": "Distribución",
},
"tab_season": {
    "PT": "Sazonalidade",
    "EN": "Seasonality",
    "ES": "Estacionalidad",
},
"tab_eras": {
    "PT": "Eras",
    "EN": "Eras",
    "ES": "Eras",
},
"tab_collab": {
    "PT": "Colaborações",
    "EN": "Collaborations",
    "ES": "Colaboraciones",
},
"tab_top": {
    "PT": "Top músicas",
    "EN": "Top songs",
    "ES": "Top canciones",
},

# ── Q1 ────────────────────────────────────────────────────────────────────────
"q1_num": {
    "PT": "Q1 · Distribuição",
    "EN": "Q1 · Distribution",
    "ES": "Q1 · Distribución",
},
"q1_title": {
    "PT": "Quão desigual é a<br>distribuição de streams?",
    "EN": "How unequal is the<br>streams distribution?",
    "ES": "¿Cuán desigual es la<br>distribución de streams?",
},
"q1_desc": {
    "PT": "Histograma, escala logarítmica, Curva de Lorenz e Coeficiente de Gini",
    "EN": "Histogram, log scale, Lorenz Curve and Gini Coefficient",
    "ES": "Histograma, escala logarítmica, Curva de Lorenz y Coeficiente de Gini",
},
"q1_chart1": {
    "PT": "Distribuição em log₁₀",
    "EN": "Distribution in log₁₀",
    "ES": "Distribución en log₁₀",
},
"q1_chart2": {
    "PT": "Curva de Lorenz",
    "EN": "Lorenz Curve",
    "ES": "Curva de Lorenz",
},
"q1_xaxis": {
    "PT": "log₁₀ (streams)",
    "EN": "log₁₀ (streams)",
    "ES": "log₁₀ (streams)",
},
"q1_yaxis": {
    "PT": "Nº de músicas",
    "EN": "No. of songs",
    "ES": "Nº de canciones",
},
"q1_x2": {
    "PT": "% músicas (acumulado)",
    "EN": "% songs (cumulative)",
    "ES": "% canciones (acumulado)",
},
"q1_y2": {
    "PT": "% streams (acumulado)",
    "EN": "% streams (cumulative)",
    "ES": "% streams (acumulado)",
},
"q1_median_lbl": {
    "PT": "Mediana",
    "EN": "Median",
    "ES": "Mediana",
},
"q1_mean_lbl": {
    "PT": "Média",
    "EN": "Mean",
    "ES": "Media",
},
"q1_perfect": {
    "PT": "Igualdade perfeita",
    "EN": "Perfect equality",
    "ES": "Igualdad perfecta",
},
"q1_insight": {
    "PT": "Distribuição em <span class='hl'>lei de potência</span> — média ({mean}M) quase o dobro da mediana ({median}M). Gini de <span class='hl'>{gini}</span>: top 10% gera <span class='hl'>{top10}%</span> de todos os streams.",
    "EN": "Distribution follows a <span class='hl'>power law</span> — mean ({mean}M) is nearly double the median ({median}M). Gini of <span class='hl'>{gini}</span>: top 10% generates <span class='hl'>{top10}%</span> of all streams.",
    "ES": "Distribución en <span class='hl'>ley de potencia</span> — la media ({mean}M) es casi el doble de la mediana ({median}M). Gini de <span class='hl'>{gini}</span>: el top 10% genera <span class='hl'>{top10}%</span> de todos los streams.",
},

# ── Q2 ────────────────────────────────────────────────────────────────────────
"q2_num": {
    "PT": "Q2 · Sazonalidade",
    "EN": "Q2 · Seasonality",
    "ES": "Q2 · Estacionalidad",
},
"q2_title": {
    "PT": "Existe sazonalidade<br>nos lançamentos?",
    "EN": "Is there seasonality<br>in music releases?",
    "ES": "¿Existe estacionalidad<br>en los lanzamientos?",
},
"q2_desc": {
    "PT": "Volume de lançamentos e streams mediana por mês — 2022–2023",
    "EN": "Release volume and median streams by month — 2022–2023",
    "ES": "Volumen de lanzamientos y streams mediana por mes — 2022–2023",
},
"q2_chart1": {
    "PT": "Lançamentos por mês",
    "EN": "Releases per month",
    "ES": "Lanzamientos por mes",
},
"q2_chart2": {
    "PT": "Streams mediana por mês",
    "EN": "Median streams per month",
    "ES": "Streams mediana por mes",
},
"q2_yaxis1": {
    "PT": "Nº de músicas",
    "EN": "No. of songs",
    "ES": "Nº de canciones",
},
"q2_yaxis2": {
    "PT": "Streams mediana (M)",
    "EN": "Median streams (M)",
    "ES": "Streams mediana (M)",
},
"q2_months": {
    "PT": ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"],
    "EN": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "ES": ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
},
"q2_insight": {
    "PT": "<span class='hl'>{best_vol}</span> lidera em lançamentos ({count_max} músicas). <strong>{worst}</strong> é o mais calmo ({count_min}). Músicas de <span class='hl'>{best_str}</span> têm maior mediana de streams — <span class='hl'>trade-off entre volume e visibilidade</span>.",
    "EN": "<span class='hl'>{best_vol}</span> leads in releases ({count_max} songs). <strong>{worst}</strong> is the quietest ({count_min}). Songs released in <span class='hl'>{best_str}</span> have the highest median streams — <span class='hl'>trade-off between volume and visibility</span>.",
    "ES": "<span class='hl'>{best_vol}</span> lidera en lanzamientos ({count_max} canciones). <strong>{worst}</strong> es el mes más tranquilo ({count_min}). Las canciones de <span class='hl'>{best_str}</span> tienen la mayor mediana de streams — <span class='hl'>trade-off entre volumen y visibilidad</span>.",
},

# ── Q3 ────────────────────────────────────────────────────────────────────────
"q3_num": {
    "PT": "Q3 · Eras",
    "EN": "Q3 · Eras",
    "ES": "Q3 · Eras",
},
"q3_title": {
    "PT": "Músicas antigas ainda<br>dominam os charts?",
    "EN": "Do older songs still<br>dominate the charts?",
    "ES": "¿Las canciones antiguas aún<br>dominan los charts?",
},
"q3_desc": {
    "PT": "Comparação de streams por era · viés de sobrevivência",
    "EN": "Streams comparison by era · survivorship bias",
    "ES": "Comparación de streams por era · sesgo de supervivencia",
},
"q3_chart1": {
    "PT": "Músicas por era",
    "EN": "Songs per era",
    "ES": "Canciones por era",
},
"q3_chart2": {
    "PT": "Streams por era (boxplot)",
    "EN": "Streams by era (boxplot)",
    "ES": "Streams por era (boxplot)",
},
"q3_yaxis1": {
    "PT": "Nº de músicas",
    "EN": "No. of songs",
    "ES": "Nº de canciones",
},
"q3_yaxis2": {
    "PT": "Streams (M)",
    "EN": "Streams (M)",
    "ES": "Streams (M)",
},
"q3_table_cols": {
    "PT": {"count":"Músicas","median":"Mediana (M)","mean":"Média (M)","max":"Máx (M)"},
    "EN": {"count":"Songs","median":"Median (M)","mean":"Mean (M)","max":"Max (M)"},
    "ES": {"count":"Canciones","median":"Mediana (M)","mean":"Media (M)","max":"Máx (M)"},
},
"q3_insight": {
    "PT": "⚠️ <strong>Viés de sobrevivência:</strong> Os <span class='hl'>anos 2000</span> têm a maior mediana — mas aqui só estão os <span class='hl'>maiores clássicos de sempre</span>. Catálogo histórico = <span class='hl'>activo passivo de alto valor</span> para as editoras.",
    "EN": "⚠️ <strong>Survivorship bias:</strong> The <span class='hl'>2000s</span> have the highest median — but only the <span class='hl'>greatest classics of all time</span> are here. Historical catalogue = <span class='hl'>high-value passive asset</span> for record labels.",
    "ES": "⚠️ <strong>Sesgo de supervivencia:</strong> Los <span class='hl'>años 2000</span> tienen la mayor mediana — pero aquí solo están los <span class='hl'>mayores clásicos de todos los tiempos</span>. El catálogo histórico = <span class='hl'>activo pasivo de alto valor</span> para las discográficas.",
},

# ── Q4 ────────────────────────────────────────────────────────────────────────
"q4_num": {
    "PT": "Q4 · Colaborações",
    "EN": "Q4 · Collaborations",
    "ES": "Q4 · Colaboraciones",
},
"q4_title": {
    "PT": "Colaborações geram mais<br>streams do que solos?",
    "EN": "Do collaborations generate<br>more streams than solos?",
    "ES": "¿Las colaboraciones generan<br>más streams que los solos?",
},
"q4_desc": {
    "PT": "Solo vs. Colaboração · análise por número de artistas",
    "EN": "Solo vs. Collaboration · analysis by number of artists",
    "ES": "Solo vs. Colaboración · análisis por número de artistas",
},
"q4_chart1": {
    "PT": "Volume no dataset",
    "EN": "Volume in dataset",
    "ES": "Volumen en el dataset",
},
"q4_chart2": {
    "PT": "Streams mediana",
    "EN": "Median streams",
    "ES": "Streams mediana",
},
"q4_chart3": {
    "PT": "Mediana por nº de artistas",
    "EN": "Median by no. of artists",
    "ES": "Mediana por nº de artistas",
},
"q4_xaxis3": {
    "PT": "Nº de artistas",
    "EN": "No. of artists",
    "ES": "Nº de artistas",
},
"q4_yaxis": {
    "PT": "Nº de músicas",
    "EN": "No. of songs",
    "ES": "Nº de canciones",
},
"q4_yaxis2": {
    "PT": "Streams mediana (M)",
    "EN": "Median streams (M)",
    "ES": "Streams mediana (M)",
},
"q4_solo": {
    "PT": "Solo",
    "EN": "Solo",
    "ES": "Solo",
},
"q4_collab": {
    "PT": "Colaboração",
    "EN": "Collaboration",
    "ES": "Colaboración",
},
"q4_insight": {
    "PT": "💡 <strong>Resultado contra-intuitivo:</strong> Solos têm mediana <span class='hl'>{diff:.0f}% superior</span> ({solo:.0f}M vs {collab:.0f}M). <strong>O factor determinante é a base de fãs do artista principal</strong>, não o número de artistas.",
    "EN": "💡 <strong>Counter-intuitive result:</strong> Solos have <span class='hl'>{diff:.0f}% higher</span> median ({solo:.0f}M vs {collab:.0f}M). <strong>The determining factor is the lead artist's fanbase</strong>, not the number of artists.",
    "ES": "💡 <strong>Resultado contraintuitivo:</strong> Los solos tienen mediana <span class='hl'>{diff:.0f}% superior</span> ({solo:.0f}M vs {collab:.0f}M). <strong>El factor determinante es la base de fans del artista principal</strong>, no el número de artistas.",
},

# ── Top tab ───────────────────────────────────────────────────────────────────
"top_num": {
    "PT": "Top · Ranking",
    "EN": "Top · Ranking",
    "ES": "Top · Ranking",
},
"top_title": {
    "PT": "As músicas<br>mais ouvidas.",
    "EN": "The most<br>streamed songs.",
    "ES": "Las canciones<br>más escuchadas.",
},
"top_desc": {
    "PT": "Ranking dinâmico — filtra e ordena por qualquer métrica",
    "EN": "Dynamic ranking — filter and sort by any metric",
    "ES": "Ranking dinámico — filtra y ordena por cualquier métrica",
},
"top_slider": {
    "PT": "Nº de músicas",
    "EN": "No. of songs",
    "ES": "Nº de canciones",
},
"top_sortby": {
    "PT": "Ordenar por",
    "EN": "Sort by",
    "ES": "Ordenar por",
},
"top_chart": {
    "PT": "Top 15 — streams totais",
    "EN": "Top 15 — total streams",
    "ES": "Top 15 — streams totales",
},
"top_xaxis": {
    "PT": "Streams (M)",
    "EN": "Streams (M)",
    "ES": "Streams (M)",
},
"top_col_song": {
    "PT": "Música",
    "EN": "Song",
    "ES": "Canción",
},
"top_col_artist": {
    "PT": "Artista(s)",
    "EN": "Artist(s)",
    "ES": "Artista(s)",
},
"top_col_year": {
    "PT": "Ano",
    "EN": "Year",
    "ES": "Año",
},
"top_col_playlists": {
    "PT": "Playlists",
    "EN": "Playlists",
    "ES": "Playlists",
},
"top_col_mode": {
    "PT": "Modo",
    "EN": "Mode",
    "ES": "Modo",
},
"top_col_type": {
    "PT": "Tipo",
    "EN": "Type",
    "ES": "Tipo",
},

# ── Correlations module ───────────────────────────────────────────────────────
"corr_eyebrow": {
    "PT": "Correlações · Atributos musicais",
    "EN": "Correlations · Musical attributes",
    "ES": "Correlaciones · Atributos musicales",
},
"corr_title1": {
    "PT": "O que faz",
    "EN": "What makes",
    "ES": "¿Qué hace",
},
"corr_title2": {
    "PT": "uma música?",
    "EN": "a song?",
    "ES": "una canción?",
},
"corr_sub": {
    "PT": "Relações entre BPM, energy, danceability, valence e streams —",
    "EN": "Relationships between BPM, energy, danceability, valence and streams —",
    "ES": "Relaciones entre BPM, energy, danceability, valence y streams —",
},
"corr_sub2": {
    "PT": "músicas analisadas.",
    "EN": "songs analysed.",
    "ES": "canciones analizadas.",
},
"corr_tabs": {
    "PT": ["Heatmap atributos","Scatter interactivo","Playlists → streams","Major vs. Minor","Por ano","Por género","Cross-platform"],
    "EN": ["Attribute heatmap","Interactive scatter","Playlists → streams","Major vs. Minor","By year","By genre","Cross-platform"],
    "ES": ["Heatmap atributos","Scatter interactivo","Playlists → streams","Mayor vs. Menor","Por año","Por género","Cross-platform"],
},
"c1_num": {
    "PT": "C1 · Heatmap",
    "EN": "C1 · Heatmap",
    "ES": "C1 · Heatmap",
},
"c1_title": {
    "PT": "Correlação entre<br>atributos musicais",
    "EN": "Correlation between<br>musical attributes",
    "ES": "Correlación entre<br>atributos musicales",
},
"c1_desc": {
    "PT": "Matriz de correlação de Pearson entre atributos e streams",
    "EN": "Pearson correlation matrix between attributes and streams",
    "ES": "Matriz de correlación de Pearson entre atributos y streams",
},
"c1_chart": {
    "PT": "Matriz de correlação (Pearson)",
    "EN": "Correlation matrix (Pearson)",
    "ES": "Matriz de correlación (Pearson)",
},
"c2_num": {
    "PT": "C2 · Scatter",
    "EN": "C2 · Scatter",
    "ES": "C2 · Scatter",
},
"c2_title": {
    "PT": "Atributo vs. streams<br>por era",
    "EN": "Attribute vs. streams<br>by era",
    "ES": "Atributo vs. streams<br>por era",
},
"c2_desc": {
    "PT": "Cada ponto é uma música — selecciona o atributo e a escala",
    "EN": "Each point is a song — select the attribute and scale",
    "ES": "Cada punto es una canción — selecciona el atributo y la escala",
},
"c2_selector": {
    "PT": "Atributo musical (eixo X)",
    "EN": "Musical attribute (X axis)",
    "ES": "Atributo musical (eje X)",
},
"c2_toggle": {
    "PT": "Escala log nos streams",
    "EN": "Log scale on streams",
    "ES": "Escala log en streams",
},
"c3_num": {
    "PT": "C3 · Playlists",
    "EN": "C3 · Playlists",
    "ES": "C3 · Playlists",
},
"c3_title": {
    "PT": "Playlists são o principal<br>driver de streams?",
    "EN": "Are playlists the main<br>driver of streams?",
    "ES": "¿Las playlists son el principal<br>driver de streams?",
},
"c3_desc": {
    "PT": "Correlação entre presença em playlists e número de streams",
    "EN": "Correlation between playlist presence and number of streams",
    "ES": "Correlación entre presencia en playlists y número de streams",
},
"c4_num": {
    "PT": "C4 · Modo",
    "EN": "C4 · Mode",
    "ES": "C4 · Modo",
},
"c4_title": {
    "PT": "Major vs. Minor —<br>importa o modo musical?",
    "EN": "Major vs. Minor —<br>does the musical mode matter?",
    "ES": "Mayor vs. Menor —<br>¿importa el modo musical?",
},
"c4_desc": {
    "PT": "Distribuição de valence, energy e streams por modo",
    "EN": "Distribution of valence, energy and streams by mode",
    "ES": "Distribución de valence, energy y streams por modo",
},
"c5_num": {
    "PT": "C5 · Temporal",
    "EN": "C5 · Temporal",
    "ES": "C5 · Temporal",
},
"c5_title": {
    "PT": "Como evoluíram<br>os atributos por ano?",
    "EN": "How did attributes<br>evolve over the years?",
    "ES": "¿Cómo evolucionaron<br>los atributos por año?",
},
"c5_desc": {
    "PT": "Heatmap de médias dos atributos musicais por ano de lançamento",
    "EN": "Heatmap of average musical attributes by release year",
    "ES": "Heatmap de promedios de atributos musicales por año de lanzamiento",
},
"c6_num": {
    "PT": "C6 · Géneros inferidos",
    "EN": "C6 · Inferred genres",
    "ES": "C6 · Géneros inferidos",
},
"c6_title": {
    "PT": "Perfis de géneros<br>sem usar labels",
    "EN": "Genre profiles<br>without using labels",
    "ES": "Perfiles de géneros<br>sin usar etiquetas",
},
"c6_desc": {
    "PT": "K-Means (k=5) sobre atributos musicais — géneros emergentes",
    "EN": "K-Means (k=5) on musical attributes — emerging genres",
    "ES": "K-Means (k=5) sobre atributos musicales — géneros emergentes",
},
"c7_num": {
    "PT": "C7 · Cross-platform",
    "EN": "C7 · Cross-platform",
    "ES": "C7 · Cross-platform",
},
"c7_title": {
    "PT": "Um hit no Spotify<br>é hit em todo o lado?",
    "EN": "Is a Spotify hit<br>a hit everywhere?",
    "ES": "¿Un hit en Spotify<br>es hit en todas partes?",
},
"c7_desc": {
    "PT": "Consistência de rankings entre Spotify, Apple Music, Deezer e Shazam",
    "EN": "Ranking consistency between Spotify, Apple Music, Deezer and Shazam",
    "ES": "Consistencia de rankings entre Spotify, Apple Music, Deezer y Shazam",
},

# ── ML module ─────────────────────────────────────────────────────────────────
"ml_eyebrow": {
    "PT": "Machine Learning · Spotify 2023",
    "EN": "Machine Learning · Spotify 2023",
    "ES": "Machine Learning · Spotify 2023",
},
"ml_title1": {
    "PT": "Prever",
    "EN": "Predicting",
    "ES": "Predecir",
},
"ml_title2": {
    "PT": "o sucesso.",
    "EN": "success.",
    "ES": "el éxito.",
},
"ml_sub": {
    "PT": "Modelos interactivos treinados sobre",
    "EN": "Interactive models trained on",
    "ES": "Modelos interactivos entrenados sobre",
},
"ml_sub2": {
    "PT": "músicas — ajusta os parâmetros e vê o impacto em tempo real.",
    "EN": "songs — adjust parameters and see the impact in real time.",
    "ES": "canciones — ajusta los parámetros y ve el impacto en tiempo real.",
},
"ml_params_label": {
    "PT": "⚙️ Parâmetros do modelo (aplicam-se a todos os tabs)",
    "EN": "⚙️ Model parameters (apply to all tabs)",
    "ES": "⚙️ Parámetros del modelo (se aplican a todas las pestañas)",
},
"ml_n_est": {
    "PT": "Nº de árvores (n_estimators)",
    "EN": "No. of trees (n_estimators)",
    "ES": "Nº de árboles (n_estimators)",
},
"ml_n_est_help": {
    "PT": "Mais árvores = modelo mais estável mas mais lento",
    "EN": "More trees = more stable model but slower",
    "ES": "Más árboles = modelo más estable pero más lento",
},
"ml_max_d": {
    "PT": "Profundidade máxima (max_depth)",
    "EN": "Maximum depth (max_depth)",
    "ES": "Profundidad máxima (max_depth)",
},
"ml_max_d_help": {
    "PT": "Mais profundidade = mais complexo, risco de overfitting",
    "EN": "More depth = more complex, risk of overfitting",
    "ES": "Más profundidad = más complejo, riesgo de overfitting",
},
"ml_features_used": {
    "PT": "Features usadas",
    "EN": "Features used",
    "ES": "Features usadas",
},
"ml_features_desc": {
    "PT": "atributos musicais + playlists + ano/mês",
    "EN": "musical attributes + playlists + year/month",
    "ES": "atributos musicales + playlists + año/mes",
},
"ml_tabs": {
    "PT": ["Regressão","Importância de features","Classificação de sucesso","Curva de aprendizagem","UMAP 2D"],
    "EN": ["Regression","Feature importance","Hit classification","Learning curve","UMAP 2D"],
    "ES": ["Regresión","Importancia de features","Clasificación de éxito","Curva de aprendizaje","UMAP 2D"],
},
"ml1_num": {
    "PT": "ML1 · Regressão",
    "EN": "ML1 · Regression",
    "ES": "ML1 · Regresión",
},
"ml1_title": {
    "PT": "Consegues prever<br>o número de streams?",
    "EN": "Can we predict<br>the number of streams?",
    "ES": "¿Podemos predecir<br>el número de streams?",
},
"ml1_desc": {
    "PT": "Random Forest Regressor — treino/teste 80/20 · target: streams (M)",
    "EN": "Random Forest Regressor — 80/20 train/test split · target: streams (M)",
    "ES": "Random Forest Regressor — split 80/20 entrenamiento/prueba · objetivo: streams (M)",
},
"ml1_r2_box": {
    "PT": "📖 <strong>O que é R²?</strong> O coeficiente de determinação mede <span class='hl'>quanto da variância dos streams o modelo consegue explicar</span>. R²=1.0 seria perfeição; R²=0 significa que o modelo não é melhor do que prever sempre a média.",
    "EN": "📖 <strong>What is R²?</strong> The coefficient of determination measures <span class='hl'>how much of the stream variance the model can explain</span>. R²=1.0 would be perfect; R²=0 means the model is no better than always predicting the mean.",
    "ES": "📖 <strong>¿Qué es R²?</strong> El coeficiente de determinación mide <span class='hl'>cuánta varianza de los streams puede explicar el modelo</span>. R²=1.0 sería perfecto; R²=0 significa que el modelo no es mejor que predecir siempre la media.",
},
"ml1_training": {
    "PT": "A treinar o modelo...",
    "EN": "Training the model...",
    "ES": "Entrenando el modelo...",
},
"ml1_kpi_r2": {
    "PT": "R² (teste)",
    "EN": "R² (test)",
    "ES": "R² (prueba)",
},
"ml1_kpi_good": {
    "PT": "✓ Bom resultado",
    "EN": "✓ Good result",
    "ES": "✓ Buen resultado",
},
"ml1_kpi_mod": {
    "PT": "⚠ Moderado",
    "EN": "⚠ Moderate",
    "ES": "⚠ Moderado",
},
"ml1_kpi_weak": {
    "PT": "✗ Fraco",
    "EN": "✗ Weak",
    "ES": "✗ Débil",
},
"ml1_kpi_rmse": {
    "PT": "RMSE",
    "EN": "RMSE",
    "ES": "RMSE",
},
"ml1_kpi_rmse_desc": {
    "PT": "erro médio em streams",
    "EN": "average prediction error",
    "ES": "error promedio en streams",
},
"ml1_kpi_test": {
    "PT": "Músicas no teste",
    "EN": "Songs in test set",
    "ES": "Canciones en prueba",
},
"ml1_kpi_test_desc": {
    "PT": "20% do dataset",
    "EN": "20% of dataset",
    "ES": "20% del dataset",
},
"ml1_chart1": {
    "PT": "Real vs. Previsto (conjunto de teste)",
    "EN": "Actual vs. Predicted (test set)",
    "ES": "Real vs. Predicho (conjunto de prueba)",
},
"ml1_chart2": {
    "PT": "Resíduos (erro do modelo)",
    "EN": "Residuals (model error)",
    "ES": "Residuos (error del modelo)",
},
"ml1_xaxis1": {
    "PT": "Streams reais (M)",
    "EN": "Actual streams (M)",
    "ES": "Streams reales (M)",
},
"ml1_yaxis1": {
    "PT": "Streams previstos (M)",
    "EN": "Predicted streams (M)",
    "ES": "Streams predichos (M)",
},
"ml1_perfect": {
    "PT": "Perfeito",
    "EN": "Perfect",
    "ES": "Perfecto",
},
"ml1_residual_x": {
    "PT": "Streams previstos (M)",
    "EN": "Predicted streams (M)",
    "ES": "Streams predichos (M)",
},
"ml1_residual_y": {
    "PT": "Resíduo (M)",
    "EN": "Residual (M)",
    "ES": "Residuo (M)",
},
"ml2_num": {
    "PT": "ML2 · Feature Importance",
    "EN": "ML2 · Feature Importance",
    "ES": "ML2 · Importancia de features",
},
"ml2_title": {
    "PT": "O que o modelo<br>aprendeu?",
    "EN": "What did the model<br>learn?",
    "ES": "¿Qué aprendió<br>el modelo?",
},
"ml2_desc": {
    "PT": "Importância de features do Random Forest — qual variável tem mais peso?",
    "EN": "Random Forest feature importance — which variable matters most?",
    "ES": "Importancia de features del Random Forest — ¿qué variable tiene más peso?",
},
"ml2_box": {
    "PT": "📖 <strong>O que é Feature Importance?</strong> Mede <span class='hl'>quanto cada variável contribui para reduzir o erro</span> nas árvores de decisão. Valores mais altos = variável mais importante para as previsões.",
    "EN": "📖 <strong>What is Feature Importance?</strong> Measures <span class='hl'>how much each variable contributes to reducing the error</span> in decision trees. Higher values = more important variable for predictions.",
    "ES": "📖 <strong>¿Qué es Feature Importance?</strong> Mide <span class='hl'>cuánto contribuye cada variable a reducir el error</span> en los árboles de decisión. Valores más altos = variable más importante para las predicciones.",
},
"ml2_spinner": {
    "PT": "A calcular importâncias...",
    "EN": "Calculating importances...",
    "ES": "Calculando importancias...",
},
"ml2_chart": {
    "PT": "Importância de features — Regressão (streams)",
    "EN": "Feature importance — Regression (streams)",
    "ES": "Importancia de features — Regresión (streams)",
},
"ml2_xaxis": {
    "PT": "Importância relativa",
    "EN": "Relative importance",
    "ES": "Importancia relativa",
},
"ml3_num": {
    "PT": "ML3 · Classificação",
    "EN": "ML3 · Classification",
    "ES": "ML3 · Clasificación",
},
"ml3_title": {
    "PT": "Hit ou não hit?<br>O modelo decide.",
    "EN": "Hit or not hit?<br>The model decides.",
    "ES": "¿Hit o no hit?<br>El modelo decide.",
},
"ml3_box": {
    "PT": "📖 <strong>O que é Accuracy?</strong> A percentagem de músicas <span class='hl'>correctamente classificadas</span> como hit ou não-hit. A matriz de confusão mostra onde o modelo erra.",
    "EN": "📖 <strong>What is Accuracy?</strong> The percentage of songs <span class='hl'>correctly classified</span> as hit or non-hit. The confusion matrix shows where the model makes mistakes.",
    "ES": "📖 <strong>¿Qué es Accuracy?</strong> El porcentaje de canciones <span class='hl'>clasificadas correctamente</span> como hit o no-hit. La matriz de confusión muestra dónde el modelo se equivoca.",
},
"ml3_spinner": {
    "PT": "A treinar classificador...",
    "EN": "Training classifier...",
    "ES": "Entrenando clasificador...",
},
"ml3_precision_desc": {
    "PT": "hits correctos previstos",
    "EN": "correctly predicted hits",
    "ES": "hits correctamente predichos",
},
"ml3_recall_desc": {
    "PT": "hits reais detectados",
    "EN": "actual hits detected",
    "ES": "hits reales detectados",
},
"ml3_cm_x": {
    "PT": ["Não-hit (prev.)","Hit (prev.)"],
    "EN": ["Non-hit (pred.)","Hit (pred.)"],
    "ES": ["No-hit (pred.)","Hit (pred.)"],
},
"ml3_cm_y": {
    "PT": ["Não-hit (real)","Hit (real)"],
    "EN": ["Non-hit (actual)","Hit (actual)"],
    "ES": ["No-hit (real)","Hit (real)"],
},
"ml3_chart1": {
    "PT": "Matriz de confusão",
    "EN": "Confusion matrix",
    "ES": "Matriz de confusión",
},
"ml3_chart2": {
    "PT": "Features mais importantes (classificação)",
    "EN": "Most important features (classification)",
    "ES": "Features más importantes (clasificación)",
},
"ml4_num": {
    "PT": "ML4 · Curva de aprendizagem",
    "EN": "ML4 · Learning curve",
    "ES": "ML4 · Curva de aprendizaje",
},
"ml4_title": {
    "PT": "O modelo tem<br>overfitting?",
    "EN": "Does the model<br>have overfitting?",
    "ES": "¿El modelo tiene<br>overfitting?",
},
"ml4_desc": {
    "PT": "Train vs. Validation score em função do tamanho do dataset",
    "EN": "Train vs. Validation score as a function of dataset size",
    "ES": "Train vs. Validation score en función del tamaño del dataset",
},
"ml4_box": {
    "PT": "📖 <strong>Overfitting vs. Underfitting:</strong> Se o score de treino é muito superior ao de validação → <span class='hl'>overfitting</span>. Se ambos são baixos → <span class='hl'>underfitting</span>. O ideal é que as duas curvas convirjam num valor alto.",
    "EN": "📖 <strong>Overfitting vs. Underfitting:</strong> If training score is much higher than validation → <span class='hl'>overfitting</span>. If both are low → <span class='hl'>underfitting</span>. Ideally both curves converge at a high value.",
    "ES": "📖 <strong>Overfitting vs. Underfitting:</strong> Si el score de entrenamiento es mucho mayor que el de validación → <span class='hl'>overfitting</span>. Si ambos son bajos → <span class='hl'>underfitting</span>. Lo ideal es que las dos curvas converjan en un valor alto.",
},
"ml4_spinner": {
    "PT": "A calcular curvas de aprendizagem (pode demorar alguns segundos)...",
    "EN": "Calculating learning curves (may take a few seconds)...",
    "ES": "Calculando curvas de aprendizaje (puede tardar unos segundos)...",
},
"ml4_train": {
    "PT": "Treino",
    "EN": "Training",
    "ES": "Entrenamiento",
},
"ml4_val": {
    "PT": "Validação (CV)",
    "EN": "Validation (CV)",
    "ES": "Validación (CV)",
},
"ml4_chart": {
    "PT": "Curva de aprendizagem — R² em função do tamanho de treino",
    "EN": "Learning curve — R² as a function of training size",
    "ES": "Curva de aprendizaje — R² en función del tamaño de entrenamiento",
},
"ml4_xaxis": {
    "PT": "Nº de amostras de treino",
    "EN": "No. of training samples",
    "ES": "Nº de muestras de entrenamiento",
},
"ml4_good": {
    "PT": "✓ Gap controlado — o modelo generaliza bem para dados não vistos.",
    "EN": "✓ Controlled gap — the model generalises well to unseen data.",
    "ES": "✓ Gap controlado — el modelo generaliza bien para datos no vistos.",
},
"ml4_overfit": {
    "PT": "⚠️ Gap elevado — sinais de overfitting. Reduz max_depth ou aumenta os dados.",
    "EN": "⚠️ High gap — signs of overfitting. Reduce max_depth or add more data.",
    "ES": "⚠️ Gap elevado — señales de overfitting. Reduce max_depth o aumenta los datos.",
},
"ml5_num": {
    "PT": "ML5 · UMAP",
    "EN": "ML5 · UMAP",
    "ES": "ML5 · UMAP",
},
"ml5_title": {
    "PT": "O espaço das músicas<br>em 2 dimensões.",
    "EN": "The song space<br>in 2 dimensions.",
    "ES": "El espacio de canciones<br>en 2 dimensiones.",
},
"ml5_desc": {
    "PT": "UMAP reduz 12 dimensões a 2 — cada ponto é uma música",
    "EN": "UMAP reduces 12 dimensions to 2 — each point is a song",
    "ES": "UMAP reduce 12 dimensiones a 2 — cada punto es una canción",
},
"ml5_box": {
    "PT": "📖 <strong>O que é UMAP?</strong> <span class='hl'>Uniform Manifold Approximation and Projection</span> — comprime múltiplas dimensões num plano 2D preservando a estrutura de vizinhança. Músicas parecidas ficam próximas; músicas diferentes ficam afastadas.",
    "EN": "📖 <strong>What is UMAP?</strong> <span class='hl'>Uniform Manifold Approximation and Projection</span> — compresses multiple dimensions into a 2D plane preserving neighbourhood structure. Similar songs stay close; different songs stay apart.",
    "ES": "📖 <strong>¿Qué es UMAP?</strong> <span class='hl'>Uniform Manifold Approximation and Projection</span> — comprime múltiples dimensiones en un plano 2D preservando la estructura de vecindad. Canciones similares se quedan cerca; canciones diferentes se alejan.",
},
"ml5_color_by": {
    "PT": "Colorir pontos por",
    "EN": "Colour points by",
    "ES": "Colorear puntos por",
},
"ml5_color_opts": {
    "PT": ["Era", "Género inferido", "Streams (M)", "Modo (Major/Minor)"],
    "EN": ["Era", "Inferred genre", "Streams (M)", "Mode (Major/Minor)"],
    "ES": ["Era", "Género inferido", "Streams (M)", "Modo (Mayor/Menor)"],
},
"ml5_spinner": {
    "PT": "A projectar com UMAP (pode demorar ~10s)...",
    "EN": "Projecting with UMAP (may take ~10s)...",
    "ES": "Proyectando con UMAP (puede tardar ~10s)...",
},
"ml5_chart": {
    "PT": "UMAP 2D — colorido por {color_by}",
    "EN": "UMAP 2D — coloured by {color_by}",
    "ES": "UMAP 2D — coloreado por {color_by}",
},

# ── Footer ────────────────────────────────────────────────────────────────────
"footer_left": {
    "PT": "🎵 Spotify 2023 · Dataset: Kaggle",
    "EN": "🎵 Spotify 2023 · Dataset: Kaggle",
    "ES": "🎵 Spotify 2023 · Dataset: Kaggle",
},
"footer_dev_by": {
    "PT": "Desenvolvido por",
    "EN": "Developed by",
    "ES": "Desarrollado por",
},
}


def t(key, lang, **kwargs):
    """Get translation for key in given language, with optional format kwargs."""
    val = T.get(key, {}).get(lang, T.get(key, {}).get("PT", key))
    if kwargs:
        try:
            val = val.format(**kwargs)
        except (KeyError, ValueError):
            pass
    return val
