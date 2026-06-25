# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import streamlit.components.v1 as components

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="For Priyaaa ❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Global CSS — Mobile-First Romantic Design
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400&display=swap');

/* ── Reset & base ── */
html, body, [data-testid="stAppViewContainer"] {
    background: #10000a !important;
    color: #ffe0ec !important;
    font-family: 'Lato', sans-serif;
}
[data-testid="stMain"] {
    background: #10000a !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"] {
    display: none !important;
}

/* ── Hero title ── */
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 8vw, 3.5rem);
    color: #ff4d88;
    text-align: center;
    letter-spacing: 0.02em;
    line-height: 1.2;
    margin: 0.5rem 0 0.25rem;
    text-shadow: 0 0 40px rgba(255, 77, 136, 0.4);
}
.hero-subtitle {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: clamp(0.85rem, 3.5vw, 1.1rem);
    color: #c97fa0;
    text-align: center;
    margin-bottom: 1.5rem;
    letter-spacing: 0.08em;
}

/* ── Divider ── */
.rose-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #ff4d88 40%, #ff4d88 60%, transparent);
    margin: 1.2rem auto;
    max-width: 320px;
}

/* ── Input box ── */
[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid #6b2040 !important;
    border-radius: 12px !important;
    color: #ffe0ec !important;
    font-family: 'Lato', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.7rem 1rem !important;
    text-align: center;
    letter-spacing: 0.05em;
    transition: border-color 0.3s;
}
[data-testid="stTextInput"] input:focus {
    border-color: #ff4d88 !important;
    box-shadow: 0 0 0 2px rgba(255,77,136,0.2) !important;
    outline: none !important;
}
[data-testid="stTextInput"] label {
    color: #c97fa0 !important;
    font-family: 'Lato', sans-serif !important;
    text-align: center;
    display: block;
    font-size: 0.95rem !important;
    letter-spacing: 0.04em;
}

/* ── Alerts ── */
[data-testid="stAlert"] {
    border-radius: 12px !important;
    font-family: 'Lato', sans-serif !important;
}

/* ── Section headings ── */
.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.1rem, 5vw, 1.6rem);
    color: #ff4d88;
    text-align: center;
    margin: 1.5rem 0 0.8rem;
    letter-spacing: 0.02em;
}

/* ── Heart animation card ──
   scrolling=True so the matplotlib toolbar (play/pause/etc) is reachable ── */
.anim-card {
    background: rgba(255,77,136,0.05);
    border: 1px solid rgba(255,77,136,0.2);
    border-radius: 18px;
    padding: 0.5rem;
    margin: 0 auto;
    max-width: 100%;
    overflow: hidden;
}

/* ── Video wrapper — forces 16:9 responsive ── */
.video-wrapper {
    position: relative;
    padding-bottom: 56.25%;
    height: 0;
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid rgba(255,77,136,0.2);
    background: #000;
}
.video-wrapper iframe {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    border: none;
}

/* ── Poem card ── */
.poem-card {
    background: linear-gradient(135deg, rgba(100,0,40,0.35), rgba(30,0,15,0.6));
    border: 1px solid rgba(255,77,136,0.25);
    border-radius: 20px;
    padding: 2rem 1.5rem;
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: clamp(1rem, 4vw, 1.2rem);
    color: #ffe0ec;
    line-height: 2;
    box-shadow: 0 0 40px rgba(255,77,136,0.1), inset 0 0 30px rgba(255,77,136,0.04);
    margin: 0.5rem 0 1.5rem;
}
.poem-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.2rem, 5vw, 1.8rem);
    color: #ff4d88;
    text-align: center;
    margin-bottom: 1rem;
    letter-spacing: 0.03em;
}

/* ── Footer ── */
.footer-love {
    text-align: center;
    color: #6b2040;
    font-size: 0.8rem;
    letter-spacing: 0.08em;
    padding: 2rem 0 1rem;
    font-family: 'Lato', sans-serif;
}

/* ── Petal particles background ── */
.petals-canvas {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

/* ── Burst canvas — sits on top of everything for 2 s ── */
#burst-canvas {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 9999;
}

/* ── Content above background particles ── */
[data-testid="stVerticalBlock"] {
    position: relative;
    z-index: 1;
}

/* ── Mobile padding ── */
[data-testid="stMainBlockContainer"] {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    padding-top: 1rem !important;
    max-width: 480px !important;
    margin: 0 auto !important;
}

/* ── Spinner ── */
[data-testid="stSpinner"] { color: #ff4d88 !important; }
</style>

<!-- ═══ Background petal rain ═══ -->
<canvas id="petals" class="petals-canvas"></canvas>

<!-- ═══ Burst canvas (roses & hearts) ═══ -->
<canvas id="burst-canvas"></canvas>

<script>
/* ─── Background petals ─── */
(function(){
    const canvas = document.getElementById('petals');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let W, H, petals = [];
    function resize(){ W = canvas.width = window.innerWidth; H = canvas.height = window.innerHeight; }
    resize();
    window.addEventListener('resize', resize);
    function Petal(){
        this.x = Math.random()*W;
        this.y = Math.random()*H - H;
        this.size = 4 + Math.random()*6;
        this.speed = 0.6 + Math.random()*1.2;
        this.drift = (Math.random()-0.5)*0.6;
        this.angle = Math.random()*Math.PI*2;
        this.spin = (Math.random()-0.5)*0.04;
        this.alpha = 0.3 + Math.random()*0.4;
        this.hue = 340 + Math.random()*20;
    }
    for(let i=0;i<35;i++){ const p=new Petal(); p.y=Math.random()*H; petals.push(p); }
    function draw(){
        ctx.clearRect(0,0,W,H);
        petals.forEach(p=>{
            ctx.save();
            ctx.translate(p.x,p.y);
            ctx.rotate(p.angle);
            ctx.globalAlpha=p.alpha;
            ctx.beginPath();
            ctx.ellipse(0,0,p.size,p.size*0.55,0,0,Math.PI*2);
            ctx.fillStyle=`hsl(${p.hue},80%,68%)`;
            ctx.fill();
            ctx.restore();
            p.y+=p.speed; p.x+=p.drift; p.angle+=p.spin;
            if(p.y>H+20){ p.y=-20; p.x=Math.random()*W; }
        });
        requestAnimationFrame(draw);
    }
    draw();
})();

/* ─── Burst: roses 🌹 & hearts ❤️ fired from screen centre ─── */
(function(){
    const bc = document.getElementById('burst-canvas');
    if (!bc) return;
    const ctx = bc.getContext('2d');
    let W, H;
    function resize(){ W = bc.width = window.innerWidth; H = bc.height = window.innerHeight; }
    resize();
    window.addEventListener('resize', resize);

    const EMOJIS = ['❤️','🌹','💕','🌸','💖','🌹','❤️','💗','🌹','💝'];
    let particles = [];
    let running = false;
    let startTime = null;
    const DURATION = 2800; // ms total burst

    function Particle(){
        // launch from a spread along the bottom-centre (like fireworks)
        this.x = W/2 + (Math.random()-0.5)*W*0.3;
        this.y = H + 20;
        const angle = -(Math.PI * (0.25 + Math.random()*0.5)); // upward arc
        const speed = 6 + Math.random()*10;
        this.vx = Math.cos(angle)*speed + (Math.random()-0.5)*4;
        this.vy = Math.sin(angle)*speed;
        this.gravity = 0.18 + Math.random()*0.12;
        this.emoji = EMOJIS[Math.floor(Math.random()*EMOJIS.length)];
        this.size = 22 + Math.floor(Math.random()*22);
        this.alpha = 1;
        this.rotation = (Math.random()-0.5)*0.4;
        this.spin = (Math.random()-0.5)*0.06;
        this.born = performance.now();
        this.life = 1200 + Math.random()*1000; // each particle lives 1.2-2.2 s
    }

    function spawnBatch(){
        for(let i=0;i<18;i++) particles.push(new Particle());
    }

    function draw(ts){
        if(!running) return;
        const elapsed = ts - startTime;

        ctx.clearRect(0,0,W,H);

        // spawn a second wave at ~600 ms
        if(elapsed > 600 && elapsed < 640 && particles.length < 36){
            spawnBatch();
        }

        particles = particles.filter(p => {
            const age = ts - p.born;
            return age < p.life;
        });

        particles.forEach(p => {
            const age = ts - p.born;
            const progress = age / p.life;
            p.vx += 0;
            p.vy += p.gravity;
            p.x += p.vx;
            p.y += p.vy;
            p.rotation += p.spin;

            // fade out last 40%
            const alpha = progress > 0.6 ? 1 - (progress - 0.6)/0.4 : 1;

            ctx.save();
            ctx.globalAlpha = alpha;
            ctx.translate(p.x, p.y);
            ctx.rotate(p.rotation);
            ctx.font = `${p.size}px serif`;
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(p.emoji, 0, 0);
            ctx.restore();
        });

        if(elapsed < DURATION){
            requestAnimationFrame(draw);
        } else {
            ctx.clearRect(0,0,W,H);
            running = false;
        }
    }

    // expose so Streamlit can trigger it
    window.triggerBurst = function(){
        if(running) return;
        running = true;
        particles = [];
        startTime = performance.now();
        spawnBatch();
        requestAnimationFrame(draw);
    };

    // auto-fire if the unlock has already happened (page re-render)
    // we detect it by checking for the success alert in the DOM
    function maybeAutoFire(){
        const alerts = document.querySelectorAll('[data-testid="stAlert"]');
        for(const a of alerts){
            if(a.innerText && a.innerText.includes('Love You')){
                window.triggerBurst();
                return;
            }
        }
    }
    // slight delay to let Streamlit paint the DOM
    setTimeout(maybeAutoFire, 400);
})();
</script>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Header
# -----------------------------
st.markdown('<div class="hero-title">❤️ A Special Surprise</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">— just for you —</div>', unsafe_allow_html=True)
st.markdown('<hr class="rose-divider">', unsafe_allow_html=True)

# -----------------------------
# Name Input
# -----------------------------
name = st.text_input("✨ Enter your name to unlock:", placeholder="Type your name…")

allowed_names = [
    "priya", "priya jha",
    "smriti", "smriti jha"
]

# -----------------------------
# Heart animation — dark-themed, controls preserved
# -----------------------------
@st.cache_resource
def generate_heart_html():
    def heart_equation(x, k=150):
        return np.abs(x)**(2/3) + 0.9 * np.sin(k * x) * np.sqrt(3 - x**2)

    x = np.linspace(-np.sqrt(3), np.sqrt(3), 8000)
    y = heart_equation(x)

    fig, ax = plt.subplots(figsize=(5, 3.6), facecolor='#10000a')
    ax.set_facecolor('#10000a')
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(y.min() - 0.3, y.max() + 0.3)
    ax.set_title("Be By My Side Until…", color='#c97fa0', fontsize=10, pad=8)
    ax.tick_params(colors='#6b2040')
    for spine in ax.spines.values():
        spine.set_edgecolor('#3a0020')
    ax.grid(True, alpha=0.15, color='#6b2040')

    line, = ax.plot([], [], color="#ff4d88", linewidth=2)
    frames = 500

    def update(frame):
        i = max(1, int((frame / (frames - 1)) * len(x)))
        line.set_data(x[:i], y[:i])
        return line,

    anim = animation.FuncAnimation(fig, update, frames=frames, interval=15, blit=True)
    # embed_frames=True keeps the full interactive toolbar (play/pause/slider)
    html = anim.to_jshtml(embed_frames=True, default_mode='once')
    plt.close()
    return html

# -----------------------------
# Main Logic
# -----------------------------
if name:
    if name.strip().lower() in allowed_names:
        st.success("💖 Love You My Babbby")

        # Burst fires automatically via JS DOM detection above,
        # but we also inject a direct call here for immediate trigger
        components.html("""
        <script>
            if(window.parent && window.parent.triggerBurst){
                window.parent.triggerBurst();
            }
        </script>
        """, height=0)

        with st.spinner("Preparing something special… ❤️"):
            heart_html = generate_heart_html()

        # ── Heart animation ──
        st.markdown('<div class="section-heading">💝 For You — press ▶ to play</div>', unsafe_allow_html=True)
        st.markdown('<div class="anim-card">', unsafe_allow_html=True)
        # height=420 + scrolling=True ensures the matplotlib toolbar is visible & usable
        components.html(heart_html, height=420, scrolling=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ── Song ──
        st.markdown('<div class="section-heading">🎵 A Song For My Bundi ka Ladoo</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="video-wrapper">
            <iframe
                src="https://www.youtube.com/embed/Jpq9tm0gnTM?autoplay=0&rel=0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
            </iframe>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<br>', unsafe_allow_html=True)

        # ── Poem ──
        st.markdown('<hr class="rose-divider">', unsafe_allow_html=True)
        st.markdown('<div class="poem-title">🌹 What Do I Want 🌹</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="poem-card">
            One day you'll ask me what do I want,<br>
            As if you never knew its silent speaks.<br>
            Through every storm, through skies so blue,<br>
            My only answer lives in you.<br>
            No dream, no star, no distant view —<br>
            All I have ever wanted is you.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="footer-love">💖 Made with love, just for you 💖</div>', unsafe_allow_html=True)

    else:
        st.error("Sorry, nothing for you 😄")

# ── Footer ──
st.markdown('<hr class="rose-divider">', unsafe_allow_html=True)
st.markdown('<div class="footer-love">© A Small Surprise App</div>', unsafe_allow_html=True)
