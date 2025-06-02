<template>
  <div class="view-card-container about-view-layout">
    <header class="about-header">
      <h1>Drone & Agro</h1>
      <p class="subtitle">
        Soluções tecnológicas e serviços especializados para o agronegócio.
      </p>
    </header>

    <section class="about-section">
      <h2>Objetivo</h2>
      <p class="objective-text">
        A Drone & Agro tem como missão fornecer serviços inovadores e de alta qualidade no setor agrícola, 
        com foco em mapeamento aéreo, pulverização de culturas, combate a pragas (como ervas daninhas e insetos), 
        manutenção de drones, reposição de peças e capacitação profissional. Atuamos para aumentar a eficiência, 
        sustentabilidade e produtividade no campo por meio da tecnologia.
      </p>
    </section>

    <section class="about-section">
      <h2>Serviços Oferecidos</h2>
      <ul>
        <li>Mapeamento agrícola por drones</li>
        <li>Pulverização agrícola automatizada</li>
        <li>Combate a ervas daninhas e insetos</li>
        <li>Manutenção corretiva e preventiva de drones</li>
        <li>Reposição de peças e acessórios para drones agrícolas</li>
        <li>Cursos de pilotagem de drones (com certificação)</li>
        <li>Capacitação para uso de defensivos agrícolas</li>
        <li>Treinamento técnico para manutenção de drones</li>
      </ul>
    </section>

    <section class="about-section">
      <h2>Tecnologias e Equipamentos</h2>
      <div class="tech-grid">
        <div class="tech-card">
          <h3>Drones Agrícolas</h3>
          <ul>
            <li><strong>DJI Agras T20, T30 e T40</strong></li>
            <li><strong>Autel EVO II Dual</strong></li>
            <li><strong>Drones customizados com RTK</strong></li>
          </ul>
        </div>
        <div class="tech-card">
          <h3>Sistemas & Software</h3>
          <ul>
            <li><strong>Software de planejamento de voo</strong></li>
            <li><strong>Processamento de imagens com IA</strong></li>
            <li><strong>Sistemas de telemetria em tempo real</strong></li>
          </ul>
        </div>
        <div class="tech-card">
          <h3>Capacitação & Certificação</h3>
          <ul>
            <li><strong>Instrutores certificados ANAC</strong></li>
            <li><strong>Material didático próprio</strong></li>
            <li><strong>Certificados válidos nacionalmente</strong></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="about-section contact-info">
      <h2>Contato</h2>
      <p>
        Para orçamentos, agendamentos ou dúvidas, entre em contato conosco.
        <a
          href="https://www.instagram.com/brothersvideodrone?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
          target="_blank"
          rel="noopener noreferrer"
          class="btn btn-accent btn-inline"
        >
          Visite nosso Instagram!
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
