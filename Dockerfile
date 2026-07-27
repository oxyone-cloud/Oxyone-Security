# ==========================================
# Stage 1: Build & Dependencies
# ==========================================
FROM node:22-alpine AS builder

# Set working directory
WORKDIR /app

# Copy dependency files first for layer caching
COPY package*.json ./

# Install ALL dependencies (including devDependencies for build scripts/TypeScript)
RUN npm ci

# Copy application source code
COPY . .

# Run build if a build script exists (e.g., TypeScript compilation, bundling)
RUN npm run build --if-present

# Prune devDependencies to keep final image minimal
RUN npm prune --production

# ==========================================
# Stage 2: Production Execution
# ==========================================
FROM node:22-alpine AS runner

# Set production environment
ENV NODE_ENV=production

WORKDIR /app

# Copy node_modules and built assets from the builder stage
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist 2>/dev/null || true
COPY --from=builder /app/src ./src 2>/dev/null || true

# Security hardening: run as non-root user 'node'
USER node

# Expose app port (adjust 3000 to your app's port)
EXPOSE 3000

# Start application
CMD ["npm", "start"]
