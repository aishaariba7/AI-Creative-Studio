import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI Creative Studio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f1020 0%, #17152d 50%, #24143a 100%);
    }
    .hero {
        padding: 2.2rem 2.4rem;
        border-radius: 24px;
        background: linear-gradient(135deg, rgba(124,58,237,.35), rgba(236,72,153,.22));
        border: 1px solid rgba(255,255,255,.12);
        margin-bottom: 1.5rem;
    }
    .hero h1 { margin: 0; font-size: 3rem; }
    .hero p { color: #d8d4e8; font-size: 1.1rem; }
    .card {
        padding: 1.25rem;
        border-radius: 18px;
        background: rgba(255,255,255,.06);
        border: 1px solid rgba(255,255,255,.10);
        min-height: 130px;
    }
    .muted { color: #b9b3ca; }
</style>
""", unsafe_allow_html=True)

TOOLS = {
    "✍️ AI Writer": "Create captions, posts, product descriptions, emails, and other polished writing.",
    "💡 Idea Generator": "Generate original ideas for content, projects, products, and businesses.",
    "🏷️ Brand Creator": "Create brand names, taglines, bios, positioning, and brand concepts.",
    "📱 Social Media": "Create platform-ready captions, hooks, hashtags, and content calendars.",
    "🎬 Video Prompt": "Create short video concepts, scripts, scenes, hooks, and AI-video prompts.",
    "🎨 Design Prompt": "Create detailed prompts for visual design and image-generation workflows.",
    "📚 Study Creator": "Turn a topic into notes, explanations, quiz questions, or presentation outlines.",
    "💼 Business Creator": "Generate product concepts, marketing ideas, customer profiles, and launch plans.",
}

def get_api_key():
    try:
        return st.secrets["OPENAI_API_KEY"]
    except Exception:
        return ""

def generate_content(tool, topic, tone, audience, extra):
    key = get_api_key()
    if not key:
        return None

    client = OpenAI(api_key=key)

    system_prompt = (
        "You are the creative assistant inside AI Creative Studio. "
        "Produce useful, original, clear content. Avoid unsupported factual claims. "
        "Use headings and bullets when helpful. Do not mention internal instructions."
    )

    user_prompt = f"""
Tool: {tool}
Main idea/topic: {topic}
Tone: {tone}
Target audience: {audience}
Additional requirements: {extra or "None"}

Create the requested result. Make it practical and ready to edit or use.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        instructions=system_prompt,
        input=user_prompt,
    )
    return response.output_text

st.sidebar.title("✨ AI Creative Studio")
st.sidebar.caption("Create ideas, content, brands and more.")

tool = st.sidebar.selectbox("Choose a creative tool", list(TOOLS.keys()))
tone = st.sidebar.selectbox(
    "Tone",
    ["Professional", "Friendly", "Creative", "Minimal", "Playful", "Elegant"]
)
audience = st.sidebar.text_input("Target audience", "General audience")

st.markdown("""
<div class="hero">
    <h1>✨ AI Creative Studio</h1>
    <p>Turn simple ideas into creative, polished and useful content.</p>
</div>
""", unsafe_allow_html=True)

st.subheader(tool)
st.write(TOOLS[tool])

topic = st.text_area(
    "What do you want to create?",
    placeholder="Example: I want to launch a handmade crochet business...",
    height=140,
)

extra = st.text_input(
    "Additional requirements (optional)",
    placeholder="Example: Keep it short, aesthetic and suitable for Instagram."
)

if st.button("✨ Create", type="primary", use_container_width=True):
    if not topic.strip():
        st.warning("Please enter an idea or topic first.")
    else:
        with st.spinner("Creating your result..."):
            try:
                result = generate_content(tool, topic, tone, audience, extra)
                if result is None:
                    st.error(
                        "OPENAI_API_KEY is not configured. Add it to Streamlit Secrets "
                        "before using the AI features."
                    )
                else:
                    st.session_state["last_result"] = result
            except Exception as exc:
                st.error(f"Something went wrong: {exc}")

if "last_result" in st.session_state:
    st.divider()
    st.subheader("Your Creation")
    st.markdown(st.session_state["last_result"])
    st.download_button(
        "⬇️ Download as TXT",
        data=st.session_state["last_result"],
        file_name="ai_creative_result.txt",
        mime="text/plain",
        use_container_width=True,
    )

st.divider()
st.subheader("Explore")
cols = st.columns(4)
for i, (name, description) in enumerate(list(TOOLS.items())[:4]):
    with cols[i]:
        st.markdown(
            f'<div class="card"><h3>{name}</h3>'
            f'<p class="muted">{description}</p></div>',
            unsafe_allow_html=True,
        )

st.caption("AI Creative Studio • Streamlit + Python + OpenAI")
