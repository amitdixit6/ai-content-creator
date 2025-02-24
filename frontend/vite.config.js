import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/generate": {
        target: process.env.VITE_BACKEND_URL,
        changeOrigin: true,
        secure: false,
      },
    },
    headers: {
      "Content-Security-Policy": "default-src *; script-src * 'unsafe-inline' 'unsafe-eval'; connect-src *; img-src * data:; style-src * 'unsafe-inline'; font-src * data:;",
    },
  },
})
