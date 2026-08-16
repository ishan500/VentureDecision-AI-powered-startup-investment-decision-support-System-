import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./styles/globals.css";
import App from "./App.jsx";

import { StartupProvider } from "./components/context/StartupContext.jsx";
import { CurrencyProvider } from "./components/context/CurrencyContext.jsx";


createRoot(document.getElementById("root")).render(

    <StrictMode>

        <StartupProvider>

            <CurrencyProvider>

                <App />

            </CurrencyProvider>

        </StartupProvider>

    </StrictMode>

);