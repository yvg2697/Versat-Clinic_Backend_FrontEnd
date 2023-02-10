import { defineConfig } from "vite";
import reactRefresh from "@vitejs/plugin-react-refresh";

// https://vitejs.dev/config/
export default defineConfig({
  build: { manifest: true },
  base: process.env.mode === "production" ? "/static/" : "/",
  //   // base: process.env.NODE_ENV === "production" ? "/static/" : "/", considerar esto
  root: "./src",
  plugins: [reactRefresh()],
});
