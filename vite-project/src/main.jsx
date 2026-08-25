import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import Counter from "./SideEffects/sideffects";
import Routing from "./Routing";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Counter />
  </StrictMode>,
);
