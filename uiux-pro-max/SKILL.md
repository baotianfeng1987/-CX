---
name: UI/UX Pro Max
description: Expert UI/UX design intelligence for creating professional, modern, and accessible interfaces in RuoYi-Vue.
---

# UI/UX Pro Max Skill

This skill allows you to design and implement premium-quality user interfaces, focusing on modern aesthetics (glassmorphism, vibrant palettes), usability (accessibility, responsiveness), and consistency within the RuoYi-Vue ecosystem.

## Core Capabilities
- **Design System Enforcer**: Ensures consistent use of Element UI components with custom overrides for a "fresh" look.
- **Aesthetic Upgrade**: Recommends modern CSS techniques (box-shadows, gradients, rounded corners) to replace "enterprise-drab" defaults.
- **Micro-Interaction Designer**: Suggests subtle animations (hover states, transitions) to make the app feel "alive".
- **Responsive Expert**: Guarantees mobile-friendly and adaptive layouts.

## Guidelines for RuoYi-Vue

### 1. Modernize Element UI
The default Element UI look is functional but dated.
- **Shadows**: Use softer, larger shadows (`box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);`) instead of harsh borders.
- **Radius**: Increase border-radius to `8px` or `12px` for cards and modals.
- **Spacing**: Increase padding/margin to give content "room to breathe".
- **Colors**:
    - Primary: Use your defined vibrant primary color (e.g., `#409EFF` -> A more vibrant blue or brand color).
    - Backgrounds: Use off-white (`#F8F9FA`) instead of pure white/gray for page backgrounds to add depth.

### 2. Layout Patterns
- **Cards**: Wrap distinct content sections in `<el-card shadow="hover">`.
- **Grid**: Use `el-row` and `el-col` for responsive grids.
- **Headers**: Page headers should have clear titles and breadcrumbs.

### 3. Anti-Patterns to Avoid
- **Dense Tables**: Avoid cramming too many columns. Use "Expand" rows or "Detail" modals.
- **Generic Confirmations**: Don't just say "Success". Say "Order #12345 created successfully".
- **Dead Clicks**: All clickable elements must have a cursor pointer and a hover state.

### 4. Code Snippets (Quick-Wins)
**Glassmorphism Card:**
```css
.glass-card {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
}
```

**Gradient Text:**
```css
.gradient-text {
  background: linear-gradient(45deg, #409EFF, #36D1DC);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

## Workflow
1. **Analyze**: When user asks for a feature, first visualize the *best* way to present it.
2. **Propose**: Suggest a UI mockup or description before coding.
3. **Refine**: Apply "polish" (spacing, shadows, hover effects) after functional implementation.
