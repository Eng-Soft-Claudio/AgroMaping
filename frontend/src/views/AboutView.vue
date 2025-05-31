<template>
  <div class="view-card-container about-view-layout">
    <header class="about-header">
      <h1>Sobre o Projeto Pytholingo</h1>
      <p class="subtitle">
        Uma plataforma gamificada para aprender Python, do iniciante ao profissional.
      </p>
    </header>

    <section class="about-section">
      <h2>Objetivo</h2>
      <p class="objective-text">
        O Pytholingo foi desenvolvido para tornar o aprendizado da linguagem Python acessível,
        envolvente e eficiente. Utilizando princípios de gamificação, repetição espaçada e imersão
        prática gradual, nosso objetivo é fornecer uma fundação sólida e divertida para quem deseja
        dominar Python, economizando tempo e tornando o estudo uma jornada motivadora.
      </p>
    </section>

    <section class="about-section">
      <h2>Tecnologias Utilizadas</h2>
      <div class="tech-grid">
        <div class="tech-card">
          <h3>Backend</h3>
          <ul>
            <li><strong>Python 3.12+</strong></li>
            <li><strong>FastAPI</strong></li>
            <li><strong>SQLAlchemy & Alembic</strong></li>
            <li><strong>Pydantic</strong></li>
            <li><strong>Passlib & python-jose</strong></li>
            <li><strong>PostgreSQL</strong></li>
            <li><strong>Pytest</strong></li>
          </ul>
        </div>
        <div class="tech-card">
          <h3>Frontend</h3>
          <ul>
            <li><strong>Vue.js 3 (Composition API)</strong></li>
            <li><strong>TypeScript</strong></li>
            <li><strong>Vite</strong></li>
            <li><strong>Pinia & Vue Router</strong></li>
            <li><strong>VeeValidate & Yup</strong></li>
            <li><strong>Vue-Toastification</strong></li>
          </ul>
        </div>
        <div class="tech-card">
          <h3>DevOps & Infraestrutura</h3>
          <ul>
            <li><strong>Docker & Docker Compose</strong></li>
            <li><strong>ESLint / Linters</strong></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="about-section">
      <h2>Funcionalidades Implementadas (Base)</h2>
      <h3>Usuário Comum:</h3>
      <ul>
        <li>Registro, Login e Logout (JWT)</li>
        <li>Visualização e Edição do próprio perfil</li>
        <li>Alteração da própria senha</li>
        <li>Recuperação de senha</li>
        <li>Deleção da própria conta</li>
      </ul>
      <h3 class="features-subtitle">Funcionalidades de Administrador:</h3>
      <ul>
        <li>Listagem de todos os usuários</li>
        <li>Criação de novos usuários</li>
        <li>Edição completa de usuários (incluindo status e permissões)</li>
        <li>Deleção de usuários</li>
      </ul>
    </section>

    <section class="about-section contact-info">
      <h2>Contato e Repositório</h2>
      <p>
        Feedback e sugestões são sempre bem-vindos.
        <a
          href="https://github.com/Eng-Soft-Claudio/CRUD-Template"
          target="_blank"
          rel="noopener noreferrer"
          class="btn btn-accent btn-inline"
        >
          Visite o Repositório no GitHub
        </a>
      </p>
    </section>
  </div>
</template>

<style scoped>
.about-view-layout {
  max-width: 900px;
  margin: var(--padding-xl) auto;
}
.about-header {
  text-align: center;
  margin-bottom: var(--padding-xl);
  padding-bottom: var(--padding-lg);
  border-bottom: 1px solid var(--color-border);
}
.about-header h1 {
  font-size: 2.2em;
  color: var(--color-brand-primary);
  margin-bottom: var(--padding-sm);
}
.subtitle {
  font-size: 1.1em;
  color: var(--color-text-secondary);
  font-family: var(--font-sans-ui);
}
.about-section {
  margin-bottom: var(--padding-xl);
}
.about-section h2 {
  font-size: 1.6em;
  color: var(--color-text-primary);
  margin-bottom: var(--padding-md);
  padding-bottom: var(--padding-sm);
  border-bottom: 2px solid var(--color-brand-secondary);
  display: inline-block;
}
.about-section h3 {
  font-size: 1.25em;
  font-family: var(--font-sans-ui);
  font-weight: 600;
  color: var(--color-text-primary);
  margin-top: var(--padding-lg);
  margin-bottom: var(--padding-sm);
}
.features-subtitle {
  margin-top: var(--padding-lg);
}
.objective-text,
.about-section p,
.about-section ul {
  font-size: 1rem;
  color: var(--color-text-secondary);
  margin-bottom: var(--padding-md);
  text-align: justify;
}
.about-section ul {
  list-style-position: inside;
  padding-left: 0;
}
.about-section ul li {
  margin-bottom: var(--padding-xs);
}
.tech-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: var(--padding-lg);
  margin-top: var(--padding-md);
}
.tech-card {
  background-color: var(--color-bg-page);
  padding: var(--padding-lg);
  border-radius: var(--border-radius-md);
  border: 1px solid var(--color-border);
}
.tech-card h3 {
  margin-top: 0;
  font-size: 1.15em;
  color: var(--color-brand-primary);
  border-bottom: none;
  padding-bottom: 0;
  margin-bottom: var(--padding-md);
}
.tech-card ul {
  font-size: 0.95rem;
  padding-left: var(--padding-md);
  color: var(--color-text-secondary);
}
.tech-card ul li strong {
  color: var(--color-text-primary);
}
.contact-info {
  text-align: center;
  padding-top: var(--padding-lg);
  border-top: 1px solid var(--color-border);
}
.contact-info p {
  text-align: center;
}
.btn.btn-inline {
  margin-left: var(--padding-sm);
}
</style>
