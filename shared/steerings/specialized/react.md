---
inclusion: always
name: specialized-react
description: React specialist agents for component architecture, Next.js development, and modern React patterns. Use for React projects requiring framework-specific expertise.
---

# React Specialist Agents

Expert agents for React development including component architecture, Next.js, and modern React patterns.

## Available Agents

| Agent | File | Purpose | When to Use |
|-------|------|---------|-------------|
| **React Component Architect** | `react/react-component-architect.md` | Component design & patterns | Component libraries, design systems |
| **React Next.js Expert** | `react/react-nextjs-expert.md` | Next.js full-stack development | Next.js apps, SSR, App Router |

## Agent Selection Guide

### By Task Type

| Task | Recommended Agent |
|------|-------------------|
| Component library | React Component Architect |
| Design system | React Component Architect |
| Next.js application | React Next.js Expert |
| Server-side rendering | React Next.js Expert |
| App Router migration | React Next.js Expert |
| Reusable components | React Component Architect |
| API routes in Next.js | React Next.js Expert |

### Detection Signals

| Signal | Confidence | Agent |
|--------|------------|-------|
| `next` in package.json | High | React Next.js Expert |
| `next.config.js` present | High | React Next.js Expert |
| `react` without `next` | Medium | React Component Architect |
| `storybook` in package.json | High | React Component Architect |
| `app/` directory (Next.js 13+) | High | React Next.js Expert |

## Integration with D.E.R.E.K

| D.E.R.E.K Phase | React Agent Role |
|-----------------|------------------|
| **D**esign | Component architecture, state management |
| **E**valuate | Requirements, performance needs |
| **E**xecute | Implementation with React best practices |
| **R**eview | Code review, accessibility, performance |
| **K**nowledge | React patterns, hooks, optimization |

## Key Technologies

- **React 18+**: Concurrent features, Suspense, transitions
- **Next.js 14+**: App Router, Server Components, Server Actions
- **State Management**: Zustand, Jotai, Redux Toolkit
- **Styling**: Tailwind CSS, CSS Modules, styled-components
- **Testing**: Jest, React Testing Library, Playwright
