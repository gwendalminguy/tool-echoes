import { useState } from "react";

import { StatisticsProvider } from "./context/StatisticsContext";

import DashboardDisplay from "./components/DashboardDisplay";
import YearSelector from "./components/YearSelector";

import "./App.css";

function App() {
  const currentYear = new Date().getFullYear();
  const [year, setYear] = useState(currentYear);

  return (
    <StatisticsProvider year={year}>
      <div className="app">
        <YearSelector year={year} setYear={setYear} />
        <DashboardDisplay />
      </div>
    </StatisticsProvider>
  );
}

export default App;
