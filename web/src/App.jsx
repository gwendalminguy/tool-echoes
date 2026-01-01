import { useState } from "react";

import { ThemeProvider } from "./context/ThemeContext";
import { StatisticsProvider } from "./context/StatisticsContext";

import Navbar from "./components/Navbar";
import DashboardDisplay from "./components/DashboardDisplay";

import "./App.css";

function App() {
  const currentYear = new Date().getFullYear();
  const [year, setYear] = useState(currentYear);

  return (
    <ThemeProvider>
      <StatisticsProvider year={year}>
        <div className="min-h-screen flex flex-col">
          <Navbar year={year} setYear={setYear} />
          <main className="flex-1 flex items-center justify-center bg-base-200">
            <DashboardDisplay year={year} />
          </main>
        </div>
      </StatisticsProvider>
    </ThemeProvider>
  );
}

export default App;
