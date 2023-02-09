import React from "react";
import ReactDOM from "react-dom/client";
import { MainEntrypoint } from "./components";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <MainEntrypoint />
  </React.StrictMode>
);
