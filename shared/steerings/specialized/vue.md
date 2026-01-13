---
inclusion: always
name: specialized-vue
description: Vue.js specialist agents for component architecture, Nuxt.js development, and state management. Use for Vue projects requiring framework-specific expertise.
---

# Vue Specialist Agents

Expert agents for Vue.js development including component architecture, Nuxt.js, and state management patterns.

## Available Agents

| Agent | File | Purpose | When to Use |
|-------|------|---------|-------------|
| **Vue Component Architect** | `vue/vue-component-architect.md` | Vue 3 Composition API & patterns | Component design, composables |
| **Vue Nuxt Expert** | `vue/vue-nuxt-expert.md` | Nuxt.js full-stack development | SSR, SSG, Nuxt apps |
| **Vue State Manager** | `vue/vue-state-manager.md` | State management patterns | Pinia, Vuex, complex state |

## Agent Selection Guide

### By Task Type

| Task | Recommended Agent |
|------|-------------------|
| Component library | Vue Component Architect |
| Composables design | Vue Component Architect |
| Nuxt.js application | Vue Nuxt Expert |
| Server-side rendering | Vue Nuxt Expert |
| Static site generation | Vue Nuxt Expert |
| Pinia store design | Vue State Manager |
| Complex state logic | Vue State Manager |
| Vuex migration | Vue State Manager |

### Detection Signals

| Signal | Confidence | Agent |
|--------|------------|-------|
| `nuxt` in package.json | High | Vue Nuxt Expert |
| `nuxt.config.ts` present | High | Vue Nuxt Expert |
| `vue` without `nuxt` | Medium | Vue Component Architect |
| `pinia` in package.json | High | Vue State Manager |
| `vuex` in package.json | High | Vue State Manager |
| `composables/` directory | Medium | Vue Component Architect |
| `stores/` directory | Medium | Vue State Manager |

## Integration with D.E.R.E.K

| D.E.R.E.K Phase | Vue Agent Role |
|-----------------|----------------|
| **D**esign | Component architecture, state design |
| **E**valuate | Requirements, performance needs |
| **E**xecute | Implementation with Vue best practices |
| **R**eview | Code review, reactivity, performance |
| **K**nowledge | Vue patterns, composables, optimization |

## Key Technologies

- **Vue 3**: Composition API, `<script setup>`, reactivity system
- **Nuxt 3**: Nitro server, file-based routing, auto-imports
- **State Management**: Pinia (recommended), Vuex 4
- **Routing**: Vue Router 4, Nuxt file-based routing
- **Testing**: Vitest, Vue Test Utils
- **Build Tools**: Vite, Nuxt DevTools

## Common Patterns

### Composition API
```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

const count = ref(0)
const doubled = computed(() => count.value * 2)
</script>
```

### Composable Pattern
```ts
export function useCounter(initial = 0) {
  const count = ref(initial)
  const increment = () => count.value++
  return { count, increment }
}
```

### Pinia Store
```ts
export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const increment = () => count.value++
  return { count, increment }
})
```
