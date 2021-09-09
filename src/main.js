import { createApp } from "vue";
import App from "./App.vue";
import "./global_styles.scss";
import router from "./router";
import mixin from "./utils/utils.js";

createApp(App).mixin(mixin)
  .use(router)
  .mount("#app");
