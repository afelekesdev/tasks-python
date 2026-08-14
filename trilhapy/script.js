// Este é o seu script.js COMPLETO. Pode apagar o antigo e colar este.
const phases = [
    {
        id: 0,
        dur: "Semanas 1–8 · ~2h/dia",
        stacks: [
            { label: "Linguagem", title: "Python Avançado", sub: "Mundo 2 e 3 do Guanabara + POO sólida", pills: ["Python", "POO", "SQL"], pc: "teal" },
            { label: "Versão", title: "Git & GitHub", sub: "Fluxo de trabalho profissional (Branches/PRs)", pills: ["Git", "GitHub"], pc: "gray" }
        ],
        tasks: [
            "Concluir Mundo 2 e 3 do Curso em Vídeo",
            "Praticar POO: Herança e Encapsulamento",
            "Configurar ambiente local com Pyenv/Venv",
            "Dominar Git: Merges e Conflitos",
            "Praticar SQL: JOINs e Subqueries",
            "Fazer atividades complementares"
        ],
        projs: [
            { icon: "P1", title: "Sistema de Cadastro CLI", desc: "CRUD via terminal com persistência em PostgreSQL.", pills: ["Python", "PostgreSQL"] }
        ],
        tip: "Como você já conhece Java, foque nas particularidades do Python como List Comprehensions e Decorators."
    },
    {
        id: 1,
        dur: "Semanas 9–20 · ~2h/dia",
        stacks: [
            { label: "Backend", title: "Django & DRF", sub: "ORM, Autenticação JWT e APIs REST", pills: ["Django", "DRF", "JWT"], pc: "purple" },
            { label: "Infra", title: "Docker", sub: "Containerização de aplicações e bancos", pills: ["Docker", "Compose"], pc: "teal" }
        ],
        tasks: [
            "Fazer o tutorial oficial do Django (Polls)",
            "Criar Endpoints CRUD com Django REST Framework",
            "Implementar Autenticação JWT",
            "Dockerizar app e banco PostgreSQL",
            "Fazer deploy no Railway ou Render"
        ],
        projs: [
            { icon: "P3", title: "API de Tarefas", desc: "Backend com JWT e documentação Swagger.", pills: ["Django", "DRF", "Docker"] }
        ],
        tip: "Use o Docker para manter seu ambiente de desenvolvimento limpo e idêntico ao de produção."
    },
    {
        id: 2,
        dur: "Semanas 21–28 · ~2h/dia",
        stacks: [
            { label: "Frontend", title: "React & Hooks", sub: "Componentização e consumo de APIs", pills: ["React", "Axios", "JS"], pc: "blue" },
            { label: "Design", title: "Tailwind CSS", sub: "Estilização rápida e responsiva", pills: ["Tailwind", "Responsive"], pc: "teal" }
        ],
        tasks: [
            "Dominar fundamentos de React (Props/State)",
            "Aprender Hooks (useState, useEffect)",
            "Integrar Frontend com sua API Django",
            "Configurar React Router para navegação",
            "Fazer deploy no Vercel"
        ],
        projs: [
            { icon: "P5", title: "Dashboard da Trilha", desc: "Interface para gerenciar seus estudos consumindo sua API.", pills: ["React", "Tailwind"] }
        ],
        tip: "Foque no React, ele tem a maior demanda de mercado atualmente para quem trabalha com Python no Backend."
    },
    {
        id: 3,
        dur: "Semanas 29–40 · ~2h/dia",
        stacks: [
            { label: "Full Stack", title: "Integração Total", sub: "CORS, CI/CD e WebSockets", pills: ["Actions", "Redis", "Socket"], pc: "amber" },
            { label: "Qualidade", title: "Testes & Clean Code", sub: "Princípios SOLID e testes de integração", pills: ["Pytest", "SOLID"], pc: "purple" }
        ],
        tasks: [
            "Resolver problemas de CORS entre Front e Back",
            "Configurar GitHub Actions (CI/CD)",
            "Implementar tarefas assíncronas com Celery/Redis",
            "Aplicar princípios SOLID no código",
            "Adicionar WebSockets (Django Channels)"
        ],
        projs: [
            { icon: "P6", title: "SaaS Financeiro (FinanceAI)", desc: "Seu projeto principal com todas as tecnologias integradas.", pills: ["Full Stack", "AI"] }
        ],
        tip: "A Fase 4 é onde você constrói o 'FinanceAI'. Capriche no README deste projeto[cite: 1]."
    },
    {
        id: 4,
        dur: "Semanas 40+ · Foco Carreira",
        stacks: [
            { label: "Soft Skills", title: "Mercado & LinkedIn", sub: "Otimização de perfil e portfólio", pills: ["LinkedIn", "Soft Skills"], pc: "gray" },
            { label: "Técnico", title: "Algoritmos", sub: "Preparação para entrevistas técnicas", pills: ["LeetCode", "Big-O"], pc: "blue" }
        ],
        tasks: [
            "Otimizar LinkedIn com Headline estratégica",
            "Resolver 30 desafios no LeetCode",
            "Gravar demos em vídeo dos seus projetos principais",
            "Aplicar para vagas de Estágio/Júnior",
            "Participar de comunidades (Python Brasil)"
        ],
        projs: [
            { icon: "CV", title: "Site Portfólio", desc: "Página centralizando todos os seus contatos e projetos.", pills: ["Next.js/React", "SEO"] }
        ],
        tip: "Não espere estar 100% pronto. A partir da semana 38, comece a aplicar para vagas[cite: 1]."
    }
];

// LÓGICA DO SISTEMA - NÃO MEXER A MENOS QUE QUEIRA MUDAR O FUNCIONAMENTO
const taskState = JSON.parse(localStorage.getItem('trilhaProgresso')) || {};

function saveProgress() {
    localStorage.setItem('trilhaProgresso', JSON.stringify(taskState));
}

function countPhase(pi) {
    const tasks = phases[pi].tasks;
    let done = 0;
    tasks.forEach((_, ti) => { if (taskState[`${pi}-${ti}`]) done++; });
    return { done, total: tasks.length };
}

function pillHtml(pills, pc) {
    return pills.map(p => `<span class="pill pill-${pc || 'blue'}">${p}</span>`).join('');
}

function renderPhase(pi) {
    const ph = phases[pi];
    const el = document.getElementById('p' + pi);
    if (!el) return;
    const { done, total } = countPhase(pi);
    const pct = Math.round(done / total * 100);

    let h = `<div style="font-size:12px;color:var(--text-dim);margin-bottom:1rem">${ph.dur}</div>`;
    h += `<div class="prog-wrap"><div class="prog-fill" style="width:${pct}%"></div></div>`;
    h += `<div class="prog-lbl">${done} de ${total} tarefas concluídas (${pct}%)</div>`;

    h += `<div class="section-title">Stack desta fase</div><div class="cards">`;
    ph.stacks.forEach(s => {
        h += `<div class="card"><div class="card-label">${s.label}</div><div class="card-title">${s.title}</div><div class="card-sub" style="color:var(--text-dim); font-size:13px">${s.sub}</div><div style="margin-top:8px">${pillHtml(s.pills, s.pc)}</div></div>`;
    });
    h += `</div>`;

    h += `<div class="section-title">Tarefas & exercícios</div>`;
    ph.tasks.forEach((t, ti) => {
        const k = `${pi}-${ti}`;
        const doneClass = taskState[k] ? 'done' : '';
        h += `<div class="task-item ${doneClass}" onclick="toggle(${pi},${ti})"><div class="chk"></div><span class="task-txt">${t}</span></div>`;
    });

    h += `<div class="section-title">Projetos obrigatórios</div>`;
    ph.projs.forEach(proj => {
        h += `<div class="proj-card"><div class="card-title"><span style="color:var(--accent-teal)">${proj.icon}</span> ${proj.title}</div><div class="card-sub" style="color:var(--text-dim); font-size:13px; margin: 5px 0 10px">${proj.desc}</div><div>${pillHtml(proj.pills, 'blue')}</div><button class="ask-btn">Detalhar Projeto ↗</button></div>`;
    });

    h += `<div class="info-box"><strong>Dica:</strong> ${ph.tip}</div>`;
    el.innerHTML = h;
}

function toggle(pi, ti) {
    const k = `${pi}-${ti}`;
    taskState[k] = !taskState[k];
    saveProgress();
    renderPhase(pi);
}

function show(idx) {
    document.querySelectorAll('.phase').forEach((el, i) => el.classList.toggle('visible', i === idx));
    document.querySelectorAll('.nav-btn').forEach((el, i) => el.classList.toggle('active', i === idx));
    renderPhase(idx);
}

// Inicializa
show(0);