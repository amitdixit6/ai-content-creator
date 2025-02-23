import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    headers: {
      "Content-Security-Policy": "default-src 'self' https://ai-content-creator-w4py.onrender.com; connect-src 'self' https://ai-content-creator-w4py.onrender.com; media-src 'self' data:;",
    },
  },
})
