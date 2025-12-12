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
        <Navbar year={year} setYear={setYear} />
        <div className="pt-20">
          <DashboardDisplay />
        </div>
      </StatisticsProvider>
    </ThemeProvider>
  );
}

export default App;
