<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import iconeMapeamento from '@/assets/images/photogrammetry.png'
import iconeDefensivos from '@/assets/images/fertilizer.png'
import iconePragas from '@/assets/images/fumigator.png'
import iconeManutencao from '@/assets/images/customer-service.png'
import iconeContato from '@/assets/images/help-desk.png'
import iconeCertificacoes from '@/assets/images/education.png'

const authStore = useAuthStore()

const handleMapeamentoClick = () => console.log('Mapeamento Clicado')
const handleDefensivosClick = () => console.log('Defensivos Clicado')
const handlePragasClick = () => console.log('Pragas Clicado')
const handleManutencaoClick = () => console.log('Manutencao Clicado')
const handleContatoClick = () => console.log('Contato Clicado')
const handleCertificacoesClick = () => console.log('Certificacoes Clicado')

</script>

<template>
  <div class="view-card-container home-view-layout">
    <div class="button-row top-button-row">
      <button class="action-button" @click="handleMapeamentoClick" aria-label="Mapeamento de Área">
        <img :src="iconeMapeamento" alt="" class="button-icon" />
        <span class="button-text">Mapeamento de Área</span>
      </button>
      <button class="action-button" @click="handleDefensivosClick" aria-label="Aplicação de Defensivos">
        <img :src="iconeDefensivos" alt="" class="button-icon" />
        <span class="button-text">Aplicação de Defensivos</span>
      </button>
      <button class="action-button" @click="handlePragasClick" aria-label="Combate a Pragas">
        <img :src="iconePragas" alt="" class="button-icon" />
        <span class="button-text">Combate a Pragas</span>
      </button>
    </div>
    <section class="hero-section" :class="{ 'logged-in-hero': authStore.isAuthenticated }">
      <div class="hero-content">
        <!-- Conteúdo sobreposto à imagem (se necessário) -->
      </div>
    </section>
    <div class="button-row bottom-button-row">
      <button class="action-button" @click="handleManutencaoClick" aria-label="Manutenção e Peças">
        <img :src="iconeManutencao" alt="" class="button-icon" />
        <span class="button-text">Manutenção e Peças</span>
      </button>
      <button class="action-button" @click="handleContatoClick" aria-label="Contato">
        <img :src="iconeContato" alt="" class="button-icon" />
        <span class="button-text">Contato</span>
      </button>
      <button class="action-button" @click="handleCertificacoesClick" aria-label="Certificações">
        <img :src="iconeCertificacoes" alt="" class="button-icon" />
        <span class="button-text">Certificações</span>
      </button>
    </div>
  </div>
</template>

<style scoped>
.home-view-layout {
  max-width: 100%;
  padding: 0;
  box-shadow: none;
  background-color: transparent;
  margin: 0;
  height: calc(80vh - var(--header-height, 60px) - var(--footer-height, 78px));
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.button-row {
  display: flex;
  gap: var(--padding-md, 16px);
  justify-content: space-around;
  align-items: stretch;
  width: 70%;
  max-width: 700px;
  padding: var(--padding-xs, 8px) 0;
}

.top-button-row {
  margin-bottom: var(--padding-md, 16px);
}

.bottom-button-row {
  margin-top: var(--padding-md, 16px);
}

.action-button {
  flex: 1;
  padding: var(--padding-md, 16px);
  background-color: var(--primary-color, #009bff);
  color: var(--text-on-primary, white);
  border: none;
  border-radius: var(--border-radius-lg, 8px);
  cursor: pointer;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: background-color 0.3s ease;
  font-weight: 500;
  box-shadow: var(--box-shadow, 0 2px 4px rgba(0, 0, 0, 0.1));
  min-width: 100px;
}

.action-button:active {
  transform: translateY(-1px);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.button-icon {
  width: 48px;
  height: 48px;
  object-fit: contain;
}

.button-text {
  font-size: clamp(0.8rem, 2.5vw, 0.95em);
  line-height: 1.3;
  word-break: break-word;
  display: block;
  max-width: 100%;
}

.hero-section {
  background-image: url('@/assets/images/agromaping.png');
  background-size: 50%;
  background-repeat: no-repeat;
  background-position: center center;
  width: 70%;
  max-width: 700px;
  min-height: 30vh;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: var(--border-radius-lg, 8px);
  margin: 0;
  position: relative;
  overflow: hidden;
}

.hero-content {
  display: none;
}

@media (max-width: 992px) {

  .button-row,
  .hero-section {
    width: 85%;
    max-width: none;
  }

  .action-button {
    min-height: 110px;
    gap: var(--padding-xxs, 4px);
  }

  .button-icon {
    width: 40px;
    height: 40px;
  }
}


@media (max-width: 768px) {
  .home-view-layout {
    justify-content: flex-start;
    padding-top: var(--padding-md, 16px);
    height: auto;
    min-height: calc(100vh - var(--header-height, 60px) - var(--footer-height, 78px));
  }

  .button-row,
  .hero-section {
    width: 95%;
    gap: var(--padding-sm, 8px);
  }

  .action-button {
    min-height: 100px;
    padding: var(--padding-sm, 12px);
  }

  .button-icon {
    width: 36px;
    height: 36px;
  }

  .button-text {
    font-size: 0.85em;
  }

  .hero-section {
    background-size: 65%;
    min-height: 25vh;
  }
}

@media (max-width: 480px) {
  .button-row {
    flex-direction: column;
    width: 90%;
    gap: var(--padding-md, 16px);
  }

  .action-button {
    flex-basis: auto;
    width: 100%;
    min-height: 90px;
  }

  .hero-section {
    min-height: 20vh;
    width: 90%;
    background-size: 70%;
  }
}
</style>