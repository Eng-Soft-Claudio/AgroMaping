<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

// As computed properties userDisplayName e greeting foram removidas
// pois o conteúdo que as utilizava foi removido do template.
</script>

<template>
  <div class="view-card-container home-view-layout">
    <section class="hero-section" :class="{ 'logged-in-hero': authStore.isAuthenticated }">
      <div class="hero-content">
        <template v-if="authStore.isAuthenticated && authStore.currentUser">
        </template>
        <template v-else>
        </template>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home-view-layout {
  max-width: 100%;
  padding: 0;
  box-shadow: none;
  background-color: transparent;
  margin: 0;
  height: calc(100vh - var(--header-height) - var(--footer-height, 78px));
  display: flex;
  flex-direction: column;
}

.hero-section {
  background-image: url('@/assets/images/agromaping.png');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center center;
  color: var(--color-text-on-brand-primary);
  padding: 50px var(--page-padding-mobile);
  text-align: center;
  min-height: 35vh;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: var(--border-radius-lg);
  flex-grow: 1;
  margin: var(--padding-md) 0 var(--padding-xl) 0;
  position: relative;
  overflow: hidden;
  z-index: 0;
}

.hero-content {
  position: relative; 
  max-width: 90%; 
  background-color: rgba(0, 0, 0, 0.3); 
  padding: 20px; 
  border-radius: var(--border-radius-md);
}
</style>
