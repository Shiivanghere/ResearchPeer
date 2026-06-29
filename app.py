# import streamlit as st
# import time
# from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# # ── Page config ──────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="ResearchMind · AI Research Agent",
#     page_icon="🔬",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ── Custom CSS ────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

# /* ── Reset & base ── */
# html, body, [class*="css"] {
#     font-family: 'DM Sans', sans-serif;
#     color: #e8e4dc;
# }

# .stApp {
#     background: #0a0a0f;
#     background-image:
#         radial-gradient(ellipse 80% 50% at 20% -10%, rgba(255,140,50,0.12) 0%, transparent 60%),
#         radial-gradient(ellipse 60% 40% at 80% 110%, rgba(255,80,30,0.08) 0%, transparent 55%);
# }

# /* ── Hide default streamlit chrome ── */
# #MainMenu, footer, header { visibility: hidden; }
# .block-container { padding: 2rem 3rem 4rem; max-width: 1200px; }

# /* ── Hero header ── */
# .hero {
#     text-align: center;
#     padding: 3.5rem 0 2.5rem;
#     position: relative;
# }
# .hero-eyebrow {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.7rem;
#     font-weight: 500;
#     letter-spacing: 0.25em;
#     text-transform: uppercase;
#     color: #ff8c32;
#     margin-bottom: 1rem;
#     opacity: 0.9;
# }
# .hero h1 {
#     font-family: 'Syne', sans-serif;
#     font-size: clamp(2.8rem, 6vw, 5rem);
#     font-weight: 800;
#     line-height: 1.0;
#     letter-spacing: -0.03em;
#     color: #f0ebe0;
#     margin: 0 0 1rem;
# }
# .hero h1 span {
#     color: #ff8c32;
# }
# .hero-sub {
#     font-size: 1.05rem;
#     font-weight: 300;
#     color: #a09890;
#     max-width: 520px;
#     margin: 0 auto;
#     line-height: 1.65;
# }

# /* ── Divider ── */
# .divider {
#     height: 1px;
#     background: linear-gradient(90deg, transparent, rgba(255,140,50,0.3), transparent);
#     margin: 2rem 0;
# }

# /* ── Input card ── */
# .input-card {
#     background: rgba(255,255,255,0.03);
#     border: 1px solid rgba(255,140,50,0.15);
#     border-radius: 16px;
#     padding: 2rem 2.5rem;
#     margin-bottom: 2rem;
#     backdrop-filter: blur(8px);
# }

# /* ── Streamlit input overrides ── */
# .stTextInput > div > div > input {
#     background: rgba(255,255,255,0.05) !important;
#     border: 1px solid rgba(255,140,50,0.25) !important;
#     border-radius: 10px !important;
#     color: #f0ebe0 !important;
#     font-family: 'DM Sans', sans-serif !important;
#     font-size: 1rem !important;
#     padding: 0.75rem 1rem !important;
#     transition: border-color 0.2s, box-shadow 0.2s !important;
# }
# .stTextInput > div > div > input:focus {
#     border-color: #ff8c32 !important;
#     box-shadow: 0 0 0 3px rgba(255,140,50,0.12) !important;
# }
# .stTextInput > label {
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.72rem !important;
#     letter-spacing: 0.15em !important;
#     text-transform: uppercase !important;
#     color: #ff8c32 !important;
#     font-weight: 500 !important;
# }

# /* ── Button ── */
# .stButton > button {
#     background: linear-gradient(135deg, #ff8c32 0%, #ff5a1a 100%) !important;
#     color: #0a0a0f !important;
#     font-family: 'Syne', sans-serif !important;
#     font-weight: 700 !important;
#     font-size: 0.95rem !important;
#     letter-spacing: 0.04em !important;
#     border: none !important;
#     border-radius: 10px !important;
#     padding: 0.7rem 2.2rem !important;
#     cursor: pointer !important;
#     transition: transform 0.15s, box-shadow 0.15s, opacity 0.15s !important;
#     box-shadow: 0 4px 20px rgba(255,140,50,0.3) !important;
#     width: 100%;
# }
# .stButton > button:hover {
#     transform: translateY(-2px) !important;
#     box-shadow: 0 8px 28px rgba(255,140,50,0.4) !important;
#     opacity: 0.95 !important;
# }
# .stButton > button:active {
#     transform: translateY(0) !important;
# }

# /* ── Pipeline step cards ── */
# .step-card {
#     background: rgba(255,255,255,0.03);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 14px;
#     padding: 1.5rem 1.8rem;
#     margin-bottom: 1.2rem;
#     position: relative;
#     overflow: hidden;
#     transition: border-color 0.3s;
# }
# .step-card.active {
#     border-color: rgba(255,140,50,0.4);
#     background: rgba(255,140,50,0.04);
# }
# .step-card.done {
#     border-color: rgba(80,200,120,0.3);
#     background: rgba(80,200,120,0.03);
# }
# .step-card::before {
#     content: '';
#     position: absolute;
#     left: 0; top: 0; bottom: 0;
#     width: 3px;
#     border-radius: 14px 0 0 14px;
#     background: rgba(255,255,255,0.05);
#     transition: background 0.3s;
# }
# .step-card.active::before { background: #ff8c32; }
# .step-card.done::before   { background: #50c878; }

# .step-header {
#     display: flex;
#     align-items: center;
#     gap: 0.8rem;
#     margin-bottom: 0.3rem;
# }
# .step-num {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.68rem;
#     font-weight: 500;
#     letter-spacing: 0.15em;
#     color: #ff8c32;
#     opacity: 0.7;
# }
# .step-title {
#     font-family: 'Syne', sans-serif;
#     font-size: 0.95rem;
#     font-weight: 700;
#     color: #f0ebe0;
# }
# .step-status {
#     margin-left: auto;
#     font-family: 'DM Mono', monospace;
#     font-size: 0.68rem;
#     letter-spacing: 0.1em;
# }
# .status-waiting  { color: #555; }
# .status-running  { color: #ff8c32; }
# .status-done     { color: #50c878; }

# /* ── Result panels ── */
# .result-panel {
#     background: rgba(255,255,255,0.025);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 14px;
#     padding: 1.8rem 2rem;
#     margin-top: 1rem;
#     margin-bottom: 1.5rem;
# }
# .result-panel-title {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.7rem;
#     font-weight: 500;
#     letter-spacing: 0.2em;
#     text-transform: uppercase;
#     color: #ff8c32;
#     margin-bottom: 1rem;
#     padding-bottom: 0.7rem;
#     border-bottom: 1px solid rgba(255,140,50,0.15);
# }
# .result-content {
#     font-size: 0.92rem;
#     line-height: 1.8;
#     color: #cdc8bf;
#     white-space: pre-wrap;
#     font-family: 'DM Sans', sans-serif;
# }

# /* ── Report & feedback panels ── */
# .report-panel {
#     background: rgba(255,255,255,0.025);
#     border: 1px solid rgba(255,140,50,0.2);
#     border-radius: 16px;
#     padding: 2rem 2.5rem;
#     margin-top: 1rem;
# }
# .feedback-panel {
#     background: rgba(255,255,255,0.025);
#     border: 1px solid rgba(80,200,120,0.2);
#     border-radius: 16px;
#     padding: 2rem 2.5rem;
#     margin-top: 1rem;
# }
# .panel-label {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.7rem;
#     letter-spacing: 0.2em;
#     text-transform: uppercase;
#     margin-bottom: 1.2rem;
#     padding-bottom: 0.7rem;
# }
# .panel-label.orange {
#     color: #ff8c32;
#     border-bottom: 1px solid rgba(255,140,50,0.15);
# }
# .panel-label.green {
#     color: #50c878;
#     border-bottom: 1px solid rgba(80,200,120,0.15);
# }

# /* ── Progress text ── */
# .stSpinner > div { color: #ff8c32 !important; }

# /* ── Expander ── */
# details summary {
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.75rem !important;
#     color: #a09890 !important;
#     letter-spacing: 0.1em !important;
#     cursor: pointer;
# }

# /* ── Section heading ── */
# .section-heading {
#     font-family: 'Syne', sans-serif;
#     font-size: 1.3rem;
#     font-weight: 700;
#     color: #f0ebe0;
#     margin: 2rem 0 1rem;
# }

# /* ── Toast-style notice ── */
# .notice {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.72rem;
#     color: #605850;
#     text-align: center;
#     margin-top: 3rem;
#     letter-spacing: 0.08em;
# }
# </style>
# """, unsafe_allow_html=True)


# # ── Helper: render a step card ────────────────────────────────────────────────
# def step_card(num: str, title: str, state: str, desc: str = ""):
#     status_map = {
#         "waiting": ("WAITING", "status-waiting"),
#         "running": ("● RUNNING", "status-running"),
#         "done":    ("✓ DONE",   "status-done"),
#     }
#     label, cls = status_map.get(state, ("", ""))
#     card_cls = {"running": "active", "done": "done"}.get(state, "")
#     st.markdown(f"""
#     <div class="step-card {card_cls}">
#         <div class="step-header">
#             <span class="step-num">{num}</span>
#             <span class="step-title">{title}</span>
#             <span class="step-status {cls}">{label}</span>
#         </div>
#         {"<div style='font-size:0.82rem;color:#706860;margin-top:0.3rem;'>"+desc+"</div>" if desc else ""}
#     </div>
#     """, unsafe_allow_html=True)


# # ── Session state init ────────────────────────────────────────────────────────
# for key in ("results", "running", "done"):
#     if key not in st.session_state:
#         st.session_state[key] = {} if key == "results" else False


# # ── Hero ──────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero">
#     <div class="hero-eyebrow">Multi-Agent AI System</div>
#     <h1>Research<span>Mind</span></h1>
#     <p class="hero-sub">
#         Four specialized AI agents collaborate — searching, scraping, writing,
#         and critiquing — to deliver a polished research report on any topic.
#     </p>
# </div>
# <div class="divider"></div>
# """, unsafe_allow_html=True)


# # ── Layout: input left, pipeline right ───────────────────────────────────────
# col_input, col_spacer, col_pipeline = st.columns([5, 0.5, 4])

# with col_input:
#     st.markdown('<div class="input-card">', unsafe_allow_html=True)
#     topic = st.text_input(
#         "Research Topic",
#         placeholder="e.g. Quantum computing breakthroughs in 2025",
#         key="topic_input",
#         label_visibility="visible",
#     )
#     run_btn = st.button("⚡  Run Research Pipeline", use_container_width=True)
#     st.markdown('</div>', unsafe_allow_html=True)

#     # Example chips
#     st.markdown("""
#     <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-bottom:1.5rem;">
#         <span style="font-family:'DM Mono',monospace;font-size:0.68rem;color:#605850;letter-spacing:0.1em;">TRY →</span>
#     """, unsafe_allow_html=True)
#     examples = ["LLM agents 2025", "CRISPR gene editing", "Fusion energy progress"]
#     for ex in examples:
#         st.markdown(f"""
#         <span style="
#             background:rgba(255,255,255,0.04);
#             border:1px solid rgba(255,255,255,0.08);
#             border-radius:6px;
#             padding:0.25rem 0.7rem;
#             font-size:0.75rem;
#             color:#a09890;
#             font-family:'DM Sans',sans-serif;
#             cursor:default;
#         ">{ex}</span>
#         """, unsafe_allow_html=True)
#     st.markdown("</div>", unsafe_allow_html=True)

# with col_pipeline:
#     st.markdown('<div class="section-heading">Pipeline</div>', unsafe_allow_html=True)

#     r = st.session_state.results
#     done = st.session_state.done

#     def s(step):
#         if not r:
#             return "waiting"
#         steps = ["search", "reader", "writer", "critic"]
#         idx = steps.index(step)
#         completed = list(r.keys())
#         # figure out which steps are done
#         if step in r:
#             return "done"
#         # which step is running now (first not in r)
#         if st.session_state.running:
#             for i, k in enumerate(steps):
#                 if k not in r:
#                     return "running" if k == step else "waiting"
#         return "waiting"

#     step_card("01", "Search Agent",  s("search"), "Gathers recent web information")
#     step_card("02", "Reader Agent",  s("reader"), "Scrapes & extracts deep content")
#     step_card("03", "Writer Chain",  s("writer"), "Drafts the full research report")
#     step_card("04", "Critic Chain",  s("critic"), "Reviews & scores the report")


# # ── Run pipeline ──────────────────────────────────────────────────────────────
# if run_btn:
#     if not topic.strip():
#         st.warning("Please enter a research topic first.")
#     else:
#         st.session_state.results = {}
#         st.session_state.running = True
#         st.session_state.done = False
#         st.rerun()

# if st.session_state.running and not st.session_state.done:
#     results = {}
#     topic_val = st.session_state.topic_input

#     # ── Step 1: Search ──
#     with st.spinner("🔍  Search Agent is working…"):
#         search_agent = build_search_agent()
#         sr = search_agent.invoke({
#             "messages": [("user", f"Find recent, reliable and detailed information about: {topic_val}")]
#         })
#         results["search"] = sr["messages"][-1].content
#         st.session_state.results = dict(results)
#     st.rerun() if False else None   # keep inline for now

#     # ── Step 2: Reader ──
#     with st.spinner("📄  Reader Agent is scraping top resources…"):
#         reader_agent = build_reader_agent()
#         rr = reader_agent.invoke({
#             "messages": [("user",
#                 f"Based on the following search results about '{topic_val}', "
#                 f"pick the most relevant URL and scrape it for deeper content.\n\n"
#                 f"Search Results:\n{results['search'][:800]}"
#             )]
#         })
#         results["reader"] = rr["messages"][-1].content
#         st.session_state.results = dict(results)

#     # ── Step 3: Writer ──
#     with st.spinner("✍️  Writer is drafting the report…"):
#         research_combined = (
#             f"SEARCH RESULTS:\n{results['search']}\n\n"
#             f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
#         )
#         results["writer"] = writer_chain.invoke({
#             "topic": topic_val,
#             "research": research_combined
#         })
#         st.session_state.results = dict(results)

#     # ── Step 4: Critic ──
#     with st.spinner("🧐  Critic is reviewing the report…"):
#         results["critic"] = critic_chain.invoke({
#             "report": results["writer"]
#         })
#         st.session_state.results = dict(results)

#     st.session_state.running = False
#     st.session_state.done = True
#     st.rerun()


# # ── Results display ───────────────────────────────────────────────────────────
# r = st.session_state.results

# if r:
#     st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
#     st.markdown('<div class="section-heading">Results</div>', unsafe_allow_html=True)

#     # Raw outputs in expanders
#     if "search" in r:
#         with st.expander("🔍 Search Results (raw)", expanded=False):
#             st.markdown(f'<div class="result-panel"><div class="result-panel-title">Search Agent Output</div>'
#                         f'<div class="result-content">{r["search"]}</div></div>', unsafe_allow_html=True)

#     if "reader" in r:
#         with st.expander("📄 Scraped Content (raw)", expanded=False):
#             st.markdown(f'<div class="result-panel"><div class="result-panel-title">Reader Agent Output</div>'
#                         f'<div class="result-content">{r["reader"]}</div></div>', unsafe_allow_html=True)

#     # Final report
#     if "writer" in r:
#         st.markdown("""
#         <div class="report-panel">
#             <div class="panel-label orange">📝 Final Research Report</div>
#         """, unsafe_allow_html=True)
#         st.markdown(r["writer"])   # render markdown natively
#         st.markdown("</div>", unsafe_allow_html=True)

#         # Download
#         st.download_button(
#             label="⬇  Download Report (.md)",
#             data=r["writer"],
#             file_name=f"research_report_{int(time.time())}.md",
#             mime="text/markdown",
#         )

#     # Critic feedback
#     if "critic" in r:
#         st.markdown("""
#         <div class="feedback-panel">
#             <div class="panel-label green">🧐 Critic Feedback</div>
#         """, unsafe_allow_html=True)
#         st.markdown(r["critic"])
#         st.markdown("</div>", unsafe_allow_html=True)


# # ── Footer ────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="notice">
#     ResearchMind · Powered by LangChain multi-agent pipeline · Built with Streamlit
# </div>
# """, unsafe_allow_html=True)

import os
import streamlit as st

# ── Page config (must be the very first Streamlit call) ──────────────────────
st.set_page_config(
    page_title="ResearchPeer",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ---------- base / reset ---------- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0f0f13;
        color: #e8e8f0;
    }

    .stApp {
        background-color: #0f0f13;
    }

    /* ---------- hide default Streamlit chrome ---------- */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1100px; }

    /* ---------- landing / hero ---------- */
    .hero-wrap {
        text-align: center;
        padding: 3.5rem 1rem 2.5rem;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255,100,20,0.12);
        border: 1px solid rgba(255,100,20,0.35);
        color: #ff7a30;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        padding: 0.3rem 0.9rem;
        border-radius: 100px;
        margin-bottom: 1.2rem;
    }
    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2.4rem, 5vw, 3.6rem);
        font-weight: 700;
        letter-spacing: -0.02em;
        line-height: 1.1;
        margin: 0 0 0.6rem;
        background: linear-gradient(135deg, #ffffff 40%, #ff7a30 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .hero-sub {
        color: #9090a8;
        font-size: 1.1rem;
        font-weight: 400;
        margin: 0 auto 2.4rem;
        max-width: 520px;
        line-height: 1.6;
    }

    /* ---------- agent selector cards ---------- */
    .agent-grid {
        display: flex;
        gap: 1.1rem;
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 2.8rem;
    }
    .agent-card {
        background: #1a1a24;
        border: 1.5px solid #2a2a38;
        border-radius: 14px;
        padding: 1.3rem 1.8rem;
        cursor: pointer;
        transition: border-color 0.2s, background 0.2s, transform 0.15s;
        min-width: 220px;
        text-align: center;
    }
    .agent-card:hover {
        border-color: #ff7a30;
        background: #1f1f2e;
        transform: translateY(-2px);
    }
    .agent-card.active {
        border-color: #ff7a30;
        background: rgba(255,122,48,0.08);
        box-shadow: 0 0 0 1px rgba(255,122,48,0.25);
    }
    .agent-icon { font-size: 1.8rem; margin-bottom: 0.4rem; }
    .agent-label {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        color: #e8e8f0;
    }
    .agent-desc { font-size: 0.78rem; color: #70708a; margin-top: 0.25rem; }

    /* ---------- divider ---------- */
    .section-divider {
        border: none;
        border-top: 1px solid #2a2a38;
        margin: 0.2rem 0 2rem;
    }

    /* ---------- cards / panels ---------- */
    .panel {
        background: #1a1a24;
        border: 1px solid #2a2a38;
        border-radius: 14px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1.2rem;
    }
    .panel-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #ff7a30;
        margin-bottom: 0.7rem;
    }
    .panel-body {
        font-size: 0.92rem;
        line-height: 1.75;
        color: #c8c8dc;
        white-space: pre-wrap;
        word-break: break-word;
    }

    /* ---------- progress pipeline ---------- */
    .pipeline-wrap {
        display: flex;
        align-items: center;
        gap: 0;
        margin: 1.6rem 0 1.2rem;
        overflow-x: auto;
        padding-bottom: 0.3rem;
    }
    .pipe-step {
        display: flex;
        flex-direction: column;
        align-items: center;
        min-width: 120px;
    }
    .pipe-dot {
        width: 36px; height: 36px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 1rem;
        font-weight: 700;
        transition: background 0.3s, border-color 0.3s;
    }
    .pipe-dot.pending   { background:#1e1e2c; border:2px solid #3a3a50; color:#4a4a66; }
    .pipe-dot.active    { background:rgba(255,122,48,0.15); border:2px solid #ff7a30; color:#ff7a30; }
    .pipe-dot.done      { background:rgba(72,210,130,0.15); border:2px solid #48d282; color:#48d282; }
    .pipe-label { font-size: 0.68rem; color:#70708a; margin-top:0.35rem; text-align:center; white-space:nowrap; }
    .pipe-line  { flex:1; height:2px; background:#2a2a38; min-width:30px; }
    .pipe-line.done { background: linear-gradient(90deg,#48d282,#ff7a30); }

    /* ---------- success banner ---------- */
    .success-banner {
        background: rgba(72,210,130,0.1);
        border: 1px solid rgba(72,210,130,0.3);
        border-radius: 10px;
        padding: 0.8rem 1.2rem;
        color: #48d282;
        font-size: 0.88rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }

    /* ---------- error banner ---------- */
    .error-banner {
        background: rgba(255,80,80,0.1);
        border: 1px solid rgba(255,80,80,0.3);
        border-radius: 10px;
        padding: 0.8rem 1.2rem;
        color: #ff6060;
        font-size: 0.88rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }

    /* ---------- Streamlit widget overrides ---------- */
    div[data-testid="stTextInput"] > div > div > input,
    div[data-testid="stTextArea"] textarea {
        background: #1a1a24 !important;
        border: 1.5px solid #2a2a38 !important;
        border-radius: 10px !important;
        color: #e8e8f0 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 0.65rem 1rem !important;
        transition: border-color 0.2s !important;
    }
    div[data-testid="stTextInput"] > div > div > input:focus,
    div[data-testid="stTextArea"] textarea:focus {
        border-color: #ff7a30 !important;
        box-shadow: 0 0 0 3px rgba(255,122,48,0.12) !important;
        outline: none !important;
    }

    div[data-testid="stFileUploader"] {
        background: #1a1a24;
        border: 1.5px dashed #3a3a50;
        border-radius: 14px;
        padding: 1rem;
        transition: border-color 0.2s;
    }
    div[data-testid="stFileUploader"]:hover { border-color: #ff7a30; }

    /* primary buttons */
    .stButton > button {
        background: linear-gradient(135deg, #ff7a30 0%, #e85d10 100%) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 10px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.4rem !important;
        letter-spacing: 0.02em !important;
        transition: opacity 0.2s, transform 0.15s !important;
        box-shadow: 0 4px 16px rgba(255,122,48,0.3) !important;
    }
    .stButton > button:hover { opacity: 0.88 !important; transform: translateY(-1px) !important; }
    .stButton > button:active { transform: translateY(0) !important; }

    /* secondary (download) button – override via a class we wrap it with */
    .download-wrap .stDownloadButton > button {
        background: #1a1a24 !important;
        border: 1.5px solid #3a3a50 !important;
        color: #c8c8dc !important;
        box-shadow: none !important;
    }
    .download-wrap .stDownloadButton > button:hover {
        border-color: #ff7a30 !important;
        color: #ff7a30 !important;
    }

    /* expander */
    .streamlit-expanderHeader {
        background: #1a1a24 !important;
        border: 1px solid #2a2a38 !important;
        border-radius: 10px !important;
        color: #c8c8dc !important;
    }

    /* spinner accent */
    .stSpinner > div > div { border-top-color: #ff7a30 !important; }

    /* label color */
    label, .stLabel { color: #9090a8 !important; font-size: 0.82rem !important; font-weight: 500 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Session-state defaults ────────────────────────────────────────────────────
def _init_state():
    defaults = {
        "active_agent": "research",   # "research" | "rag"
        "pipeline_stage": 0,           # 0=idle, 1-4=stages, 5=done
        "search_results": "",
        "scraped_content": "",
        "report": "",
        "feedback": "",
        "pdf_indexed": False,
        "rag_answer": "",
        "pipeline_error": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init_state()

# ── Hero / Landing header ─────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero-wrap">
        <div class="hero-badge">Multi-Agent AI System</div>
        <div class="hero-title">ResearchPeer</div>
        <div class="hero-sub">Multi-Agent AI Research Assistant — search the web or interrogate your documents with specialized AI agents.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Agent selector ────────────────────────────────────────────────────────────
col_left, col_r1, col_r2, col_right = st.columns([1, 2, 2, 1])

with col_r1:
    research_active = "active" if st.session_state.active_agent == "research" else ""
    if st.button("🌐  Research Agent", use_container_width=True, key="btn_research"):
        st.session_state.active_agent = "research"
        st.rerun()
    st.markdown(
        f'<div style="text-align:center;font-size:0.72rem;color:#70708a;margin-top:-0.5rem">Web search · Scrape · Report · Critic</div>',
        unsafe_allow_html=True,
    )

with col_r2:
    if st.button("📄  Document Intelligence", use_container_width=True, key="btn_rag"):
        st.session_state.active_agent = "rag"
        st.rerun()
    st.markdown(
        '<div style="text-align:center;font-size:0.72rem;color:#70708a;margin-top:-0.5rem">Upload PDF · Embed · Ask questions</div>',
        unsafe_allow_html=True,
    )

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  RESEARCH AGENT PAGE
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.active_agent == "research":

    # ── Pipeline progress renderer ────────────────────────────────────────────
    def render_pipeline(stage: int):
        """stage: 0=idle, 1=search running, 2=reader, 3=writer, 4=critic, 5=done"""
        steps = [
            ("🔍", "Search Agent"),
            ("📰", "Reader Agent"),
            ("✍️", "Writer Chain"),
            ("🎯", "Critic Chain"),
        ]
        html = '<div class="pipeline-wrap">'
        for i, (icon, label) in enumerate(steps):
            step_num = i + 1
            if stage > step_num:
                dot_cls = "done"
                dot_icon = "✓"
            elif stage == step_num:
                dot_cls = "active"
                dot_icon = icon
            else:
                dot_cls = "pending"
                dot_icon = icon

            html += f'<div class="pipe-step"><div class="pipe-dot {dot_cls}">{dot_icon}</div><div class="pipe-label">{label}</div></div>'
            if i < len(steps) - 1:
                line_cls = "done" if stage > step_num else ""
                html += f'<div class="pipe-line {line_cls}"></div>'

        html += "</div>"
        return html

    # ── Input area ────────────────────────────────────────────────────────────
    topic_col, btn_col = st.columns([4, 1])
    with topic_col:
        topic = st.text_input(
            "Research Topic",
            placeholder="e.g.  Quantum computing breakthroughs in 2025",
            label_visibility="collapsed",
        )
    with btn_col:
        run_clicked = st.button("Run Pipeline", use_container_width=True, key="run_pipeline")

    # ── Pipeline execution ────────────────────────────────────────────────────
    if run_clicked:
        if not topic.strip():
            st.markdown('<div class="error-banner">⚠️  Please enter a research topic before running the pipeline.</div>', unsafe_allow_html=True)
        else:
            # Reset state for a fresh run
            st.session_state.pipeline_stage = 0
            st.session_state.search_results = ""
            st.session_state.scraped_content = ""
            st.session_state.report = ""
            st.session_state.feedback = ""
            st.session_state.pipeline_error = ""

            try:
                # ── Import backend (deferred to avoid import errors on UI-only runs) ──
                from pipeline import run_research_pipeline
                from agents import (
                    build_search_agent,
                    build_reader_agent,
                    writer_chain,
                    critic_chain,
                )

                progress_placeholder = st.empty()
                status_placeholder = st.empty()

                # ── Stage 1: Search Agent ─────────────────────────────────────
                st.session_state.pipeline_stage = 1
                progress_placeholder.markdown(render_pipeline(1), unsafe_allow_html=True)
                with status_placeholder:
                    with st.spinner("🔍  Search Agent is scouring the web…"):
                        search_agent = build_search_agent()
                        search_result = search_agent.invoke({
                            "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
                        })
                        st.session_state.search_results = search_result["messages"][-1].content

                # ── Stage 2: Reader Agent ─────────────────────────────────────
                st.session_state.pipeline_stage = 2
                progress_placeholder.markdown(render_pipeline(2), unsafe_allow_html=True)
                with status_placeholder:
                    with st.spinner("📰  Reader Agent is scraping top resources…"):
                        reader_agent = build_reader_agent()
                        reader_result = reader_agent.invoke({
                            "messages": [("user",
                                f"Based on the following search results about '{topic}', "
                                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                                f"Search Results:\n{st.session_state.search_results[:800]}"
                            )]
                        })
                        st.session_state.scraped_content = reader_result["messages"][-1].content

                # ── Stage 3: Writer Chain ─────────────────────────────────────
                st.session_state.pipeline_stage = 3
                progress_placeholder.markdown(render_pipeline(3), unsafe_allow_html=True)
                with status_placeholder:
                    with st.spinner("✍️  Writer is drafting the research report…"):
                        research_combined = (
                            f"SEARCH RESULTS:\n{st.session_state.search_results}\n\n"
                            f"DETAILED SCRAPED CONTENT:\n{st.session_state.scraped_content}"
                        )
                        st.session_state.report = writer_chain.invoke({
                            "topic": topic,
                            "research": research_combined,
                        })

                # ── Stage 4: Critic Chain ─────────────────────────────────────
                st.session_state.pipeline_stage = 4
                progress_placeholder.markdown(render_pipeline(4), unsafe_allow_html=True)
                with status_placeholder:
                    with st.spinner("🎯  Critic is reviewing the report…"):
                        st.session_state.feedback = critic_chain.invoke({
                            "report": st.session_state.report
                        })

                # ── Done ──────────────────────────────────────────────────────
                st.session_state.pipeline_stage = 5
                progress_placeholder.markdown(render_pipeline(5), unsafe_allow_html=True)
                status_placeholder.empty()

            except Exception as e:
                st.session_state.pipeline_error = str(e)
                st.session_state.pipeline_stage = 0

    # ── Persistent pipeline progress display (after rerun) ───────────────────
    if st.session_state.pipeline_stage > 0:
        st.markdown(render_pipeline(st.session_state.pipeline_stage), unsafe_allow_html=True)

    # ── Error display ─────────────────────────────────────────────────────────
    if st.session_state.pipeline_error:
        st.markdown(
            f'<div class="error-banner">⚠️  Pipeline error: {st.session_state.pipeline_error}</div>',
            unsafe_allow_html=True,
        )

    # ── Results ───────────────────────────────────────────────────────────────
    if st.session_state.pipeline_stage == 5:
        st.markdown('<div class="success-banner">✅  Pipeline complete — all four stages finished successfully.</div>', unsafe_allow_html=True)

        # Search & Scraped outputs in two columns
        col_a, col_b = st.columns(2)
        with col_a:
            with st.expander("🔍  Search Agent Output", expanded=False):
                st.markdown(
                    f'<div class="panel-body">{st.session_state.search_results}</div>',
                    unsafe_allow_html=True,
                )
        with col_b:
            with st.expander("📰  Reader Agent Output", expanded=False):
                st.markdown(
                    f'<div class="panel-body">{st.session_state.scraped_content}</div>',
                    unsafe_allow_html=True,
                )

        # Final Report
        st.markdown('<div class="panel"><div class="panel-title">📋 Final Research Report</div>', unsafe_allow_html=True)
        st.markdown(st.session_state.report)
        st.markdown("</div>", unsafe_allow_html=True)

        # Critic Feedback
        st.markdown('<div class="panel"><div class="panel-title">🎯 Critic Feedback</div>', unsafe_allow_html=True)
        st.markdown(st.session_state.feedback)
        st.markdown("</div>", unsafe_allow_html=True)

        # Download report button
        st.markdown('<div class="download-wrap">', unsafe_allow_html=True)
        st.download_button(
            label="⬇️  Download Report (.txt)",
            data=st.session_state.report,
            file_name=f"research_report_{topic[:30].replace(' ', '_')}.txt",
            mime="text/plain",
        )
        st.markdown("</div>", unsafe_allow_html=True)

    elif st.session_state.pipeline_stage == 0 and not st.session_state.pipeline_error:
        # Idle placeholder
        st.markdown(
            """
            <div style="text-align:center;padding:3rem 1rem;color:#3a3a58;">
                <div style="font-size:2.8rem;margin-bottom:0.8rem">🌐</div>
                <div style="font-family:'Space Grotesk',sans-serif;font-size:1.1rem;font-weight:600;color:#4a4a6a">
                    Ready to research
                </div>
                <div style="font-size:0.85rem;margin-top:0.4rem">
                    Enter a topic above and hit <strong style="color:#ff7a30">Run Pipeline</strong> to start.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ─────────────────────────────────────────────────────────────────────────────
#  DOCUMENT INTELLIGENCE (RAG) PAGE
# ─────────────────────────────────────────────────────────────────────────────
else:
    left_col, right_col = st.columns([1, 1], gap="large")

    # ── Left: Upload & Index ──────────────────────────────────────────────────
    with left_col:
        st.markdown(
            '<div style="font-family:\'Space Grotesk\',sans-serif;font-size:1rem;font-weight:600;color:#e8e8f0;margin-bottom:1rem;">📤  Upload Document</div>',
            unsafe_allow_html=True,
        )

        uploaded_file = st.file_uploader(
            "Drop a PDF here",
            type=["pdf"],
            label_visibility="collapsed",
        )

        if uploaded_file is not None:
            st.markdown(
                f'<div style="font-size:0.8rem;color:#9090a8;margin:0.5rem 0 0.8rem;">📎  {uploaded_file.name} — {uploaded_file.size / 1024:.1f} KB</div>',
                unsafe_allow_html=True,
            )

        index_btn = st.button("Create Vector Database", use_container_width=True, key="create_vdb")

        if index_btn:
            if uploaded_file is None:
                st.markdown('<div class="error-banner">⚠️  Please upload a PDF first.</div>', unsafe_allow_html=True)
            else:
                # Save the uploaded file to the uploads/ directory so the backend can read it
                # os.makedirs("uploads", exist_ok=True)
                # save_path = os.path.join("uploads", uploaded_file.name)
                # with open(save_path, "wb") as f:
                #     f.write(uploaded_file.getbuffer())

                # with st.spinner("⚙️  Building vector database — chunking & embedding…"):
                #     try:
                #         from rag_pipeline import process_pdf
                #         success = process_pdf(save_path)

                with st.spinner("⚙️  Building vector database — chunking & embedding…"):
                    try:
                        from rag_pipeline import process_pdf
                        success = process_pdf(uploaded_file)
                        if success:
                            st.session_state.pdf_indexed = True
                            st.session_state.rag_answer = ""
                        else:
                            st.markdown('<div class="error-banner">⚠️  Failed to create vector database. Check the uploaded file.</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.markdown(f'<div class="error-banner">⚠️  Error: {e}</div>', unsafe_allow_html=True)

        if st.session_state.pdf_indexed:
            st.markdown(
                '<div class="success-banner">✅  Vector database created successfully. Ready to answer questions.</div>',
                unsafe_allow_html=True,
            )

        # Tip card
        st.markdown(
            """
            <div class="panel" style="margin-top:1.6rem">
                <div class="panel-title">How it works</div>
                <div class="panel-body" style="font-size:0.82rem">
                    1. Upload a PDF document<br>
                    2. Click <strong style="color:#ff7a30">Create Vector Database</strong> to embed it into ChromaDB<br>
                    3. Type any question about the document on the right<br>
                    4. The RAG agent retrieves relevant chunks and generates an answer
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Right: Q&A ───────────────────────────────────────────────────────────
    with right_col:
        st.markdown(
            '<div style="font-family:\'Space Grotesk\',sans-serif;font-size:1rem;font-weight:600;color:#e8e8f0;margin-bottom:1rem;">💬  Ask a Question</div>',
            unsafe_allow_html=True,
        )

        question = st.text_area(
            "Your question",
            placeholder="What are the main conclusions of this document?",
            height=110,
            label_visibility="collapsed",
        )

        ask_btn = st.button("Ask", use_container_width=True, key="ask_rag")

        if ask_btn:
            if not question.strip():
                st.markdown('<div class="error-banner">⚠️  Please enter a question.</div>', unsafe_allow_html=True)
            elif not st.session_state.pdf_indexed:
                st.markdown('<div class="error-banner">⚠️  Please upload a PDF and create the vector database first.</div>', unsafe_allow_html=True)
            else:
                with st.spinner("🧠  Retrieving context and generating answer…"):
                    try:
                        from rag_pipeline import answer_question
                        answer = answer_question(question)
                        st.session_state.rag_answer = answer
                    except Exception as e:
                        st.session_state.rag_answer = f"Error: {e}"

        if st.session_state.rag_answer:
            st.markdown(
                f"""
                <div class="panel" style="margin-top:1.2rem">
                    <div class="panel-title">Answer</div>
                    <div class="panel-body">{st.session_state.rag_answer}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif not ask_btn:
            st.markdown(
                """
                <div style="text-align:center;padding:2.5rem 1rem;color:#3a3a58;margin-top:1rem">
                    <div style="font-size:2.2rem;margin-bottom:0.6rem">📄</div>
                    <div style="font-family:'Space Grotesk',sans-serif;font-size:0.95rem;font-weight:600;color:#4a4a6a">
                        No answer yet
                    </div>
                    <div style="font-size:0.8rem;margin-top:0.35rem">
                        Index a document, then ask a question.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div style="text-align:center;padding:2.5rem 0 1rem;color:#2e2e46;font-size:0.75rem;letter-spacing:0.05em;">
        RESEARCHPEER &nbsp;·&nbsp; Multi-Agent AI &nbsp;·&nbsp; Powered by Mistral + LangChain
    </div>
    """,
    unsafe_allow_html=True,
)