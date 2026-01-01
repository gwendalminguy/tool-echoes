import { createContext, useContext, useState, useEffect } from "react";

const StatisticsContext = createContext();

export function StatisticsProvider({ year, children }) {
  const [statistics, setStatistics] = useState(null);
  const [loading, setLoading] = useState(true);

  const [prev, setPrev] = useState(false);
  const [next, setNext] = useState(false);

  useEffect(() => {
    fetch(`/exports/${year}.json`)
      .then((r) => r.json())
      .then(setStatistics)
      .finally(() => setLoading(false));
  }, [year]);

  useEffect(() => {
    const prevYear = year - 1;
    const nextYear = year + 1;

    fetch("/exports/index.json")
      .then(res => res.json())
      .then(data => {
        setPrev(data.years.includes(prevYear));
        setNext(data.years.includes(nextYear));
      });
  }, [year]);

  return (
    <StatisticsContext.Provider value={{ statistics, loading, year, prev, next }}>
      {children}
    </StatisticsContext.Provider>
  );
}

export function useStatistics() {
  return useContext(StatisticsContext);
}
